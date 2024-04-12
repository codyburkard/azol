"""A module containing a unfied client for interacting with all supported APIs.

Typical usage example:

    cred=User(username="username@domain.com")
    client=UnifiedClient(tenant="tenant.com", cred=cred)
    users=client.get_all_users()

"""
import logging

from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.constants import OAuthResourceIDs
from azol.clients import ArmClient, GraphClient, KeyVaultClient
from azol.models.generic_resource import GenericResource
from azol.resources.rbac_roles import rbac_roles

class UnifiedClient():
    """
        A unified HTTP client that can access all supported HTTP clients from azol
    """

    def __init__( self, tenant, cred, *args, **kwargs ):
        self.arm_client=ArmClient(tenant=tenant, cred=cred)
        self.graph_client=GraphClient.from_client(self.arm_client)

    def get_tenants( self ):
        """Get user's tenants. See ARMClient"""
        return self.arm_client.get_tenants()

    def whoami( self ):
        upn=None
        app_displayname=None
        home_tenant=None
        current_tenant=None
        principal_type="unknown"
        name=None
        appid=None
        results = {
            "principal_type": principal_type,
            "user": upn,
            "name": name,
            "client": app_displayname,
            "client_id": appid,
            "home_tenant": home_tenant,
            "current_tenant": current_tenant            
        }
        claims=self.arm_client.get_token_claims()
        if claims is None:
            # not authenticated
            return results
        if "app_displayname" in claims.keys():
            app_displayname=claims["app_displayname"]
        if "appid" in claims.keys():
            appid=claims["appid"]
        current_tenant=claims["tid"]

        if "upn" in claims.keys():
            principal_type="user"
            upn=claims["upn"]
            name=claims["name"]
            if "idp" in claims.keys():
                home_tenant=claims["idp"]
            else:
                home_tenant=current_tenant
        else:
            principal_type="app"
        
        results = {
            "principal_type": principal_type,
            "user": upn,
            "name": name,
            "client": app_displayname,
            "client_id": appid,
            "home_tenant": home_tenant,
            "current_tenant": current_tenant            
        }
        return results

    def switch_tenant( self, tenant ):
        self.graph_client.switch_tenant(tenant)
        self.arm_client.switch_tenant(tenant)

    def fetch_tokens( self ):
        self.graph_client.fetch_token()
        self.arm_client.fetch_token()

    def get_graph_client( self ):
        return self.graph_client

    def get_arm_client( self ):
        return self.arm_client

    def get_management_groups( self, expand=False ):
        """Get management groups. See ArmClient"""
        return self.arm_client.get_management_groups(expand)

    def get_subscriptions( self, expand=False ):
        """Get subscriptions. See ArmClient"""
        return self.arm_client.get_subscriptions(expand)
    
    def get_all_users( self, expand=False ):
        return self.graph_client.get_all_users(expand)
    
