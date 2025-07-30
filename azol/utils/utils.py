"""Module that contains functions that are useful when working with Entra ID and Azure"""
import logging
import json
import base64
import time
import uuid
import requests
from cryptography import x509
from cryptography.hazmat.primitives.serialization import pkcs12, Encoding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta, timezone
from dataclasses import dataclass
import hashlib
import hmac
import ctypes
import ctypes.wintypes

class AzolEasyAuthIdpNotSupportedException(Exception):
    """
        Exception that is raised when a user tries to use an
        unsupported easy auth idp
    """

class AzolEasyAuthUnauthorizedZumoTokenException(Exception):
    """
        Exception that is raised when x-zumo-header is not valid
    """

def decrypt_dpapi(encrypted_data):

    buffer = ctypes.create_string_buffer(len(encrypted_data))
    buffer[:len(encrypted_data)] = encrypted_data

    # Call CryptUnprotectData
    class DATA_BLOB(ctypes.Structure):
        _fields_ = [("cbData", ctypes.wintypes.DWORD),
                    ("pbData", ctypes.POINTER(ctypes.c_char))]

    encrypted_blob = DATA_BLOB(len(encrypted_data), buffer)
    decrypted_blob = DATA_BLOB()

    result = ctypes.windll.crypt32.CryptUnprotectData(
        ctypes.byref(encrypted_blob),
        None,
        None,
        None,
        None,
        0,
        ctypes.byref(decrypted_blob)
    )

    if not result:
        raise ctypes.WinError()

    # Extract the decrypted data
    decrypted_data = ctypes.string_at(decrypted_blob.pbData, decrypted_blob.cbData)
    ctypes.windll.kernel32.LocalFree(decrypted_blob.pbData)
    return decrypted_data.decode('utf-8')

@dataclass()
class AzolX509:
    """
        A data class containing an X509 cert in PEM format, both with and without a private key
    """
    public_cert: str
    private_cert: str

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

def create_x509_cert(common_name, password=None, country_name=None, state=None, locality=None,
                     org_name=None, private_key_size=2048, subject_alternative_name=None,
                     cert_name="azol_cert", private_key_public_exponent=65537,
                     cert_valid_days=365):

    private_key = rsa.generate_private_key(
        public_exponent=private_key_public_exponent,
        key_size=2048,
    )

    name_attributes=[]

    if country_name: name_attributes.append(x509.NameAttribute(NameOID.COUNTRY_NAME, country_name))
    if state: name_attributes.append(x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state))
    if locality: name_attributes.append(x509.NameAttribute(NameOID.LOCALITY_NAME, locality))
    if org_name: name_attributes.append(x509.NameAttribute(NameOID.ORGANIZATION_NAME, org_name))
    if common_name: name_attributes.append(x509.NameAttribute(NameOID.COMMON_NAME, common_name))

    subject = x509.Name(name_attributes)

    certificate = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, common_name)])
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        # Certificate valid for 1 year
        datetime.utcnow() + timedelta(days=cert_valid_days)
    )
    if subject_alternative_name: certificate.add_extension(
        x509.SubjectAlternativeName([x509.DNSName(subject_alternative_name.encode())]),
        critical=False,
    )

    signed_cert=certificate.sign(private_key, hashes.SHA256())

    if not password:
        encryption_alg=serialization.NoEncryption()
    else:
        encryption_alg=serialization.BestAvailableEncryption(password)

    pfx = pkcs12.serialize_key_and_certificates(
        name=cert_name.encode(),
        key=private_key,
        cert=signed_cert,
        cas=None,
        encryption_algorithm=encryption_alg
    )
    res=AzolX509(
        public_cert=signed_cert.public_bytes(Encoding.PEM),
        private_cert=base64.b64encode(pfx)
    )
    return res

def decrypt_easy_auth_token(encrypted_b64_data, hex_key):
    key = bytes.fromhex(hex_key)
    encrypted_token_and_iv_bytes = base64.b64decode(encrypted_b64_data)
    iv = encrypted_token_and_iv_bytes[0:16]
    encrypted_token_bytes = encrypted_token_and_iv_bytes[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_token_contents=decryptor.update(encrypted_token_bytes) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_token_contents)
    token_contents = data + unpadder.finalize()
    token_plaintext_json_contents = json.loads(token_contents)
    return token_plaintext_json_contents

def get_easy_auth_user_tokens(zumo_token, site_url):
    """
        Use an X-ZUMO-TOKEN to collect user tokens from Easy Auth

        zumo-token: the easy auth JWT token used for end user authentication

        site_url: the url of the app service or function
    """

    res = requests.get(site_url + "/.auth/me", headers = {"X-ZUMO-AUTH": zumo_token})
    if res.status_code != 200:
        raise AzolEasyAuthUnauthorizedZumoTokenException

    return res.json()

def create_easy_auth_subject(identifier):
    return str(uuid.UUID(bytes_le=hashlib.md5(identifier.encode()).digest())).replace("-", "")

def create_signed_easy_auth_token(site_url, signing_key_hex, user_object_id, user_principal_name,
                                  valid_days=7, idp="aad"):
    """
        Create a signed token that may be used against an easy auth-authenticated app service
        or function, for the provided user.

        Curently, only supports the aad idp.

        site_url: the url of the app service or function, ending with a "/" - this is used for the
                  issuer and audience field of the token
        
        signing_key_hex: the raw signing key in hex format, as found in the environment variables

        user_object_id: the object id of the target user, from entra ID

        user_principal_name: the UPN of the entra user

        valid_days: how long the token should be valid for

        idp: the easyAuth idp to craft a token for. Currently only supports "aad"
    """
    if idp not in ["aad"]: raise AzolEasyAuthIdpNotSupportedException
    signing_key_bytes = bytes.fromhex(signing_key_hex)
    expiry=str(int((datetime.now(timezone.utc) + timedelta(days=valid_days)).timestamp()))
    iat=str(int(datetime.now(timezone.utc).timestamp()))
    nbf=str(int(datetime.now(timezone.utc).timestamp()))
    ver="3"
    idp=idp
    aud=site_url
    iss=site_url
    subject = create_easy_auth_subject(user_principal_name)
    stable_subject = create_easy_auth_subject(user_object_id)
    sub=f"sid:{subject}"
    stable_sid=f"sid:{stable_subject}"

    # create token
    header = {
        "alg": "HS256",
        "typ": "JWT"
    }

    body = {
        "stable_sid": stable_sid,
        "sub": sub,
        "idp": idp,
        "ver": ver,
        "nbf": nbf,
        "exp": expiry,
        "iat": iat,
        "iss": iss,
        "aud": aud
    }

    header_string=json.dumps(header).encode()
    body_string=json.dumps(body).encode()
    b64_header_string=base64.b64encode(header_string).rstrip(b"=")
    b64_body_string=base64.b64encode(body_string).rstrip(b"=")
    body_and_header = b64_header_string + b"." + b64_body_string

    # sign the token
    signature=base64.urlsafe_b64encode(hmac.new(signing_key_bytes, msg=body_and_header, 
                                                digestmod=hashlib.sha256).digest()).rstrip(b"=")
    jwt=body_and_header + b"." + signature
    return jwt.decode()

def get_strings_from_bytes(raw_bytes, min_length=3):
    ascii_string = ''
    current_string = ''
    for b in raw_bytes:
        if 31 < b < 127:
            current_string += chr(b)
        else:
            if len(current_string) >= min_length:
                ascii_string += current_string
                ascii_string += "\n"
            current_string = ''
    return ascii_string.split("\n")


