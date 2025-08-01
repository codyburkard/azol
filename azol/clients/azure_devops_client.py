"""A module containing an Azure Devops HTTP Client"""
import logging
from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.constants import OAuthResourceIDs

class AzureDevopsClient( OAuthHTTPClient ):
    """
        An HTTP client for interacting with the Azure Devops API
    """

    def __init__( self, *args, **kwargs ):
        devops_resource_id=OAuthResourceIDs.AzureDevOps
        devops_base_url=f"https://dev.azure.com"

        super().__init__( oauth_resource=devops_resource_id,
                          base_url=devops_base_url, *args, **kwargs)

    def get_projects( self, organization=None ):
        """Get all projects that the current logged in credential has access to
        
        Returns:
            A list of projects
        """
        query_params = { "api-version": "7.2-preview.4"}
        raw_response = self._send_request( f"/{organization}/_apis/projects", query_parameters=query_params )

        if raw_response.status_code != 200:
            logging.error( "ERROR while getting devops projects" )
            logging.error( raw_response.json())
            raise Exception("Could not fetch Azure DevOps Projects")
        return raw_response.json()["value"]

    def get_self(self):
        query_params = { "api-version": "7.2-preview.1"}
        raw_response = self._send_request(url="https://aex.dev.azure.com/_apis/User/User",
                                          method="GET", query_parameters=query_params)
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting logged in user" )
            logging.error( raw_response.json())
            raise Exception("Could not get logged in user from devops API")
        return raw_response.json()
    
    def get_profile(self):
        query_params = { "api-version": "7.2-preview.1"}
        raw_response = self._send_request(url="https://app.vssps.visualstudio.com/_apis/profile/profiles/me",
                                          method="GET", query_parameters=query_params)
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting logged in users profiles" )
            logging.error( raw_response.json())
            raise Exception("Could not get logged in users profiles from devops API")
        profile_data = raw_response.json()
        return {
            "displayName": profile_data["coreAttributes"]["DisplayName"]["value"],
            "id": profile_data["id"],
            "EmailAddress": profile_data["coreAttributes"]["EmailAddress"]["value"],
            "avatar": profile_data["coreAttributes"]["Avatar"]["value"]["value"],
        }

    def get_web_session_token(self, token_name="Aex.DeploymentProfile", token_type=0):
        query_params = { "api-version": "7.2-preview.1"}
        body = {
            'appId': '00000000-0000-0000-0000-000000000000',
            "force": False,
            "namedTokenId": token_name,
            "tokenType": token_type
        }
        raw_response = self._send_request(url="https://aex.dev.azure.com/_apis/WebPlatformAuth/SessionToken",
                                          method="POST", json=body, query_parameters=query_params)
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting session token" )
            logging.error( raw_response.json())
            raise Exception("Could not get Web Session token in Azure devops")
        return raw_response.json()

    def get_organizations(self, member_id):
        """Get all organizations that the current logged in credential has access to
        
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