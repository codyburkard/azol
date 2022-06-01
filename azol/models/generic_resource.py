"""A module containing an azure generic resource model"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class GenericResource( object ):
    """
        A generic resource model that represents azure objects
    """
    id: str
    name: str
    properties: object
    type: str
    changedTime: Optional[str] = None
    createdTime: Optional[str] = None
    extendedLocation: Optional[object] = None
    identity: Optional[object] = None
    kind: Optional[str] = None
    location: Optional[str] = None
    managedBy: Optional[str] = None
    plan: Optional[object] = None
    provisioningState: Optional[str] = None
    sku: Optional[object] = None
    tags: Optional[object] = None
    azolAnnotations : Optional[object] = None

    