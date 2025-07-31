"""A module containing the parent credential class"""
import uuid

class Credential:
    """
        Parent class of other credential classes. 
    """

    credentialType=None
    
    def __init__( self, azol_id=None ):

        if azol_id is None:
            azol_id = uuid.uuid4()
        self._id = str(azol_id)

    def get_id( self ):
        """
            Get the azol id of the object.
    
            Returns: string containing the azol id
        """
        return self._id
