"""A module containing the Service Principal credential class"""
from azol.credentials.entraid_credential import EntraIdCredential
from azol.constants import OAUTHFLOWS

class ServicePrincipal( EntraIdCredential ):
    """
        A credential to log in as a service principal
    """

    supportedOAuthFlows = [ OAUTHFLOWS.CLIENT_CREDENTIALS ]
    credentialType="app"
    default_oauth_flow=OAUTHFLOWS.CLIENT_CREDENTIALS
    def __init__( self, client_id, client_secret, *args, **kwargs ):
        super().__init__( *args, **kwargs)
        self._client_id = client_id
        self._client_secret = client_secret

    def get_client_secret( self ):
        """
            Get the client secret being used by this credential object.

            Returns: string containing the client secret
        """
        return self._client_secret
