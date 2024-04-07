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
import urllib.parse
from html.parser import HTMLParser
from azol.constants import IDENTITYPLATFORMURL, DEFAULTSCOPE
from azol.utils import is_token_expired, parse_jwt, string_between
from azol.caches import LocalTokenCache, InMemoryTokenCache
from azol.constants import OAUTHFLOWS, FOCIClients, known_client_redirect_uris
from copy import deepcopy
from azol.utils.auth_utils import start_azure_portal_login, end_azure_portal_login

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
        self._register_flow( OAUTHFLOWS.AUTHORIZATION_CODE, self._authorization_code)
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

    def _authorization_code( self ):
        """
            authorization code flow

            This flow defaults to an idp-initiated login flow. If a client is used that does not
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
        
        supported_SP_initiated_clients={
            FOCIClients.AzurePortal: [start_azure_portal_login, end_azure_portal_login]
        }

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

        client_id=self.credential_object.get_client_id()

        # interrupt login if it is a supported SP-initiated-only client.
        if client_id in supported_SP_initiated_clients.keys():
            SP_init_func=supported_SP_initiated_clients[client_id][0]
            sp_init=SP_init_func() # returns sp_login_model

            resp=requests.get(sp_init.login_uri) # this is login.microsoftonline.com

        else:

            response_type="code"
            scope="openid profile"
            tenant=self._tenant_id

            queryParams= {
                "redirect_uri": self.credential_object._redirect_uri,
                "response_type": response_type,
                "scope": extended_scope_string,
                "response_mode": "form_post",
                "client_id": client_id,
                "code_challenge":"YTFjNjI1OWYzMzA3MTI4ZDY2Njg5M2RkNmVjNDE5YmE",
                "code_challenge_method":"plain"
            }
            resp=requests.get(f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize", params=queryParams, allow_redirects=False)

        # Get the login configurations for the client and tenant
        config_text=string_between(resp.text, "$Config=", ";\n//]]>")
        config=json.loads(config_text)

        # Extract the ctx token, flow token, and canary from the client configurations
        ctx=config["sCtx"]
        flow=config["sFT"]
        canary=config["apiCanary"]

        headers={
            "Canary": canary
        }

        data={
            "username": self.credential_object.get_username(),
            "isOtherIdpSupported": "true",
            "checkPhones": "false",
            "isRemoteNGCSupported": "false",
            "isCookieBannerShown": "false",
            "isFidoSupported": "false",
            "originalRequest": ctx,
            "forceotclogin": "false",
            "isExternalFederationDisallowed": "false",
            "isRemoteConnectSupported": "false",
            "federationFlags": "0",
            "isSignup": "false",
            "isAccessPassSupported": "true",
            "flowToken": flow,
            "Country": "NO"
        }

        resp=requests.post("https://login.microsoftonline.com/common/GetCredentialType", json=data, headers=headers, allow_redirects=False)

        userLoginParams=resp.json()
        flow=userLoginParams["FlowToken"]
        canary=userLoginParams["apiCanary"]
        hasPassword=userLoginParams["Credentials"]["HasPassword"]
        while True:
            if hasPassword:
                password = getpass.getpass('Password:')

            data={
                "login": self.credential_object.get_username(),
                "loginfmt": self.credential_object.get_username(),
                "passwd": password,
                "ctx": ctx,
                "flowToken": flow,
                "LoginOptions": 3
            }

            resp=requests.post("https://login.microsoftonline.com/common/login", data=data, allow_redirects=False)

            config_text=string_between(resp.text, "$Config=", ";\n//]]>")
            config=json.loads(config_text)
            if "sErrorCode" in config.keys():
                if config["sErrorCode"] == "50126":
                    print("Wrong password. Try again.")
            else:
                break

        flow=config["sFT"]
        canary=config["apiCanary"]
        ctx=config["sCtx"]

        supported_mfa_methods=["PhoneAppNotification", "PhoneAppOTP", "OneWaySMS"]

        mfa_option_list=config["arrUserProofs"]

        options=[method["authMethodId"] for method in mfa_option_list ]

        option_list=list(map(str, range(len(options))))

        mfa_option_dict=dict(zip(option_list, options))

        text="Which MFA method would you like to pick?\n"
        for number, option in mfa_option_dict.items():
            if option not in supported_mfa_methods:
                text += f"{number}: {option}(not supported)\n"
            else:
                text += f"{number}: {option}\n"

        text += "\n"

        res=input(text)
        while True:
            if res not in option_list:
                print("Please pick a valid option...")
                res=input()
                continue
            if mfa_option_dict[res] not in supported_mfa_methods:
                print("Please pick a supported MFA option...")
                res=input()
                continue
            break


        mfaMethod=mfa_option_dict[res]

        # Start the authentication process.
        # Spoof the Edge user agent. Endpoint throws "Bad Reputation" error if python requests user agent is used.
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0" 
        }

        data={  
            "AuthMethodId":mfaMethod,
            "Method": "BeginAuth",
            "ctx": ctx,
            "flowToken": flow
        }

        resp=requests.post("https://login.microsoftonline.com/common/SAS/BeginAuth", json=data, headers=headers, allow_redirects=False)

        results=resp.json()
        if not results["Success"]:
            print(f"error while beginning mfa process. error: {results['Message']}. Exiting...")
            exit()


        # Based on the Auth method, complete MFA
        match mfaMethod:
            case "PhoneAppNotification":
                MFAChallenge=results["Entropy"]
                print(f"Please respond to the prompt on the authenticator app with the following number: {MFAChallenge}")

                while True:
                    flow=results["FlowToken"]
                    ctx=results["Ctx"]
                    sessionId=results["SessionId"]

                    query={
                        "authMethodId":mfaMethod
                    }

                    headers={
                        "X-Ms-Ctx": ctx,
                        "X-Ms-Flowtoken": flow,
                        "X-Ms-Sessionid": sessionId,
                        "Canary": canary
                    }

                    resp=requests.get( "https://login.microsoftonline.com/common/SAS/EndAuth", headers=headers, params=query, allow_redirects=False )

                    results=resp.json()
                    if results["Success"]:
                        break
                    sleep(3)

            case "PhoneAppOTP":

                poll_count=0

                while True:
                    poll_count+=1
                    flow=results["FlowToken"]
                    ctx=results["Ctx"]
                    sessionId=results["SessionId"]
                    otp=input("Please enter an OTP from your phone authenticator app: ")
                    headers={
                        "Canary": canary
                    }

                    data={
                        "Method": "EndAuth",
                        "Ctx": ctx,
                        "FlowToken": flow,
                        "AuthMethodId": mfaMethod,
                        "AdditionalAuthData": otp,
                        "pollCount": poll_count,
                        "SessionId": sessionId
                    }

                    resp=requests.post( "https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

                    results=resp.json()
                    if results["Success"]:
                        break
                    else:
                        print(f"Error: {results['Message']}")

            case "OneWaySMS":

                poll_count=0

                while True:
                    poll_count+=1
                    flow=results["FlowToken"]
                    ctx=results["Ctx"]
                    sessionId=results["SessionId"]

                    otp=input("Please enter the code from the SMS: ")

                    headers={
                        "Canary": canary
                    }

                    data={
                        "Method": "EndAuth",
                        "Ctx": ctx,
                        "FlowToken": flow,
                        "AuthMethodId": mfaMethod,
                        "AdditionalAuthData": otp,
                        "pollCount": poll_count,
                        "SessionId": sessionId
                    }

                    resp=requests.post( "https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

                    results=resp.json()
                    if results["Success"]:
                        break
                    else:
                        print(f"Error: {results['Message']}")
            case _:
                print( f"MFA Type {mfaMethod} not supported by azol. exiting")
                exit()

        flow=results["FlowToken"]
        ctx=results["Ctx"]
        sessionId=results["SessionId"]

        data={
            "request": ctx,
            "login": self.credential_object.get_username(),
            "flowToken": flow,
            "mfaAuthMethod": mfaMethod,
            "type":22
        }

        resp=requests.post( "https://login.microsoftonline.com/common/SAS/ProcessAuth", data=data, allow_redirects=False)

        #look for kmsi interrupt. If no interrupt, eat exception and continue
        try:
            config_text=string_between(resp.text, "$Config=", ";\n//]]>")

            config=json.loads(config_text)
            flow=config["sFT"]
            canary=config["apiCanary"]
            ctx=config["sCtx"]
            pgid=config["pgid"]

            # If Keep Me Signed In(KMSI) interrupt, send "yes"
            if pgid=="KmsiInterrupt":
                data={
                    "ctx": ctx,
                    "flowToken": flow,
                    "LoginOptions": 1
                }

                # kmsi = keep me signed in
                resp=requests.post("https://login.microsoftonline.com/kmsi", data=data, allow_redirects=False)
        except ValueError:
            pass

        secrets={}

        class SimpleParser(HTMLParser):
            def handle_starttag(self, tag, attrs):

                name=None
                value=None
                if tag != "input": return
                for attr in attrs:
                    if attr[0] == "name":
                        name=attr[1]
                    if attr[0] == "value":
                        value=attr[1]
                if name is not None and value is not None:
                    secrets[name]=value

        parser = SimpleParser()
        parser.feed(resp.text)

        code=secrets["code"]
        if "state" in secrets.keys():
            state=urllib.parse.unquote(secrets["state"])
        if "id_token" in secrets.keys():
            id_token=secrets["id_token"]

        # if SP-initiated, we need to send the code to the SP. Else, send code to IDP
        if client_id in supported_SP_initiated_clients.keys():
            SP_complete_login_func=supported_SP_initiated_clients[client_id][1]

            sp_login_output=SP_complete_login_func(sp_init.args, code, state, id_token)

            code=sp_login_output

            data={
                "client_id": client_id,
                "code": code,
                "scope": extended_scope_string,
                "grant_type":"authorization_code"
            }

            headers={
                "origin": "http://localhost"
            }

            resp=requests.post(f"https://login.microsoftonline.com/{self._tenant_id}/oauth2/v2.0/token", data=data, allow_redirects=False, headers=headers)

        else:
            data={
                "client_id": client_id,
                "code": code,
                "scope": extended_scope_string,
                "grant_type":"authorization_code",
                "redirect_uri": self.credential_object._redirect_uri,
                "code_verifier": "YTFjNjI1OWYzMzA3MTI4ZDY2Njg5M2RkNmVjNDE5YmE"
            }

            headers={
                "origin": "http://localhost"
            }

            resp=requests.post(f"https://login.microsoftonline.com/{self._tenant_id}/oauth2/v2.0/token", data=data, allow_redirects=False, headers=headers)


        json_response=resp.json()
        new_token_data = {
            "access_token": json_response["access_token"],
            "refresh_token": json_response["refresh_token"],
            "flow_type": "delegated"
        }

        # start refreshing tokens in the http client instead of re-authenticating
        self.oauth_flow=OAUTHFLOWS.REFRESH_TOKEN

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
