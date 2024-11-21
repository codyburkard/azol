"""A module containing the parent credential class"""
import uuid

class Credential:
    """
        Parent class of other Entra ID credential classes. Sub-classes simply overwrite "getToken"
    """

    credentialType=None
    supportedOAuthFlows = []
    default_oauth_flow=None
    def __init__( self, azol_id=None ):

        self._client_id=None
        self._username=None
        if azol_id is None:
            azol_id = uuid.uuid4()
        self._id = str(azol_id)

    def get_default_oauth_flow( self ):
        """
            Get the default oauth flow for the credential type.
            This oauth flow is one of the following:
            - client_credential
            - raw_token
            - refresh_token
            - device_code

            This is defined in each credential class in the default_oauth_flow class variable

            Returns: string containing the name of the oauth flow

        """
        return self.default_oauth_flow

    def get_client_id( self ):
        """
            Get the current client id set in the credential.
    
            Returns: A string containing the client id
        """
        return self._client_id

    def has_ests(self):
        """
            Determine if the credential was initialized with an ESTS cookie. Return False by default.

            Overridden in User Class

            Returns: bool
        """
        return False

    def get_username( self ):
        """
            Get the username of the user object

            Returns: A string containing the username of the credential
        """
        if self._username is not None:
            return self._username
        return None

    def get_id( self ):
        """
            Get the azol id of the object.
    
            Returns: string containing the azol id
        """
        return self._id

    def has_refresh_token(self):
        """
            Check if a user credential object has a refresh token saved.
        
            This will only return true for user objects that have a saved refresh token

            Returns: bool for whether a refresh token exists on the credential
        """
        return False
    