"""Module containing utilities for working with Azure DevOps Agents. For use in Azure Devops pipeline tasks."""

import os
from azol.utils.local.windows import decrypt_dpapi
import json
from azol.models.devops_rsa_parameters import DevOpsRSAParameters
import base64
import re

def is_self_hosted():
    '''
        For use in Azure Devops pipeline tasks.

        Tries to identify if this is a self-hosted agent or a Microsoft-hosted agent. 
    '''
    self_hosted = os.getenv("AGENT_ISSELFHOSTED")
    if self_hosted == "0":
        return False
    if self_hosted == "1":
        return True
    return None

def get_agent_home_directory():
    '''
        For use in Azure Devops pipeline tasks.

        Tries to read the agent home directory environment variable
    '''
    return os.getenv("AGENT_HOMEDIRECTORY")

def is_windows():
    '''
        For use in Azure Devops pipeline tasks.

        Returns true if windows OS else false
    '''
    if os.name == "nt":
        return True
    else:
        return False

def get_rsa_credentials_file():
    '''
        For use in Azure Devops pipeline tasks.

        Search and read the agent's .credentials_rsaparams file. Decrypt it if
        this is a Windows machine.

        returns a dictionary containing the raw contents of the file.
    '''


    home_directory = get_agent_home_directory()
    if is_self_hosted():
        rsa_credentials_file = os.path.normpath( home_directory + "/.credentials_rsaparams") 
        raw_contents = b""
        with open(rsa_credentials_file, "rb") as f:
            raw_contents = raw_contents + f.read()
        if is_windows():
            decrypted_bytes = decrypt_dpapi(raw_contents)
        else:
            decrypted_bytes = raw_contents
            
        credentials = json.loads(decrypted_bytes)
        return credentials
    else:
        raise Exception("Microsoft hosted agents do not have a .credentuals_rsaparams file")

def load_rsa_credentials(credentials_dict):
    '''
        For use in Azure Devops pipeline tasks.

        Load a .credentials_rsaparams file into a DevOpsRSAParameters object

            Args:
                credentials_dict - (dict) A dictionary containing the deserialized contents 
                                        of a -credentials_rsaparams file
            Returns:
                A DevOpsRSAParameters object containing the RSA parameters

    '''
    b64_d = credentials_dict["d"]
    b64_p = credentials_dict["p"]
    b64_q = credentials_dict["q"]
    b64_dq = credentials_dict["dq"]
    b64_dp = credentials_dict["dp"]
    b64_inverseq = credentials_dict["inverseQ"]
    b64_modulus = credentials_dict["modulus"]
    b64_exponent = credentials_dict["exponent"]
    d = int.from_bytes(base64.b64decode(b64_d), "big")
    q = int.from_bytes(base64.b64decode(b64_q), "big")
    p = int.from_bytes(base64.b64decode(b64_p), "big")
    dq = int.from_bytes(base64.b64decode(b64_dq), "big")
    dp = int.from_bytes(base64.b64decode(b64_dp), "big")
    inverseq = int.from_bytes(base64.b64decode(b64_inverseq), "big")
    modulus = int.from_bytes(base64.b64decode(b64_modulus), "big")
    exponent = int.from_bytes(base64.b64decode(b64_exponent), "big")
    rsa_parameters = DevOpsRSAParameters(
        d=d,
        p=p,
        q=q,
        dp=dp,
        dq=dq,
        inverseq=inverseq,
        modulus=modulus,
        exponent=exponent
    )
    return rsa_parameters


def get_agent_id():
    '''
        For use in Azure Devops pipeline tasks.

        return the agent ID from environment variables

         Returns:
            The agent ID, or None if the environment variable cannot be found

    '''
    return os.getenv("AGENT_ID")


def get_agent_file():
    '''
        For use in Azure Devops pipeline tasks.

        Get the contents of the agent file for the build agent

         Returns:
            A dictionary containing the contents of the .agent file
    '''
    home_directory = get_agent_home_directory()
    agent_file = os.path.normpath( home_directory + "/.agent") 
    f = open(agent_file, "rb")
    agent_data=json.load(f)
    f.close()
    return agent_data

def get_credentials_file():
    '''
        For use in Azure Devops pipeline tasks.

        Get the contents of the .credentials file for the build agent

         Returns:
            A dictionary containing the contents of the .credentials file
    '''
    home_directory = get_agent_home_directory()
    credentials_file = os.path.normpath( home_directory + "/.credentials") 
    f = open(credentials_file, "rb")
    agent_data=json.load(f)
    f.close()
    return agent_data

def get_latest_session_id():
    '''
        For use in Azure Devops pipeline tasks.

        Try to get the latest session ID from the agent logs.

        The session ID is needed in order to kill an agent and spoof it. 
        The session ID can be found in 'agent_home/_diag/Agent_date-utc.logs' files.
        This method searches for the most recent file, and looks for the last session
        ID in those logs. This shoud represent the current session ID

         Returns:
            A session ID if one was found, else None
    '''
    home_directory = get_agent_home_directory()
    diagnostics_directory = os.path.normpath(home_directory + "/_diag") 
    files = [f for f in os.listdir(diagnostics_directory) 
             if os.path.isfile(os.path.join(diagnostics_directory, f))
             and f.startswith("Agent")]
    files.sort()
    latest = files[-1]
    full_path=os.path.join(diagnostics_directory, latest)
    with open(full_path) as f: content = f.read()
    q = re.compile("[sS]ession '([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})'",re.S|re.M)
    session_ids = q.findall(content)
    if session_ids == []: return None
    return session_ids[-1]
