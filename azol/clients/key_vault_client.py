"""A module containing an azol key vault http client"""
import logging
from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.constants import KEYVAULTAPIVERSION, OAuthResourceIDs

class KeyVaultClient( OAuthHTTPClient ):
    """
        An HTTP client for interacting with Azure key vaults.
        Works with all credential objects
    """

    def __init__( self, key_vault_name, *args, **kwargs ):
        key_vault_resource_id=OAuthResourceIDs.KeyVault
        kv_base_url=f"https://{key_vault_name}.vault.azure.net"
        super().__init__( oauth_resource=key_vault_resource_id,
                          base_url=kv_base_url, *args, **kwargs)
        self.kv_name = key_vault_name

    def get_keys( self ):
        """Get all keys in the key vault.

        Get all keys from the key vault connected to this client,
        which the credential object can access.

        Returns:
           None if error, or <dict> containing raw response from the key vault
        """
        query_params = { "api-version": KEYVAULTAPIVERSION}
        raw_response = self._send_request( "/keys", query_parameters=query_params )

        if raw_response.status_code != 200:
            logging.error( "ERROR while getting keys from key vault" )
            logging.error( raw_response.json())
            return None
        return raw_response.json()['value']

    def get_secret( self, secret_name, secret_version=None ):
        """Get a secret from the key vault.

        Args:
            - secret_name - (string) The name of the secret
            - secret_version - (string) defaults to None. the version of the secret, or 
                               None if requesting the most recent
        
        Returns:
           None if error, or <dict> containing raw response from the key vault
        """
        query_params = { "api-version": KEYVAULTAPIVERSION}
        
        if secret_version is None:
            raw_response = self._send_request( f"/secrets/{secret_name}",
                                             query_parameters=query_params )
        else:
            raw_response = self._send_request( f"/secrets/{secret_name}/{secret_version}",
                                             query_parameters=query_params )
        if raw_response.status_code != 200:
            logging.error( "ERROR while getting secret from key vault" )
            logging.error( raw_response.json())
            return None
        return raw_response.json()['value']

    def get_secrets( self ):
        """Get all secrets in the key vault.

        Get all secrets from the key vault connected to this client,
        which the credential object can access.

        Returns:
           None if error, or <dict> containing raw response from the key vault
        """
        query_params = { "api-version": KEYVAULTAPIVERSION}
        raw_response = self._send_request( "/secrets", query_parameters=query_params )

        if raw_response.status_code != 200:
            logging.error( "ERROR while listing secrets from key vault" )
            logging.error( raw_response.json())
            return None
        return raw_response.json()['value']

    def get_certificates( self ):
        """Get all certificates in the key vault.

        Get all certificates from the key vault connected to this client,
        which the credential object can access.

        Returns:
           None if error, or <dict> containing raw response from the key vault
        """
        query_params = { "api-version": KEYVAULTAPIVERSION}
        raw_response = self._send_request( "/certificates", query_parameters=query_params )

        if raw_response.status_code != 200:
            logging.error( "ERROR while getting cert from key vault" )
            logging.error( raw_response.json())
            return None
        return raw_response.json()['value']
