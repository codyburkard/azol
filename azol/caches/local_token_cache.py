"""Module containing a token cache that persists on the local filesystem"""
import json
import sys
from pathlib import Path
import logging

from azol.constants import TOKENCACHEDIR
from azol.caches.azol_cache import AzolCache

class LocalTokenCache( AzolCache ):
    """class for an azol token cache that persists on the local filesystem"""

    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs)
        Path(TOKENCACHEDIR).mkdir(parents=True, exist_ok=True)
        self.file_name=TOKENCACHEDIR+"/default"
        Path(self.file_name).touch(exist_ok=True)

    def try_get_token(self, *args, **kwargs):
        """
            Attempt to get a token from the cache that matches the requested tenantId,
            clientId, scope, and user.
        """

        with open(self.file_name, "r", encoding="utf-8") as f:
            try:
                self.tokens=json.load(fp=f)
            except json.decoder.JSONDecodeError:
                logging.info("cannot load token cache as %s because it is an empty file. "
                             "SNo tokens saved", self.file_name)
                return None

        return super().try_get_token(*args, **kwargs)

    def cache_or_update(self, *args, **kwargs):
        """
            Saves an access and refresh token to the cache, or updates an existing entry.
            Overwrites the existing local cache file
        """

        #read configuration from file
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                self.tokens=json.load(fp=f)
        except json.decoder.JSONDecodeError as msg:
            data=""
            with open(self.file_name, "r", encoding="utf-8") as f:
                data = f.read()
            if data == "":
                logging.warning("Token cache was empty. initializing")
                with open(self.file_name, "w", encoding="utf-8") as f:
                    json.dump({}, fp=f)
                self.tokens={}
            else:
                logging.error( "fatal error: %s", msg)
                sys.exit()

        super().cache_or_update(*args, **kwargs)

        #re-write the new tokenCache to the file
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.tokens, indent=4, sort_keys=True, fp=f)
