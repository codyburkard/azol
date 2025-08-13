"""Module containing all http clients"""
from azol.clients.arm_client import ArmClient
from azol.clients.graph_client import GraphClient
from azol.clients.key_vault_client import KeyVaultClient
from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.clients.datafactory_client import DataFactoryClient
from azol.clients.kudu_client import KuduClient
from azol.clients.devops_agent_client import AzureDevOpsAgentClient
from azol.clients.azure_devops_client import AzureDevOpsClient


__all__ = [
    "ArmClient",
    "GraphClient",
    "KeyVaultClient",
    "OAuthHTTPClient",
    "DataFactoryClient",
    "KuduClient",
    "AzureDevOpsAgentClient",
    "AzureDevOpsClient"
]
