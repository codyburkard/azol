"""A module containing the Azure CLI Credential class"""
import logging

from azol.constants import FOCIClients, known_client_redirect_uris, OAuthResourceIDs
from azol.credentials.user import User
from azol.utils.local.windows import decrypt_dpapi
import os
import json

class AzureCliUser( User ):
    """
        Use an existing Azure CLI session as a User Credential Object
    """

    supportedOAuthFlows = [ "refresh_token", "device_code", "authorization_code" ]
    credentialType="user"
    default_oauth_flow="refresh_token"

    def __init__( self, username=None, tenant_id=None, resource=OAuthResourceIDs.ArmLegacy,
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
        client_id = FOCIClients.MicrosoftAzureCLI
        credential_file_contents = self._get_azure_cli_credential_file()
        refresh_tokens = credential_file_contents["RefreshToken"]
        refresh_token_map = {}
        for refresh_token_key, refresh_token_data in refresh_tokens.items():
            if refresh_token_data['home_account_id'] not in refresh_token_map.keys():
                refresh_token_map[refresh_token_data['home_account_id']] = []
            refresh_token_map[refresh_token_data['home_account_id']].append(refresh_token_data)

        accounts = credential_file_contents["Account"]
        account_map = {}
        for account_key, account in accounts.items():
            if account['username'] not in account_map.keys():
                account_map[account['username']]=[]
            account_map[account['username']].append(account)

        if username not in account_map.keys():
            raise Exception(f"User {username} has no active sessions in the msal cache")

        user_accounts = account_map[username]

        
        if tenant_id != None:
            a=None
            for user in user_accounts:
                if user["realm"] == tenant_id:
                    a=user
                    break
            if a == None:
                raise Exception( f"User {username} has no active sessions in the msal cache for tenant {tenant_id}"
                                 f"Log in with Azure CLI to {tenant_id} first, using az login --tenant {tenant_id}" )

        user_refresh_tokens=refresh_token_map[user_accounts[0]['home_account_id']]
        token_found = False
        for t in user_refresh_tokens:
            if resource in t["target"]:
                token_found=True
                break
        if not token_found:
            raise Exception( f"User {username} has no active sessions in the msal cache for tenant {tenant_id}"
                             f" and resource {resource}" )
        rt = t["secret"]
        super().__init__( username=username, refresh_token=rt, 
                           client_id=client_id, *args, **kwargs )

    def _get_azure_cli_credential_file( self ):
        os_name = os.name
        # nt if windows
        home_directory = os.path.expanduser ("~")
        azure_directory = home_directory + "/.azure"
        msal_file = azure_directory + "/msal_token_cache.bin"
        #throw exception if directory doesnt exist
        if not os.path.isdir(azure_directory):
            raise Exception("Could not find an Azure CLI directory in the user's home directory")
        dir_contents = os.listdir(azure_directory)
        if not os.path.isfile(msal_file):
            raise Exception("msal_token_cache not found in the user's .azure directory")
        fp = open(msal_file, "rb")
        contents = fp.read()
        fp.close()
        if os_name == "nt":
            contents = decrypt_dpapi(contents)
        return json.loads(contents)