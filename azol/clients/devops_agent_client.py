"""A module containing azure devops agent http client"""
import logging
from azol.constants import  OAuthResourceIDs
import time
import base64
import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, padding as pad
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateNumbers, RSAPublicNumbers
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import requests
from pprint import pprint

class DevOpsAgentSessionExistsAzolException(Exception):
    """An exception when a devops agent session already exists for an agent"""
    pass

class DevOpsAgentSessionCreationException(Exception):
    """An exception when an error arises while creating a devops session"""
    pass

class AzureDevOpsAgentClient( object ):
    """
        An HTTP client for spoofing a devOps Agent
    """

    def __init__( self, agent_credentials, devops_org_name, agent_id,
                  pool_id, agent_client_id, *args, **kwargs ):
        
        # If no arguments are supplied, assume the code is running on a devops agent.
        self.devops_org_name = devops_org_name
        self.agent_id = agent_id
        self.pool_id = pool_id
        self.agent_client_id = agent_client_id
        self._agent_credentials = agent_credentials
        self._current_token=None
        self.encryption_key = None
        self.session_id = None

        public_numbers = RSAPublicNumbers( self._agent_credentials.rsa_parameters.exponent, self._agent_credentials.rsa_parameters.modulus )
        private_numbers = RSAPrivateNumbers( self._agent_credentials.rsa_parameters.p, self._agent_credentials.rsa_parameters.q,
                                           self._agent_credentials.rsa_parameters.d, self._agent_credentials.rsa_parameters.dp,
                                           self._agent_credentials.rsa_parameters.dq, self._agent_credentials.rsa_parameters.inverseq,
                                           public_numbers )
        
        self._agent_private_key = private_numbers.private_key(backend=default_backend())

    def fetch_token(self):
        assertion = self._generate_assertion()
        body={
            "grant_type": "client_credentials",
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion": assertion
        }
        
        headers = {
            "Accept": "application/json"
        }

        resp=requests.post(f"https://vssps.dev.azure.com/{self.devops_org_name}/_apis/oauth2/token",
                            headers=headers, data=body)
        
        token=resp.json()["access_token"]
        self._current_token=token
        return token

    def _generate_assertion(self, expiry=300):
        epoch_time = int(time.time())
        expiry_time = epoch_time + expiry
        token_headers={
            "typ": "JWT",
            "alg": "RS256"
        }
        token_body={
            "sub": self.agent_client_id,
            "jti": self.agent_client_id,
            "iss": self.agent_client_id,
            "aud": f"https://vssps.dev.azure.com/{self.devops_org_name}/_apis/oauth2/token",
            "nbf": epoch_time,
            "exp": expiry_time
        }
        header_b64 = base64.urlsafe_b64encode(json.dumps(token_headers).encode()).decode().rstrip("=")
        body_b64 = base64.urlsafe_b64encode(json.dumps(token_body).encode()).decode().rstrip("=")
        b64_header_body = header_b64 + "." + body_b64

        signature = base64.urlsafe_b64encode(
            self._agent_private_key.sign(
                b64_header_body.encode(), padding=padding.PKCS1v15(),
                algorithm=hashes.SHA256()
            )
        ).decode().rstrip("=")

        assertion  = b64_header_body + "." + signature
        return assertion
    


    def kill_session(self, session_id):
        self.fetch_token()
        headers = {
            "Authorization": f"Bearer {self._current_token}",
            "Accept": "application/json; api-version=7.2-preview.1",
            "Content-Type": "application/json; api-version=7.2-preview.1"
        }
        resp=requests.delete(f"https://dev.azure.com/{self.devops_org_name}"
                             f"/_apis/distributedtask/pools/{self.pool_id}"
                             f"/sessions/{session_id}", headers=headers)
        # TODO
        logging.info(f"Session {session_id} ended ")
    
    def create_session(self):
        self.fetch_token()
        headers = {
            "Authorization": f"Bearer {self._current_token}",
            "Accept": "application/json; api-version=7.2-preview.1",
            "Content-Type": "application/json; api-version=7.2-preview.1"
        }
        body={
            "ownerName": "testing",
            "agent": {
                "id": self.agent_id,
                "version": "4.251.0"
            }
        }
        
        resp=requests.post(f"https://dev.azure.com/{self.devops_org_name}"
                           f"/_apis/distributedtask/pools/{self.pool_id}/sessions",
                           headers=headers, json=body)
        if resp.status_code == 409:
            logging.warning("Could not create session - Session already exists.")
            raise DevOpsAgentSessionExistsAzolException(f"A session for agent {self.agent_id}"
                                                        f" against organization {self.devops_org_name}"
                                                        "already exists")

        contents=resp.json()

        b64_encrypted_encryption_key = contents["encryptionKey"]
        self.session_id = contents["sessionId"]
        
        encrypted_b64_aes_key=b64_encrypted_encryption_key["value"]
        encrypted_bytes_aes_key=base64.b64decode(encrypted_b64_aes_key)
        
        aes_key=self._agent_private_key.decrypt(encrypted_bytes_aes_key,
                                    padding=padding.OAEP(mgf=padding.MGF1(hashes.SHA1()),
                                                   algorithm=hashes.SHA1(), label=None))
        self._session_key = algorithms.AES(aes_key)
        logging.info(f"Session Created with ID {self.session_id}")

    def poll(self, message_callback=None, max_messages=1, max_time=None):
        '''
            Poll the devOps pool for new messages.

            When a new message is received, it is decrypted and the message contents are
            used as a parameter to the message_callback.

            If no message_callback is set, the message contents will be printed to stdout

            Args:
                message_callback - (function) A callback that can be used to process each message.
                max_messages - (int) the maximum number of messages to receive before endoing the
                                     polling loop. defaults to 1
                max_time - (int) The maximum amount of time in seconds to poll for new messages.
                                 if None, poll forever. defaults to None                                 

            Returns:
                None

        '''

        def stdout_callback(message):
            pprint(message)

        if not message_callback:
            message_callback = stdout_callback

        number_messages_received = 0
        epoch_time = int(time.time())
        time_limit=False
        poll_expiry = None
        if max_time:
            time_limit=True
            poll_expiry = epoch_time + max_time
        
        while True:
            if number_messages_received >= max_messages:
                break
            # devops agent requests are not asynchronous, and may block for 60 seconds or so.
            if time_limit and int(time.time()) >= poll_expiry-60:
                break

            # listen to new jobs and print the job contents
            self.fetch_token()
            logging.info("Polling for messages...")
            headers = {
                "Authorization": f"Bearer {self._current_token}",
                "Accept": "application/json; api-version=7.2-preview.1",
                "Content-Type": "application/json; api-version=7.2-preview.1"
            }
            try:
                resp=requests.get(f"https://dev.azure.com/{self.devops_org_name}"
                              f"/_apis/distributedtask/pools/{self.pool_id}"
                              f"/messages?sessionId={self.session_id}", headers=headers,
                              timeout=60)
                if resp.status_code != 200:

                    logging.error(resp.status_code)
                    logging.error(resp.content)
                    raise DevOpsAgentSessionCreationException("Could not create a devops session")
                message_json = resp.json()

                iv_b64 = message_json["iv"]
                iv=base64.b64decode(iv_b64)
                encrypted_b64_message=message_json["body"]
                encrypted_bytes=base64.b64decode(encrypted_b64_message)

                cipher = Cipher(self._session_key, modes.CBC(iv))
                decryptor=cipher.decryptor()
                plaintext=decryptor.update(encrypted_bytes) + decryptor.finalize()
                
                block_size=128
                unpadder = pad.PKCS7(block_size).unpadder()

                plaintext = unpadder.update(plaintext) + unpadder.finalize()
                decrypted_message=json.loads(plaintext)
                message_callback(decrypted_message)
                number_messages_received += 1

            except requests.exceptions.Timeout:
                logging.info("No new messages.")