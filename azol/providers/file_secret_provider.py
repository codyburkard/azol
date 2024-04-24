"""A module containing a local file secret provider"""
import uuid
from pathlib import Path
import json
from azol.constants import AZOLSECRETPROVIDERFOLDER

class FileSecretProvider( object ):
    """
        A local file secret provider for the azol token service
    """

    def __init__( self, file=None, directory=AZOLSECRETPROVIDERFOLDER ):

        if file is None:
            file = uuid.uuid4()
        self.file = file
        self.file_path=directory + "/" + self.file
        Path(directory).mkdir(parents=True, exist_ok=True)

    def get_secret( self, secret_reference ):
        """
            Get a secret value based on its reference name

            Args:
                - secretReference - (string) The secret reference name

            Returns string - contents of the secret 
        """
        with open( self.file_path, 'r', encoding="utf-8") as f:
            contents=json.load(f)
        if secret_reference not in contents.keys():
            return None
        return contents[secret_reference]
