"""A module containing a key vault secret provider"""
import uuid
from azol.clients.key_vault_client import KeyVaultClient
from azol.credentials.user import User

class KeyVaultProvider:
    """
        A Key Vault secret provider for the azol token service
    """

    def __init__( self, username, key_vault_name, tenant_id, client_id=None, azol_id=None,
                  credential=None, cache_refresh_token=True ):
        self.key_vault_name = key_vault_name
        self.client_id=client_id
        self.tenant_id=tenant_id
        self.cache_refresh_token=cache_refresh_token
        if azol_id is None:
            azol_id = uuid.uuid4()
        self._id = azol_id
        if credential is None:
            self.credential = User(username=username)
        else:
            self.credential = credential
        self.kv_client = KeyVaultClient( key_vault_name, cred=self.credential,
                                       tenant=tenant_id, oauth_flow="device_code",
                                       use_persistent_cache=cache_refresh_token )

    def get_id( self ):
        """
            Get the azol id of the provider

            Returns:
                string containing the azol id
        """
        return self._id

    def get_secret( self, secret_reference ):
        """
            Get a secret using the provider

            Args:
                - secret_reference - A string containing the reference text for the secret
            
            Returns:
                string containing the secret
        """
        response = self.kv_client.get_secret( secret_reference )
        if response is None:
            return None
        return response
    