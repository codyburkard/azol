"""Module containing all token caches for azol"""
from azol.caches.in_memory_token_cache import InMemoryTokenCache
from azol.caches.local_token_cache import LocalTokenCache

__all__ = [
    "InMemoryTokenCache",
    "LocalTokenCache"
]
