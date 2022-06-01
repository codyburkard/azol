"""A module containing the parent class for an EntraID Credential"""
from azol.credentials.credential import Credential

class EntraIdCredential( Credential ):
    """
        Parent class of other Entra ID credential classes. Sub-classes simply overwrite "getToken"
    """

    supportedOAuthFlows = []
    credentialType=None
    default_oauth_flow=None
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs)
    