"""A module containing the Service Principal credential class"""
from azol.credentials.entraid_credential import EntraIdCredential
from azol.constants import OAUTHFLOWS
from cryptography.hazmat.primitives.serialization import pkcs12
import base64

class ServicePrincipal( EntraIdCredential ):
    """
        A credential to log in as a service principal
    """

    supportedOAuthFlows = [ OAUTHFLOWS.CLIENT_CREDENTIALS ]
    credentialType="app"
    default_oauth_flow=OAUTHFLOWS.CLIENT_CREDENTIALS
    def __init__( self, client_id, client_secret=None, pfx_path=None, b64_cert=None,
                  cert_password=None, *args, **kwargs ):
        super().__init__( *args, **kwargs)
        if not client_secret and not pfx_path and not b64_cert:
            raise Exception("No secret added for the service principal.")
        cert=None
        if client_secret is not None:
            self._credential_type="secret"
        elif b64_cert is not None:
            self._credential_type="x509"
            if cert_password is None:
                cert=pkcs12.load_pkcs12(base64.b64decode(b64_cert), cert_password)
            else:
                cert=pkcs12.load_pkcs12(base64.b64decode(b64_cert), cert_password.encode())
        elif pfx_path is not None:
            self._credential_type="x509"
            f = open(pfx_path, 'rb')
            contents=f.read()
            f.close()
            cert=pkcs12.load_key_and_certificates(contents, cert_password.encode())
        self._cert=cert
        self._client_id = client_id
        self._client_secret = client_secret
        self._cert_password=cert_password

    def get_credential_type( self ):
        """
            Returns: string - secret or x509, depending on what type of secret was defined for
                     the service principal
        """
        return self._credential_type

    def get_certificate( self ):
        """
            Get the certificate being used by this credential object.

            Returns: cryptography PKCS12KeyAndCertificates object
        """
        return self._cert

    def get_client_secret( self ):
        """
            Get the client secret being used by this credential object.

            Returns: string containing the client secret
        """
        return self._client_secret
