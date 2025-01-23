"""azol module, which imports all other modules"""
from pathlib import Path
from azol.constants import ( AZOL_HOME, PROVIDER_CACHE_DIR, PROVIDER_CACHE,
                             RBACRoleDefinitionIds, OAuthResourceIDs, OAUTHFLOWS,
                             FOCIClients )

from azol.clients import ( KeyVaultClient, ArmClient, OAuthHTTPClient, GraphClient,
                           DataFactoryClient, KuduClient )
from azol.credentials import User, ApplicationObject, ServicePrincipal, AccessToken
from azol.utils import parse_jwt, get_tenant_id, is_token_expired
from azol.providers import KeyVaultProvider, FileSecretProvider

# Create the azol home directory
Path(AZOL_HOME).mkdir(parents=True, exist_ok=True)

# Create the folder structure below
Path(PROVIDER_CACHE_DIR).mkdir(parents=True, exist_ok=True)
Path(PROVIDER_CACHE).touch(exist_ok=True)

__all__ = [
    "RBACRoleDefinitionIds",
    "OAuthResourceIDs",
    "OAUTHFLOWS",
    "FOCIClients",
    "GraphClient",
    "OAuthHTTPClient",
    "DataFactoryClient",
    "KuduClient",
    "ArmClient",
    "KeyVaultClient",
    "AccessToken",
    "ServicePrincipal",
    "ApplicationObject",
    "User",
    "parse_jwt",
    "get_tenant_id",
    "is_token_expired",
    "KeyVaultProvider",
    "FileSecretProvider"
]