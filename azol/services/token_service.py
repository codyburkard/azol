"""
    Module containing the token service, which is used for fetching tokens
    for the azol entra ID OAuth clients
"""
import logging
import uuid
import json
from time import sleep
import requests
import getpass
import base64
import urllib.parse
from html.parser import HTMLParser
from azol.constants import IDENTITYPLATFORMURL, DEFAULTSCOPE
from azol.utils import is_token_expired, parse_jwt, string_between
from azol.caches import LocalTokenCache, InMemoryTokenCache
from azol.constants import OAUTHFLOWS, FOCIClients, known_client_redirect_uris, UserAgents
from copy import deepcopy
from cryptography import x509
from cryptography.hazmat.primitives.serialization import pkcs12, Encoding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta

from .token_service_helpers import build_scope_string, auth_code_flow, ests_login_flow

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
                  offline_access_scope, azol_id=None, 
                  useragent=UserAgents.Windows_Edge):
        self.credential_object=cred
        self._tenant=tenant_id
        self._useragent=useragent
        self.oauth_flow=oauth_flow
        self.secrets_provider=secrets_provider
        self.oauth_resource=oauth_resource
        self.scopes=scopes
        self.default_scope=default_scope
        self.profile_scope=profile_scope
        self.openid_scope=openid_scope
        self.offline_access_scope=offline_access_scope
        self.ests_cookie=None
        self.ests_persistent_cookie=None
        if self.credential_object.has_ests():
            cookies=self.credential_object.get_ests()
            self.ests_cookie=cookies.ests
            self.ests_persistent_cookie=cookies.ests_persistent
        else:
            self.ests_cookie=None
            self.ests_persistent_cookie=None
        if self.credential_object.has_refresh_token():
            self._refresh_token=self.credential_object.get_refresh_token()
        else:
            self._refresh_token=None

        if self.credential_object.credentialType == "user":
            self.flow_type="delegated"
        else:
            self.flow_type="application"

        self._client_id=self.credential_object.get_client_id()

        self.registered_token_flows={}
        self._register_flow( OAUTHFLOWS.CLIENT_CREDENTIALS, self._get_client_credential_token )
        self._register_flow( OAUTHFLOWS.REFRESH_TOKEN , self._refresh_token_flow )
        self._register_flow( OAUTHFLOWS.DEVICE_CODE, self._device_code )
        self._register_flow( OAUTHFLOWS.RAW_TOKEN, self._raw_token )
        self._register_flow( OAUTHFLOWS.AUTHORIZATION_CODE, self._authorization_code )
        if azol_id is None:
            azol_id = uuid.uuid4()
        self._id = azol_id

        if use_persistent_cache:
            self.token_cache=LocalTokenCache()
        else:
            self.token_cache=InMemoryTokenCache()

        if ( OAUTHFLOWS.DEVICE_CODE in self.credential_object.supportedOAuthFlows 
             or OAUTHFLOWS.REFRESH_TOKEN in self.credential_object.supportedOAuthFlows
              or OAUTHFLOWS.AUTHORIZATION_CODE in self.credential_object.supportedOAuthFlows ):
            get_cached_token_result = self.token_cache.try_get_token(self._tenant,
                                                            self._client_id,
                                                            self.default_scope, self.scopes,
                                                            self.oauth_resource,
                                                            self.credential_object._username )
            if get_cached_token_result is not None:
                refresh_token=get_cached_token_result["refresh_token"]
                ests=get_cached_token_result["ests_cookie"]
                ests_persistent_cookie=get_cached_token_result["ests_persistent_cookie"]
                self._refresh_token=refresh_token
                self.ests_cookie=ests
                self.ests_persistent_cookie=ests_persistent_cookie
                self.oauth_flow=OAUTHFLOWS.REFRESH_TOKEN
            else:
                logging.info( "Tried to use a token from the cache but none exists" )

    def set_tenant( self, tenant ):
        self._tenant=tenant

    def set_scope(self, scopes, default, profile, offline_access, openid):
        self.scopes=scopes
        self.default_scope=default
        self.profile_scope=profile
        self.offline_access_scope=offline_access
        self.openid_scope=openid

    def switch_client( self, client_id ):
        self._client_id=client_id

    def refresh_token( self ):
        if self.credential_object.credentialType != "user":
            raise Exception("Cannot refresh a token for a non user credential type")
        if self._refresh_token == None:
            raise Exception('Cannot refresh token - no refresh token present to refresh')

        token_data_object=self._refresh_token_flow()
        refresh_token = token_data_object["refresh_token"]
        access_token=token_data_object["access_token"]
        self._refresh_token=refresh_token

        self.token_cache.cache_or_update( access_token, self._tenant,
                                         self._client_id,
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
        token_data=self.token_cache.try_get_token( self._tenant,
                                                  self._client_id,
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

    def _sign_token( self, validity, client_id ):
        now=int(datetime.now().timestamp()-100)
        later=int(datetime.now().timestamp()+validity)

        header={
            "alg": "RS256",
            "typ": "JWT",
            "x5t": x5t,#'CDC6D70E0D295EDA890CC75E0721E0C5080D11F1'#x5t#"hOBcHZi846VCHSJbFAs26Go9VTQ"
        }
        body={
            "aud": f"https://login.microsoftonline.com/{self._tenant}/oauth2/v2.0/token",
            "exp": later,
            "iss": client_id,
            "jti": str(uuid.uuid4()),
            "nbf": now,
            "iat": now,
            "sub": client_id
        }

    def fetch_token( self, validity=28800 ):
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
        ests_cookie=None
        ests_persistent_cookie=None
        if "ests" in token_data_object.keys():
            ests_cookie=token_data_object["ests"]
        if "estspersistent" in token_data_object.keys():
            ests_persistent_cookie=token_data_object["estspersistent"]

        if self._tenant=="common":
            _, body, _ = parse_jwt(access_token)
            self.set_tenant(body["tid"])
            
        if self.offline_access_scope and self.credential_object.credentialType=="user":
            refresh_token = token_data_object["refresh_token"]
            self.token_cache.cache_or_update( access_token, self._tenant,
                                            self._client_id,
                                            self.default_scope, self.scopes, self.oauth_resource,
                                            refresh_token=refresh_token,
                                            username=self.credential_object.get_username(),
                                            ests_cookie=ests_cookie,
                                            ests_persistent_cookie=ests_persistent_cookie )
        else:
            self.token_cache.cache_or_update( access_token, self._tenant,
                                            self._client_id,
                                            self.default_scope, self.scopes, self.oauth_resource,
                                            ests_cookie=ests_cookie,
                                            ests_persistent_cookie=ests_persistent_cookie )
        return access_token

    def get_cached_token( self ):
        """
            Get a cached token from the token Cache if it exists.
            Will also return expired tokens.

            Returns: string of ascii encoded token, or None if no token found in cache
        """
        token_data=self.token_cache.try_get_token( self._tenant,
                                                self._client_id,
                                                self.default_scope, self.scopes,
                                                self.oauth_resource,
                                                self.credential_object.get_username() )

        if token_data is None:
            return None

        token = token_data["access_token"]
        return token

    def get_client_id(self):
        return self._client_id

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

        url = f"{IDENTITYPLATFORMURL}/{self._tenant}/oauth2/v2.0/token"
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
            scope_string = f"{self.oauth_resource}/{DEFAULTSCOPE}"
            extended_scope_string=scope_string+extension
        else:
            expanded_scopes = [ f"{self.oauth_resource}/{s}" for s in self.scopes ]
            scope_string = " ".join(expanded_scopes)
            extended_scope_string=scope_string+extension
        
        credential_type=self.credential_object.get_credential_type()
        now=int(datetime.now().timestamp()-100)
        later=int(datetime.now().timestamp()+10000)
        
        if credential_type == "x509":

            cert_and_key=self.credential_object.get_certificate()
            cert=cert_and_key.cert
            key=cert_and_key.key
            

            der_binary=cert.certificate.public_bytes(Encoding.DER)
            digest = hashes.Hash(hashes.SHA256())
            digest.update(der_binary)
            thumbprint_bytes=digest.finalize()
            x5t=base64.urlsafe_b64encode(thumbprint_bytes).decode().rstrip('=')
            header={
                "alg": "RS256",
                "typ": "JWT",
                "x5t#S256": x5t,
            }
            assertion_body={
                "aud": f"https://login.microsoftonline.com/{self._tenant}/oauth2/v2.0/token",
                "exp": later,
                "iss": self.credential_object.get_client_id(),
                "jti": str(uuid.uuid4()),
                "nbf": now,
                "iat": now,
                "sub": self.credential_object.get_client_id()
            }

            
            b64_header=base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip('=')
            b64_body=base64.urlsafe_b64encode(json.dumps(assertion_body).encode()).decode().rstrip('=')
            header_body=b64_header + '.' + b64_body
            signature=base64.urlsafe_b64encode(key.sign(header_body.encode(), padding=padding.PKCS1v15(), 
                                               algorithm=hashes.SHA256())).decode().rstrip("=")
            jwt=header_body + "." + signature

            body={
                "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
                "client_assertion": jwt,
                "client_id": self.credential_object.get_client_id(),
                "scope": extended_scope_string,
                "grant_type": OAUTHFLOWS.CLIENT_CREDENTIALS
            }

        elif credential_type == "secret":
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

            
            body = {
                "client_id": self.credential_object.get_client_id(),
                "client_secret": client_secret,
                "scope": extended_scope_string,
                "grant_type": OAUTHFLOWS.CLIENT_CREDENTIALS
            }

        response = requests.post( url, data=body, timeout=10, headers={"User-Agent": self._useragent} )
        response_status = response.status_code
        logging.info( "response status for client credential grant: %s", str(response_status) )
        if response_status != 200:
            error_msg = response.content
            logging.error( "Client credential grant failed for client id "
                          "%s at scope %s."
                          " Raw Identity Platform error message:\r\n%s", 
                          self._client_id, extended_scope_string,
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

        client_id=self._client_id

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
            scope_string = f"{self.oauth_resource}/{DEFAULTSCOPE}"
            extended_scope_string=scope_string+extension
        else:
            expanded_scopes = [ f"{self.oauth_resource}/{s}" for s in self.scopes ]
            scope_string = " ".join(expanded_scopes)
            extended_scope_string=scope_string+extension

        body = {
            "client_id" : client_id,
            "refresh_token": self._refresh_token,
            "scope": extended_scope_string,
            "grant_type": "refresh_token"
        }

        headers={
            "origin": "http://localhost"
        }

        response = requests.post( "https://login.microsoftonline.com/"
                                 f"{self._tenant}/oauth2/v2.0/token", data=body,  timeout=10, headers={"User-Agent": self._useragent} )
        if "error" in response.json().keys():
            error_msg = response.content
            msg_dict = json.loads(error_msg)
            eid_error_code=msg_dict["error_description"].split(":")[0]
            if eid_error_code=="AADSTS50076":
                # We need to use MFA to switch tenants.
                # This requires an ESTSAUTH or ESTSPERSISTENTAUTH cookie
                if self.ests_cookie!=None:
                    # Use the ests cookie to start MFA again
                    new_token_data=ests_login_flow(self._tenant, self._client_id,
                                                   self.ests_cookie, self.ests_persistent_cookie, 
                                                   self.credential_object.get_username(),
                                                   extended_scope_string, self.credential_object._redirect_uri)
                    self._refresh_token=new_token_data["refresh_token"]
                    return new_token_data
            else:
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

    def _authorization_code( self ):
        """
            authorization code flow

            This flow defaults to an idp-initiated login flow.
            
            If a client is used that does not
            support idp-initiated flows, it will fail by default. However, some clients such as 
            Azure Portal are supported by Azol, and Azol will interrupt the login to force an
            SP-initiated flow. The supported clients that only support SP intiated flows include:

              - Azure Portal

            Returns: dictionary containing token data
        """
        if OAUTHFLOWS.AUTHORIZATION_CODE not in self.credential_object.supportedOAuthFlows:
            logging.error( "credential type of %s does not support OAuth flow of "
                          "type authorization_code.", self.credential_object )
            raise Exception( "Credential does not support OAuth Flow" )
        
        client_id=self._client_id

        redirect_url=self.credential_object._redirect_uri

        scope_string=build_scope_string(self.oauth_resource, self.scopes, self.default_scope,
                                        self.openid_scope, self.profile_scope, self.offline_access_scope )
        
        new_token_data=auth_code_flow(self._tenant, self.credential_object.get_username(), client_id, redirect_url, scope_string)
        
        self.ests_cookie=new_token_data["ests"]
        self.ests_persistent_cookie=new_token_data["estspersistent"]

        self._refresh_token=new_token_data["refresh_token"]
        # start refreshing tokens in the http client instead of re-authenticating
        self.oauth_flow=OAUTHFLOWS.REFRESH_TOKEN

        return new_token_data

    def _device_code( self ):
        """
            device code flow

            Returns: dictionary containing token data
        """

        client_id = self._client_id
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
            scope_string = f"{self.oauth_resource}/{DEFAULTSCOPE}"
            extended_scope_string=scope_string+extension
        else:
            expanded_scopes = [ f"{self.oauth_resource}/{s}" for s in self.scopes ]
            scope_string = " ".join(expanded_scopes)
            extended_scope_string=scope_string+extension
        body = {
            "client_id": client_id,
            "scope": extended_scope_string, 
        }
        response = requests.post( "https://login.microsoftonline.com/"
                                 f"{self._tenant}/oauth2/v2.0/devicecode",
                                 data=body, timeout=10, headers={"User-Agent": self._useragent} )
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
                                     f"{self._tenant}/oauth2/v2.0/token",
                                     data=body, timeout=10, headers={"User-Agent": self._useragent} )
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
