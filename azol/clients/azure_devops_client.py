"""A module containing an Azure Devops HTTP Client"""
import logging
from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.constants import OAuthResourceIDs
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric import rsa
import base64

class AzureDevopsClient( OAuthHTTPClient ):
    """
        An HTTP client for interacting with the Azure Devops API
    """

    def __init__( self, *args, **kwargs ):
        devops_resource_id=OAuthResourceIDs.AzureDevOps
        devops_base_url=f"https://dev.azure.com"

        super().__init__( oauth_resource=devops_resource_id,
                          base_url=devops_base_url, *args, **kwargs)

    def get_service_endpoint_types( self, org_name ):
        '''
            Get all the current service connection types

            Args
                org_name - the name of the devops organization

            Returns:
                A list of service connection objects
        '''
        query_params = { "api-version": "7.1-preview.1"}

        url = f"/{org_name}/_apis/serviceendpoint/types"
        resp=self._send_request( url,  method="GET", query_parameters=query_params ) 
        response_data = resp.json()
        return response_data

    def create_agent(self, org_name, pool_id, name):
        '''
            Create a new devops agent in the specified pool.

            Args:

                org_name - the name of the devops org that the pool is in

                pool_id - the id of the devops agent pool that the agent should be added to

                name - a unique name for the new devops agent

            Returns:
                A tuple ( agent_data, rsa_parameters )

                Where agent_data is information about the agent resulting from the HTTP response,
                and rsa_parameters is the base64 encoded rsa parameters used to create the agent.
        '''

        def get_b64encoded_int_bytes(integer):
            num_bytes = (integer.bit_length() + 7) // 8
            byte_representation = integer.to_bytes(num_bytes, byteorder='big')
            return base64.b64encode(byte_representation).decode()

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_numbers = private_key.public_key().public_numbers()
        modulus=public_numbers.n
        exponent=public_numbers.e
        dq=private_key.private_numbers().dmq1
        dp=private_key.private_numbers().dmp1
        q=private_key.private_numbers().q
        p=private_key.private_numbers().p
        d=private_key.private_numbers().d
        inverseq=private_key.private_numbers().iqmp

        b64_encoded_modulus=get_b64encoded_int_bytes(modulus)
        b64_encoded_exponent=get_b64encoded_int_bytes(exponent)
        b64_encoded_dq = get_b64encoded_int_bytes(dq)
        b64_encoded_dp = get_b64encoded_int_bytes(dp)
        b64_encoded_q = get_b64encoded_int_bytes(q)
        b64_encoded_p = get_b64encoded_int_bytes(p)
        b64_encoded_d = get_b64encoded_int_bytes(d)
        b64_encoded_inverseq = get_b64encoded_int_bytes(inverseq)

        rsa_params = {
            "p": b64_encoded_p,
            "q": b64_encoded_q,
            "d": b64_encoded_d,
            "dp": b64_encoded_dp,
            "dq": b64_encoded_dq,
            "inverseQ": b64_encoded_inverseq,
            "modulus": b64_encoded_modulus,
            "exponent": b64_encoded_exponent
        }

        url = f"/{org_name}/_apis/distributedtask/pools/{pool_id}/agents"
        
        query_params = { "api-version": "7.1-preview.1"}
        body = {
            "systemCapabilities": {},
            "maxParallelism": 1,
            "authorization": {
                "publicKey": {
                    "exponent": b64_encoded_exponent,
                    "modulus": b64_encoded_modulus
                }
            },
            "name": name,
            "version": "4.251.0",
            "osDescription": "Microsoft Windows 10.0.26100",
            "status": 0
        }

        resp=self._send_request( url, json=body, method="POST", query_parameters=query_params ) 
        response_data = resp.json()
        return (response_data, rsa_params)

    def get_service_connection_role_assignments(self, org_name, project_id, endpoint_id):
        """
            Get all role assignments on a service connection(endpoint).

            Note that if the service endpoint/project id combination does not exist, this
            endpoint will still return 200 OK with an empty list as a result. Ensure that the
            correct project_id value is used.

            Args:
                org_name - The devops organization name

                project_id - The project ID that contains the service endpoint. Note that the
                             project name will not work, the name needs to be resolved to an ID
                
                endpoint_id - The id of the service endpoint
            
            Returns:
                A list of role assignments
        """
        query_params = { "api-version": "7.1-preview.1"}
        url = (f"/{org_name}/_apis/securityroles/scopes/"
                f"distributedtask.serviceendpointrole/roleassignments/resources/{project_id}_{endpoint_id}" )
        raw_response = self._send_request( url, query_parameters=query_params)
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting service conection role assignments" )
            logging.error( raw_response.content )
            raise Exception( "Could not fetch service connection role assignments" )
            
        return raw_response.json()["value"]

    def get_allowed_pipelines( self, org_name, project_name, endpoint_id ):
        """
            Get all pipelines that are authorized to use a service connection.

            This command resurns an object that includes high level settings for the
            service connection as well as pipelines that are authorized.

            Args:
                org_name - The devops organization name

                project_name - The project name that contains the service endpoint
                
                endpoint_id - The id of the service endpoint
            
            Returns:
                An object containing the allowed pipelines, as high level settings for pipeline authorization
                for the service connection
        """
        query_params = { "api-version": "7.1-preview.1"}
        raw_response = self._send_request( f"/{org_name}/{project_name}/_apis/pipelines/pipelinepermissions/endpoint/{endpoint_id}", query_parameters=query_params )
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting allowed pipelines for service connection" )
            logging.error( raw_response.content )
            raise Exception("Could not fetch allowed pipelines for service connection")
            
        return raw_response.json()

    def get_service_connection( self, org_name, project_name, endpoint_id ):
        """
            Get a service connections

            Note that this will still return 200 OK and an empty object if the endpoint or project
            does not exist. Ensure that correct values are used.

            Args:
                org_name - The devops organization name

                project_name - The project name that contains the service endpoint

                endpoint_id - The id of the service endpoint
            
            Returns:
                A service connection
        """
        query_params = { "api-version": "7.2-preview.4"}
        raw_response = self._send_request( f"/{org_name}/{project_name}/"
                                           f"_apis/serviceendpoint/endpoints/{endpoint_id}",
                                           query_parameters=query_params )
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting devops project service connections" )
            logging.error( raw_response.json() )
            raise Exception("Could not fetch service connections for project")
        return raw_response.json()

    def try_download_permissions_report( self, report_url ):
        """
            Try to download a permissions report, or return None if it is not ready

            Args:
                report_url - the report url returned from create_permission_report

            returns:
                deserialized report object if successful, or None if the report is not
                ready yet
        """
        query_params = { "api-version": "7.2-preview.1"}
        r = raw_response = self._send_request( url=report_url,
                                          query_parameters=query_params )
        status = r.status_code
        if status == 404:
            error_type = r.json()["typeKey"]
            if error_type == "PermissionsReportDownloadNotAvailableException":
                logging.warning( "Permissions report is not ready for download" )
                return None
            else:
                logging.error( "ERROR while downloading permissions report" )
                logging.error( raw_response.json() )
                raise Exception("Could not download permissions report")
        elif status != 200:
            logging.error( "ERROR while downloading permissions report" )
            logging.error( raw_response.json() )
            raise Exception("Could not download permissions report")
        
        return r.json()

    def create_permission_report( self, org_name, resource_id, resource_type ):
        """
            Create a permissions report for the resource id and resource types.
            https://learn.microsoft.com/en-us/rest/api/azure/devops/permissionsreport/

            Example to create a report on project permissions: 
            client.create_permission_report("[org_Name]", 
                   "[projectId]", "ProjectGit")

            Args:
                org_name - The devops organization name

                resource_id - The Azure DevOps resource ID that should be reported on.
                              For example, the project ID, project collection ID, etc.

                resource_type - The type of the resource to fetch permissions for.
                                Alowed values: ProjectGit, ref, repo, release, tfvc
            
            Returns:
                A URL to download the permissions report
        """
        query_params = { "api-version": "7.2-preview.1"}
        body = {
            "descriptors": [],
            "reportName": str(datetime.now().isoformat()),
            "resources": [
                {
                    "resourceId": resource_id,
                    "resourceType": resource_type
                }
            ]
        }
        raw_response = self._send_request( f"/{org_name}/_apis/permissionsreport", 
                                          method="POST", json=body, query_parameters=query_params )
        if raw_response.status_code != 202:
            logging.error( "ERROR while creating devops permissions report" )
            logging.error( raw_response.json() )
            raise Exception("Could not create devops permissions report")
        return raw_response.json()["_downloadLink"]["href"]


    def get_service_connections( self, org_name, project_name ):
        """
            Get all service connections in a project

            Args:
                org_name - The devops organization name

                project_name - The project name that contains the service endpoint
            
            Returns:
                A list of service connection objects
        """
        query_params = { "api-version": "7.2-preview.4"}
        raw_response = self._send_request( f"/{org_name}/{project_name}/_apis/serviceendpoint/endpoints", query_parameters=query_params )
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting devops project service connections" )
            logging.error( raw_response.json() )
            raise Exception("Could not fetch service connections for project")
        return raw_response.json()["value"]

    def get_all_service_connections( self, org_name ):
        """
            Get all service connections in an organization

            Args:
                org_name - The devops organization name

            Returns:
                A dictionary where the keys are project names, and the values
                are a list of service connections found in that project
        """
        projects = self.get_projects(org_name)
        results = {}

        for project in projects:
            results[project["name"]] = []
            service_connections = self.get_service_connections(org_name, project["name"])
            for sc in service_connections:
                results[project["name"]].append(sc)
        return results

    def get_projects( self, org_name ):
        """Get all projects that the current logged in credential has access to
        
            Args:
                org_name - The devops organization name

            Returns:
                A list of projects
        """
        query_params = { "api-version": "7.2-preview.4"}
        raw_response = self._send_request( f"/{org_name}/_apis/projects", query_parameters=query_params )

        if raw_response.status_code != 200:
            logging.error( "ERROR while getting devops projects" )
            logging.error( raw_response.json())
            raise Exception("Could not fetch Azure DevOps Projects")
        return raw_response.json()["value"]

    def get_connection_data( self, org_name ):
        """
            Get the currently logged on user's information from the /connectionData endpoint

            Args:
                org_name - The devops organization name

            Returns:
                an object containing user information
        """
        query_params = { "api-version": "7.2-preview.1"}
        raw_response = self._send_request(f"/{org_name}/_apis/connectionData",
                                          method="GET", query_parameters=query_params)
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting logged in users connection data" )
            logging.error( raw_response.content)
            raise Exception("Could not get logged in user connection data from devops API")
        return raw_response.json()

    def get_self(self):
        """
            Get the currently logged on user's information from the /User endpoint

            Returns:
                an object containing user information
        """
        query_params = { "api-version": "7.2-preview.1"}
        raw_response = self._send_request(url="https://aex.dev.azure.com/_apis/User/User",
                                          method="GET", query_parameters=query_params)
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting logged in user" )
            logging.error( raw_response.json())
            raise Exception("Could not get logged in user from devops API")
        return raw_response.json()
    
    def get_profile(self):
        """
            Get the currently logged on user's profiles from the /profiles/me endpoint

            Returns:
                a list of profile objects
        """
        query_params = { "api-version": "7.2-preview.1"}
        raw_response = self._send_request(url="https://app.vssps.visualstudio.com/_apis/profile/profiles/me",
                                          method="GET", query_parameters=query_params)
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting logged in users profiles" )
            logging.error( raw_response.json())
            raise Exception("Could not get logged in users profiles from devops API")
        return raw_response.json()


    def get_organizations(self, member_id):
        """Get all organizations that the current logged in credential has access to
        
            Args:
                member_id - the id of the user, found from /profiles/me

            Returns:
                A list of organizations
        """
        query_params = { "api-version": "7.2-preview.1", "memberId": member_id}
        raw_response = self._send_request( url=f"https://app.vssps.visualstudio.com/_apis/accounts",
                                          query_parameters=query_params )

        if raw_response.status_code != 200:
            logging.error( "ERROR while getting devops organizations" )
            logging.error( raw_response.json())
            raise Exception("Could not fetch Azure DevOps organizations")
        return raw_response.json()["value"]