"""A module containing an azure generic resource model"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class ESTS( object ):
    """
        A dataclass object that contains an ests and ests_persistent cookie
    """
    ests: str
    ests_persistent: str
    