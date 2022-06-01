"""A module containing the Access Token credential class"""
from azol.utils import parse_jwt
from azol.credentials.entraid_credential import EntraIdCredential

class AccessToken( EntraIdCredential ):
    '''
        A credential object that may be used when all that is known is a raw access token
    '''

    supportedOAuthFlows = [ "raw_token" ]
    credentialType="unknown"
    default_oauth_flow="raw_token"
    def __init__( self, token, *args, **kwargs ):
        super().__init__( *args, **kwargs)
        self.token = token
        _, body, _ = parse_jwt(token)
        self._client_id=body["appid"]
