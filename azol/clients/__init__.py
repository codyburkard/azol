"""Module containing all http clients"""
from azol.clients.arm_client import ArmClient
from azol.clients.graph_client import GraphClient
from azol.clients.key_vault_client import KeyVaultClient
from azol.clients.oauth_http_client import OAuthHTTPClient

__all__ = [
    "ArmClient",
    "GraphClient",
    "KeyVaultClient",
    "OAuthHTTPClient"
]
