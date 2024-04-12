"""Module containing a parent class for an azol cache object"""
import logging
from azol.constants import DEFAULTSCOPE

class AzolCache:
    """Azol parent class for token caching"""

    def __init__( self, ):
        self.tokens={}


    def try_get_token(self, tenant_id, client_id, default_scope, scopes,
                      oauth_resource, username=None):
        """
            Attempt to get a token from the cache that matches the requested tenant_id,
            client_id, scope, and user.

            Args:
                - tenant_id: string - the tenant Id that issued the token
                - client_id: string - the Azure service principal client Id to fetch a token for
                - default_scope: bool - if true, use the default scope for the resource
                - scopes: list - a list of scopes to be issued in the token
                - oauth_resource: string - the OAuth resource issued in the token.
                - username: string - optional. The username that should be issued in the token

            Returns:
                Dictionary containing the scope, username, access and refresh tokens 
        """

        if default_scope:
            scopes=[DEFAULTSCOPE]

        if tenant_id not in self.tokens.keys():
            return None

        if oauth_resource not in self.tokens[tenant_id].keys():
            return None

        if client_id not in self.tokens[tenant_id][oauth_resource].keys():
            return None

        for token_data in self.tokens[tenant_id][oauth_resource][client_id]:

            if token_data["type"] == "delegated":

                if username != token_data["username"]:
                    continue

            # If the token in the cache has all of the scopes that are in the requested scope list,
            # return the token data

            token_found=True

            # Assume the token being reviewed contains all the required scopes. If a scope is found
            # that is not in the list of required scopes, set token_found to False.
            # Otherwise, return token_data after testing all scopes
            for s in scopes:
                if s not in token_data["scopes"]:
                    token_found=False
            if token_found:
                return token_data

    def cache_or_update(self, access_token, tenant_id, client_id, default_scope, scopes,
                        oauth_resource, refresh_token=None, username=None, 
                        ests_cookie=None, ests_persistent_cookie=None):
        """
            Saves an access and refresh token to the cache, or updates an existing entry

             Args:
                - access_token: string - an OAuth2 access token to cache
                - tenant_id: string - the tenant Id that issued the token
                - client_id: string - the Azure service principal client Id to fetch a token for
                - default_scope: bool - if true, use the default scope for the resource
                - scopes: list - a list of scopes to be issued in the token
                - oauth_resource: string - the OAuth resource issued in the token.
                - refresh_token: string - refresh token to cache
                - username: string - optional. The username that should be issued in the token
                - ests_cookie: string - optional. ests cookie to cache
                
            Returns:
                Null
        """
        if default_scope:
            scopes=[DEFAULTSCOPE]
        if tenant_id not in self.tokens.keys():
            self.tokens[ tenant_id ] = {}
        if oauth_resource not in self.tokens[ tenant_id ].keys():
            self.tokens[ tenant_id ][ oauth_resource ] = {}
        if client_id not in self.tokens[ tenant_id ][ oauth_resource ].keys():
            self.tokens[ tenant_id ][ oauth_resource ][ client_id ] = []

        # check to see if a token exists already
        for token_data in self.tokens[tenant_id][oauth_resource][client_id]:
            # in this case, we are trying to write an app token so we dont
            # need to check delegated tokens
            if token_data[ "type" ] == "delegated" and refresh_token is None:
                continue
            if token_data[ "type" ] == "delegated" and refresh_token is not None:
                if token_data[ "username" ] != username:
                    continue

                token_scopes = scopes
                for s in token_data[ "scopes" ]:
                    if s not in token_scopes:
                        continue

                # if we get here, our token matches all attributes in the cached token
                # Update the cached token
                # Note: todo: check to make sure the dictionary actually gets update.
                # offline and cant run the code.

                token_data[ "access_token" ] = access_token
                if token_data["type"] == "delegated":
                    token_data[ "refresh_token" ] = refresh_token
                logging.info("updating token in cache")
                break

            if token_data[ "type" ] == "application" and refresh_token is not None:
                continue
            if token_data[ "type" ] == "application" and refresh_token is None:
                #in this case, we want to check if there is an existing SP token to update:
                token_scopes = scopes
                for s in token_data[ "scopes" ]:
                    if s not in token_scopes:
                        continue
                token_data[ "access_token" ] = access_token
                return

        if refresh_token is None:
            new_token = {
                "type": "application",
                "scopes":scopes,
                "access_token": access_token,
            }
        else:
            new_token = {
                "type": "delegated",
                "scopes":scopes,
                "username":username,
                "access_token": access_token,
                "refresh_token": refresh_token,
                "ests_cookie": ests_cookie,
                "ests_persistent_cookie": ests_persistent_cookie
            }
        self.tokens[ tenant_id ][ oauth_resource ][ client_id ].append(new_token)
        