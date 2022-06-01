"""A module containing all azol providers"""
from azol.providers.key_vault_secret_provider import KeyVaultProvider
from azol.providers.file_secret_provider import FileSecretProvider

__all__ = [
    "FileSecretProvider",
    "KeyVaultProvider"
]
