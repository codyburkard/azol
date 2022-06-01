"""A module containing the Application Object credential class"""
from azol.credentials.entraid_credential import EntraIdCredential
from azol.constants import OAUTHFLOWS

class ApplicationObject( EntraIdCredential ):
    """
        A credential that may be used when a client secret and 
        client id of an application object is known
    """

    supportedOAuthFlows = [ OAUTHFLOWS.CLIENT_CREDENTIALS ]
    credentialType="app"
    default_oauth_flow=OAUTHFLOWS.CLIENT_CREDENTIALS

    def __init__( self, client_id, client_secret, *args, **kwargs ):
        super().__init__( *args, **kwargs)
        self._client_id = client_id
        self._client_secret = client_secret

    def get_client_secret( self ):
        """Get the client secret that is saved in this credential class

            Returns: A string containing the client secret
        """
        return self._client_secret
