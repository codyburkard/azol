"""
    Module containing the token service, which is used for fetching tokens
    for the azol entra ID OAuth clients
"""
import logging
import uuid
from time import sleep
import requests
from azol.constants import IDENTITYPLATFORMURL, DEFAULTSCOPE
from azol.utils import is_token_expired, parse_jwt
from azol.caches import LocalTokenCache, InMemoryTokenCache
from azol.constants import OAUTHFLOWS
from copy import deepcopy

class IdentityPlatformRequestFailedException(Exception):
    """
        Exception that is raised when requests to the identity platform
        unexpectedly fail
    """

class TokenService( object ):
    """
        Generic OAuth2 token service for Entra ID
    """

    def __init__( self, cred, tenant_id, oauth_flow,
                  secrets_provider, use_persistent_cache, oauth_resource,
                  scopes, default_scope, profile_scope, openid_scope,
                  offline_access_scope, azol_id=None):

        self.credential_object=deepcopy(cred)
        self._tenant_id=tenant_id
        self.oauth_flow=oauth_flow
        self.secrets_provider=secrets_provider
        self.oauth_resource=oauth_resource
        self.scopes=scopes
        self.default_scope=default_scope
        self.profile_scope=profile_scope
        self.openid_scope=openid_scope
        self.offline_access_scope=offline_access_scope
        if self.credential_object.has_refresh_token():
            self._refresh_token=self.credential_object.get_refresh_token()
        else:
            self._refresh_token=None

        if self.credential_object.credentialType == "user":
            self.flow_type="delegated"
        else:
            self.flow_type="application"

        self.registered_token_flows={}
        self._register_flow( OAUTHFLOWS.CLIENT_CREDENTIALS, self._get_client_credential_token )
        self._register_flow( OAUTHFLOWS.REFRESH_TOKEN , self._refresh_token_flow )
        self._register_flow( OAUTHFLOWS.DEVICE_CODE, self._device_code )
        self._register_flow( OAUTHFLOWS.RAW_TOKEN, self._raw_token )
        if azol_id is None:
            azol_id = uuid.uuid4()
        self._id = azol_id

        if use_persistent_cache:
            self.token_cache=LocalTokenCache()
        else:
            self.token_cache=InMemoryTokenCache()

        if ( OAUTHFLOWS.DEVICE_CODE in self.credential_object.supportedOAuthFlows 
             or OAUTHFLOWS.REFRESH_TOKEN in self.credential_object.supportedOAuthFlows ):
            get_cached_token_result = self.token_cache.try_get_token(self._tenant_id,
                                                            self.credential_object.get_client_id(),
                                                            self.default_scope, self.scopes,
                                                            self.oauth_resource,
                                                            self.credential_object._username )
            if get_cached_token_result is not None:
                refresh_token=get_cached_token_result["refresh_token"]
                self._refresh_token=refresh_token
                self.oauth_flow=OAUTHFLOWS.REFRESH_TOKEN
            else:
                logging.info( "Tried to use a token from the cache but none exists" )

    def set_tenant( self, tenant ):
        self._tenant_id=tenant

    def set_scope(self, scopes, default, profile, offline_access, openid):
        self.scopes=scopes
        self.default_scope=default
        self.profile_scope=profile
        self.offline_access_scope=offline_access
        self.openid_scope=openid

    def switch_client( self, client_id ):
        self.credential_object.set_client_id(client_id)

    def refresh_token( self ):
        if self.credential_object.credentialType != "user":
            raise Exception("Cannot refresh a token for a non user credential type")
        if self._refresh_token == None:
            raise Exception('Cannot refresh token - no refresh token present to refresh')

        token_data_object=self._refresh_token_flow()
        refresh_token = token_data_object["refresh_token"]
        access_token=token_data_object["access_token"]
        self._refresh_token=refresh_token

        self.token_cache.cache_or_update( access_token, self._tenant_id,
                                         self.credential_object.get_client_id(),
                                         self.default_scope, self.scopes, self.oauth_resource,
                                         refresh_token=refresh_token,
                                         username=self.credential_object.get_username() )
        return access_token

    def get_refresh_token_if_exists( self ):
        """
            Returns the current refresh token saved by the token service

            Returns: string - raw refresh token if it is saved, else None
        """
        if self.credential_object.credentialType != "user":
            raise Exception("Cannot use a refresh token for a non user credential type")

        if self._refresh_token is not None:
            return self._refresh_token
        return None

    def get_id( self ):
        """
            Get the azol Id of the tokenService object

            Returns string - azol id
        """
        return self._id

    def _register_flow( self, flow_name, flow_function ):
        """
            Internal method. register an oauth flow function with the tokenService tokenFlows map

            Args:
                - flow_name - string - the azol name of the oauth flow to call
                - flow_function -function - the function that
                                  should be added to the registered flows map

            Returns None
        """
        self.registered_token_flows[ flow_name ] = flow_function

    def get_cached_token_if_not_expired( self ):
        """
            Get a cached token from the token Cache if it exists

            Returns: string of ascii encoded token, or None if no token found in cache
        """
        token_data=self.token_cache.try_get_token( self._tenant_id,
                                                  self.credential_object.get_client_id(),
                                                  self.default_scope, self.scopes,
                                                  self.oauth_resource,
                                                  self.credential_object.get_username() )

        if token_data is None:
            logging.info("get_cached_token_if_not_expired: Token does not exist in cache")
            return None
        token = token_data["access_token"]
        if is_token_expired( token ):
            return None
        return token

    def fetch_token( self ):
        """
            Initiates an authorization flow and caches a new token.

            Returns: None if a token couldnt be fetched, or the access token
        """
        get_token_function = self.registered_token_flows[self.oauth_flow]
        token_data_object = get_token_function()
        if token_data_object is None:
            logging.error("Could not get a new token")
            raise IdentityPlatformRequestFailedException()
        access_token = token_data_object["access_token"]

        if self._tenant_id=="common":
            _, body, _ = parse_jwt(access_token)
            self.set_tenant(body["tid"])
        if self.offline_access_scope and self.credential_object.credentialType=="user":
            refresh_token = token_data_object["refresh_token"]
            self.token_cache.cache_or_update( access_token, self._tenant_id,
                                            self.credential_object.get_client_id(),
                                            self.default_scope, self.scopes, self.oauth_resource,
                                            refresh_token=refresh_token,
                                            username=self.credential_object.get_username() )
        else:
            self.token_cache.cache_or_update( access_token, self._tenant_id,
                                            self.credential_object.get_client_id(),
                                            self.default_scope, self.scopes, self.oauth_resource )
        return access_token

    def get_cached_token( self ):
        """
            Get a cached token from the token Cache if it exists.
            Will also return expired tokens.

            Returns: string of ascii encoded token, or None if no token found in cache
        """
        token_data=self.token_cache.try_get_token( self._tenant_id,
                                                self.credential_object.get_client_id(),
                                                self.default_scope, self.scopes,
                                                self.oauth_resource,
                                                self.credential_object.get_username() )

        if token_data is None:
            return None

        token = token_data["access_token"]
        return token

    def _raw_token( self ):
        """
            registered when a raw token is used as a credential -
                dont perform any oauth flow, just return the raw token

            :returns dictionary containing token data
        """
        if OAUTHFLOWS.RAW_TOKEN not in self.credential_object.supportedOAuthFlows:
            logging.error( "credential type of %s does not support "
                          "login flow of type raw_token.", 
                          self.credential_object )
            raise Exception( "Unsupported Flow" )
        credential_value = self.credential_object.token
        if credential_value.startswith("secret:"):
            if self.secrets_provider:
                return self.secrets_provider.getSecret(credential_value.split("secret:")[1])
            else:
                logging.error( "critical error: secret referenced used "
                              "for raw_token credential, but no secret provider configured. "
                              "exiting..." )
                exit()
        new_token_data = {
            "access_token": self.credential_object.token,
            "refresh_token": None,
            "flow_type": "unknown"
        }
        return new_token_data

    def _get_client_credential_token( self ):
        """
            client credential grant

            Returns: dictionary containing token data
        """
        if OAUTHFLOWS.CLIENT_CREDENTIALS not in self.credential_object.supportedOAuthFlows:
            logging.error( "credential type of %s does not"
                          " support OAuth flow of type client_credential.",
                          self.credential_object )
            raise Exception( "Unsupported OAuth Flow" )

        url = f"{IDENTITYPLATFORMURL}/{self._tenant_id}/oauth2/v2.0/token"

        secret_from_credential = self.credential_object.get_client_secret()
        if secret_from_credential.startswith("secret:"):
            if self.secrets_provider:
                client_secret = self.secrets_provider.get_secret(
                       secret_from_credential.split("secret:")[1] )
            else:
                logging.error( "critical error: secret referenced used for servicePrincipal "
                              "credential, but no secret provider configured. exiting..." )
                raise Exception("secret refrerence used for sp credential, "
                                "but there no secret provider")
        else:
            client_secret = secret_from_credential

        openid_scope = "openid"
        profile_scope = "profile"
        offline_access_scope = "offline_access"
        extension = ""
        if self.openid_scope:
            extension+=f" {openid_scope}"
        if self.profile_scope:
            extension+=f" {profile_scope}"
        if self.offline_access_scope:
            extension+=f" {offline_access_scope}"

        if self.default_scope:
            scope_string = f"{self.oauth_resource}{DEFAULTSCOPE}"
            extended_scope_string=scope_string+extension
        else:
            expanded_scopes = [ f"{self.oauth_resource}{s}" for s in self.scopes ]
            scope_string = " ".join(expanded_scopes)
            extended_scope_string=scope_string+extension
        body = {
            "client_id": self.credential_object.get_client_id(),
            "client_secret": client_secret,
            "scope": extended_scope_string,
            "grant_type": OAUTHFLOWS.CLIENT_CREDENTIALS
        }

        response = requests.post( url, data=body, timeout=10 )
        response_status = response.status_code
        logging.info( "response status for client credential grant: %s", str(response_status) )
        if response_status != 200:
            error_msg = response.content
            logging.error( "Client credential grant failed for client id "
                          "%s at scope %s."
                          " Raw Identity Platform error message:\r\n%s", 
                          self.credential_object.get_client_id(), extended_scope_string,
                          error_msg )
            return
        response_body = response.json()
        token = response_body[ "access_token" ]
        new_token_data = {
            "access_token": token,
            "flow_type": "application"
        }
        return new_token_data

    def _refresh_token_flow( self ):
        """
            Refresh token flow

            Returns: dictionary containing token data
        """
        if OAUTHFLOWS.REFRESH_TOKEN not in self.credential_object.supportedOAuthFlows:
            logging.error( "credential type of %s does not support OAuth flow of "
                          "type refresh_token.", self.credential_object )
            raise Exception( "Unsupported OAuth Flow" )

        client_id=self.credential_object.get_client_id()

        openid_scope = "openid"
        profile_scope = "profile"
        offline_access_scope = "offline_access"
        extension = ""
        if self.openid_scope:
            extension+=f" {openid_scope}"
        if self.profile_scope:
            extension+=f" {profile_scope}"
        if self.offline_access_scope:
            extension+=f" {offline_access_scope}"

        if self.default_scope:
            scope_string = f"{self.oauth_resource}{DEFAULTSCOPE}"
            extended_scope_string=scope_string+extension
        else:
            expanded_scopes = [ f"{self.oauth_resource}{s}" for s in self.scopes ]
            scope_string = " ".join(expanded_scopes)
            extended_scope_string=scope_string+extension

        body = {
            "client_id" : client_id,
            "refresh_token": self._refresh_token,
            "scope": extended_scope_string,
            "grant_type": "refresh_token"
        }

        response = requests.post( "https://login.microsoftonline.com/"
                                 f"{self._tenant_id}/oauth2/v2.0/token", data=body, timeout=10 )
        if "error" in response.json().keys():
            error_msg = response.content
            logging.error( "Error: error while refreshing token. "
                           "Raw Error Message from Identity Platform: %s", error_msg )
            raise IdentityPlatformRequestFailedException()
        if "refresh_token" in response.json().keys():
            token = response.json()[ "access_token" ]
            refresh_token = response.json()[ "refresh_token" ]

            # It is possible that we dont know whos refresh token this is.
            # Extract the username and set it in the credential object
            if not self.credential_object.username_is_known():
                _, body, _ = parse_jwt(token)
                self.credential_object.set_username(body["unique_name"])
            new_token_data = {
                "access_token": token,
                "refresh_token": refresh_token,
                "flow_type": "delegated"
            }
            return new_token_data

    def _device_code( self ):
        """
            device code flow

            Returns: dictionary containing token data
        """

        client_id = self.credential_object.get_client_id()
        if OAUTHFLOWS.DEVICE_CODE not in self.credential_object.supportedOAuthFlows:
            logging.error( "credential type of %s does not support "
                          "OAuth flow of type device_code.", self.credential_object.__name__ )
            raise Exception( "Unsupported OAuth Flow" )
        openid_scope = "openid"
        profile_scope = "profile"
        offline_access_scope = "offline_access"
        extension = ""
        if self.openid_scope:
            extension+=f" {openid_scope}"
        if self.profile_scope:
            extension+=f" {profile_scope}"
        if self.offline_access_scope:
            extension+=f" {offline_access_scope}"

        if self.default_scope:
            scope_string = f"{self.oauth_resource}{DEFAULTSCOPE}"
            extended_scope_string=scope_string+extension
        else:
            expanded_scopes = [ f"{self.oauth_resource}{s}" for s in self.scopes ]
            scope_string = " ".join(expanded_scopes)
            extended_scope_string=scope_string+extension
        body = {
            "client_id": client_id,
            "scope": extended_scope_string, 
        }
        response = requests.post( "https://login.microsoftonline.com/"
                                 f"{self._tenant_id}/oauth2/v2.0/devicecode",
                                 data=body, timeout=10 )
        if response.status_code != 200:
            logging.error("Error while getting a device code: %s", response.content)
            raise IdentityPlatformRequestFailedException()
        auth_url = response.json()[ "verification_uri" ]
        user_code = response.json()[ "user_code" ]
        device_code = response.json()[ "device_code" ]
        print( f"Visit site {auth_url} from a browser, and enter code {user_code}" )
        timeout = 24
        retry_number = 0
        while True:
            sleep( 5 )
            logging.info( "Polling device code endpoint for auth token..." )
            body = {
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                "client_id": client_id,
                "device_code": device_code
            }
            response = requests.post( "https://login.microsoftonline.com/"
                                     f"{self._tenant_id}/oauth2/v2.0/token",
                                     data=body, timeout=10 )
            if response.status_code != 200:

                if response.json()[ "error" ] != "authorization_pending":
                    logging.error( "error while logging in via device code flow. description: %s",
                                  response.json()[ 'error_description' ] )
                    logging.error( response.json()[ "error_description" ] )
                    raise Exception("Error getting token during device_code flow.")
                logging.info("Authorization pending, continuing to poll...")
                retry_number = retry_number + 1
                if retry_number == timeout:
                    logging.error( "timeout on device code flow. token not retrieved" )
                    raise Exception("Error getting token during device_code flow.")
                continue

            token = response.json()[ "access_token" ]
            refresh_token = response.json()[ "refresh_token" ]

            # check if the user logged in with the user that they specified
            _, body, _ = parse_jwt(token)
            username=body["unique_name"].lower()

            # We need to know the username at startup so that we can check for cached tokens
            if username != self.credential_object.get_username():
                logging.error("Please log in with the same user specified in the User() object." )
                raise Exception("username of credential object does not "
                                "match username of logged-in user")

            self._refresh_token=refresh_token

            # start refreshing tokens from now on
            self.oauth_flow=OAUTHFLOWS.REFRESH_TOKEN

            # We dont know what user the user logged in with at this point.
            # Extract the username from the token
            _, body, _ = parse_jwt(token)
            logging.info( "Retrieved refresh token for the user" )
            break

        new_token_data = {
            "access_token": token,
            "refresh_token": refresh_token,
            "flow_type": "delegated"
        }
        return new_token_data
