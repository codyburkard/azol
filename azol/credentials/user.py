"""A module containing the User credential class"""
import logging

from azol.constants import FOCIClients, known_client_redirect_uris
from azol.credentials.entraid_credential import EntraIdCredential

class User( EntraIdCredential ):
    """
        A credential object that may be used when a refresh token is stolen, 
        or a username/password combo is stolen
    """

    supportedOAuthFlows = [ "refresh_token", "device_code", "authorization_code" ]
    credentialType="user"
    default_oauth_flow="authorization_code"

    def __init__( self, username=None, refresh_token=None,
                  client_id=FOCIClients.AzurePortal,
                  redirect_uri=known_client_redirect_uris[FOCIClients.AzurePortal], 
                  *args, **kwargs ):
        """
            User objects always have a username, pasword and refresh token. 
            However, sometimes some or all of these are unknown
            during a test. Accept any combo except for password only, 
            and if none are provided, ask the user.
        """

        super().__init__( *args, **kwargs)
        if refresh_token:
            self.default_oauth_flow="refresh_token"
        if username:
            self._username=username.lower()
        else:
            self._username=username
        self._refresh_token=refresh_token

        self._client_id=client_id
        self._redirect_uri=redirect_uri

    def username_is_known( self ):
        """
            Returns True if the username is set on the user object
    
            Returns: bool depending on whether the username is set or not
        """
        return False if self._username is None else True

    def get_client_id(self):
        return self._client_id

    def has_refresh_token(self):
        if self._refresh_token is None:
            return False
        return True

    def get_refresh_token(self):
        """
            Get the current refresh token of the user object
    
            Returns: string containing the raw refresh token, or None
        """
        return self._refresh_token

    def get_username( self ):
        """
            Get the username of the user object

            Returns: username (string)
        """
        return self._username

    def set_username( self, username ):
        """
            Set the username of the user object

            Args:
                -username - (string) The username to set for the user object

            Returns: None
        """
        logging.info("Setting username for user object to %s", username)
        self._username=username
