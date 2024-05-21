"""A module containing the User credential class"""
import logging

from azol.constants import FOCIClients, known_client_redirect_uris
from azol.credentials.entraid_credential import EntraIdCredential
from azol.models.ests_cookie import ESTS

class User( EntraIdCredential ):
    """
        A credential object that may be used when a refresh token is stolen, 
        or a username/password combo is stolen
    """

    supportedOAuthFlows = [ "refresh_token", "device_code", "authorization_code" ]
    credentialType="user"
    default_oauth_flow="device_code"

    def __init__( self, username=None, refresh_token=None, ests=None,
                 ests_persistent=None, redirect_uri=None,
                 client_id=FOCIClients.MicrosoftAzurePowershell,  
                  *args, **kwargs ):
        """
            User objects always have a username, pasword and refresh token. 
            However, sometimes some or all of these are unknown
            during a test. Accept any combo except for password only, 
            and if none are provided, ask the user.

            If an ests cookies is provided, it will be overridden if an ests
            cookies is also found for the user in the cache. to avoid this, 
            consider useing use_persistent_cache=False
        """

        super().__init__( *args, **kwargs)
        if refresh_token:
            self.default_oauth_flow="refresh_token"
        if username:
            self._username=username.lower()
        else:
            self._username=username
        self._refresh_token=refresh_token
        self._ests=ests
        self._ests_persistent=None

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

    def has_ests(self):
        if self._ests is None and self._ests_persistent is None:
            return False
        return True

    def has_refresh_token(self):
        if self._refresh_token is None:
            return False
        return True

    def get_ests(self):
        """
            Get the user's ests and ests_persistent cookies
    
            Returns: ESTS object containing ests cookies for the user
        """
        cookies=ESTS(
            ests=self._ests,
            ests_persistent=self._ests_persistent
        )
        return cookies

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
