"""A module containing the parent credential class"""
import uuid
from azol.credentials.credential import Credential
from azol.models import DevOpsRSAParameters
import logging
import json
import base64

class DevOpsAgentCredential( Credential ):
    """
        Credential for authenticating as an Azure DevOps Agent

        The agent authenticates with an RSA key and a client_credential grant towards devops.
        The RSA key can be input as a devops agent credentials file path or as the raw RSA
        parameters, base64 encoded.
    """

    credentialType="devops_agent_credential"

    def __init__( self, rsa_parameters_file_path=None, rsa_parameters=None, *args, **kwargs ):
        super().__init__( *args, **kwargs )

        if rsa_parameters_file_path:
            if rsa_parameters:
                logging.warning( "DevOpsAgentCredential: rsa_parameters ignored because"
                                 "rsa_parameters_file_path argument was also supplied."
                                 "rsa_parameters_file_path argument will be used" )
            f=open(rsa_parameters_file_path, encoding="ascii")
            #print(f.readlines())
            params_json=json.load(f)
            f.close()

            b64_d = params_json["d"]
            b64_p = params_json["p"]
            b64_q = params_json["q"]
            b64_dq = params_json["dq"]
            b64_dp = params_json["dp"]
            b64_inverseq = params_json["inverseQ"]
            b64_modulus = params_json["modulus"]
            b64_exponent = params_json["exponent"]
            d = int.from_bytes(base64.b64decode(b64_d), "big")
            q = int.from_bytes(base64.b64decode(b64_q), "big")
            p = int.from_bytes(base64.b64decode(b64_p), "big")
            dq = int.from_bytes(base64.b64decode(b64_dq), "big")
            dp = int.from_bytes(base64.b64decode(b64_dp), "big")
            inverseq = int.from_bytes(base64.b64decode(b64_inverseq), "big")
            modulus = int.from_bytes(base64.b64decode(b64_modulus), "big")
            exponent = int.from_bytes(base64.b64decode(b64_exponent), "big")
            self.rsa_parameters = DevOpsRSAParameters(
                d=d,
                p=p,
                q=q,
                dp=dp,
                dq=dq,
                inverseq=inverseq,
                modulus=modulus,
                exponent=exponent
            )
        elif rsa_parameters:
            self.rsa_parameters = rsa_parameters