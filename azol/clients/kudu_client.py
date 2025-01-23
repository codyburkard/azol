"""A module containing a client for interacting with the Kudu API.
"""
import logging

from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.constants import OAuthResourceIDs


class KuduClient( OAuthHTTPClient ):
    """
        An HTTP client for interacting with the App Service Kudu resource
    """
    
    def __init__( self, app_service_name, *args, **kwargs ):
        kudu_base_url=f"https://{app_service_name}.scm.azurewebsites.net"
        super().__init__( oauth_resource=OAuthResourceIDs.Arm, base_url=kudu_base_url, *args, **kwargs)

        self.app_service_name = app_service_name

    def command( self, command, directory=None ):
        """Execute a command via the Kudu API.
        
        Returns:
            A dict containing the results of the command

        """
        body={
            "command":command
        }
        if directory is not None:
            body["dir"]=directory
        raw_response = self.post( "/api/command", json=body )

        if raw_response.status_code != 200:
            logging.error( "ERROR while running command via kudu: %s", raw_response.content )
            raise Exception()
        res = raw_response.json()

        return res
    
    def get_settings( self ):
        """Get settings
        
        Returns:
            A dict containing the settings

        """
        
        raw_response = self.get( "/api/settings" )

        if raw_response.status_code != 200:
            logging.error( "ERROR while running command via kudu: %s", raw_response.content )
            raise Exception()
        res = raw_response.json()

        return res
    
    def get_setting( self, setting ):
        """Get setting
        
        Returns:
            A dict containing the settings

        """
        
        raw_response = self.get( f"/api/settings/{setting}" )

        if raw_response.status_code != 200:
            logging.error( "ERROR while running command via kudu: %s", raw_response.content )
            raise Exception()
        res = raw_response.content

        return res

    