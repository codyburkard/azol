"""A module containing all credential types"""
from azol.credentials.credential import Credential
from azol.credentials.access_token import AccessToken
from azol.credentials.service_principal import ServicePrincipal
from azol.credentials.application_object import ApplicationObject
from azol.credentials.user import User

__all__ = [
    "AccessToken",
    "ServicePrincipal",
    "ApplicationObject",
    "User"
]
