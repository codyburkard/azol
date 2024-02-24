"""A module containing a client for interacting with the Graph API"""
import logging
from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.constants import GRAPHBETAURL, OAuthResourceIDs

class GraphRequestFailedException(Exception):
    """
        Exception that is raised when requests to MS Graph
        unexpectedly fail
    """

class GraphClient( OAuthHTTPClient ):
    """
        An HTTP client for interacting with the Microsoft Graph API
    """

    def __init__( self, *args, base_url=GRAPHBETAURL, **kwargs ):
        super().__init__(  oauth_resource=OAuthResourceIDs.Graph, base_url=base_url, *args, **kwargs )

    def _send_request( self, *args, success_code=200, **kwargs ):
        response = super()._send_request(*args, **kwargs)
        if response.status_code != success_code:
            logging.error( "Error on GRAPH API request. Raw error: %s ", str(response.content))
            raise GraphRequestFailedException()
        return response

    def _get_all_graph_objects(self, response):
        """Get all objects from graph api request

        read all pages from a graph api request
        
        Args:
            response - (requests.Response) TThe requests response object for a graph request

        Returns:
            A list of dictionaries containing the entire Graph response

        """

        all_objects=[]
        objects=response.json()["value"]
        all_objects += objects
        while "@odata.nextLink" in response.json().keys():
            response = self._send_request( url=response.json()["@odata.nextLink"] )
            objects = response.json()[ "value" ]
            all_objects += objects
        return all_objects

    def get_directory_role_definitions( self ):
        """Get all directory role definitions.
        
        Returns:
            A list of dictionaries containing the role definitions in the directory.

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API

        """
        response = self._send_request( "/roleManagement/directory/roleDefinitions?"
                                       "$select=displayName,id,isBuiltIn" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_active_pim_sessions( self ):
        """Get all active PIM sessions.
        
        Returns:
            A list of dictionaries containing the active PIM sessions in the directory.

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API

        """
        response = self._send_request( "/roleManagement/directory/roleAssignmentSchedules?"
                                      "$select=roleDefinitionId,principalId,"
                                      "directoryScopeId,scheduleInfo,scheduleInfo" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()


    def get_eligible_pim_sessions( self ):
        """Get all eligible PIM sessions.
        
        Returns:
            A list of dictionaries containing the eligible PIM sessions in the directory.

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API

        """
        response = self._send_request( "/roleManagement/directory/roleEligibilitySchedules" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_transitive_group_memberships( self, group_id ):
        """Get transitive group memberships of a specific group.
        
        Args:
            group_id - (str) object id of the group

        Returns:
            A list of objects containing members of the group.

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API

        """
        response = self._send_request( f"/groups/{group_id}/transitiveMembers" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_all_users( self, abbreviate=True ):
        """Get all users in the directory.

        Returns:
            A list of objects containing object id and displayName of all users

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """

        if abbreviate:
            url_with_filter = "/users?$select=id,displayName"
        else:
            url_with_filter = "/users"

        response = self._send_request( url_with_filter )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_all_service_principals( self, abbreviate=True ):
        """Get all service principals in the directory.

        Returns:
            A list of objects containing object id and displayName of all service principals

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        
        if abbreviate:
            url_with_filter = "/servicePrincipals?$select=id,displayName"
        else:
            url_with_filter = "/servicePrincipals"
        
        response = self._send_request( url_with_filter )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_all_applications( self ):
        """Get all application objects in the directory.

        Returns:
            A list of objects containing object id and displayName of all application objects

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/applications?$select=id,displayName" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_directory_role_assignments( self ):
        """Get directory role assignments.

        Get all Entra ID role assignments in the directory, ignoring assignments through PIM

        Returns:
            A list of dictionaries containing role assignment metadata

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/roleManagement/directory/roleAssignments" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def delete_directory_role_assignments( self, assignment_id ):
        """Remove an Entra ID role from a principal in the directory.

        Args:
            assignment_id - (str) - The ID of the role assignment to delete

        Returns:
            A list of dictionaries containing the graph response to the deletion

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( f"/roleManagement/directory/roleAssignments/{assignment_id}",
                                       method="DELETE" )
        if response:
            return response.json()
        raise GraphRequestFailedException()

    def add_directory_role_assignment( self, role_definition_id, principal_id ):
        """Assign an Entra ID role to a principal in the directory.

        Args:
            role_definition_id - (str) - The ID of the role to assign
            principal_id - (str) - the principal to assign to the role

        Returns:
            A dictionary containing the graph ressponse

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        body = {
            "@odata.type": "#microsoft.graph.unifiedRoleAssignment",
            "roleDefinitionId": role_definition_id,
            "principalId": principal_id,
            "directoryScopeId": "/"
        }
        response = self._send_request( "/roleManagement/directory/roleAssignments",
                                       method="POST", json=body )
        if response:
            return response.json()
        raise GraphRequestFailedException()

    def add_app_owner( self, app_object_id, principal_id ):
        """Add an owner to an application object.

        Args:
            app_object_id - (str) - The ID of the application
            principal_id - (str) - the principal to assign to owner

        Returns:
            A dictionary containing the graph ressponse

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        body = {
            "@odata.id": f"https://graph.microsoft.com/v1.0/directoryObjects/{principal_id}"
        }
        # ERROR: this always errors out, even if it succeeds. its a requests library error
        response = self._send_request( f"/applications/{app_object_id}/owners/$ref",
                                       method="POST", json=body )

        if response:
            return response.json()
        raise GraphRequestFailedException()

    def remove_app_owner( self, app_object_id, principal_id ):
        """Remove an owner from an application object.

        Args:
            app_object_id - (str) - The ID of the application
            principal_id - (str) - the principal to assign to owner

        Returns:
            A dictionary containing the graph ressponse

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( f"/applications/{app_object_id}/owners/{principal_id}/$ref",
                                       method="DELETE")
        if response:
            return response.json()
        raise GraphRequestFailedException()

    def get_all_service_principals_owners( self ):
        """Get all owners of all service principals.

        Calls the graph API get get all service prinicpals, as well as their
        owners.

        Returns:
            A list of dictionaries, containing service principal ids,
            names, and owners

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/servicePrincipals?$expand=owners($select=id,displayName)&"
                                       "$select=owners,id,displayName" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_all_application_owners( self ):
        """Get all owners of all application objects.

        Calls the graph API get get all application objects, as well as their
        owners.

        Returns:
            A list of dictionaries, containing app object ids,
            names, and owners

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/applications?$expand=owners($select=id,displayName)&"
                                       "$select=owners,id,displayName" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_all_groups_and_memberships( self ):
        """Get all groups and group memberships.

        Calls the graph API get get all groups, and nested memberships.

        Returns:
            A list of dictionaries, containing group ids, names, and nested relationships

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/groups?$expand=memberOf($select=id,displayName)"
                                       "&$select=memberOf,id,displayName" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_all_groups( self ):
        """Get all group ids and displaynames in Entra Id.

        Calls the graph API get get all groups, and nested memberships.

        Returns:
            A list of dictionaries, containing group ids and names

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/groups?$select=id,displayName" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_all_groups_and_owners( self ):
        """Get all group owners in all Entra ID groups.

        Calls the graph API get get all groups, and owners of those groups.

        Returns:
            A list of dictionaries, containing groupIds, groupNames, and owners

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/groups?$expand=owners($select=id,displayName)"
                                       "&$select=owners,id,displayName" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_all_sp_api_permissions( self ):
        """Get all the API permissions assigned to all service principals.

        Returns:
           A list of dictionaries with API permissions assigned to all service principal

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/servicePrincipals?$expand=appRoleAssignments("
                                       "$select=resourceId,resourceDisplayName,principalType,"
                                       "appRoleId)&$select=appRoleAssignments,id,displayName" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    #def get_all_sp_delegated_permissions( self ): # TODO: currently errors
    #    """Get all the API permissions assigned to all service principals.
    #
    #    Returns:
    #       A list of dictionaries with API permissions assigned to all service principal
    #
    #    Raises:
    #        GraphRequestFailedException: An error occurred accessing the Graph API
    #    """
    #    response = self._send_request( "/servicePrincipals?&$select=oauth2PermissionGrants,"
    #                                   "id,displayName" )
    #    if response:
    #        return self._get_all_graph_objects(response)
    #    raise GraphRequestFailedException()

    def get_service_principal(self, sp_object_id):
        """Get service principals.

        Returns:
           A list of dictionaries containing service principal properties from Graph

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( f"/servicePrincipals/{sp_object_id}" )
        if response:
            return response.json()
        raise GraphRequestFailedException()

    def get_all_sp_reply_urls( self ):
        """Get all the reply Urls for all service principals.

        Returns:
           A list of dictionaries containing service principals and
           their reply urls.

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( "/servicePrincipals?&$select=replyUrls,id,displayName" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_api_permissions( self, sp_object_id ):
        """Get all API permissions assigned to a service principal.

        Get all the API permissions assigned to a service principal. 

        Args:
            - sp_object_id - (string) The object ID of a service principal

        Returns:
           A dictionary containing the service principal and
           its API permissions 

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( f"/servicePrincipals/{sp_object_id}/appRoleAssignments" )
        if response:
            return self._get_all_graph_objects(response)
        raise GraphRequestFailedException()

    def get_delegated_permissions( self, sp_object_id ):
        """Get all the delegated permissions assigned to a service principal.

        Get all the API permissions assigned to a service principal. 

        Includes all users that have consented to the permission.
        Principal Id displayNames are annotated at runtime for human readability.

        Args:
            - sp_object_id - (string) The object ID of a service principal

        Returns:
           A dictionary containing the service principal and
           its consented delegated permissions 

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( f"/servicePrincipals/{sp_object_id}/oauth2PermissionGrants" )
        if response.status_code != 200:
            logging.error( "error on GRAPH API request. Raw error: %s", response.content )
            raise GraphRequestFailedException()

        delegated_permissions=response.json()["value"]
        annotated_permissions=[]
        for p in delegated_permissions:
            annotated_permission = p.copy()
            if p["consentType"] == "AllPrincipals":
                annotated_permission["principalName"] = "all"
            else:
                resp = self._send_request( f"/directoryObjects/{p[ 'principalId' ]}" )
                obj = resp.json()
                principal_name = obj["userPrincipalName"]
                annotated_permission[ "principalName" ] = principal_name
            annotated_permissions.append(annotated_permission)
        return annotated_permissions

    def get_all_principals( self ):
        """Get all principals in the directory.

        Get all users, service principals, and groups in the directory.

        These are the objects that may be assigned permissions in M365 and Azure. 

        Returns:
           A dictionary mapping object ids to users, groups and service principals

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        users=self.get_all_users()
        service_principals=self.get_all_service_principals()
        groups=self.get_all_groups()
        principals = {}
        for directory_object in users:
            val = {
                "displayName": directory_object["displayName"],
                "principalType": "User"
            }
            key = directory_object["id"]
            principals[key] = val

        for directory_object in service_principals:
            val = {
                "displayName": directory_object["displayName"],
                "principalType": "ServicePrincipal"
            }
            key = directory_object["id"]
            principals[key] = val

        for directory_object in groups:
            val = {
                "displayName": directory_object["displayName"],
                "principalType": "Group"
            }
            key = directory_object["id"]
            principals[key] = val

        return principals

    def add_app_secret( self, app_object_id, name="inconspicuous" ):
        """Add a secret to a service principal in Entra ID.

        Args:
            - app_object_id - (string) the object ID of the Entra ID
                                application for which to generate a new secret
            - name - (string) The name of the new secret.

        Returns:
           A dictionary containing the properties for the new app secret

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        body= {
            "passwordCredential": {
                "displayName": name
            }
        }
        response = self._send_request( f"/applications/{app_object_id}/addPassword",
                                      method="POST", json=body )
        if response:
            return response.json()
        raise GraphRequestFailedException()

    def add_sp_secret( self, sp_object_id, name="inconspicuous" ):
        """Add a secret to an application object in Entra ID.

        Args:
            - sp_object_id - (string) the object ID of the Entra ID
                            service principal for which to generate a new secret.
            - name - (string) The name of the new secret.

        Returns:
           A dictionary containing the properties for the new sp secret

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        body= {
            "passwordCredential": {
                "displayName": name
            }
        }
        response = self._send_request( f"/servicePrincipals/{sp_object_id}/addPassword",
                                       method="POST", json=body )
        if response:
            return response.json()
        raise GraphRequestFailedException()

    def get_directory_object( self, object_id ):
        """Get a directory object from its object id.

        Attempt to get a directory object from its object id. This could be any type
        of directory object. Useful when a guid is identified, and it is not clear what it is.

        Args:
            - object_id - (string) The directory object Id.

        Returns:
           A dictionary containing information from graph about the object

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( f"/directoryObjects/{object_id}" )

        if response:
            directory_object = response.json()
            return directory_object
        raise GraphRequestFailedException()

    def try_get_object_type( self, object_id ):
        """Get a directory object type from its object id.

        Attempt to get a directory object's type base on its object id. This could be any type
        of directory object. Useful when a guid is identified, and it is not clear what it is.

        Args:
            - object_id - (string) The directory object Id.

        Returns:
           (string) the type of the directory object, from Graph, or None if it is not a
                    directory object

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( f"/directoryObjects/{object_id}" )

        if response:
            if "@odata.type" in response.json().keys():

                directory_object_type = response.json()[ "@odata.type" ]
                return directory_object_type
            return None
        raise GraphRequestFailedException()

    def create_new_local_service_principal( self, name="inconspicuous" ):
        """Create a new service principal.

        Create an application object an service principal in the current tenant of the client.
        Requires a user with an Entra ID role or a service principal with a graph API
        permission capable of creating service principals.

        Also creates a secret for this new service principal.

        Args:
            - name - (string) The name of the new service principal.

        Returns:
           (string) A dictionary containing properties for the new service principal,
                    including the newly created secret

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        body = {
            "displayName": name
        }
        response = self._send_request( "/applications", method="POST", json=body )

        if response.status_code != 201:
            logging.error( "error on GRAPH API request. Raw error: %s ", response.content )
            raise GraphRequestFailedException()

        app = response.json()
        app_id = app[ "appId" ]
        app_object_id = app[ "id" ]

        # Create the logcal service principal
        body = {
            "appId": app_id
        }
        response = self._send_request( "/servicePrincipals", method="POST", json=body )

        if response.status_code != 201:
            logging.error( "error on GRAPH API request. Raw error: %s ", response.content )
            raise GraphRequestFailedException()

        sp = response.json()
        sp_id = sp[ "id" ]

        # create a secret for the service principal
        body = {
            "passwordCredential": {
                "displayName": "inconspicuous"
            }
        }
        response = self._send_request( f"/servicePrincipals/{sp_id}/addPassword",
                                      method="POST", json=body )

        if response.status_code != 200:
            logging.error( "error on GRAPH API request. Raw error: %s ", response.content )
            raise GraphRequestFailedException()

        secret = response.json()[ "secretText" ]

        output = {
            "clientId": app_id,
            "appObjectId": app_object_id,
            "spId": sp_id,
            "spSecret": secret
        }

        return output

    def create_new_remote_service_principal( self, client_id ):
        """Create a new service principal referencing a remote application.

        Create avservice principal in the current tenant of the client.
        This service principall will reference an application in another directory.

        This means the application object in the other directory may be used to access
        the permissions of this principal

        Requires a user with an Entra ID role or a service principal with a graph API
        permission capable of creating service principals.

        Args:
            - client_id - (string) The client id of the service principal.

        Returns:
           (string) A dictionary containing properties for the new service principal

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        # Create the service principal
        body = {
            "appId": client_id
        }
        response = self._send_request( "/servicePrincipals", method="POST", json=body, success_code=201 )

        sp = response.json()
        sp_id = sp[ "id" ]

        output = {
            "clientId": client_id,
            "spId": sp_id
        }

        return output

    def get( self, path ):
        """Make a get request to a specific API path within the Graph API.

        Args:
            - path - (string) The graph API path.

        Returns:
           Request.Response object from the GET request

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( path )
        if response:
            return response.json()
        raise GraphRequestFailedException()

    def post( self, path, data ):
        """Send a POST request to Graph, and return the raw results

        Calls Graph at the path specified, and returns the raw deserialized results.
        
        Args:
            path - (str) The API path to call on Graph
            data - (dict) The JSON data to send to Graph in the API request body

        Returns:
            A dictionary containing the raw results from the ARM request.

        """
        response = self._send_request( path, method="POST",
                                              json=data )
        return response.json()

    def put( self, path, data ):
        """Send a PUT request to Graph, and return the raw results

        Calls Graph at the path specified, and returns the raw deserialized results.
        
        Args:
            path - (str) The API path to call on Graph
            data - (dict) The JSON data to send to Graph in the API request body

        Returns:
            A dictionary containing the raw results from the ARM request.

        """
        response = self._send_request( path, method="PUT",
                                              json=data )
        return response.json()

    def patch( self, path, data ):
        """Send a PATCH request to Graph, and return the raw results

        Calls Graph at the path specified, and returns the raw deserialized results.
        
        Args:
            path - (str) The API path to call on Graph
            data - (dict) The JSON data to send to Graph in the API request body

        Returns:
            A dictionary containing the raw results from the ARM request.

        """
        response = self._send_request( path, method="PATCH",
                                              json=data )
        return response.json()

    def delete( self, path ):
        """Make a DELETE request to a specific API path within the Graph API.

        Args:
            - path - (string) The graph API path.

        Returns:
           Request.Response object from the DELETE request

        Raises:
            GraphRequestFailedException: An error occurred accessing the Graph API
        """
        response = self._send_request( path, method="DELETE" )
        if response:
            return response.json()
        raise GraphRequestFailedException()
