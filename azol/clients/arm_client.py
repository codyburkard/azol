"""A module containing a client for interacting with the ARM API.

Typical usage example:

    cred=User(username="username@domain.com")
    client=ArmClient(tenant="tenant.com", cred=cred)
    users=client.get_all_users()

"""
import logging

from azol.clients.oauth_http_client import OAuthHTTPClient
from azol.constants import OAuthResourceIDs, ARMURL
from azol.models.generic_resource import GenericResource
from azol.resources.rbac_roles import rbac_roles

class ArmRequestFailedException(Exception):
    """
        Exception that is raised when requests to ARM
        unexpectedly fail
    """

class ArmClient( OAuthHTTPClient ):
    """
        An HTTP client for interacting with the Azure Resource Manager API
    """

    def __init__( self, *args, principal_lookup_table=None, **kwargs ):
        super().__init__( oauth_resource=OAuthResourceIDs.Arm, base_url=ARMURL, *args, **kwargs)

        # get all providers immediately when logging in
        self.providers=self.get_providers()
        self.principal_lookup_table=principal_lookup_table

    def get_tenants( self ):
        """Get user's tenants.
        
        Get tenants that the client's credential has access to.
        ARM only allows this API call with credential type is not "User".

        Returns:
            A dict containing the response from the ARM '/tenants' API.

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        arm_raw_response = self._send_request( "/tenants",
                        query_parameters={ "api-version": "2020-01-01" }, method="GET" )

        if arm_raw_response.status_code != 200:
            logging.error( "ERROR while retrieving tenants: %s", arm_raw_response.content )
            raise ArmRequestFailedException()
        tenants = arm_raw_response.json()[ "value" ]

        return tenants

    def get_management_groups( self, expand=False ):
        """Get management groups
        
        Get all management groups that the current credentials have access to.
        
        Args:
            expand - (bool) Return the full ARM API output, or an abreviated version.

        Returns:
            A list of dicts containing management group metadata,
            or a list of management group ids if abreviated.

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        arm_raw_response = self._send_request( "/providers/Microsoft.Management/managementGroups",
                        query_parameters={ "api-version": "2020-05-01" }, method="GET" )

        if arm_raw_response.status_code != 200:
            logging.error( "ERROR retrieving management groups: %s", arm_raw_response.content )
            raise ArmRequestFailedException()
        management_group_raw_list = arm_raw_response.json()[ "value" ]

        if expand:
            return management_group_raw_list

        management_group_ids = [  mgroup[ "id" ] for mgroup in management_group_raw_list ]
        return management_group_ids

    def get_subscriptions( self, expand=False ):
        """Get subscriptions
        
        Get all subscriptions that the current credentials have access to.
        
        Args:
            expand - (bool) Return the full ARM API output, or an abreviated version.

        Returns:
            A list of dicts containing subscription metadata, or a list of subscriptions ids
            if abreviated

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        arm_raw_response = self._send_request( "/subscriptions",
                                query_parameters={ "api-version": "2019-03-01" }, method="GET" )
        if arm_raw_response.status_code != 200:
            logging.error( "ERROR while retrieving subscriptions: %s", arm_raw_response.content )
            raise ArmRequestFailedException()
        subscriptions_raw_list = arm_raw_response.json()[ "value" ]


        if expand:
            return subscriptions_raw_list

        subscription_ids = [ subDict[ 'subscriptionId' ] for subDict in subscriptions_raw_list ]
        return subscription_ids

    def get_resource_groups( self, subscriptions=None ):
        """Get resource groups
        
        Get all resource groups that the current credentials have access to.
        
        Args:
            subscriptions - (list) Default None. A list of subscriptions to enumerate. If None, 
                            enumerate all subscriptions

        Returns:
            A list of resource group ids

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        if subscriptions is None:

            arm_raw_response = self._send_request( "/subscriptions",
                                              query_parameters={ "api-version": "2019-03-01" },
                                              method="GET" )
            if arm_raw_response.status_code != 200:
                logging.error( "ERROR retrieving resource groups: %s", arm_raw_response.content )
                raise ArmRequestFailedException()
            subscriptions_raw_list = arm_raw_response.json()[ "value" ]
            subscriptions_abreviated_list = [ subDict[ 'subscriptionId' ]
                                             for subDict in subscriptions_raw_list ]
        else:
            subscriptions_abreviated_list = subscriptions
        resource_groups = []
        for subscription in subscriptions_abreviated_list:
            arm_raw_response = self._send_request( f"/subscriptions/{subscription}/resourceGroups",
                                                  query_parameters={ "api-version": "2019-03-01" },
                                                  method="GET" )

            resource_groups += arm_raw_response.json()[ "value" ]


        resource_group_ids = [ rgDict[ 'id' ] for rgDict in resource_groups ]
        return resource_group_ids

    def get_providers( self ):
        """Get azure providers
        
        Get ARM providers and api versions (/providers API).

        Returns:
            A dictionary containing the provider namespace mapped
            to a list of api versions

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        query_parameters = {
            "api-version": "2023-07-01"
        }
        resp = self._send_request("/providers",
                                    query_parameters=query_parameters, method="GET" )
        if resp.status_code != 200:
            logging.error( "ERROR getting providers: %s", resp.content )
            raise ArmRequestFailedException()

        try:
            json_response=resp.json()

            providers={}
            for p in json_response["value"]:
                providers[p["namespace"].lower()] = {}
                for resource_type in p["resourceTypes"]:
                    rt=resource_type["resourceType"].lower()
                    ns=p["namespace"].lower()
                    providers[ns][rt] = resource_type["apiVersions"]

            return providers
        except Exception as e:
            logging.error("Unable to automatically fetch providers in the tenant."
                          " provider version auto-resolution will fail")     
            raise ArmRequestFailedException() from e

    def get_resource( self, resource_id, api_version=None ):
        """Get an individual resource.
        
        Get the resource properties of a specific resource.
        
        
        Args:
            resource_id - (str) required. The ARM resource Id of the resource.

            api_version - (str) Default None. The API version of the provider to use in the ARM
                         request. If None, azol will attempt to auto-resolve the resource type and
                         use the latest known version of the provider from the last build.

        Returns:
            GenericResource object

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        # extract the resource provider name from the resource id
        namespace = resource_id.split('/providers/')[-1].split("/")[0].lower()
        provider = "/".join(resource_id.split('/providers/')[-1].split("/")[1:-1]).lower()

        provider_versions=self.providers[namespace][provider]
        latest=provider_versions[0]

        if api_version is None:
            api_version = latest
        query_parameters = {
            "api-version": api_version
        }
        resp = self._send_request(resource_id,
                                    query_parameters=query_parameters, method="GET" )
        if resp.status_code != 200:
            logging.error( "ERROR getting resource: %s", resp.content )
        # sometimes value isnt actually required...
        json_response=resp.json()
        if "value" in json_response.keys():
            resource = json_response[ "value" ]
        else:
            resource = json_response
        new_resource = self._deserialize_resource(resource)
        return new_resource

    def get_resources( self, resource_type=None, subscriptions=None, ignore_subscriptions=None ):
        """Get all resources.
        
        Get all resources that the client's credential has access to.

        This will not return the resource's properties - this is not supported in a single ARM
        request.
        
        Args:
            resource_type - (str) Default None. Only get resources of this type.
                            Example: 'Microsoft.Network/virtualNetworks'

            subscriptions - (list) Default None. A list of subscription IDs
                            to enumerate.

            ignore_subscriptions - (list) Default None. A list of subscription IDs
                                   to ignore during enumeration of resources.

        Returns:
            A list of GenericResource objects

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        query_parameters = {
             "api-version": "2019-03-01" 
        }
        if subscriptions is None:
            arm_raw_response = self._send_request( "/subscriptions",
                            query_parameters=query_parameters, method="GET" )
            if arm_raw_response.status_code != 200:
                logging.error( "error while getting subscriptions: %s", arm_raw_response.content )
            subscriptions_raw_list = arm_raw_response.json()[ "value" ]

            subscriptions_abreviated_list = [ subDict[ 'subscriptionId' ]
                                             for subDict in subscriptions_raw_list ]
        else:
            subscriptions_abreviated_list = subscriptions
        resources = []
        for subscription in subscriptions_abreviated_list:
            if ignore_subscriptions is not None and subscription in ignore_subscriptions:
                continue
            query_parameters = {
             "api-version": "2019-03-01",
             "$expand": "createdTime,changedTime,provisioningState,location,tags,type,properties"
            }
            if resource_type is not None:
                query_parameters[ "$filter" ] = f"resourceType eq '{resource_type}'"
            resp = self._send_request( f"/subscriptions/{subscription}/resources",
                                      query_parameters=query_parameters, method="GET" )
            if resp.status_code != 200:
                logging.error( "ERROR getting resources: %s", resp.content )
                raise ArmRequestFailedException()

            # deserialize current results
            for resource in resp.json()[ "value" ]:
                new_resource = self._deserialize_resource(resource)
                resources.append(new_resource)

            while "nextLink" in resp.json().keys():
                resp = self._send_request( url=resp.json()["nextLink"] )
                if resp.status_code != 200:
                    logging.error( "ERROR getting resources: %s", resp.content )
                    raise ArmRequestFailedException()
                # deserialize current results
                for resource in resp.json()[ "value" ]:
                    new_resource = self._deserialize_resource(resource)
                    resources.append(new_resource)

        return resources

    def get_resource_ids( self, resource_type=None, subscriptions=None, ignore_subscriptions=None ):
        """Get all resource ids.
        
        Get the resource ids of all resources the client has access to
        
        Args:
            resource_type - (str) Default None. Only get resources of this type.
                            Example: 'Microsoft.Network/virtualNetworks'

            subscriptions - (list) Default None. A list of subscription IDs
                            to enumerate.

            ignore_subscriptions - (list) Default None. A list of subscription IDs
                                   to ignore during enumeration of resources.

        Returns:
            a list of resource ids

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        query_parameters = {
             "api-version": "2019-03-01" 
        }
        if subscriptions is None:
            arm_raw_response = self._send_request( "/subscriptions",
                            query_parameters=query_parameters, method="GET" )
            if arm_raw_response.status_code != 200:
                logging.error( "ERROR getting subscriptions: %s", arm_raw_response.content )
                raise ArmRequestFailedException()
            subscriptions_raw_list = arm_raw_response.json()[ "value" ]

            subscriptions_abreviated_list = [ subDict[ 'subscriptionId' ]
                                             for subDict in subscriptions_raw_list ]
        else:
            subscriptions_abreviated_list = subscriptions
        resources = []
        for subscription in subscriptions_abreviated_list:
            if ignore_subscriptions is not None and subscription in ignore_subscriptions:
                continue
            query_parameters = {
             "api-version": "2019-03-01" 
            }
            if resource_type is not None:
                query_parameters[ "$filter" ] = f"resourceType eq '{resource_type}'"

            resp = self._send_request( f"/subscriptions/{subscription}/resources",
                                                query_parameters=query_parameters, method="GET" )

            resources_raw_list = resp.json()[ "value" ]
            resources += resources_raw_list
        resources_abreviated_list = [ rDict[ 'id' ] for rDict in resources ]
        return resources_abreviated_list

    def get_rbac_role_definition_map( self ):
        """Get a dict of role definition ids mapped to names
        
        Enumerate all role definitions, and return a dictionary mapping all ids to names.

        This is helpful when performing data annotations of raw data gathered from a tenant.

        Returns:
            A dict mapping role definition ids to role definition names.
        """
        arm_roles_map = {}
        # enumerate management groups first
        management_group_permissions = True
        management_groups = self.get_management_groups( expand=False )
        if management_groups is None:
            management_group_permissions = False

        if management_group_permissions:
            for managementgroup in management_groups:
                arm_raw_response = self._send_request( f"{managementgroup}/providers/"
                                                    "Microsoft.Authorization/roleDefinitions",
                                                    query_parameters={
                                                        "api-version": "2015-07-01"
                                                    } )

                temp_arm_roles_list = [ { "name": definition["properties"][ "roleName" ],
                                            "id": definition[ "id" ] } for definition
                                            in arm_raw_response.json()[ 'value' ] ]
                for role_definition in temp_arm_roles_list:
                    if role_definition['id'] in arm_roles_map.keys():
                        pass
                    arm_roles_map[ role_definition['id'] ] = role_definition[ 'name' ]

        subscriptions = self.get_subscriptions( expand=False )
        for subscription in subscriptions:
            arm_raw_response = self._send_request(f"/subscriptions/{subscription}/providers/"
                                                    "Microsoft.Authorization/roleDefinitions", 
                                                    query_parameters={
                                                        "api-version": "2015-07-01"
                                                    } )

            temp_arm_roles_list = [ { "name": definition["properties"][ "roleName" ],
                                        "id": definition[ "id" ] } for definition
                                        in arm_raw_response.json()[ 'value' ] ]
            for role_definition in temp_arm_roles_list:
                if role_definition['id'] in arm_roles_map.keys():
                    pass
                arm_roles_map[ role_definition['id'] ] = role_definition[ 'name' ]

        return arm_roles_map

    def get_rbac_role_assignments(self):
        """Get all RBAC role assignments
        
        Get all RBAC role assignments at all scopes in the tenant,
        with the client's current credential.
        
        If principal_lookup_table is populated in the client, it will be used to annotate the
        assignments with the displayNames of principal Ids.
        
        Returns:
            A list of GenericResource objects containing the RBAC assignments

        """
        role_assignments = []
        management_group_permissions = True
        management_groups = self.get_management_groups( expand=False )
        if management_groups is None:
            management_group_permissions = False

        if management_group_permissions:
            for managementgroup in management_groups:
                arm_raw_response = self._send_request( f"{managementgroup}/providers/"
                                                "Microsoft.Authorization/roleAssignments",
                                                query_parameters={ "api-version": "2015-07-01"} )

                assignments = arm_raw_response.json()[ "value" ]
                for assignment in assignments:
                    if assignment[ "id" ] not in role_assignments:
                        role_assignments.append( assignment )

        resources = self.get_resource_ids()
        for resource in resources:
            arm_raw_response = self._send_request( f"{resource}/providers/"
                                                  "Microsoft.Authorization/roleAssignments",
                                                  query_parameters={ "api-version": "2015-07-01"} )
            assignments = arm_raw_response.json()[ "value" ]
            for assignment in assignments:
                if assignment[ "id" ] not in role_assignments:
                    role_assignments.append( assignment )

        #convert dictionaries to list of generic resources
        generic_resource_list=[]
        for resource in role_assignments:
            definition_id = resource[ "properties" ]["roleDefinitionId"]
            role_definition_name = rbac_roles[definition_id] if (
                    definition_id in rbac_roles.keys() ) else "unknown"
            annotations={
                "roleDefinitionName": role_definition_name
            }
            if self.principal_lookup_table:
                p_id = resource[ "properties" ]["principalId"]
                annotations[ "principalName" ] = self.principal_lookup_table[p_id]["displayName"]
            new_resource = self._deserialize_resource(resource)
            new_resource.azolAnnotations=annotations
            generic_resource_list.append(new_resource)

        return generic_resource_list

    def get_rbac_assignments_at_scope( self, scope ):
        """Get all RBAC role assignments at a given scope
        
        If principal_lookup_table is populated in the client, it will be used to annotate the
        assignments with the displayNames of principal Ids.
        
        Args:
            scope - (str) The id of a management group, subscription, resource group, or resource.

        Returns:
            A list of GenericResource objects containing rbac assignments

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        role_assignments=[]
        arm_raw_response=self._send_request( f"{scope}/providers/"
                                            "Microsoft.Authorization/roleAssignments",
                                             query_parameters={ "api-version": "2022-04-01",
                                                               "$filter": "atScope()"} )
        role_assignments=arm_raw_response.json()[ "value" ]
        #convert dictionaries to list of generic resources
        generic_resource_list=[]
        for resource in role_assignments:
            if resource["properties"]["scope"] != scope:
                continue
            definition_id = resource[ "properties" ]["roleDefinitionId"]
            role_definition_name = rbac_roles[definition_id] if (
                        definition_id in rbac_roles.keys() ) else "unknown"
            annotations={
                "roleDefinitionName": role_definition_name
            }
            if self.principal_lookup_table:
                principal_id = resource[ "properties" ]["principalId"]
                annotations[ "principalName" ] = self.principal_lookup_table[principal_id]["displayName"]
            new_resource = self._deserialize_resource(resource)
            new_resource.azolAnnotations=annotations
            generic_resource_list.append(new_resource)

        return generic_resource_list

    def elevate_access_as_global_admin( self ):
        """Elevate access to Azure as Global Administrator.
        
        Toggle elevated access to Azure as a global administrator.
        This toggle sets the Global Administrator to User Access Administrator
        On the tenant scope of the directory.

        This only works if the current identity is a User, and is a Global Administrator
        
        Args:
            None

        Returns:
            dict containing raw ARM response 

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( "/providers/Microsoft.Authorization/elevateAccess",
                                      query_parameters={ "api-version": "2017-05-01"},
                                      method="POST"  )
        if response.status_code != 200:
            logging.error( "ERROR on ARM request: %s", response.content )
            raise ArmRequestFailedException()

        return response.json()

    def get_logic_app_runs( self, logic_app_resource_id ):
        """Get logic app run.
        
        Get metadata of logic app runs for a specific logic app
        
        Args:
            logic_app_resource_id - (str) The complete resource Id of the logic app

        Returns:
            A list of Generic Resource objects containing the logic app runs

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{logic_app_resource_id}/runs",
                                      query_parameters={ "api-version": "2016-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "ERROR on ARM request: %s", response.content )
            raise ArmRequestFailedException()
        resources = response.json()
        deserialized_resource_list = []
        for resource in resources:
            new_resource = self._deserialize_resource(resource)
            deserialized_resource_list.append(new_resource)

        return deserialized_resource_list

    def get_logic_app_run_actions( self, logic_app_run_resource_id ):
        """Get logic app run actions.
        
        Get all run actions for a single logic app
        
        Args:
            logic_app_run_resource_id - (str) The complete resource Id of the logic app run

        Returns:
            Dictionary containing Logic App Actions

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{logic_app_run_resource_id}/actions",
                                      query_parameters={ "api-version": "2016-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "ERROR on ARM request: %s", response.content )
            raise ArmRequestFailedException()

        return response.json()

    def get_logic_app( self, logic_app_resource_id ):
        """Get a logic app.
        
        Get a logic app resource's properties
        
        Args:
            logic_app_resource_id - (str) The complete resource Id of the logic app

        Returns:
            GenericResource of the logic app

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{logic_app_resource_id}",
                                      query_parameters={ "api-version": "2016-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "ERROR on ARM request: %s", response.content )
            raise ArmRequestFailedException()

        resource = response.json()["value"]
        new_resource = self._deserialize_resource(resource)
        return new_resource

    def get_logic_app_versions( self, logic_app_resource_id ):
        """Get a logic app's versions.
        
        Get a logic app resource's versions
        
        Args:
            logic_app_resource_id - (str) The complete resource Id of the logic app

        Returns:
            list of dictionaries containing all logic app versions

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{logic_app_resource_id}/versions",
                                      query_parameters={ "api-version": "2016-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "ERROR on ARM request: %s", response.content )
            raise ArmRequestFailedException()

        return response.json()

    def get_runbooks( self, automation_account_id ):
        """Get runbook metadata in an automation account.
        
        Get all runbook objects in an automation account.
        Calls the '/runbooks' endpoint.
        
        Args:
            automation_account_id - (str) The complete resource Id of the automation account

        Returns:
            dictionary containing a list of metadata for
            the runbooks in the automation account

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{automation_account_id}/runbooks",
                                      query_parameters={ "api-version": "2019-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "ERROR on ARM request: %s", response.content )
            raise ArmRequestFailedException()

        return response.json()[ "value" ]

    def get_runbook_content( self, automation_account_runbook_id ):
        """Get runbook content.
        
        Get the contents of a runbook.
        Calls the '/content' endpoint.
        
        Args:
            automation_account_runbook_id - (str) Complete resource Id of the automation account
                                            runbook

        Returns:
            (string) the raw contents of a runbook

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{automation_account_runbook_id}/content",
                                       query_parameters={ "api-version": "2019-06-01"},
                                       method="GET"  )
        if response.status_code != 200:
            logging.error( "%s error on ARM API request"
                          "to get runbook content for runbook %s." 
                          "Raw error: %s", response.status_code, automation_account_runbook_id,
                          response.content )
            raise ArmRequestFailedException()

        return response

    def get_runbook_draft_content( self, automation_account_runbook_id ):
        """Get runbook draft content.
        
        Get the draft contents of a runbook.
        Calls the '/draft/content' endpoint.
        
        Args:
            automation_account_runbook_id - (str) Complete resource Id of the automation account
                                            runbook

        Returns:
            (string) the raw contents of a runbook draft

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{automation_account_runbook_id}/draft/content",
                                      query_parameters={ "api-version": "2019-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "%s error on ARM API request"
                          "to get runbook content for runbook content for runbook %s." 
                          "Raw error: %s", response.status_code, automation_account_runbook_id,
                          response.content )
            raise ArmRequestFailedException()

        return response

    def get_automation_webhooks( self, automation_account_id ):
        """Get automation account webhooks.
        
        Get the webhooks in an automation account.
        Calls the '/webhooks' endpoint.
        
        Args:
            automation_account_id - (str) Complete resource Id of the automation account

        Returns:
            List of dictionaries containing webhooks in the automation account

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{automation_account_id}/webhooks",
                                      query_parameters={ "api-version": "2015-10-31"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "%s error on ARM API request"
                          "to get webhooks on %s." 
                          "Raw error: %s", response.status_code, automation_account_id,
                          response.content )
            raise ArmRequestFailedException()

        return response.json()["value"]

    def get_automation_variables( self, automation_account_id ):
        """Get automation account variables.
        
        Get the variables in an automation account.
        Calls the '/variables' endpoint.
        
        Args:
            automation_account_id - (str) Complete resource Id of the automation account

        Returns:
            List of dictionaries containing variables in the automation account

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{automation_account_id}/variables",
                                      query_parameters={ "api-version": "2019-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "%s error on ARM API request"
                          "to get variables on %s." 
                          "Raw error: %s", response.status_code, automation_account_id,
                          response.content )
            raise ArmRequestFailedException()

        return response.json()["value"]

    def get_automation_jobs( self, automation_account_runbook_id ):
        """Get automation account runbook jobs.
        
        Get metadata on the jobs that have been run for an Automation Account runbook
        
        Args:
            automation_account_runbook_id - (str) Complete resource Id of the 
                                          automation account runbook

        Returns:
            A list of dictioaries containing metdata for automation account jobs.

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{automation_account_runbook_id}/jobs",
                                      query_parameters={ "api-version": "2019-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "%s error on ARM API request"
                          "to get jobs on %s." 
                          "Raw error: %s", response.status_code, automation_account_runbook_id,
                          response.content )
            raise ArmRequestFailedException()

        return response.json()["value"]

    def get_automation_job_output( self, automation_account_job_id ):
        """Get automation account runbook job output.
        
        Get the job output of a specific automation account job

        
        Args:
            automation_account_job_id - (str) Complete resource Id of the
                                        automation account job

        Returns:
            string - raw ascii text of the job output

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{automation_account_job_id}/output",
                                      query_parameters={ "api-version": "2019-06-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "%s error on ARM API request"
                          "to get output from job %s." 
                          "Raw error: %s", response.status_code, automation_account_job_id,
                          response.content )
            raise ArmRequestFailedException()

        return response.text

    def get_deployment_history( self, scope ):
        """Get deployment history at a given scope
        
        Args:
            scope - (str) The resource ID of the scope for which to get deployment history

        Returns:
            A list of dictionaries containing the ARM deployments at the given scope

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( f"{scope}/providers/Microsoft.Resources/deployments/",
                                      query_parameters={ "api-version": "2021-04-01"},
                                      method="GET"  )
        if response.status_code != 200:
            logging.error( "%s error on ARM API request to get deployments at scope"
                          "to get output from job %s." 
                          "Raw error: %s", response.status_code, scope,
                          response.content )
            raise ArmRequestFailedException()

        deployments = response.json()
        return deployments

    def get_current_user_pim_eligibility(self, scope):
        response = self._send_request( f"{scope}/providers/Microsoft.Authorization/roleEligibilityScheduleInstances",
                                       query_parameters={ "api-version": "2020-10-01",
                                                         "$filter": "asTarget()"},
                                       method="GET" )


        roles = response.json()
        return roles

    def get_descendants( self, management_group ):
        """Get direct descendants of a management group.

        This function will return subscriptions or management groups that are nested under
        the management group.
        
        Args:
            management_group - (str) the management group id to enumerate descendants

        Returns:
            A list of dictionaries containing the descendants of the management group

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        response = self._send_request( "/providers/Microsoft.Management/management_group"
                                       "/{management_group}/descendants", 
                                       query_parameters={ "api-version": "2020-05-01"},
                                       method="GET" )
        if response.status_code != 200:
            logging.error( "% error on ARM API request to get mgmt group descendants at scope %s."
                           " Raw error: %s", response.status_code, 
                           management_group, response.content )
            raise ArmRequestFailedException()

        descendants = response.json()["value"]
        return descendants

    def post( self, path, api_version, data ):
        """Send a POST request to ARM, and return the raw results

        Calls ARM at the path specified, and returns the raw deserialized results.
        
        Args:
            path - (str) The API path to call on ARM
            api_version - (str) The api-version to call for the ARM API
            data - (dict) The JSON data to send to ARM in the API request body

        Returns:
            A dictionary containing the raw results from the ARM request.

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        arm_raw_response = self._send_request( path, method="POST",
                                              query_parameters={ "api-version": api_version},
                                              json=data )
        return arm_raw_response.json()

    def put( self, path, api_version, data ):
        """Send a PUT request to ARM, and return the raw results

        Calls ARM at the path specified, and returns the raw deserialized results.
        
        Args:
            path - (str) The API path to call on ARM
            api_version - (str) The api-version to call for the ARM API
            data - (dict) The JSON data to send to ARM in the API request body

        Returns:
            A dictionary containing the raw results from the ARM request.

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        arm_raw_response = self._send_request( path, method="PUT",
                                              query_parameters={ "api-version": api_version},
                                              json=data )
        return arm_raw_response.json()

    def patch( self, path, api_version, data ):
        """Send a PATCH request to ARM, and return the raw results

        Calls ARM at the path specified, and returns the raw deserialized results.
        
        Args:
            path - (str) The API path to call on ARM
            api_version - (str) The api-version to call for the ARM API
            data - (dict) The JSON data to send to ARM in the API request body

        Returns:
            A dictionary containing the raw results from the ARM request.

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        arm_raw_response = self._send_request( path, method="PATCH",
                                              query_parameters={ "api-version": api_version},
                                              json=data )
        return arm_raw_response.json()

    def get( self, path, api_version=None ):
        """Send a GET request to ARM, and return the raw results

        Calls ARM at the path specified, and returns the raw deserialized results.
        
        Args:
            path - (str) The API path to call on ARM
            api_version - (str) The api-version to call for the ARM API

        Returns:
            A dictionary containing the raw results from the ARM request.

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        if "/providers" not in path:
            namespace="microsoft.resources"
            provider=path.split("/")[1]
        else:    
            namespace_and_provider=path.split('/providers/')[-1]
            namespace_and_provider_list=namespace_and_provider.split("/")
            namespace = namespace_and_provider_list[0].lower()
            provider_and_resource = "/".join(namespace_and_provider_list[1:])
            matching_providers=[]
            for provider in self.providers[namespace].keys():
                if provider in provider_and_resource:
                    matching_providers.append(provider)
            
            provider=max(p for p in matching_providers)
            logging.info("Resolved namespace to ", namespace)
            logging.info("Resolved provider to ", provider)

        provider_versions=self.providers[namespace][provider]
        latest=provider_versions[0]
        logging.info("Resolved latest provider version to ", latest)
        api_version = latest
        arm_raw_response = self._send_request( path,
            query_parameters={ "api-version": api_version} )
        return arm_raw_response.json()

    def delete( self, path ):
        """Make a DELETE request to a specific API path within the ARM API.

        Args:
            - path - (string) The ARM API path.

        Returns:
           Request.Response object from the DELETE request

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API
        """
        response = self._send_request( path, method="DELETE" )
        if response:
            return response.json()
        raise ArmRequestFailedException()

    def _deserialize_resource( self, resource ):
        """Deserialize ARM output to a GenericResource

        Deserialize a raw JSON object from the ARM API resopnse into a generic resource
        in AZOL.

        Instantiates an object with all possible fields from ARM. If a property does not exist
        in the raw response, instantiate it to None
        
        Args:
            resource - (dict) dictionary containing the raw JSON from an ARM request

        Returns:
            GenericResource containing all deserialized properties.

        Raises:
            ArmRequestFailedException: An error occurred accessing the ARM API

        """
        r = GenericResource(
            id=resource[ "id" ],
            changedTime=resource[ "changedTime" ] if "changedTime" in resource.keys() else None,
            createdTime=resource[ "createdTime" ] if "createdTime" in resource.keys() else None,
            extendedLocation=resource[ "extendedLocation" ] if (
                "extendedLocation" in resource.keys() ) else None,
            identity=resource[ "identity" ] if "identity" in resource.keys() else None,
            kind=resource[ "kind" ] if "kind" in resource.keys() else None,
            location=resource[ "location" ] if 'location' in resource.keys() else None,
            managedBy=resource[ "managedBy" ] if "managedBy" in resource.keys() else None,
            name=resource[ "name" ],
            plan=resource[ "plan" ] if "plan" in resource.keys() else None,
            properties=resource[ "properties" ] if "properties" in resource.keys() else {},
            provisioningState=resource[ "provisioningState" ] if (
                "provisioningState" in resource.keys() ) else None,
            sku=resource[ "sku" ] if "sku" in resource.keys() else None,
            tags=resource[ "tags" ] if "tags" in resource.keys() else None,
            type=resource[ "type" ]
        )
        return r
    