"""Module that contains functions that are useful when working with Entra ID and Azure"""
import logging
import json
import base64
import time
import requests

def string_between(whole_string, start_string, end_string, include_start=False):
    i=whole_string.index(start_string)
    z=whole_string[i:].index(end_string)+i
    if not include_start:
        i=i+len(start_string)
    sub_string=whole_string[i:z]
    return sub_string

def get_tenant_id( tenant_name ):
    """
        Call the openid-configuration of a domain name to check if it exists in Entra ID as a tenant

        Returns: (string) tenant ID if the domain name is registered, or None
    """
    response = requests.get(f"https://login.microsoftonline.com/{tenant_name}/"
                            "v2.0/.well-known/openid-configuration", timeout=10)

    if response.status_code == 400:
        logging.info("domain name not registered as a tenant")
        return None
    well_known=response.json()
    issuer=well_known['token_endpoint']
    tenant_id = issuer.split('/')[3]
    return tenant_id

def parse_jwt( token ):
    """
        parse the jwt and return an object for each piece

        Args:
            - token - (string) The raw ascii token to parse

        Returns: a tuple ( <dict>header, <dict>data, <string>signature )
    """
    def fix_padding( raw_string ):
        while True:
            if len(raw_string) % 4 == 0:
                break
            raw_string += "="
        return raw_string
    if token is None:
        return True
    header, data, signature = token.split(".")
    headerb64 = fix_padding( header )
    datab64 = fix_padding( data )
    signatureb64 = fix_padding( signature )
    header = json.loads(base64.b64decode(headerb64).decode())
    data = json.loads(base64.b64decode(datab64).decode())
    return header, data, signatureb64

def is_token_expired( token, padding_time=0 ):
    """
        Check if the current access token is expired. The credential
        object caches access tokens in memory. This method will check
        if the current cached token is expired.

        Args:
            - paddingTime - (int) Check if token expires, [paddingTime]
                                  seconds before it actually expires.
                                  Useful if you want to get a new token
                                  prior to expiry by some margin.
        
        Returns: True if expired, False if not expired
        
    """
    _, data, _ = parse_jwt(token)
    expiry = data[ "exp" ]
    current_time = int( time.time() )
    if current_time >= expiry-padding_time:
        return True
    return False
