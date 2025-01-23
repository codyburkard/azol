import logging
import uuid
import json
from time import sleep
import requests
import getpass
import urllib.parse
import string
import random
from html.parser import HTMLParser
from azol.constants import IDENTITYPLATFORMURL, DEFAULTSCOPE
from azol.utils import is_token_expired, parse_jwt, string_between
from azol.caches import LocalTokenCache, InMemoryTokenCache
from azol.constants import OAUTHFLOWS, FOCIClients, known_client_redirect_uris, UserAgents
from copy import deepcopy
from azol.utils.auth_utils import start_azure_portal_login, end_azure_portal_login

def build_scope_string(oauth_resource, scopes=[], default_scope=None, openid_scope=None,
                       profile_scope=None, offline_access_scope=None ):
    extension = ""
    if openid_scope:
        extension+=f" openid"
    if profile_scope:
        extension+=f" profile"
    if offline_access_scope:
        extension+=f" offline_access"

    if default_scope:
        scope_string = f"{oauth_resource}{DEFAULTSCOPE}"
        extended_scope_string=scope_string+extension
    else:
        expanded_scopes = [ f"{oauth_resource}{s}" for s in scopes ]
        scope_string = " ".join(expanded_scopes)
        extended_scope_string=scope_string+extension
    return extended_scope_string

def ests_portal_login_flow(tenant, username, cookies, useragent=UserAgents.Windows_Edge):

    resp=requests.get(f"https://portal.azure.com:443/signin/index/@{tenant}?feature.argsubscriptions=true&feature.showservicehealthalerts=true&feature.prefetchtokens=true&feature.internalgraphapiversion=true&feature.selftoken=true&feature.globalresourcefilter=true&feature.msaljs=true&feature.fetchpolicyforrestypes=true&feature.testcrosscloudpuid=true&feature.useredirecthint=true&feature.usetenanthint=true&idpc=0")

    portalCookies=resp.cookies
    
    # Extract portal redirect URL
    portalRedirectUrl=string_between(resp.text, f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize", "\")", include_start=True)

    # Begin auth code flow with portal-generated login flow
    resp=requests.get(portalRedirectUrl, cookies=cookies)

    # Get the login configurations for the client and tenant
    config_text=string_between(resp.text, "$Config=", ";\n//]]>")
    config=json.loads(config_text)

    # Extract the ctx token, flow token, and canary from the client configurations
    ctx=config["sCtx"]
    flow=config["sFT"]
    canary=config["apiCanary"]

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
        "User-Agent": useragent 
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
                    "Canary": canary,
                    "User-Agent": useragent
                }

                resp=requests.get( f"https://login.microsoftonline.com/common/SAS/EndAuth", headers=headers, params=query, allow_redirects=False )

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
                    "Canary": canary,
                    "User-Agent": useragent
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

                resp=requests.post( f"https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

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
                    "Canary": canary,
                    "User-Agent": useragent
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

                resp=requests.post( f"https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

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
        "login": username,
        "flowToken": flow,
        "mfaAuthMethod": mfaMethod,
        "type":22
    }

    resp=requests.post( f"https://login.microsoftonline.com/common/SAS/ProcessAuth", data=data, allow_redirects=False, headers={"User-Agent": useragent})

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
            resp=requests.post("https://login.microsoftonline.com/kmsi", data=data, allow_redirects=False, headers={"User-Agent": useragent})

    except ValueError:
        pass

    secrets={}

    class SecretExtractor(HTMLParser):
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

    parser = SecretExtractor()
    parser.feed(resp.text)
    code=secrets["code"]
    if "state" in secrets.keys():
        state=urllib.parse.unquote(secrets["state"])
    if "id_token" in secrets.keys():
        id_token=secrets["id_token"]
    data={
        "state": state,
        "code": code,
        "id_token": id_token
    }

    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }

    resp=requests.post("https://portal.azure.com/signin/index/", data=data, allow_redirects=False, cookies=portalCookies, headers=headers)

    boot_params=string_between(resp.text, "MsPortalImpl.setBootstrapStateAndRedirect(", ");")
    portalbootstrapParams="[" + boot_params + "]"
    params=json.loads(portalbootstrapParams)

    portal_token_data=params[1]
    return portal_token_data

def ests_login_flow( tenant, client_id, ests, ests_persistent, username, scope_string, redirect_url ):
    # if ESTSAUTH and ESTSAUTHPERSISTENT are both present, we can only use one.
    # request will fail if both are used. preference should be ESTSAUTHPERSISTENT
    if ests_persistent is not None:
        cookies={
            "ESTSAUTHPERSISTENT": ests_persistent
        }
    elif ests_persistent is None and ests is not None:
        cookies={
            "ESTSAUTH": ests
        }
    else:
        raise Exception()
    
    if client_id==FOCIClients.AzurePortal:
        portalTokens=ests_portal_login_flow(tenant, username, cookies)
        code=portalTokens["spaAuthCode"]
    else:
        code_challenge=''.join(random.choices(string.ascii_letters, k=43))
        queryParams= {
            "redirect_uri": redirect_url,
            "response_type": "code",
            "scope": scope_string,
            "response_mode": "form_post",
            "client_id": client_id,
            "code_challenge":code_challenge,
            "code_challenge_method":"plain"
        }
        resp=requests.get(f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize", params=queryParams, allow_redirects=False, cookies=cookies)


        # Get the login configurations for the client and tenant
        config_text=string_between(resp.text, "$Config=", ";\n//]]>")
        config=json.loads(config_text)

        # Extract the ctx token, flow token, and canary from the client configurations
        ctx=config["sCtx"]
        flow=config["sFT"]
        canary=config["apiCanary"]

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

                    resp=requests.get( f"https://login.microsoftonline.com/common/SAS/EndAuth", headers=headers, params=query, allow_redirects=False )

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

                    resp=requests.post( f"https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

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

                    resp=requests.post( f"https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

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
            "login": username,
            "flowToken": flow,
            "mfaAuthMethod": mfaMethod,
            "type":22
        }

        resp=requests.post( f"https://login.microsoftonline.com/common/SAS/ProcessAuth", data=data, allow_redirects=False)
        

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

        class SecretExtractor(HTMLParser):
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

        parser = SecretExtractor()
        parser.feed(resp.text)
        code=secrets["code"]
        state=None
        id_token=None
        if "state" in secrets.keys():
            state=urllib.parse.unquote(secrets["state"])
        if "id_token" in secrets.keys():
            id_token=secrets["id_token"]
        data={
                "code": code
            }
        if state is not None:
            data["state"]=state
        if id_token is not None:
            data["id_token"]=id_token

        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }

    if client_id==FOCIClients.AzurePortal:
        data={
            "client_id": client_id,
            "code": code,
            "scope": scope_string,
            "grant_type":"authorization_code"
        }
    
    else:
        data={
            "client_id": client_id,
            "code": code,
            "scope": scope_string,
            "grant_type":"authorization_code",
            "redirect_uri": redirect_url,
            "code_verifier": code_challenge
        }

    headers={
        "origin": "http://localhost"
    }

    resp=requests.post(f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token", data=data, allow_redirects=False, headers=headers)

    json_response=resp.json()
    new_token_data = {
        "access_token": json_response["access_token"],
        "refresh_token": json_response["refresh_token"],
        "flow_type": "delegated"
    }
    return new_token_data

def get_portal_tokens(tenant, username):
    ests=None
    ests_persistent=None
    # Azure portal has a weird auth code flow. Perform extra steps
    # Azure Portal step 1: get portal-generated redirect uri with nonce
    resp=requests.get(f"https://portal.azure.com:443/signin/index/@{tenant}?feature.argsubscriptions=true&feature.showservicehealthalerts=true&feature.prefetchtokens=true&feature.internalgraphapiversion=true&feature.selftoken=true&feature.globalresourcefilter=true&feature.msaljs=true&feature.fetchpolicyforrestypes=true&feature.testcrosscloudpuid=true&feature.useredirecthint=true&feature.usetenanthint=true&idpc=0")

    # Save Portal cookies for later - required when finishing login flow
    portalCookies=resp.cookies

    # Extract portal redirect URL
    portalRedirectUrl=string_between(resp.text, f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize", "\")", include_start=True)

    # Begin auth code flow with portal-generated login flow
    resp=requests.get(portalRedirectUrl)

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
        "username": username,
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

    resp=requests.post(f"https://login.microsoftonline.com/{tenant}/GetCredentialType", json=data, headers=headers, allow_redirects=False)

    userLoginParams=resp.json()
    flow=userLoginParams["FlowToken"]
    canary=userLoginParams["apiCanary"]
    hasPassword=userLoginParams["Credentials"]["HasPassword"]

    while True:
        if hasPassword:
            password = getpass.getpass('Password:')

        data={
            "login": username,
            "loginfmt": username,
            "passwd": password,
            "ctx": ctx,
            "flowToken": flow,
            "LoginOptions": 3
        }

        resp=requests.post(f"https://login.microsoftonline.com/{tenant}/login", data=data, allow_redirects=False)
        
        # if an exception occurs, there is probably no MFA requirement. code is returned in a form_post
        try:
            config_text=string_between(resp.text, "$Config=", ";\n//]]>")
            config=json.loads(config_text)
            if "arrUserProofs" not in config.keys():
                require_mfa=False
            if "sErrorCode" in config.keys():
                if config["sErrorCode"] == "50126":
                    print("Wrong password. Try again.")
            else:
                break
        except:
            require_mfa=False
            break

    if "arrUserProofs" in config.keys():
        require_mfa=True

    if require_mfa:
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

                    resp=requests.get( f"https://login.microsoftonline.com/common/SAS/EndAuth", headers=headers, params=query, allow_redirects=False )

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

                    resp=requests.post( f"https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

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

                    resp=requests.post( f"https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

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
            "login": username,
            "flowToken": flow,
            "mfaAuthMethod": mfaMethod,
            "type":22
        }

        resp=requests.post( f"https://login.microsoftonline.com/common/SAS/ProcessAuth", data=data, allow_redirects=False)
        

    #look for kmsi interrupt. If no interrupt, eat exception and continue
    try:
        config_text=string_between(resp.text, "$Config=", ";\n//]]>")

        if "ESTSAUTH" in resp.cookies.keys():
            ests= resp.cookies.get("ESTSAUTH")

            
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

            if "ESTSAUTHPERSISTENT" in resp.cookies.keys():
                estspersistent= resp.cookies.get("ESTSAUTHPERSISTENT")

    except ValueError:
        pass

    secrets={}

    class SecretExtractor(HTMLParser):
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

    parser = SecretExtractor()
    parser.feed(resp.text)
    code=secrets["code"]
    if "state" in secrets.keys():
        state=urllib.parse.unquote(secrets["state"])
    if "id_token" in secrets.keys():
        id_token=secrets["id_token"]
    data={
        "state": state,
        "code": code,
        "id_token": id_token
    }

    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }

    resp=requests.post("https://portal.azure.com/signin/index/", data=data, allow_redirects=False, cookies=portalCookies, headers=headers)

    boot_params=string_between(resp.text, "MsPortalImpl.setBootstrapStateAndRedirect(", ");")
    portalbootstrapParams="[" + boot_params + "]"
    params=json.loads(portalbootstrapParams)

    token_data=params[1]
    token_data["ESTSAUTH"]=ests
    token_data["ESTSAUTHPERSISTENT"]=estspersistent
    return token_data

def auth_code_flow(tenant, username, client_id, redirect_url, scope_string):
    ests=None
    ests_persistent=None
    if client_id == FOCIClients.AzurePortal:
        portalTokens=get_portal_tokens(tenant, username)
        code=portalTokens["spaAuthCode"]

    else:
        code_challenge=''.join(random.choices(string.ascii_letters, k=43))
        queryParams= {
            "redirect_uri": redirect_url,
            "response_type": "code",
            "scope": scope_string,
            "response_mode": "form_post",
            "client_id": client_id,
            "code_challenge":code_challenge,
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
            "username": username,
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

        resp=requests.post(f"https://login.microsoftonline.com/{tenant}/GetCredentialType", json=data, headers=headers, allow_redirects=False)

        userLoginParams=resp.json()
        flow=userLoginParams["FlowToken"]
        canary=userLoginParams["apiCanary"]
        hasPassword=userLoginParams["Credentials"]["HasPassword"]

        while True:
            if hasPassword:
                password = getpass.getpass('Password:')

            data={
                "login": username,
                "loginfmt": username,
                "passwd": password,
                "ctx": ctx,
                "flowToken": flow,
                "LoginOptions": 3
            }

            resp=requests.post(f"https://login.microsoftonline.com/{tenant}/login", data=data, allow_redirects=False)
            
            # if an exception occurs, there is probably no MFA requirement. code is returned in a form_post
            try:
                config_text=string_between(resp.text, "$Config=", ";\n//]]>")
                config=json.loads(config_text)
                if "arrUserProofs" not in config.keys():
                    require_mfa=False
                if "sErrorCode" in config.keys():
                    if config["sErrorCode"] == "50126":
                        print("Wrong password. Try again.")
                else:
                    break
            except:
                require_mfa=False
                break

        if "arrUserProofs" in config.keys():
            require_mfa=True

        if require_mfa:
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

                        resp=requests.get( f"https://login.microsoftonline.com/common/SAS/EndAuth", headers=headers, params=query, allow_redirects=False )

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

                        resp=requests.post( f"https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

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

                        resp=requests.post( f"https://login.microsoftonline.com/common/SAS/EndAuth", json=data, headers=headers, allow_redirects=False )

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
                "login": username,
                "flowToken": flow,
                "mfaAuthMethod": mfaMethod,
                "type":22
            }

            resp=requests.post( f"https://login.microsoftonline.com/common/SAS/ProcessAuth", data=data, allow_redirects=False)
            
            if "ESTSAUTH" in resp.cookies.keys():
                ests= resp.cookies.get("ESTSAUTH")
            

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
                if "ESTSAUTHPERSISTENT" in resp.cookies.keys():
                    ests_persistent= resp.cookies.get("ESTSAUTHPERSISTENT")
        except ValueError:
            pass

        secrets={}

        class SecretExtractor(HTMLParser):
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

        parser = SecretExtractor()
        parser.feed(resp.text)
        code=secrets["code"]
        if "state" in secrets.keys():
            state=urllib.parse.unquote(secrets["state"])
        if "id_token" in secrets.keys():
            id_token=secrets["id_token"]

    if client_id==FOCIClients.AzurePortal:
        data={
            "client_id": client_id,
            "code": code,
            "scope": scope_string,
            "grant_type":"authorization_code"
        }
        ests=portalTokens["ESTSAUTH"]
        ests_persistent=portalTokens["ESTSAUTHPERSISTENT"]
    
    else:
        data={
            "client_id": client_id,
            "code": code,
            "scope": scope_string,
            "grant_type":"authorization_code",
            "redirect_uri": redirect_url,
            "code_verifier": code_challenge
        }
    
    headers={
        "origin": "http://localhost"
    }

    resp=requests.post(f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token", data=data, allow_redirects=False, headers=headers)

    json_response=resp.json()
    new_token_data = {
        "access_token": json_response["access_token"],
        "refresh_token": json_response["refresh_token"],
        "flow_type": "delegated",
        "ests": ests,
        "estspersistent": ests_persistent
    }
    return new_token_data