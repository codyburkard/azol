"""Module that contains functions that are useful when working with Entra ID and Azure"""
import logging
import json
import requests
from azol.utils import string_between
from azol.models.sp_login_init_model import SPLoginModel

def start_azure_portal_login(*args):
    # get a nonce cookie from portal, and have the portal initiate a login flow
    resp=requests.get("https://portal.azure.com/signin/idpRedirect.js/?feature.argsubscriptions=true&feature.showservicehealthalerts=true&feature.prefetchtokens=true&feature.internalgraphapiversion=true&feature.selftoken=true&feature.globalresourcefilter=true&feature.msaljs=true&feature.fetchpolicyforrestypes=true&feature.testcrosscloudpuid=true&feature.useredirecthint=true&feature.usetenanthint=true&idpc=0")

    # Save Portal cookies for later - required when finishing login flow
    portalCookies=resp.cookies

    # Extract portal redirect URL
    portalRedirectUrl=string_between(resp.text, "https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize", "\")", include_start=True)

    init_params=SPLoginModel(
        login_uri=portalRedirectUrl,
        args={
            "portalCookies": portalCookies
        }
    )
    return init_params

def end_azure_portal_login(sp_init_args, code, state, id_token):
    data={
        "state": state,
        "code": code,
        "id_token": id_token
    }

    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }

    resp=requests.post("https://portal.azure.com/signin/index/", data=data, allow_redirects=False, cookies=sp_init_args["portalCookies"], headers=headers)

    boot_params=string_between(resp.text, "MsPortalImpl.setBootstrapStateAndRedirect(", ");")
    portalbootstrapParams="[" + boot_params + "]"
    params=json.loads(portalbootstrapParams)

    token_data=params[1]

    altRefreshToken=token_data["altRefreshToken"]
    oAuthTokenHeader=token_data["oAuthToken"]["authHeader"]
    access_token=oAuthTokenHeader.split()[1] # the header is "bearer token"
    refresh_token=token_data["refreshToken"]
    selfOAuthToken=token_data["selfOAuthToken"]["authHeader"]
    spaAuthCode=token_data["spaAuthCode"]

    return spaAuthCode