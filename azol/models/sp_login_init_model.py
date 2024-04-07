"""A module containing a data structure used in the initialization of OAuth login flows"""
from dataclasses import dataclass

@dataclass
class SPLoginModel( object ):
    """
        An object containing necessary data for SP-initiated login flows 
    """
    login_uri: str
    args: object