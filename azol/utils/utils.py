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
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.x509.oid import NameOID
from datetime import datetime, timedelta
from dataclasses import dataclass

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