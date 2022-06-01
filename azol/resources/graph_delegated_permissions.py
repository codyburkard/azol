delegated_permissions = [
    {
        "adminConsentDescription": "Allows the app to read the available Teams templates, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read available Teams templates",
        "id": "cd87405c-5792-4f15-92f7-debc0db6d1d6",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Read available Teams templates, on your behalf.",
        "userConsentDisplayName": "Read available Teams templates",
        "value": "TeamTemplates.Read"
    },
    {
        "adminConsentDescription": "Allows the app to see your users' basic profile (e.g., name, picture, user name, email address)",
        "adminConsentDisplayName": "View users' basic profile",
        "id": "14dad69e-099b-42c9-810b-d002981feec1",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to see your basic profile (e.g., name, picture, user name, email address)",
        "userConsentDisplayName": "View your basic profile",
        "value": "profile"
    },
    {
        "adminConsentDescription": "Allows the app to read attack simulation and training data for an organization for the signed-in user.",
        "adminConsentDisplayName": "Read attack simulation data of an organization",
        "id": "104a7a4b-ca76-4677-b7e7-2f4bc482f381",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read attack simulation and training data for an organization on your behalf.",
        "userConsentDisplayName": "Read attack simulation data of an organization",
        "value": "AttackSimulation.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's directory access review default policy on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write your organization's directory access review default policy",
        "id": "4f5bc9c8-ea54-4772-973a-9ca119cb0409",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's directory access review default policy on your behalf.",
        "userConsentDisplayName": "Read and write your organization's directory access review default policy",
        "value": "Policy.ReadWrite.AccessReview"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's threat submissions and threat submission policies on behalf of the signed-in user. Also allows the app to create new threat submissions on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all threat submissions",
        "id": "8458e264-4eb9-4922-abe9-768d58f13c7f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization's threat submissions and threat submission policies on your behalf. Also allows the app to create new threat submissions on your behalf.",
        "userConsentDisplayName": "Read and write all threat submissions",
        "value": "ThreatSubmission.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to read any data from Records Management, such as configuration, labels, and policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read Records Management configuration,\u00a0labels, and policies",
        "id": "07f995eb-fc67-4522-ad66-2b8ca8ea3efd",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read any data from Records Management, such as configuration, labels and policies on your behalf.",
        "userConsentDisplayName": "Read Records Management configuration,\u00a0labels, and policies",
        "value": "RecordsManagement.Read.All"
    },
    {
        "adminConsentDescription": "Allow the application to create, update and delete any data from Records Management, such as configuration, labels, and policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write Records Management configuration, labels, and policies",
        "id": "f2833d75-a4e6-40ab-86d4-6dfe73c97605",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allow the application to create, update and delete any data from Records Management, such as configuration, labels, and policies on your behalf.",
        "userConsentDisplayName": "Read and write Records Management configuration, labels, and policies",
        "value": "RecordsManagement.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read details of delegated admin relationships with customers like access details (that includes roles) and the duration as well as specific role assignments to security groups on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read Delegated Admin relationships with customers",
        "id": "0c0064ea-477b-4130-82a5-4c2cc4ff68aa",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read details of Delegated Admin relationships with customers like access details (that includes roles) and the duration as well as specific role assignments to security groups on your behalf.",
        "userConsentDisplayName": "Read Delegated Admin relationships with customers",
        "value": "DelegatedAdminRelationship.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to manage (create-update-terminate) Delegated Admin relationships with customers as well as role assignments to security groups for active Delegated Admin relationships on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage Delegated Admin relationships with customers",
        "id": "885f682f-a990-4bad-a642-36736a74b0c7",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage (create-update-terminate) Delegated Admin relationships with customers and role assignments to security groups for active Delegated Admin relationships on your behalf.",
        "userConsentDisplayName": "Manage Delegated Admin relationships with customers",
        "value": "DelegatedAdminRelationship.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write all managed tenant information on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all managed tenant information",
        "id": "b31fa710-c9b3-4d9e-8f5e-8036eecddab9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write all managed tenant information on your behalf.",
        "userConsentDisplayName": "Read and write all managed tenant information",
        "value": "ManagedTenants.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all managed tenant information on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all managed tenant information",
        "id": "dc34164e-6c4a-41a0-be89-3ae2fbad7cd3",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all managed tenant information on your behalf.",
        "userConsentDisplayName": "Read all managed tenant information",
        "value": "ManagedTenants.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and manage the Cloud PC role-based access control (RBAC) settings, on behalf of the signed-in user. This includes reading and managing Cloud PC role definitions and role assignments.",
        "adminConsentDisplayName": "Read and write Cloud PC RBAC settings",
        "id": "501d06f8-07b8-4f18-b5c6-c191a4af7a82",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and manage the Cloud PC role-based access control (RBAC) settings, on your behalf. This includes reading and managing Cloud PC role definitions and memberships.",
        "userConsentDisplayName": "Read and write Cloud PC RBAC settings",
        "value": "RoleManagement.ReadWrite.CloudPC"
    },
    {
        "adminConsentDescription": "Allows the app to read the Cloud PC role-based access control (RBAC) settings, on behalf of the signed-in user.\u00a0 This includes reading Cloud PC role definitions and role assignments.",
        "adminConsentDisplayName": "Read Cloud PC RBAC settings",
        "id": "9619b88a-8a25-48a7-9571-d23be0337a79",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the Cloud PC role-based access control (RBAC) settings, on your behalf.\u00a0 This includes reading Cloud PC role definitions and role assignments.",
        "userConsentDisplayName": "Read Cloud PC RBAC settings",
        "value": "RoleManagement.Read.CloudPC"
    },
    {
        "adminConsentDescription": "Allows the app to read and write settings of external connections on behalf of a signed-in user. The signed-in user must be an administrator. The app can only read and write settings of connections that it is authorized to.",
        "adminConsentDisplayName": "Read and write external connections",
        "id": "4082ad95-c812-4f02-be92-780c4c4f1830",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write external connections on your behalf. The signed-in user must be an administrator. The app can only read and write external connections that it is authorized to, or it can create new external connections. ",
        "userConsentDisplayName": "Read and write external connections",
        "value": "ExternalConnection.ReadWrite.OwnedBy"
    },
    {
        "adminConsentDescription": "Allows the app to read all external connections on behalf of a signed-in user. The signed-in user must be an administrator.",
        "adminConsentDisplayName": "Read all external connections",
        "id": "a38267a5-26b6-4d76-9493-935b7599116b",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all external connections on your behalf. The signed-in user must be an administrator.",
        "userConsentDisplayName": "Read all external connections",
        "value": "ExternalConnection.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write all external connections on behalf of a signed-in user. The signed-in user must be an administrator.",
        "adminConsentDisplayName": "Read and write all external connections",
        "id": "bbbbd9b3-3566-4931-ac37-2b2180d9e334",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write all external connections on your behalf. The signed-in user must be an administrator.",
        "userConsentDisplayName": "Read and write all external connections",
        "value": "ExternalConnection.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write external items on behalf of a signed-in user. The signed-in user must be an administrator. The app can only read external items of the connection that it is authorized to.",
        "adminConsentDisplayName": "Read and write external items",
        "id": "4367b9d7-cee7-4995-853c-a0bdfe95c1f9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write external items on your behalf. The signed-in user must be an administrator. The app can only read external items of the connection that it is authorized to.",
        "userConsentDisplayName": "Read and write external items",
        "value": "ExternalItem.ReadWrite.OwnedBy"
    },
    {
        "adminConsentDescription": "Allows the app to read and write all external items on behalf of a signed-in user. The signed-in user must be an administrator.",
        "adminConsentDisplayName": "Read and write all external items",
        "id": "b02c54f8-eb48-4c50-a9f0-a149e5a2012f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write all external items on your behalf. The signed-in user must be an administrator.",
        "userConsentDisplayName": "Read and write all external items",
        "value": "ExternalItem.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read custom security attribute assignments for all principals in the tenant on behalf of a signed in user.",
        "adminConsentDisplayName": "Read custom security attribute assignments",
        "id": "b46ffa80-fe3d-4822-9a1a-c200932d54d0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read custom security attribute assignments for all principals in the tenant on your behalf.",
        "userConsentDisplayName": "Read custom security attribute assignments",
        "value": "CustomSecAttributeAssignment.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read custom security attribute definitions for the tenant on behalf of a signed in user.",
        "adminConsentDisplayName": "Read custom security attribute definitions",
        "id": "ce026878-a0ff-4745-a728-d4fedd086c07",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read custom security attribute definitions for the tenant on your behalf.",
        "userConsentDisplayName": "Read custom security attribute definitions",
        "value": "CustomSecAttributeDefinition.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's cross tenant access policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write your organization's cross tenant access policies",
        "id": "014b43d0-6ed4-4fc6-84dc-4b6f7bae7d85",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's cross tenant access policies on your behalf.",
        "userConsentDisplayName": "Read and write your organization's cross tenant access policies",
        "value": "Policy.ReadWrite.CrossTenantAccess"
    },
    {
        "adminConsentDescription": "Allows the app to read and write tags in Teams, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write tags in Teams",
        "id": "539dabd7-b5b6-4117-b164-d60cd15a8671",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write tags in Teams, on your behalf.",
        "userConsentDisplayName": "Read and write tags in Teams",
        "value": "TeamworkTag.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read tags in Teams, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read tags in Teams",
        "id": "57587d0b-8399-45be-b207-8050cec54575",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read tags in Teams, on your behalf.",
        "userConsentDisplayName": "Read tags in Teams",
        "value": "TeamworkTag.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read and write security incidents, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write to incidents",
        "id": "128ca929-1a19-45e6-a3b8-435ec44a36ba",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write to all security incidents that you have access to.",
        "userConsentDisplayName": "Read and write to security incidents",
        "value": "SecurityIncident.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read security incidents, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read incidents",
        "id": "b9abcc4f-94fc-4457-9141-d20ce80ec952",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all security incidents that you have access to.",
        "userConsentDisplayName": "Read security incidents",
        "value": "SecurityIncident.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write to all security alerts, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write to all security alerts",
        "id": "471f2a7f-2a42-4d45-a2bf-594d0838070d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write all alerts that you have access to.",
        "userConsentDisplayName": "Read and write all alerts",
        "value": "SecurityAlert.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all security alerts, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all security alerts",
        "id": "bc257fb8-46b4-4b15-8713-01e91bfbe4ea",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all security alerts that you have access to.",
        "userConsentDisplayName": "Read all alerts",
        "value": "SecurityAlert.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to update service announcement messages' user status on behalf of the signed-in user. The message status can be marked as read, archive, or favorite.",
        "adminConsentDisplayName": "Update user status on service announcement messages",
        "id": "636e1b0b-1cc2-4b1c-9aa9-4eeed9b9761b",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to update service announcement messages' status on your behalf. Your status for messages can be marked as read, archive, or favorite.",
        "userConsentDisplayName": "Update your user status on service announcement messages",
        "value": "ServiceMessageViewpoint.Write"
    },
    {
        "adminConsentDescription": "Allows the app to run hunting queries, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Run hunting queries",
        "id": "b152eca8-ea73-4a48-8c98-1a6742673d99",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to run hunting queries that you can execute.",
        "userConsentDisplayName": "Run hunting queries",
        "value": "ThreatHunting.Read.All"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself to teams the signed-in user can access.",
        "adminConsentDisplayName": "Allow the app to manage itself in teams",
        "id": "0f4595f7-64b1-4e13-81bc-11a249df07a9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself to teams you can access.",
        "userConsentDisplayName": "Allow the Teams app to manage itself in teams",
        "value": "TeamsAppInstallation.ReadWriteSelfForTeam"
    },
    {
        "adminConsentDescription": "Allow the app to read the management data for Teams devices on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read Teams devices",
        "id": "b659488b-9d28-4208-b2be-1c6652b3c970",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allow the app to read the management data for Teams devices on your behalf.",
        "userConsentDisplayName": "Read Teams devices",
        "value": "TeamworkDevice.Read.All"
    },
    {
        "adminConsentDescription": "Allow the app to read and write the management data for Teams devices on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write Teams devices",
        "id": "ddd97ecb-5c31-43db-a235-0ee20e635c40",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allow the app to read and write the management data for Teams devices on your behalf.",
        "userConsentDisplayName": "Read and write Teams devices",
        "value": "TeamworkDevice.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all identity risky service principal information for your organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all identity risky service principal information",
        "id": "ea5c4ab0-5a73-4f35-8272-5d5337884e5d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all identity risky service principal information for your organization, on your behalf.",
        "userConsentDisplayName": "Read all identity risky service principal information",
        "value": "IdentityRiskyServicePrincipal.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and update identity risky service principal information for all service principals in your organization, on behalf of the signed-in user. Update operations include dismissing risky service principals.",
        "adminConsentDisplayName": "Read and write all identity risky service principal information",
        "id": "bb6f654c-d7fd-4ae3-85c3-fc380934f515",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and update identity risky service principal information for all service principals in your organization, on your behalf. Update operations include dismissing risky service principals.",
        "userConsentDisplayName": "Read and write all identity risky service principal information",
        "value": "IdentityRiskyServicePrincipal.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs to teams the signed-in user can access.",
        "adminConsentDisplayName": "Allow the Teams app to manage only its own tabs in teams",
        "id": "f266662f-120a-4314-b26a-99b08617c7ef",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs to teams you can access.",
        "userConsentDisplayName": "Allow the Teams app to manage only its own tabs in teams",
        "value": "TeamsTab.ReadWriteSelfForTeam"
    },
    {
        "adminConsentDescription": "Allows the app to read the presence information and write activity and availability on behalf of the signed-in user. Presence information includes activity, availability, status note, calendar out-of-office message, timezone and location.",
        "adminConsentDisplayName": "Read and write a user's presence information",
        "id": "8d3c54a7-cf58-4773-bf81-c0cd6ad522bb",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read the presence information and write activity and availability on your behalf. Presence information includes activity, availability, status note, calendar out-of-office message, timezone and location.",
        "userConsentDisplayName": "Read and write your presence information",
        "value": "Presence.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read subject rights requests on behalf of the signed-in user",
        "adminConsentDisplayName": "Read subject rights requests",
        "id": "9c3af74c-fd0f-4db4-b17a-71939e2a9d77",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read subject rights requests on your behalf.",
        "userConsentDisplayName": "Read data subject requests",
        "value": "SubjectRightsRequest.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write subject rights requests on behalf of the signed-in user",
        "adminConsentDisplayName": "Read and write subject rights requests",
        "id": "2b8fcc74-bce1-4ae3-a0e8-60c53739299d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write subject rights requests on your behalf.",
        "userConsentDisplayName": "Read and write data subject requests",
        "value": "SubjectRightsRequest.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs for the signed-in user.",
        "adminConsentDisplayName": "Allow the Teams app to manage only its own tabs for a user",
        "id": "395dfec1-a0b9-465f-a783-8250a430cb8c",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs for you.",
        "userConsentDisplayName": "Allow the Teams app to manage only its own tabs for you",
        "value": "TeamsTab.ReadWriteSelfForUser"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs in chats the signed-in user can access.",
        "adminConsentDisplayName": "Allow the Teams app to manage only its own tabs in chats",
        "id": "0c219d04-3abf-47f7-912d-5cca239e90e6",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs in chats you can access.",
        "userConsentDisplayName": "Allow the Teams app to manage only its own tabs in chats",
        "value": "TeamsTab.ReadWriteSelfForChat"
    },
    {
        "adminConsentDescription": "Allows the app to read and write search configuration, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write your organization's search configuration",
        "id": "b1a7d408-cab0-47d2-a2a5-a74a3733600d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write search configuration, on your behalf.",
        "userConsentDisplayName": "Read and write your organization's search configuration",
        "value": "SearchConfiguration.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read search configuration, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read your organization's search configuration",
        "id": "7d307522-aa38-4cd0-bd60-90c6f0ac50bd",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read search configuration, on your behalf.",
        "userConsentDisplayName": "Read your organization's search configuration",
        "value": "SearchConfiguration.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read online meeting artifacts on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user's online meeting artifacts",
        "id": "110e5abb-a10c-4b59-8b55-9b4daa4ef743",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read online meeting artifacts on your behalf.",
        "userConsentDisplayName": "Read user's online meeting artifacts",
        "value": "OnlineMeetingArtifact.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and manage the active role-based access control (RBAC) assignments for your company's directory, on behalf of the signed-in user. This includes managing active directory role membership, and reading directory role templates, directory roles and active memberships.",
        "adminConsentDisplayName": "Read, update, and delete all active role assignments for your company's directory",
        "id": "8c026be3-8e26-4774-9372-8d5d6f21daff",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and manage the active role-based access control (RBAC) assignments for your company's directory, on your behalf. This includes managing active directory role membership, and reading directory role templates, directory roles and active memberships.",
        "userConsentDisplayName": "Read, update, and delete all active role assignments for your company's directory",
        "value": "RoleAssignmentSchedule.ReadWrite.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read and manage the eligible role-based access control (RBAC) assignments for your company's directory, on behalf of the signed-in user. This includes managing eligible directory role membership, and reading directory role templates, directory roles and eligible memberships.",
        "adminConsentDisplayName": "Read, update, and delete  all eligible role assignments for your company's directory",
        "id": "62ade113-f8e0-4bf9-a6ba-5acb31db32fd",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and manage the eligible role-based access control (RBAC) assignments for your company's directory, on your behalf. This includes managing eligible directory role membership, and reading directory role templates, directory roles and eligible memberships.",
        "userConsentDisplayName": "Read, update, and delete  all eligible role assignments for your company's directory",
        "value": "RoleEligibilitySchedule.ReadWrite.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read, update, and delete policies for privileged role-based access control (RBAC) assignments of your company's directory, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read, update, and delete all policies for privileged role assignments of your company's directory",
        "id": "1ff1be21-34eb-448c-9ac9-ce1f506b2a68",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, update, and delete policies for privileged role-based access control (RBAC) assignments of your company's directory, on your behalf.",
        "userConsentDisplayName": "Read, update, and delete all policies for privileged role assignments of your company's directory",
        "value": "RoleManagementPolicy.ReadWrite.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read the active role-based access control (RBAC) assignments for your company's directory, on behalf of the signed-in user. This includes reading directory role templates, and directory roles.",
        "adminConsentDisplayName": "Read all active role assignments for your company's directory",
        "id": "344a729c-0285-42c6-9014-f12b9b8d6129",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the active role-based access control (RBAC) assignments for your company's directory, on your behalf. This includes reading directory role templates, and directory roles.",
        "userConsentDisplayName": "Read all active role assignments for your company's directory",
        "value": "RoleAssignmentSchedule.Read.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read the eligible role-based access control (RBAC) assignments for your company's directory, on behalf of the signed-in user. This includes reading directory role templates, and directory roles.",
        "adminConsentDisplayName": "Read all eligible role assignments for your company's directory",
        "id": "eb0788c2-6d4e-4658-8c9e-c0fb8053f03d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the eligible role-based access control (RBAC) assignments for your company's directory, on your behalf. This includes reading directory role templates, and directory roles.",
        "userConsentDisplayName": "Read all eligible role assignments for your company's directory",
        "value": "RoleEligibilitySchedule.Read.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read policies for privileged role-based access control (RBAC) assignments of your company's directory, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all policies for privileged role assignments of your company's directory",
        "id": "3de2cdbe-0ff5-47d5-bdee-7f45b4749ead",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read policies for privileged role-based access control (RBAC) assignments of your company's directory, on your behalf.",
        "userConsentDisplayName": "Read all policies for privileged role assignments of your company's directory",
        "value": "RoleManagementPolicy.Read.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read and write all Windows update deployment settings for the organization on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all Windows update deployment settings",
        "id": "11776c0c-6138-4db3-a668-ee621bea2555",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write all Windows update deployment settings for the organization on your behalf.",
        "userConsentDisplayName": "Read and write all Windows update deployment settings",
        "value": "WindowsUpdates.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's mobility management policies on behalf of the signed-in user.  For example, a mobility management policy can set the enrollment scope for a given mobility management application.",
        "adminConsentDisplayName": "Read and write your organization's mobility management policies",
        "id": "a8ead177-1889-4546-9387-f25e658e2a79",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's mobility management policies on your behalf.  For example, a mobility management policy can set the enrollment scope for a given mobility management application.",
        "userConsentDisplayName": "Read and write your organization's mobility management policies",
        "value": "Policy.ReadWrite.MobilityManagement"
    },
    {
        "adminConsentDescription": "Allows the app to read basic unified group properties, memberships and owners of the group the signed-in guest is a member of.",
        "adminConsentDisplayName": "Read unified group memberships as guest",
        "id": "73e75199-7c3e-41bb-9357-167164dbb415",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read basic unified group properties, memberships and owners of the group you are a member of.",
        "userConsentDisplayName": "Read unified group memberships as guest",
        "value": "UnifiedGroupMember.Read.AsGuest"
    },
    {
        "adminConsentDescription": "Allows the app to update service principal endpoints",
        "adminConsentDisplayName": "Read and update service principal endpoints",
        "id": "7297d82c-9546-4aed-91df-3d4f0a9b3ff0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to update service principal endpoints",
        "userConsentDisplayName": "Read and update service principal endpoints",
        "value": "ServicePrincipalEndpoint.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read service principal endpoints",
        "adminConsentDisplayName": "Read service principal endpoints",
        "id": "9f9ce928-e038-4e3b-8faf-7b59049a8ddc",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read service principal endpoints",
        "userConsentDisplayName": "Read service principal endpoints",
        "value": "ServicePrincipalEndpoint.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to create new notifications in users' teamwork activity feeds on behalf of the signed in user. These notifications may not be discoverable or be held or governed by compliance policies.",
        "adminConsentDisplayName": "Send a teamwork activity as the user",
        "id": "7ab1d787-bae7-4d5d-8db6-37ea32df9186",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to create new activities in your teamwork activity feed, and send new activities to other users' activity feed, on your behalf.",
        "userConsentDisplayName": "Send a teamwork activity",
        "value": "TeamsActivity.Send"
    },
    {
        "adminConsentDescription": "Allows the app to read and write eDiscovery objects such as cases, custodians, review sets and other related objects on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all eDiscovery objects",
        "id": "acb8f680-0834-4146-b69e-4ab1b39745ad",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write eDiscovery objects such as cases, custodians, review sets and other related objects on your behalf.",
        "userConsentDisplayName": "Read and write all eDiscovery objects",
        "value": "eDiscovery.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read eDiscovery objects such as cases, custodians, review sets and other related objects on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all eDiscovery objects",
        "id": "99201db3-7652-4d5a-809a-bdb94f85fe3c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read eDiscovery objects such as cases, custodians, review sets and other related objects on your behalf.",
        "userConsentDisplayName": "Read all eDiscovery objects",
        "value": "eDiscovery.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write custom security attribute assignments for all principals in the tenant on behalf of a signed in user.",
        "adminConsentDisplayName": "Read and write custom security attribute assignments",
        "id": "ca46335e-8453-47cd-a001-8459884efeae",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write custom security attribute assignments for all principals in the tenant on your behalf.",
        "userConsentDisplayName": "Read and write custom security attribute assignments",
        "value": "CustomSecAttributeAssignment.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write custom security attribute definitions for the tenant on behalf of a signed in user.",
        "adminConsentDisplayName": "Read and write custom security attribute definitions",
        "id": "8b0160d4-5743-482b-bb27-efc0a485ca4a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write custom security attribute definitions for the tenant on your behalf.",
        "userConsentDisplayName": "Read and write custom security attribute definitions",
        "value": "CustomSecAttributeDefinition.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read email in the signed-in user's mailbox except body, previewBody, attachments and any extended properties.",
        "adminConsentDisplayName": "Read user basic mail",
        "id": "a4b8392a-d8d1-4954-a029-8e668a39a170",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read email in the signed-in user's mailbox except body, previewBody, attachments and any extended properties.",
        "userConsentDisplayName": "Read user basic mail",
        "value": "Mail.ReadBasic"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's feature rollout policies on behalf of the signed-in user. Includes abilities to assign and remove users and groups to rollout of a specific feature.",
        "adminConsentDisplayName": "Read and write your organization's feature rollout policies",
        "id": "92a38652-f13b-4875-bc77-6e1dbb63e1b2",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's feature rollout policies on your behalf. Includes abilities to assign and remove users and groups to rollout of a specific feature.",
        "userConsentDisplayName": "Read and write your organization's feature rollout policies",
        "value": "Policy.ReadWrite.FeatureRollout"
    },
    {
        "adminConsentDescription": "Allows the app to read and manage the role-based access control (RBAC) settings for your company's directory, on behalf of the signed-in user. This includes instantiating directory roles and managing directory role membership, and reading directory role templates, directory roles and memberships.",
        "adminConsentDisplayName": "Read and write directory RBAC settings",
        "id": "d01b97e9-cbc0-49fe-810a-750afd5527a3",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and manage the role-based access control (RBAC) settings for your company's directory, on your behalf. This includes instantiating directory roles and managing directory role membership, and reading directory role templates, directory roles and memberships.",
        "userConsentDisplayName": "Read and write directory RBAC settings",
        "value": "RoleManagement.ReadWrite.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read the role-based access control (RBAC) settings for your company's directory, on behalf of the signed-in user.  This includes reading directory role templates, directory roles and memberships.",
        "adminConsentDisplayName": "Read directory RBAC settings",
        "id": "741c54c3-0c1e-44a1-818b-3f97ab4e8c83",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the role-based access control (RBAC) settings for your company's directory, on your behalf.  This includes reading directory role templates, directory roles and memberships.",
        "userConsentDisplayName": "Read directory RBAC settings",
        "value": "RoleManagement.Read.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the organization and related resources, on behalf of the signed-in user.\u00a0Related resources include things like subscribed skus and tenant branding information.",
        "adminConsentDisplayName": "Read and write organization information",
        "id": "46ca0847-7e6b-426e-9775-ea810a948356",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the organization and related resources, on your behalf.\u00a0Related resources include things like subscribed skus and tenant branding information.",
        "userConsentDisplayName": "Read and write organization information",
        "value": "Organization.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the organization and related resources, on behalf of the signed-in user.\u00a0Related resources include things like subscribed skus and tenant branding information.",
        "adminConsentDisplayName": "Read organization information",
        "id": "4908d5b9-3fb2-4b1e-9336-1888b7937185",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the organization and related resources, on your behalf.\u00a0Related resources include things like subscribed skus and tenant branding information.",
        "userConsentDisplayName": "Read organization information",
        "value": "Organization.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your company's places (conference rooms and room lists) for calendar events and other applications, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all company places",
        "id": "cb8f45a0-5c2e-4ea1-b803-84b870a7d7ec",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your company's places (conference rooms and room lists) for calendar events and other applications, on your behalf.",
        "userConsentDisplayName": "Read all company places",
        "value": "Place.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to manage workforce integrations, to synchronize data from Microsoft Teams Shifts, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write workforce integrations",
        "id": "08c4b377-0d23-4a8b-be2a-23c1c1d88545",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage workforce integrations, to synchronize data from Microsoft Teams Shifts, on your behalf.",
        "userConsentDisplayName": "Read and write workforce integrations",
        "value": "WorkforceIntegration.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read workforce integrations, to synchronize data from Microsoft Teams Shifts, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read workforce integrations",
        "id": "f1ccd5a7-6383-466a-8db8-1a656f7d06fa",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read workforce integrations, to synchronize data from Microsoft Teams Shifts, on your behalf.",
        "userConsentDisplayName": "Read workforce integrations",
        "value": "WorkforceIntegration.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, update, delete and perform actions on access reviews, reviewers, decisions and settings for group and app memberships that the signed-in user has access to in the organization.",
        "adminConsentDisplayName": "Manage access reviews for group and app memberships",
        "id": "5af8c3f5-baca-439a-97b0-ea58a435e269",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, update and perform action on access reviews, reviewers, decisions and settings that you have access to.",
        "userConsentDisplayName": "Manage access reviews for group and app memberships",
        "value": "AccessReview.ReadWrite.Membership"
    },
    {
        "adminConsentDescription": "Allows the app to manage hybrid identity service configuration by creating, viewing, updating and deleting on-premises published resources, on-premises agents and agent groups, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage on-premises published resources",
        "id": "8c4d5184-71c2-4bf8-bb9d-bc3378c9ad42",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage hybrid identity service configuration by creating, viewing, updating and deleting on-premises published resources, on-premises agents and agent groups, on your behalf.",
        "userConsentDisplayName": "Manage on-premises published resources",
        "value": "OnPremisesPublishingProfiles.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows an app to read information protection sensitivity labels and label policy settings, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user sensitivity labels and label policies.",
        "id": "4ad84827-5578-4e18-ad7a-86530b12f884",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read information protection sensitivity labels and label policy settings, on behalf of the signed-in user.",
        "userConsentDisplayName": "Read user sensitivity labels and label policies.",
        "value": "InformationProtectionPolicy.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read administrative units and administrative unit membership on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read administrative units",
        "id": "3361d15d-be43-4de6-b441-3c746d05163d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read administrative units and administrative unit membership on your behalf.",
        "userConsentDisplayName": "Read administrative units",
        "value": "AdministrativeUnit.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete administrative units and manage administrative unit membership on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write administrative units",
        "id": "7b8a2d34-6b3f-4542-a343-54651608ad81",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to create, read, update, and delete administrative units and manage administrative unit membership on your behalf.",
        "userConsentDisplayName": "Read and write administrative units",
        "value": "AdministrativeUnit.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your family information, members and their basic profile.",
        "adminConsentDisplayName": "Read your family info",
        "id": "3a1e4806-a744-4c70-80fc-223bf8582c46",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your family information, members and their basic profile.",
        "userConsentDisplayName": "Read your family info",
        "value": "Family.Read"
    },
    {
        "adminConsentDescription": "Allows the app to create threat indicators, and fully manage those threat indicators (read, update and delete), on behalf of the signed-in user. \u00a0It cannot update any threat indicators it does not own.",
        "adminConsentDisplayName": "Manage threat indicators this app creates or owns",
        "id": "91e7d36d-022a-490f-a748-f8e011357b42",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to create threat indicators, and fully manage those threat indicators (read, update and delete), on your behalf. \u00a0It cannot update any threat indicators that it is not an owner of.",
        "userConsentDisplayName": "Manage threat indicators this app creates or owns",
        "value": "ThreatIndicators.ReadWrite.OwnedBy"
    },
    {
        "adminConsentDescription": "Allows the app to read or update security actions, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and update your organization's security actions",
        "id": "dc38509c-b87d-4da0-bd92-6bec988bac4a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and update security actions, on your behalf.",
        "userConsentDisplayName": "Read and update your organization's security actions",
        "value": "SecurityActions.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read security actions, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read your organization's security actions",
        "id": "1638cddf-07a4-4de2-8645-69c96cacad73",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read security actions, on your behalf.",
        "userConsentDisplayName": "Read your organization's security actions",
        "value": "SecurityActions.Read.All"
    },
    {
        "adminConsentDescription": "Allows an app to read 1 on 1 or group chats threads, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user chat messages",
        "id": "f501c180-9344-439a-bca0-6cbf209fd270",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read your 1 on 1 or group chat messages in Microsoft Teams, on your behalf.",
        "userConsentDisplayName": "Read your chat messages",
        "value": "Chat.Read"
    },
    {
        "adminConsentDescription": "Allows an app to read and write 1 on 1 or group chats threads, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write user chat messages",
        "id": "9ff7295e-131b-4d94-90e1-69fde507ac11",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read and write your 1 on 1 or group chat messages in Microsoft Teams, on your behalf.",
        "userConsentDisplayName": "Read and write your chat messages",
        "value": "Chat.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's trust framework policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write your organization's trust framework policies",
        "id": "cefba324-1a70-4a6e-9c1d-fd670b7ae392",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's trust framework policies on your behalf.",
        "userConsentDisplayName": "Read and write trust framework policies",
        "value": "Policy.ReadWrite.TrustFramework"
    },
    {
        "adminConsentDescription": "Allows the app to read trust framework key set properties on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read trust framework key sets",
        "id": "7ad34336-f5b1-44ce-8682-31d7dfcd9ab9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read trust framework key sets, on your behalf.",
        "userConsentDisplayName": "Read trust framework key sets",
        "value": "TrustFrameworkKeySet.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write trust framework key set properties on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write trust framework key sets",
        "id": "39244520-1e7d-4b4a-aee0-57c65826e427",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read or write trust framework key sets, on your behalf.",
        "userConsentDisplayName": "Read and write trust framework key sets",
        "value": "TrustFrameworkKeySet.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and update identity risk event information for all users in your organization on behalf of the signed-in user.\u00a0Update operations include confirming risk event detections.\u00a0",
        "adminConsentDisplayName": "Read and write risk event information",
        "id": "9e4862a5-b68f-479e-848a-4e07e25c9916",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and update identity risk event information for all users in your organization on your behalf.\u00a0Update operations include confirming risk event detections.\u00a0",
        "userConsentDisplayName": "Read and write risk event information",
        "value": "IdentityRiskEvent.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and update identity risky user information for all users in your organization on behalf of the signed-in user.\u00a0Update operations include dismissing risky users.",
        "adminConsentDisplayName": "Read and write risky user information",
        "id": "e0a7cdbb-08b0-4697-8264-0069786e9674",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and update identity risky user information for all users in your organization on your behalf.\u00a0Update operations include dismissing risky users.",
        "userConsentDisplayName": "Read and write identity risky user information",
        "value": "IdentityRiskyUser.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the signed-in user's mailbox.",
        "adminConsentDisplayName": "Read user mail ",
        "id": "570282fd-fa5c-430d-a7fd-fc8dc98a9dca",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read email in your mailbox. ",
        "userConsentDisplayName": "Read your mail ",
        "value": "Mail.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read identity risky user information for all users in your organization on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read identity risky user information",
        "id": "d04bb851-cb7c-4146-97c7-ca3e71baf56c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read identity risky user information for all users in your organization on behalf of the signed-in user.",
        "userConsentDisplayName": "Read identity risky user information",
        "value": "IdentityRiskyUser.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the signed-in user's activity statistics, such as how much time the user has spent on emails, in meetings, or in chat sessions.",
        "adminConsentDisplayName": "Read user activity statistics",
        "id": "e03cf23f-8056-446a-8994-7d93dfc8b50e",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your activity statistics, such as how much time you've spent on emails, in meetings, or in chat sessions.",
        "userConsentDisplayName": "Read your activity statistics",
        "value": "Analytics.Read"
    },
    {
        "adminConsentDescription": "Allows the app to see and update the data you gave it access to, even when users are not currently using the app. This does not give the app any additional permissions.",
        "adminConsentDisplayName": "Maintain access to data you have given it access to",
        "id": "7427e0e9-2fba-42fe-b0c0-848c9e6a8182",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to see and update the data you gave it access to, even when you are not currently using the app. This does not give the app any additional permissions.",
        "userConsentDisplayName": "Maintain access to data you have given it access to",
        "value": "offline_access"
    },
    {
        "adminConsentDescription": "Allows the app to have the same access to mailboxes as the signed-in user via Exchange Web Services.",
        "adminConsentDisplayName": "Access mailboxes as the signed-in user via Exchange Web Services",
        "id": "9769c687-087d-48ac-9cb3-c37dde652038",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app full access to your mailboxes on your behalf.",
        "userConsentDisplayName": "Access your mailboxes",
        "value": "EWS.AccessAsUser.All"
    },
    {
        "adminConsentDescription": "Allows the app to export data (e.g. customer content or system-generated logs), associated with any user in your company, when the app is used by a privileged user (e.g. a Company Administrator).",
        "adminConsentDisplayName": "Export user's data",
        "id": "405a51b5-8d8d-430b-9842-8be4b0e9f324",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to export data (e.g. customer content or system-generated logs), associated with any user in your company, when the app is used by a privileged user (e.g. a Company Administrator).",
        "userConsentDisplayName": "Export user's data",
        "value": "User.Export.All"
    },
    {
        "adminConsentDescription": "Allows the app to deliver its notifications on behalf of signed-in users. Also allows the app to read, update, and delete the user's notification items for this app.",
        "adminConsentDisplayName": "Deliver and manage user notifications for this app",
        "id": "89497502-6e42-46a2-8cb2-427fd3df970a",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to deliver its notifications, on your behalf. Also allows the app to read, update, and delete your notification items for this app.",
        "userConsentDisplayName": "Deliver and manage your notifications for this app",
        "value": "Notifications.ReadWrite.CreatedByApp"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's conditional access policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write your organization's conditional access policies",
        "id": "ad902697-1014-4ef5-81ef-2b4301988e8c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's conditional access policies on your behalf.",
        "userConsentDisplayName": "Read and write your organization's conditional access policies",
        "value": "Policy.ReadWrite.ConditionalAccess"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read your organization's policies",
        "id": "572fea84-0151-49b2-9301-11cb16974376",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization's policies on your behalf.",
        "userConsentDisplayName": "Read your organization's policies",
        "value": "Policy.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read access reviews, reviewers, decisions and settings that the signed-in user has access to in the organization.",
        "adminConsentDisplayName": "Read all access reviews that user can access",
        "id": "ebfcd32b-babb-40f4-a14b-42706e83bd28",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read information on access reviews, reviewers, decisions and settings that you have access to.",
        "userConsentDisplayName": "Read access reviews that you can access",
        "value": "AccessReview.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, update, delete and perform actions on access reviews, reviewers, decisions and settings that the signed-in user has access to in the organization.",
        "adminConsentDisplayName": "Manage all access reviews that user can access",
        "id": "e4aa47b9-9a69-4109-82ed-36ec70d85ff1",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, update and perform action on access reviews, reviewers, decisions and settings that you have access to.",
        "userConsentDisplayName": "Manage access reviews that you can access",
        "value": "AccessReview.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read programs and program controls that the signed-in user has access to in the organization.",
        "adminConsentDisplayName": "Read all programs that user can access",
        "id": "c492a2e1-2f8f-4caa-b076-99bbf6e40fe4",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read information on programs and program controls that you have access to.",
        "userConsentDisplayName": "Read programs that you can access",
        "value": "ProgramControl.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, update, delete and perform actions on programs and program controls that the signed-in user has access to in the organization.",
        "adminConsentDisplayName": "Manage all programs that user can access",
        "id": "50fd364f-9d93-4ae1-b170-300e87cccf84",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, update and perform action on programs and program controls that you have access to.",
        "userConsentDisplayName": "Manage programs that you can access",
        "value": "ProgramControl.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete apps in the app catalogs.",
        "adminConsentDisplayName": "Read and write to all app catalogs",
        "id": "1ca167d5-1655-44a1-8adf-1414072e1ef9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to create, read, update, and delete apps in the app catalogs.",
        "userConsentDisplayName": "Read and write to all app catalogs",
        "value": "AppCatalog.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to request and manage just in time elevation (including scheduled elevation) of users to Azure AD built-in administrative roles, on behalf of signed-in users.",
        "adminConsentDisplayName": "Read and write privileged access to Azure AD",
        "id": "3c3c74f5-cdaa-4a97-b7e0-4e788bfcfb37",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to request and manage just in time elevation (including scheduled elevation) of users to Azure AD built-in administrative roles, on your behalf.",
        "userConsentDisplayName": "Read and write privileged access to Azure AD",
        "value": "PrivilegedAccess.ReadWrite.AzureAD"
    },
    {
        "adminConsentDescription": "Allows the app to read terms of use agreements on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all terms of use agreements",
        "id": "af2819c9-df71-4dd3-ade7-4d7c9dc653b7",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read terms of use agreements on your behalf.",
        "userConsentDisplayName": "Read all terms of use agreements",
        "value": "Agreement.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write terms of use agreements on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all terms of use agreements",
        "id": "ef4b5d93-3104-4664-9053-a5c49ab44218",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write terms of use agreements on your behalf.",
        "userConsentDisplayName": "Read and write all terms of use agreements",
        "value": "Agreement.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read terms of use acceptance statuses on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user terms of use acceptance statuses",
        "id": "0b7643bb-5336-476f-80b5-18fbfbc91806",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your terms of use acceptance statuses.",
        "userConsentDisplayName": "Read your terms of use acceptance statuses",
        "value": "AgreementAcceptance.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read terms of use acceptance statuses on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read terms of use acceptance statuses that user can access",
        "id": "a66a5341-e66e-4897-9d52-c2df58c2bfb9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read terms of use acceptance statuses on your behalf.",
        "userConsentDisplayName": "Read all terms of use acceptance statuses",
        "value": "AgreementAcceptance.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and query your audit log activities, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read audit log data",
        "id": "e4c9e354-4dc5-45b8-9e7c-e1393b0b1a20",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and query your audit log activities, on your behalf.",
        "userConsentDisplayName": "Read audit log data",
        "value": "AuditLog.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and report the signed-in user's activity in the app.",
        "adminConsentDisplayName": "Read and write app activity to users' activity feed",
        "id": "47607519-5fb1-47d9-99c7-da4b48f369b1",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read and report your activity in the app.",
        "userConsentDisplayName": "Read and write app activity to your activity feed",
        "value": "UserActivity.ReadWrite.CreatedByApp"
    },
    {
        "adminConsentDescription": "Allows the app to read properties of Microsoft Intune-managed device configuration and device compliance policies and their assignment to groups.",
        "adminConsentDisplayName": "Read Microsoft Intune Device Configuration and Policies",
        "id": "f1493658-876a-4c87-8fa7-edb559b3476a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read properties of Microsoft Intune-managed device configuration and device compliance policies and their assignment to groups.",
        "userConsentDisplayName": "Read Microsoft Intune Device Configuration and Policies",
        "value": "DeviceManagementConfiguration.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write properties of Microsoft Intune-managed device configuration and device compliance policies and their assignment to groups.",
        "adminConsentDisplayName": "Read and write Microsoft Intune Device Configuration and Policies",
        "id": "0883f392-0a7a-443d-8c76-16a6d39c7b63",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write properties of Microsoft Intune-managed device configuration and device compliance policies and their assignment to groups.",
        "userConsentDisplayName": "Read and write Microsoft Intune Device Configuration and Policies",
        "value": "DeviceManagementConfiguration.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the properties, group assignments and status of apps, app configurations and app protection policies managed by Microsoft Intune.",
        "adminConsentDisplayName": "Read Microsoft Intune apps",
        "id": "4edf5f54-4666-44af-9de9-0144fb4b6e8c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the properties, group assignments and status of apps, app configurations and app protection policies managed by Microsoft Intune.",
        "userConsentDisplayName": "Read Microsoft Intune apps",
        "value": "DeviceManagementApps.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the properties, group assignments and status of apps, app configurations and app protection policies managed by Microsoft Intune.",
        "adminConsentDisplayName": "Read and write Microsoft Intune apps",
        "id": "7b3f05d5-f68c-4b8d-8c59-a2ecd12f24af",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the properties, group assignments and status of apps, app configurations and app protection policies managed by Microsoft Intune.",
        "userConsentDisplayName": "Read and write Microsoft Intune apps",
        "value": "DeviceManagementApps.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the properties relating to the Microsoft Intune Role-Based Access Control (RBAC) settings.",
        "adminConsentDisplayName": "Read Microsoft Intune RBAC settings",
        "id": "49f0cc30-024c-4dfd-ab3e-82e137ee5431",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the properties relating to the Microsoft Intune Role-Based Access Control (RBAC) settings.",
        "userConsentDisplayName": "Read Microsoft Intune RBAC settings",
        "value": "DeviceManagementRBAC.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the properties relating to the Microsoft Intune Role-Based Access Control (RBAC) settings.",
        "adminConsentDisplayName": "Read and write Microsoft Intune RBAC settings",
        "id": "0c5e8a55-87a6-4556-93ab-adc52c4d862d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the properties relating to the Microsoft Intune Role-Based Access Control (RBAC) settings.",
        "userConsentDisplayName": "Read and write Microsoft Intune RBAC settings",
        "value": "DeviceManagementRBAC.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the properties of devices managed by Microsoft Intune.",
        "adminConsentDisplayName": "Read Microsoft Intune devices",
        "id": "314874da-47d6-4978-88dc-cf0d37f0bb82",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the properties of devices managed by Microsoft Intune.",
        "userConsentDisplayName": "Read devices Microsoft Intune devices",
        "value": "DeviceManagementManagedDevices.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the properties of devices managed by Microsoft Intune. Does not allow high impact operations such as remote wipe and password reset on the device\u2019s owner.",
        "adminConsentDisplayName": "Read and write Microsoft Intune devices",
        "id": "44642bfe-8385-4adc-8fc6-fe3cb2c375c3",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the properties of devices managed by Microsoft Intune. Does not allow high impact operations such as remote wipe and password reset on the device\u2019s owner.",
        "userConsentDisplayName": "Read and write Microsoft Intune devices",
        "value": "DeviceManagementManagedDevices.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to perform remote high impact actions such as wiping the device or resetting the passcode on devices managed by Microsoft Intune.",
        "adminConsentDisplayName": "Perform user-impacting remote actions on Microsoft Intune devices",
        "id": "3404d2bf-2b13-457e-a330-c24615765193",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to perform remote high impact actions such as wiping the device or resetting the passcode on devices managed by Microsoft Intune.",
        "userConsentDisplayName": "Perform user-impacting remote actions on Microsoft Intune devices",
        "value": "DeviceManagementManagedDevices.PrivilegedOperations.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write Microsoft Intune service properties including device enrollment and third party service connection configuration.",
        "adminConsentDisplayName": "Read and write Microsoft Intune configuration",
        "id": "662ed50a-ac44-4eef-ad86-62eed9be2a29",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write Microsoft Intune service properties including device enrollment and third party service connection configuration.",
        "userConsentDisplayName": "Read and write Microsoft Intune configuration",
        "value": "DeviceManagementServiceConfig.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read Microsoft Intune service properties including device enrollment and third party service connection configuration.",
        "adminConsentDisplayName": "Read Microsoft Intune configuration",
        "id": "8696daa5-bce5-4b2e-83f9-51b6defc4e1e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read Microsoft Intune service properties including device enrollment and third party service connection configuration.",
        "userConsentDisplayName": "Read Microsoft Intune configuration",
        "value": "DeviceManagementServiceConfig.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization\u2019s security events on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read your organization\u2019s security events",
        "id": "64733abd-851e-478a-bffb-e47a14b18235",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization\u2019s security events on your behalf.",
        "userConsentDisplayName": "Read your organization\u2019s security events",
        "value": "SecurityEvents.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization\u2019s security events on behalf of the signed-in user. Also allows the app to update editable properties in security events on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and update your organization\u2019s security events",
        "id": "6aedf524-7e1c-45a7-bd76-ded8cab8d0fc",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization\u2019s security events on your behalf. Also allows you to update editable properties in security events.",
        "userConsentDisplayName": "Read and update your organization\u2019s security events",
        "value": "SecurityEvents.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read a scored list of relevant people of the signed-in user or other users in the signed-in user's organization. The list can include local contacts, contacts from social networking, your organization's directory, and people from recent communications (such as email and Skype).",
        "adminConsentDisplayName": "Read all users' relevant people lists",
        "id": "b89f9189-71a5-4e70-b041-9887f0bc7e4a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read a list of people in the order that is most relevant to you. Allows the app to read a list of people in the order that is most relevant to another user in your organization. These can include local contacts, contacts from social networking, people listed in your organization\u2019s directory, and people from recent communications.",
        "userConsentDisplayName": "Read all users\u2019 relevant people lists",
        "value": "People.Read.All"
    },
    {
        "adminConsentDescription": "Manage the state and settings of all Microsoft education apps on behalf of the user.",
        "adminConsentDisplayName": "Manage education app settings",
        "id": "63589852-04e3-46b4-bae9-15d5b1050748",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage the state and settings of all Microsoft education apps on your behalf.",
        "userConsentDisplayName": "Manage your education app settings",
        "value": "EduAdministration.ReadWrite"
    },
    {
        "adminConsentDescription": "Read the state and settings of all Microsoft education apps on behalf of the user.",
        "adminConsentDisplayName": "Read education app settings",
        "id": "8523895c-6081-45bf-8a5d-f062a2f12c9f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to view the state and settings of all Microsoft education apps on your behalf.",
        "userConsentDisplayName": "View your education app settings",
        "value": "EduAdministration.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read and write assignments and their grades on behalf of the user.",
        "adminConsentDisplayName": "Read and write users' class assignments and their grades",
        "id": "2f233e90-164b-4501-8bce-31af2559a2d3",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to view and modify your assignments on your behalf including \u00a0grades.",
        "userConsentDisplayName": "View and modify your assignments and grades",
        "value": "EduAssignments.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read assignments and their grades on behalf of the user.",
        "adminConsentDisplayName": "Read users' class assignments and their grades",
        "id": "091460c9-9c4a-49b2-81ef-1f3d852acce2",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to view your assignments on your behalf including grades.",
        "userConsentDisplayName": "View your assignments and grades",
        "value": "EduAssignments.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read and write assignments without grades on behalf of the user.",
        "adminConsentDisplayName": "Read and write users' class assignments without grades",
        "id": "2ef770a1-622a-47c4-93ee-28d6adbed3a0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to view and modify your assignments on your behalf without seeing grades.",
        "userConsentDisplayName": "View and modify your assignments without grades",
        "value": "EduAssignments.ReadWriteBasic"
    },
    {
        "adminConsentDescription": "Allows the app to read assignments without grades on behalf of the user.",
        "adminConsentDisplayName": "Read users' class assignments without grades",
        "id": "c0b0103b-c053-4b2e-9973-9f3a544ec9b8",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to view your assignments on your behalf without seeing grades.",
        "userConsentDisplayName": "View your assignments without grades",
        "value": "EduAssignments.ReadBasic"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the structure of schools and classes in an organization's roster and education-specific information about users to be read and written on behalf of the user.",
        "adminConsentDisplayName": "Read and write users' view of the roster",
        "id": "359e19a6-e3fa-4d7f-bcab-d28ec592b51e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to view and modify information about schools and classes in your organization and education-related information about you and other users on your behalf.",
        "userConsentDisplayName": "View and modify your school, class and user information",
        "value": "EduRoster.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read the structure of schools and classes in an organization's roster and education-specific information about users to be read on behalf of the user.",
        "adminConsentDisplayName": "Read users' view of the roster",
        "id": "a4389601-22d9-4096-ac18-36a927199112",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to view information about schools and classes in your organization and education-related information about you and other users on your behalf.",
        "userConsentDisplayName": "View your school, class and user information",
        "value": "EduRoster.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read a limited subset of the properties from the structure of schools and classes in an organization's roster and a limited subset of properties about users to be read on behalf of the user.\u00a0Includes name, status, education role, email address and photo.",
        "adminConsentDisplayName": "Read a limited subset of users' view of the roster",
        "id": "5d186531-d1bf-4f07-8cea-7c42119e1bd9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to view minimal \u00a0information about both schools and classes in your organization and education-related information about you and other users on your behalf.",
        "userConsentDisplayName": "View a limited subset of your school, class and user information",
        "value": "EduRoster.ReadBasic"
    },
    {
        "adminConsentDescription": "Allows the app to report the signed-in user's app activity information to Microsoft Timeline.",
        "adminConsentDisplayName": "Write app activity to users' timeline",
        "id": "367492fc-594d-4972-a9b5-0d58c622c91c",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to report your app activity information to Microsoft Timeline.",
        "userConsentDisplayName": "Write app activity to your timeline",
        "value": "UserTimelineActivity.Write.CreatedByApp"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete user's mailbox settings. Does not include permission to send mail.",
        "adminConsentDisplayName": "Read and write user mailbox settings",
        "id": "818c620a-27a9-40bd-a6a5-d96f7d610b4b",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create, and delete your mailbox settings.",
        "userConsentDisplayName": "Read and write to your mailbox settings",
        "value": "MailboxSettings.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to launch another app or communicate with another app on a user's device on behalf of the signed-in user.",
        "adminConsentDisplayName": "Communicate with user devices",
        "id": "bac3b9c2-b516-4ef4-bd3b-c2ef73d8d804",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to launch another app or communicate with another app on a device that you own.",
        "userConsentDisplayName": "Communicate with your other devices",
        "value": "Device.Command"
    },
    {
        "adminConsentDescription": "Allows the app to read a user's list of devices on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user devices",
        "id": "11d4cd79-5ba5-460f-803f-e22c8ab85ccd",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to see your list of devices.",
        "userConsentDisplayName": "View your list of devices",
        "value": "Device.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read, share, and modify OneNote notebooks that the signed-in user has access to in the organization.",
        "adminConsentDisplayName": "Read and write all OneNote notebooks that user can access",
        "id": "64ac0503-b4fa-45d9-b544-71a463f05da0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, share, and modify all the OneNote notebooks that you have access to.",
        "userConsentDisplayName": "Read and write all OneNote notebooks that you can access",
        "value": "Notes.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read OneNote notebooks that the signed-in user has access to in the organization.",
        "adminConsentDisplayName": "Read all OneNote notebooks that user can access",
        "id": "dfabfca6-ee36-4db2-8208-7a28381419b3",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read all the OneNote notebooks that you have access to.",
        "userConsentDisplayName": "Read all OneNote notebooks that you can access",
        "value": "Notes.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, share, and modify OneNote notebooks on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write user OneNote notebooks",
        "id": "615e26af-c38a-4150-ae3e-c3b0d4cb1d6a",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, share, and modify OneNote notebooks on your behalf.",
        "userConsentDisplayName": "Read and write your OneNote notebooks",
        "value": "Notes.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read OneNote notebooks on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user OneNote notebooks",
        "id": "371361e4-b9e2-4a3f-8315-2a301a3b0a3d",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read OneNote notebooks on your behalf.",
        "userConsentDisplayName": "Read your OneNote notebooks",
        "value": "Notes.Read"
    },
    {
        "adminConsentDescription": "This is deprecated!  Do not use! This permission no longer has any effect. You can safely consent to it. No additional privileges will be granted to the app.",
        "adminConsentDisplayName": "Limited notebook access (deprecated)",
        "id": "ed68249d-017c-4df5-9113-e684c7f8760b",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "This permission no longer has any effect. You can safely consent to it. No additional privileges will be granted to the app.",
        "userConsentDisplayName": "Limited access to your OneNote notebooks for this app (preview)",
        "value": "Notes.ReadWrite.CreatedByApp"
    },
    {
        "adminConsentDescription": "Allows the app to read the titles of OneNote notebooks and sections and to create new pages, notebooks, and sections on behalf of the signed-in user.",
        "adminConsentDisplayName": "Create user OneNote notebooks",
        "id": "9d822255-d64d-4b7a-afdb-833b9a97ed02",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to view the titles of your OneNote notebooks and sections and to create new pages, notebooks, and sections on your behalf.",
        "userConsentDisplayName": "Create your OneNote notebooks",
        "value": "Notes.Create"
    },
    {
        "adminConsentDescription": "Allows the app to invite guest users to the organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Invite guest users to the organization",
        "id": "63dd7cd9-b489-4adf-a28c-ac38b9a0f962",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to invite guest users to the organization, on your behalf.",
        "userConsentDisplayName": "Invite guest users to the organization",
        "value": "User.Invite.All"
    },
    {
        "adminConsentDescription": "Allows the app to the read user's mailbox settings. Does not include permission to send mail.",
        "adminConsentDisplayName": "Read user mailbox settings",
        "id": "87f447af-9fa4-4c32-9dfa-4a57a73d18ce",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your mailbox settings.",
        "userConsentDisplayName": "Read your mailbox settings",
        "value": "MailboxSettings.Read"
    },
    {
        "adminConsentDescription": "(Preview) Allows the app to read files that the user selects. The app has access for several hours after the user selects a file.",
        "adminConsentDisplayName": "Read files that the user selects (preview)",
        "id": "5447fe39-cb82-4c1a-b977-520e67e724eb",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "(Preview) Allows the app to read files that you select. After you select a file, the app has access to the file for several hours.",
        "userConsentDisplayName": "Read selected files",
        "value": "Files.Read.Selected"
    },
    {
        "adminConsentDescription": "(Preview) Allows the app to read and write files that the user selects. The app has access for several hours after the user selects a file.",
        "adminConsentDisplayName": "Read and write files that the user selects (preview)",
        "id": "17dde5bd-8c17-420f-a486-969730c1b827",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "(Preview) Allows the app to read and write files that you select. After you select a file, the app has access to the file for several hours.",
        "userConsentDisplayName": "Read and write selected files",
        "value": "Files.ReadWrite.Selected"
    },
    {
        "adminConsentDescription": "(Preview) Allows the app to read, create, update and delete files in the application's folder.",
        "adminConsentDisplayName": "Have full access to the application's folder (preview)",
        "id": "8019c312-3263-48e6-825e-2b833497195b",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "(Preview) Allows the app to read, create, update and delete files in the application's folder.",
        "userConsentDisplayName": "Have full access to the application's folder",
        "value": "Files.ReadWrite.AppFolder"
    },
    {
        "adminConsentDescription": "Allows an app to read all service usage reports on behalf of the signed-in user.  Services that provide usage reports include Office 365 and Azure Active Directory.",
        "adminConsentDisplayName": "Read all usage reports",
        "id": "02e97553-ed7b-43d0-ab3c-f8bace0d040c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows an app to read all service usage reports on your behalf. Services that provide usage reports include Office 365 and Azure Active Directory.",
        "userConsentDisplayName": "Read all usage reports",
        "value": "Reports.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to edit or delete documents and list items in all site collections on behalf of the signed-in user.",
        "adminConsentDisplayName": "Edit or delete items in all site collections",
        "id": "89fe6a52-be36-487e-b7d8-d061c450a026",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allow the application to edit or delete documents and list items in all site collections on your behalf.",
        "userConsentDisplayName": "Edit or delete items in all site collections",
        "value": "Sites.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete tasks a user has permissions to, including their own and shared tasks.",
        "adminConsentDisplayName": "Read and write user and shared tasks",
        "id": "c5ddf11b-c114-4886-8558-8a4e557cd52b",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create, and delete tasks you have permissions to access, including your own and shared tasks.",
        "userConsentDisplayName": "Read and write to your and shared tasks",
        "value": "Tasks.ReadWrite.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to read tasks a user has permissions to access, including their own and shared tasks.",
        "adminConsentDisplayName": "Read user and shared tasks",
        "id": "88d21fd4-8e5a-4c32-b5e2-4a1c95f34f72",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read tasks you have permissions to access, including your own and shared tasks.",
        "userConsentDisplayName": "Read your and shared tasks",
        "value": "Tasks.Read.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete contacts a user has permissions to, including their own and shared contacts.",
        "adminConsentDisplayName": "Read and write user and shared contacts",
        "id": "afb6c84b-06be-49af-80bb-8f3f77004eab",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create, and delete contacts you have permissions to access, including your own and shared contacts.",
        "userConsentDisplayName": "Read and write to your and shared contacts",
        "value": "Contacts.ReadWrite.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to read contacts a user has permissions to access, including their own and shared contacts.",
        "adminConsentDisplayName": "Read user and shared contacts",
        "id": "242b9d9e-ed24-4d09-9a52-f43769beb9d4",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read contacts you have permissions to access, including your own and shared contacts.",
        "userConsentDisplayName": "Read your and shared contacts",
        "value": "Contacts.Read.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update and delete events in all calendars in the organization user has permissions to access. This includes delegate and shared calendars.",
        "adminConsentDisplayName": "Read and write user and shared calendars",
        "id": "12466101-c9b8-439a-8589-dd09ee67e8e9",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create and delete events in all calendars in your organization you have permissions to access. This includes delegate and shared calendars.",
        "userConsentDisplayName": "Read and write to your and shared calendars",
        "value": "Calendars.ReadWrite.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to read events in all calendars that the user can access, including delegate and shared calendars.",
        "adminConsentDisplayName": "Read user and shared calendars",
        "id": "2b9c4092-424d-4249-948d-b43879977640",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read events in all calendars that you can access, including delegate and shared calendars.\u00a0",
        "userConsentDisplayName": "Read calendars\u00a0you can access",
        "value": "Calendars.Read.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to send mail as the signed-in user, including sending on-behalf of others.",
        "adminConsentDisplayName": "Send mail on behalf of others",
        "id": "a367ab51-6b49-43bf-a716-a1fb06d2a174",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to send mail as you or on-behalf of someone else.",
        "userConsentDisplayName": "Send mail on behalf of others or yourself",
        "value": "Mail.Send.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete mail a user has permission to access, including their own and shared mail. Does not include permission to send mail.",
        "adminConsentDisplayName": "Read and write user and shared mail",
        "id": "5df07973-7d5d-46ed-9847-1271055cbd51",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create, and delete mail you have permission to access, including your own and shared mail. Does not allow the app to send mail on your behalf.",
        "userConsentDisplayName": "Read and write mail\u00a0you can access",
        "value": "Mail.ReadWrite.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to read mail a user can access, including their own and shared mail.",
        "adminConsentDisplayName": "Read user and shared mail",
        "id": "7b9103a5-4610-446b-9670-80643382c1fa",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read mail you can access, including shared mail.",
        "userConsentDisplayName": "Read mail you can access",
        "value": "Mail.Read.Shared"
    },
    {
        "adminConsentDescription": "Allows users to sign-in to the app, and allows the app to read the profile of signed-in users. It also allows the app to read basic company information of signed-in users.",
        "adminConsentDisplayName": "Sign in and read user profile",
        "id": "e1fe6dd8-ba31-4d61-89e7-88639da4683d",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows you to sign in to the app with your organizational account and let the app read your profile. It also allows the app to read basic company information.",
        "userConsentDisplayName": "Sign you in and read your profile",
        "value": "User.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read your profile. It also allows the app to update your profile information on your behalf.",
        "adminConsentDisplayName": "Read and write access to user profile",
        "id": "b4e74841-8e56-480b-be8b-910348b18b4c",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your profile, and discover your group membership, reports and manager. It also allows the app to update your profile information on your behalf.",
        "userConsentDisplayName": "Read and update your profile",
        "value": "User.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read a basic set of profile properties of other users in your organization on behalf of the signed-in user. This includes display name, first and last name, email address and photo.",
        "adminConsentDisplayName": "Read all users' basic profiles",
        "id": "b340eb25-3456-403f-be2f-af7a0d370277",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read a basic set of profile properties of other users in your organization on your behalf. Includes display name, first and last name, email address and photo.",
        "userConsentDisplayName": "Read all users' basic profiles",
        "value": "User.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the full set of profile properties, reports, and managers of other users in your organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all users' full profiles",
        "id": "a154be20-db9c-4678-8ab7-66f6cc099a59",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the full set of profile properties, reports, and managers of other users in your organization, on your behalf.",
        "userConsentDisplayName": "Read all users' full profiles",
        "value": "User.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the full set of profile properties, reports, and managers of other users in your organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all users' full profiles",
        "id": "204e0828-b5ca-4ad8-b9f3-f32a958e7cc4",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the full set of profile properties, reports, and managers of other users in your organization, on your behalf.",
        "userConsentDisplayName": "Read and write all users' full profiles",
        "value": "User.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to list groups, and to read their properties and all group memberships on behalf of the signed-in user.  Also allows the app to read calendar, conversations, files, and other group content for all groups the signed-in user can access. ",
        "adminConsentDisplayName": "Read all groups",
        "id": "5f8c59db-677d-491f-a6b8-5f174b11ec1d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to list groups, and to read their properties and all group memberships on your behalf.  Also allows the app to read calendar, conversations, files, and other group content for all groups you can access.  ",
        "userConsentDisplayName": "Read all groups",
        "value": "Group.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to create groups and read all group properties and memberships on behalf of the signed-in user.  Additionally allows group owners to manage their groups and allows group members to update group content.",
        "adminConsentDisplayName": "Read and write all groups",
        "id": "4e46008b-f24c-477d-8fff-7bb4ec7aafe0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to create groups and read all group properties and memberships on your behalf.  Additionally allows the app to manage your groups and to update group content for groups you are a member of.",
        "userConsentDisplayName": "Read and write all groups",
        "value": "Group.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read data in your organization's directory, such as users, groups and apps.",
        "adminConsentDisplayName": "Read directory data",
        "id": "06da0dbc-49e2-44d2-8312-53f166ab848a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read data in your organization's directory.",
        "userConsentDisplayName": "Read directory data",
        "value": "Directory.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write data in your organization's directory, such as users, and groups.  It does not allow the app to delete users or groups, or reset user passwords.",
        "adminConsentDisplayName": "Read and write directory data",
        "id": "c5366453-9fb0-48a5-a156-24f0c49a4b84",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write data in your organization's directory, such as other users, groups.  It does not allow the app to delete users or groups, or reset user passwords.",
        "userConsentDisplayName": "Read and write directory data",
        "value": "Directory.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to have the same access to information in the directory as the signed-in user.",
        "adminConsentDisplayName": "Access directory as the signed in user",
        "id": "0e263e50-5827-48a4-b97c-d940288653c7",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to have the same access to information in your work or school directory as you do.",
        "userConsentDisplayName": "Access the directory as you",
        "value": "Directory.AccessAsUser.All"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete email in user mailboxes. Does not include permission to send mail. ",
        "adminConsentDisplayName": "Read and write access to user mail ",
        "id": "024d486e-b451-40bb-833d-3e66d98c5c73",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create and delete email in your mailbox. Does not include permission to send mail. ",
        "userConsentDisplayName": "Read and write access to your mail ",
        "value": "Mail.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to send mail as users in the organization. ",
        "adminConsentDisplayName": "Send mail as a user ",
        "id": "e383f46e-2787-4529-855e-0e479a3ffac0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to send mail as you. ",
        "userConsentDisplayName": "Send mail as you ",
        "value": "Mail.Send"
    },
    {
        "adminConsentDescription": "Allows the app to read events in user calendars . ",
        "adminConsentDisplayName": "Read user calendars ",
        "id": "465a38f9-76ea-45b9-9f34-9e8b0d4b0b42",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read events in your calendars. ",
        "userConsentDisplayName": "Read your calendars ",
        "value": "Calendars.Read"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete events in user calendars. ",
        "adminConsentDisplayName": "Have full access to user calendars ",
        "id": "1ec239c2-d7c9-4623-a91a-a9775856bb36",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create and delete events in your calendars. ",
        "userConsentDisplayName": "Have full access to your calendars  ",
        "value": "Calendars.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read user contacts.  ",
        "adminConsentDisplayName": "Read user contacts ",
        "id": "ff74d97f-43af-4b68-9f2a-b77ee6968c5d",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read contacts in your contact folders. ",
        "userConsentDisplayName": "Read your contacts ",
        "value": "Contacts.Read"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete user contacts. ",
        "adminConsentDisplayName": "Have full access to user contacts ",
        "id": "d56682ec-c09e-4743-aaf4-1a3aac4caa21",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create and delete contacts in your contact folders. ",
        "userConsentDisplayName": "Have full access of your contacts ",
        "value": "Contacts.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read the signed-in user's files.",
        "adminConsentDisplayName": "Read user files",
        "id": "10465720-29dd-4523-a11a-6a75c743c9d9",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your files.",
        "userConsentDisplayName": "Read your files",
        "value": "Files.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read, create, update and delete the signed-in user's files.",
        "adminConsentDisplayName": "Have full access to user files",
        "id": "5c28f0bf-8a70-41f1-8ab2-9032436ddb65",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, create, update, and delete your files.",
        "userConsentDisplayName": "Have full access to your files",
        "value": "Files.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read all files the signed-in user can access.",
        "adminConsentDisplayName": "Read all files that user can access",
        "id": "df85f4d6-205c-4ac5-a5ea-6bf408dba283",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read all files you can access.",
        "userConsentDisplayName": "Read all files that you have access to",
        "value": "Files.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, create, update and delete all files the signed-in user can access.",
        "adminConsentDisplayName": "Have full access to all files user can access",
        "id": "863451e7-0667-486c-a5d6-d135439485f0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, create, update and delete all files that you can access.",
        "userConsentDisplayName": "Have full access to all files you have access to",
        "value": "Files.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to read documents and list  items in all site collections on behalf of the signed-in user",
        "adminConsentDisplayName": "Read items in all site collections",
        "id": "205e70e5-aba6-4c52-a976-6d2d46c48043",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allow the application to read documents and list items in all site collections on your behalf",
        "userConsentDisplayName": "Read items in all site collections",
        "value": "Sites.Read.All"
    },
    {
        "adminConsentDescription": "Allows users to sign in to the app with their work or school accounts and allows the app to see basic user profile information.",
        "adminConsentDisplayName": "Sign users in",
        "id": "37f7f235-527c-4136-accd-4a02d197296e",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows you to sign in to the app with your work or school account and allows the app to read your basic profile information.",
        "userConsentDisplayName": "Sign in as you",
        "value": "openid"
    },
    {
        "adminConsentDescription": "Allows the app to read your users' primary email address",
        "adminConsentDisplayName": "View users' email address",
        "id": "64a6cdd6-aab1-4aaf-94b8-3cc8405e90d0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your primary email address",
        "userConsentDisplayName": "View your email address",
        "value": "email"
    },
    {
        "adminConsentDescription": "Allows the app to read identity risk event information for all users in your organization on behalf of the signed-in user. ",
        "adminConsentDisplayName": "Read identity risk event information",
        "id": "8f6a01e7-0391-4ee5-aa22-a3af122cef27",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read identity risk event information for all users in your organization on behalf of the signed-in user. ",
        "userConsentDisplayName": "Read identity risk event information",
        "value": "IdentityRiskEvent.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the memberships of hidden groups and administrative units on behalf of the signed-in user, for those hidden groups and administrative units that the signed-in user has access to.",
        "adminConsentDisplayName": "Read hidden memberships",
        "id": "f6a3db3e-f7e8-4ed2-a414-557c8c9830be",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the memberships of hidden groups or administrative units on your behalf, for those hidden groups or adminstrative units that you have access to.",
        "userConsentDisplayName": "Read your hidden memberships",
        "value": "Member.Read.Hidden"
    },
    {
        "adminConsentDescription": "Allows the app to read a ranked list of relevant people of the signed-in user. The list includes local contacts, contacts from social networking, your organization's directory, and people from recent communications (such as email and Skype).",
        "adminConsentDisplayName": "Read users' relevant people lists",
        "id": "ba47897c-39ec-4d83-8086-ee8256fa737d",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read a list of people in the order that's most relevant to you. This includes your local contacts, your contacts from social networking, people listed in your organization's directory, and people from recent communications.",
        "userConsentDisplayName": "Read your relevant people list",
        "value": "People.Read"
    },
    {
        "adminConsentDescription": "Allows the application to create or delete document libraries and lists in all site collections on behalf of the signed-in user.",
        "adminConsentDisplayName": "Create, edit, and delete items and lists in all site collections",
        "id": "65e50fdc-43b7-4915-933e-e8138f11f40a",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allow the application to create or delete document libraries and lists in all site collections on your behalf.",
        "userConsentDisplayName": "Create, edit, and delete items and lists in all your site collections",
        "value": "Sites.Manage.All"
    },
    {
        "adminConsentDescription": "Allows the application to have full control of all site collections on behalf of the signed-in user.",
        "adminConsentDisplayName": "Have full control of all site collections",
        "id": "5a54b8b3-347c-476d-8f8e-42d5c7424d29",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allow the application to have full control of all site collections on your behalf.",
        "userConsentDisplayName": "Have full control of all your site collections",
        "value": "Sites.FullControl.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization\u2019s identity (authentication) providers\u2019 properties on behalf of the user.",
        "adminConsentDisplayName": "Read and write identity providers",
        "id": "f13ce604-1677-429f-90bd-8a10b9f01325",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization\u2019s identity (authentication) providers\u2019 properties on your behalf.",
        "userConsentDisplayName": "Read and write identity providers",
        "value": "IdentityProvider.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization\u2019s identity (authentication) providers\u2019 properties on behalf of the user.",
        "adminConsentDisplayName": "Read identity providers",
        "id": "43781733-b5a7-4d1b-98f4-e8edff23e1a9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization\u2019s identity (authentication) providers\u2019 properties on your behalf.",
        "userConsentDisplayName": "Read identity providers",
        "value": "IdentityProvider.Read.All"
    },
    {
        "adminConsentDescription": "Allows an app to read bookings appointments, businesses, customers, services, and staff on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read bookings information",
        "id": "33b1df99-4b29-4548-9339-7a7b83eaeebc",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read bookings appointments, businesses, customers, services, and staff on your behalf.",
        "userConsentDisplayName": "Read bookings information",
        "value": "Bookings.Read.All"
    },
    {
        "adminConsentDescription": "Allows an app to read and write bookings appointments and customers, and additionally allows read businesses information, services, and staff on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write booking appointments",
        "id": "02a5a114-36a6-46ff-a102-954d89d9ab02",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read and write bookings appointments and customers, and additionally allows read businesses information, services, and staff on your behalf.",
        "userConsentDisplayName": "Read and write booking appointments",
        "value": "BookingsAppointment.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows an app to read and write bookings appointments, businesses, customers, services, and staff on behalf of the signed-in user. Does not allow create, delete and publish of booking businesses.",
        "adminConsentDisplayName": "Read and write bookings information",
        "id": "948eb538-f19d-4ec5-9ccc-f059e1ea4c72",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read and write Bookings appointments, businesses, customers, services, and staff on your behalf. Does not allow create, delete and publish of booking businesses.",
        "userConsentDisplayName": "Read and write bookings information",
        "value": "Bookings.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows an app to read, write and manage bookings appointments, businesses, customers, services, and staff on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage bookings information",
        "id": "7f36b48e-542f-4d3b-9bcb-8406f0ab9fdb",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read, write and manage bookings appointments, businesses, customers, services, and staff on your behalf.",
        "userConsentDisplayName": "Manage bookings information",
        "value": "Bookings.Manage.All"
    },
    {
        "adminConsentDescription": "Allows the app to have the same access to mailboxes as the signed-in user via Exchange ActiveSync.",
        "adminConsentDisplayName": "Access mailboxes via Exchange ActiveSync",
        "id": "ff91d191-45a0-43fd-b837-bd682c4a0b0f",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app full access to your mailboxes on your behalf.",
        "userConsentDisplayName": "Access your mailboxes",
        "value": "EAS.AccessAsUser.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write financials data on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write financials data",
        "id": "f534bf13-55d4-45a9-8f3c-c92fe64d6131",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read and write financials data on your behalf.",
        "userConsentDisplayName": "Read and write financials data",
        "value": "Financials.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's user flows, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all identity user flows",
        "id": "2903d63d-4611-4d43-99ce-a33f3f52e343",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization's user flows, on your behalf.",
        "userConsentDisplayName": "Read all identity user flows",
        "value": "IdentityUserFlow.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read or write your organization's user flows, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all identity user flows",
        "id": "281892cc-4dbf-4e3a-b6cc-b21029bb4e82",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read or write your organization's user flows, on your behalf.",
        "userConsentDisplayName": "Read and write all identity user flows",
        "value": "IdentityUserFlow.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all organizational contacts on behalf of the signed-in user. \u00a0These contacts are managed by the organization and are different from a user's personal contacts.",
        "adminConsentDisplayName": "Read organizational contacts",
        "id": "08432d1b-5911-483c-86df-7980af5cdee0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all organizational contacts on your behalf.\u00a0 These contacts are managed by the organization and are different from your personal contacts.",
        "userConsentDisplayName": "Read organizational contacts",
        "value": "OrgContact.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to manage permission grants for application permissions to any API (including Microsoft Graph) and application assignments for any app, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage app permission grants and app role assignments",
        "id": "84bccea3-f856-4a8a-967b-dbe0a3d53a64",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage permission grants for application permissions to any API (including Microsoft Graph) and application assignments for any app, on your behalf.",
        "userConsentDisplayName": "Manage app permission grants and app role assignments",
        "value": "AppRoleAssignment.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to manage permission grants for delegated permissions exposed by any API (including Microsoft Graph), on behalf of the signed in user.",
        "adminConsentDisplayName": "Manage all delegated permission grants",
        "id": "41ce6ca6-6826-4807-84f1-1c82854f7ee5",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage permission grants for delegated permissions exposed by any API (including Microsoft Graph), on your behalf. ",
        "userConsentDisplayName": "Manage all delegated permission grants",
        "value": "DelegatedPermissionGrant.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read online meeting details on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user's online meetings",
        "id": "9be106e1-f4e3-4df5-bdff-e4bc531cbe43",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read online meeting details on your behalf.",
        "userConsentDisplayName": "Read your online meetings",
        "value": "OnlineMeetings.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read and create online meetings on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and create user's online meetings",
        "id": "a65f2972-a4f8-4f5e-afd7-69ccb046d5dc",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read and create online meetings on your behalf.",
        "userConsentDisplayName": "Read and create your online meetings",
        "value": "OnlineMeetings.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read the signed-in user's teamwork activity feed.",
        "adminConsentDisplayName": "Read user's teamwork activity feed",
        "id": "0e755559-83fb-4b44-91d0-4cc721b9323e",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your teamwork activity feed.",
        "userConsentDisplayName": "Read your teamwork activity feed",
        "value": "TeamsActivity.Read"
    },
    {
        "adminConsentDescription": "Allows the app to request and manage time-based assignment and just-in-time elevation of user privileges to manage Azure resources (like subscriptions, resource groups, storage, compute) on behalf of the signed-in users.",
        "adminConsentDisplayName": "Read and write privileged access to Azure resources",
        "id": "a84a9652-ffd3-496e-a991-22ba5529156a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to request and manage time-based assignment and just-in-time elevation of user privileges to manage \u00a0your Azure resources (like your subscriptions, resource groups, storage, compute) on your behalf.",
        "userConsentDisplayName": "Read and write privileged access to Azure resources",
        "value": "PrivilegedAccess.ReadWrite.AzureResources"
    },
    {
        "adminConsentDescription": "Allows the app to read time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD built-in and custom administrative roles, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read privileged access to Azure AD",
        "id": "b3a539c9-59cb-4ad5-825a-041ddbdc2bdb",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD built-in and custom administrative roles, on your behalf.",
        "userConsentDisplayName": "Read privileged access to Azure AD",
        "value": "PrivilegedAccess.Read.AzureAD"
    },
    {
        "adminConsentDescription": "Allows the app to read time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD groups, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read privileged access to Azure AD groups",
        "id": "d329c81c-20ad-4772-abf9-3f6fdb7e5988",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD groups, on your behalf.",
        "userConsentDisplayName": "Read privileged access to Azure AD groups",
        "value": "PrivilegedAccess.Read.AzureADGroup"
    },
    {
        "adminConsentDescription": "Allows the app to read time-based assignment and just-in-time elevation of Azure resources (like your subscriptions, resource groups, storage, compute) on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read privileged access to Azure resources",
        "id": "1d89d70c-dcac-4248-b214-903c457af83a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read time-based assignment and just-in-time elevation of Azure resources (like your subscriptions, resource groups, storage, compute) on your behalf.",
        "userConsentDisplayName": "Read privileged access to your Azure resources",
        "value": "PrivilegedAccess.Read.AzureResources"
    },
    {
        "adminConsentDescription": "Allows the app to request and manage time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD groups, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write privileged access to Azure AD groups",
        "id": "32531c59-1f32-461f-b8df-6f8a3b89f73b",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to request and manage time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD groups, on your behalf.",
        "userConsentDisplayName": "Read and write privileged access to Azure AD groups",
        "value": "PrivilegedAccess.ReadWrite.AzureADGroup"
    },
    {
        "adminConsentDescription": "Allows the app to read all the indicators for your organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all threat indicators",
        "id": "9cc427b4-2004-41c5-aa22-757b755e9796",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all the indicators for your organization, on your behalf.",
        "userConsentDisplayName": "Read all threat indicators",
        "value": "ThreatIndicators.Read.All"
    },
    {
        "adminConsentDescription": "Allow the app to read external datasets and content, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read items in external datasets",
        "id": "922f9392-b1b7-483c-a4be-0089be7704fb",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read external datasets and content that you have access to.",
        "userConsentDisplayName": "Read items in external datasets",
        "value": "ExternalItem.Read.All"
    },
    {
        "adminConsentDescription": "Allows an app to edit channel messages in Microsoft Teams, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Edit user's channel messages",
        "id": "2b61aa8a-6d36-4b2f-ac7b-f29867937c53",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to edit channel messages in Microsoft Teams, on your behalf.",
        "userConsentDisplayName": "Edit your channel messages",
        "value": "ChannelMessage.Edit"
    },
    {
        "adminConsentDescription": "Allows an app to send channel messages in Microsoft Teams, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Send channel messages",
        "id": "ebf0f66e-9fb1-49e4-a278-222f76911cf4",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to send channel messages in Microsoft Teams, on your behalf.",
        "userConsentDisplayName": "Send channel messages",
        "value": "ChannelMessage.Send"
    },
    {
        "adminConsentDescription": "Allows the app to manage organization places (conference rooms and room lists) for calendar events and other applications, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write organization places",
        "id": "4c06a06a-098a-4063-868e-5dfee3827264",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage organization places (conference rooms and room lists) for calendar events and other applications, on your behalf.",
        "userConsentDisplayName": "Read and write organization places",
        "value": "Place.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to request access to and management of access packages and related entitlement management resources on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write entitlement management resources",
        "id": "ae7a573d-81d7-432b-ad44-4ed5c9d89038",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to request access to and management of access packages and related entitlement management resources that you have access to.",
        "userConsentDisplayName": "Read and write entitlement management resources",
        "value": "EntitlementManagement.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to send, read, update and delete user\u2019s notifications.",
        "adminConsentDisplayName": "Deliver and manage user's notifications",
        "id": "26e2f3e8-b2a1-47fc-9620-89bb5b042024",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to send, read, update and delete your app-specific notifications.",
        "userConsentDisplayName": "Deliver and manage your notifications",
        "value": "UserNotification.ReadWrite.CreatedByApp"
    },
    {
        "adminConsentDescription": "Allows the app to read applications and service principals on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read applications",
        "id": "c79f8feb-a9db-4090-85f9-90d820caa0eb",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read applications and service principals on your behalf.",
        "userConsentDisplayName": "Read applications",
        "value": "Application.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update and delete applications and service principals on behalf of the signed-in user. Does not allow management of consent grants.",
        "adminConsentDisplayName": "Read and write all applications",
        "id": "bdfbf15f-ee85-4955-8675-146e8e5296b5",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to create, read, update and delete applications and service principals on your behalf. Does not allow management of consent grants.",
        "userConsentDisplayName": "Read and write applications",
        "value": "Application.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read BitLocker keys on behalf of the signed-in user, for their owned devices. Allows read of the recovery key.",
        "adminConsentDisplayName": "Read BitLocker keys",
        "id": "b27a61ec-b99c-4d6a-b126-c4375d08ae30",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read BitLocker keys for your owned devices. Allows read of the recovery key.",
        "userConsentDisplayName": "Read your BitLocker keys",
        "value": "BitlockerKey.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read basic BitLocker key properties on behalf of the signed-in user, for their owned devices. Does not allow read of the recovery key itself.",
        "adminConsentDisplayName": "Read BitLocker keys basic information",
        "id": "5a107bfc-4f00-4e1a-b67e-66451267bc68",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read basic BitLocker key properties for your owned devices. Does not allow read of the recovery key itself.",
        "userConsentDisplayName": "Read your BitLocker keys basic information",
        "value": "BitlockerKey.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Allows the app to list groups, read basic group properties and read membership of all groups the signed-in user has access to.",
        "adminConsentDisplayName": "Read group memberships",
        "id": "bc024368-1153-4739-b217-4326f2e966d0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to list groups, read basic group properties and read membership of all your groups.",
        "userConsentDisplayName": "Read group memberships",
        "value": "GroupMember.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to list groups, read basic properties, read and update the membership of the groups the signed-in user has access to. Group properties and owners cannot be updated and groups cannot be deleted.",
        "adminConsentDisplayName": "Read and write group memberships",
        "id": "f81125ac-d3b7-4573-a3b2-7099cc39df9e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to list groups, read basic properties, read and update the membership of your groups. Group properties and owners cannot be updated and groups cannot be deleted.",
        "userConsentDisplayName": "Read and write group memberships",
        "value": "GroupMember.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows an app to read your organization's threat assessment requests on behalf of the signed-in user. Also allows the app to create new requests to assess threats received by your organization on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write threat assessment requests",
        "id": "cac97e40-6730-457d-ad8d-4852fddab7ad",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows an app to read your organization's threat assessment requests on your behalf. Also allows the app to create new requests to assess threats received by your organization on your behalf.",
        "userConsentDisplayName": "Read and write threat assessment requests",
        "value": "ThreatAssessment.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read schedule, schedule groups, shifts and associated entities in the Teams or Shifts application on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user schedule items",
        "id": "fccf6dd8-5706-49fa-811f-69e2e1b585d0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read schedule, schedule groups, shifts and associated entities in the Teams or Shifts application on your behalf.",
        "userConsentDisplayName": "Read your schedule items",
        "value": "Schedule.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to manage schedule, schedule groups, shifts and associated entities in the Teams or Shifts application on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write user schedule items",
        "id": "63f27281-c9d9-4f29-94dd-6942f7f1feb0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage schedule, schedule groups, shifts and associated entities in the Teams or Shifts application on your behalf.",
        "userConsentDisplayName": "Read and write your schedule items",
        "value": "Schedule.ReadWrite.All"
    },
    {
        "adminConsentDescription": " Allows the app to read and write authentication methods of all users in your organization that the signed-in user has access to.                       Authentication methods include things like a user\u2019s phone numbers and Authenticator app settings. This                      does not allow the app to see secret information like passwords, or to sign-in or otherwise use the authentication methods.",
        "adminConsentDisplayName": "Read and write all users' authentication methods.",
        "id": "b7887744-6746-4312-813d-72daeaee7e2d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write authentication methods of all users you have access to in your organization.                       Authentication methods include things like a user\u2019s phone numbers and Authenticator app settings. This does not allow                      the app to see secret information like passwords, or to sign-in or otherwise use the authentication methods.",
        "userConsentDisplayName": "Read and write all users' authentication methods",
        "value": "UserAuthenticationMethod.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the signed-in user's authentication methods, including phone numbers and Authenticator app settings.                       This does not allow the app to see secret information like the signed-in user's passwords, or                      to sign-in or otherwise use the signed-in user's authentication methods.  ",
        "adminConsentDisplayName": "Read and write user authentication methods",
        "id": "48971fc1-70d7-4245-af77-0beb29b53ee2",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your authentication methods, including phone numbers and Authenticator app settings.This does not allow the app to see secret information like your passwords, or to sign-in or otherwise use your authentication methods.",
        "userConsentDisplayName": "Read and write your authentication methods",
        "value": "UserAuthenticationMethod.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read authentication methods of all users in your organization that the signed-in user has access to. Authentication methods include things like a user\u2019s phone numbers and Authenticator app settings. This does not allow the app to see secret information like passwords, or to sign-in or otherwise use the authentication methods.",
        "adminConsentDisplayName": "Read all users' authentication methods",
        "id": "aec28ec7-4d02-4e8c-b864-50163aea77eb",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read authentication methods of all users you have access to in your organization. Authentication methods include things like a user\u2019s phone numbers and Authenticator app settings. This does not allow the app to see secret information like passwords, or to sign-in or otherwise use the authentication methods.",
        "userConsentDisplayName": "Read all users' authentication methods",
        "value": "UserAuthenticationMethod.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the signed-in user's authentication methods, including phone numbers and Authenticator app settings. This does not allow the app to see secret information like the signed-in user's passwords, or to sign-in  or otherwise use the signed-in user's authentication methods.",
        "adminConsentDisplayName": "Read user authentication methods.",
        "id": "1f6b61c5-2f65-4135-9c9f-31c0f8d32b52",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your authentication methods, including phone numbers and Authenticator app settings. This does not allow the app to see secret information like your passwords, or to sign-in or otherwise use your authentication methods.",
        "userConsentDisplayName": "Read your authentication methods.",
        "value": "UserAuthenticationMethod.Read"
    },
    {
        "adminConsentDescription": "Allows the app to create tabs in any team in Microsoft Teams, on behalf of the signed-in user. This does not grant the ability to read, modify or delete tabs after they are created, or give access to the content inside the tabs.",
        "adminConsentDisplayName": "Create tabs in Microsoft Teams.",
        "id": "a9ff19c2-f369-4a95-9a25-ba9d460efc8e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to create tabs in any team in Microsoft Teams, on your behalf. This does not grant the ability to read, modify or delete tabs after they are created, or give access to the content inside the tabs.",
        "userConsentDisplayName": "Create tabs in Microsoft Teams.",
        "value": "TeamsTab.Create"
    },
    {
        "adminConsentDescription": "Read the names and settings of tabs inside any team in Microsoft Teams, on behalf of the signed-in user. This does not give access to the content inside the tabs.",
        "adminConsentDisplayName": "Read tabs in Microsoft Teams.",
        "id": "59dacb05-e88d-4c13-a684-59f1afc8cc98",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read the names and settings of tabs inside any team in Microsoft Teams, on your behalf. This does not give access to the content inside the tabs.",
        "userConsentDisplayName": "Read tabs in Microsoft Teams.",
        "value": "TeamsTab.Read.All"
    },
    {
        "adminConsentDescription": "Read and write tabs in any team in Microsoft Teams, on behalf of the signed-in user. This does not give access to the content inside the tabs.",
        "adminConsentDisplayName": "Read and write tabs in Microsoft Teams.",
        "id": "b98bfd41-87c6-45cc-b104-e2de4f0dafb9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read and write tabs in any team in Microsoft Teams, on your behalf. This does not give access to the content inside the tabs.",
        "userConsentDisplayName": "Read and write tabs in Microsoft Teams.",
        "value": "TeamsTab.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to have the same access to mailboxes as the signed-in user via IMAP protocol.",
        "adminConsentDisplayName": "Read and write access to mailboxes via IMAP.",
        "id": "652390e4-393a-48de-9484-05f9b1212954",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create and delete email in your mailbox. Does not include permission to send mail.",
        "userConsentDisplayName": "Read and write access to your mail.",
        "value": "IMAP.AccessAsUser.All"
    },
    {
        "adminConsentDescription": "Allows the app to have the same access to mailboxes as the signed-in user via POP protocol.",
        "adminConsentDisplayName": "Read and write access to mailboxes via POP.",
        "id": "d7b7f2d9-0f45-4ea1-9d42-e50810c06991",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, update, create and delete email in your mailbox. Does not include permission to send mail.",
        "userConsentDisplayName": "Read and write access to your mail.",
        "value": "POP.AccessAsUser.All"
    },
    {
        "adminConsentDescription": "Allows the app to be able to send emails from the user\u2019s mailbox using the SMTP AUTH client submission protocol.",
        "adminConsentDisplayName": "Send emails from mailboxes using SMTP AUTH.",
        "id": "258f6531-6087-4cc4-bb90-092c5fb3ed3f",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to send emails on your behalf from your mailbox.",
        "userConsentDisplayName": "Access to sending emails from your mailbox.",
        "value": "SMTP.Send"
    },
    {
        "adminConsentDescription": "Allows the app to read all domain properties on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read domains.",
        "id": "2f9ee017-59c1-4f1d-9472-bd5529a7b311",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all domain properties on your behalf.",
        "userConsentDisplayName": "Read domains.",
        "value": "Domain.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write all domain properties on behalf of the signed-in user. Also allows the app to add, verify and remove domains.",
        "adminConsentDisplayName": "Read and write domains",
        "id": "0b5d694c-a244-4bde-86e6-eb5cd07730fe",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write all domain properties on your behalf. Also allows the app to add, verify and remove domains.",
        "userConsentDisplayName": "Read and write domains",
        "value": "Domain.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's application configuration policies on behalf of the signed-in user.  This includes policies such as activityBasedTimeoutPolicy, claimsMappingPolicy, homeRealmDiscoveryPolicy,  tokenIssuancePolicy and tokenLifetimePolicy.",
        "adminConsentDisplayName": "Read and write your organization's application configuration policies",
        "id": "b27add92-efb2-4f16-84f5-8108ba77985c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's application configuration policies on your behalf.  This includes policies such as activityBasedTimeoutPolicy, claimsMappingPolicy, homeRealmDiscoveryPolicy, tokenIssuancePolicy  and tokenLifetimePolicy.",
        "userConsentDisplayName": "Read and write your organization's application configuration policies",
        "value": "Policy.ReadWrite.ApplicationConfiguration"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's devices' configuration information on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all devices",
        "id": "951183d1-1a61-466f-a6d1-1fde911bfd95",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read devices' configuration information on your behalf.",
        "userConsentDisplayName": "Read all devices",
        "value": "Device.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, update and delete identities that are associated with a user's account that the signed-in user has access to. This controls the identities users can sign-in with.",
        "adminConsentDisplayName": "Manage  user identities",
        "id": "637d7bec-b31e-4deb-acc9-24275642a2c9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, update and delete identities that are associated with a user's account that you have access to. This controls the identities users can sign-in with.",
        "userConsentDisplayName": "Manage  user identities",
        "value": "User.ManageIdentities.All"
    },
    {
        "adminConsentDescription": "Allows the app to read access packages and related entitlement management resources on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all entitlement management resources",
        "id": "5449aa12-1393-4ea2-a7c7-d0e06c1a56b2",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read access packages and related entitlement management resources that you have access to.",
        "userConsentDisplayName": "Read all entitlement management resources",
        "value": "EntitlementManagement.Read.All"
    },
    {
        "adminConsentDescription": "Create channels in any team, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Create channels",
        "id": "101147cf-4178-4455-9d58-02b5c164e759",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Create channels in any team, on your behalf.",
        "userConsentDisplayName": "Create channels",
        "value": "Channel.Create"
    },
    {
        "adminConsentDescription": "Delete channels in any team, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Delete channels",
        "id": "cc83893a-e232-4723-b5af-bd0b01bcfe65",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Delete channels in any team, on your behalf.",
        "userConsentDisplayName": "Delete channels",
        "value": "Channel.Delete.All"
    },
    {
        "adminConsentDescription": "Read all channel names, channel descriptions, and channel settings, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read the names, descriptions, and settings of channels",
        "id": "233e0cf1-dd62-48bc-b65b-b38fe87fcf8e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read all channel names, channel descriptions, and channel settings, on your behalf.",
        "userConsentDisplayName": "Read the names, descriptions, and settings of channels",
        "value": "ChannelSettings.Read.All"
    },
    {
        "adminConsentDescription": "Read and write the names, descriptions, and settings of all channels, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write the names, descriptions, and settings of channels",
        "id": "d649fb7c-72b4-4eec-b2b4-b15acf79e378",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read and write the names, descriptions, and settings of all channels, on your behalf.",
        "userConsentDisplayName": "Read and write the names, descriptions, and settings of channels",
        "value": "ChannelSettings.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all webhook subscriptions on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all webhook subscriptions ",
        "id": "5f88184c-80bb-4d52-9ff2-757288b2e9b7",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all webhook subscriptions on your behalf.",
        "userConsentDisplayName": "Read all webhook subscriptions ",
        "value": "Subscription.Read.All"
    },
    {
        "adminConsentDescription": "Read the names and  descriptions of teams, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read the names and descriptions of teams",
        "id": "485be79e-c497-4b35-9400-0e3fa7f2a5d4",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Read the names and  descriptions of teams, on your behalf.",
        "userConsentDisplayName": "Read the names and descriptions of teams",
        "value": "Team.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Read channel names and channel descriptions, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read the names and descriptions of channels",
        "id": "9d8982ae-4365-4f57-95e9-d6032a4c0b87",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Read channel names and channel descriptions, on your behalf.",
        "userConsentDisplayName": "Read the names and descriptions of channels",
        "value": "Channel.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Read all teams' settings, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read teams' settings",
        "id": "48638b3c-ad68-4383-8ac4-e6880ee6ca57",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read all teams' settings, on your behalf.",
        "userConsentDisplayName": "Read teams' settings",
        "value": "TeamSettings.Read.All"
    },
    {
        "adminConsentDescription": "Read and change all teams' settings, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and change teams' settings",
        "id": "39d65650-9d3e-4223-80db-a335590d027e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read and change all teams' settings, on your behalf.",
        "userConsentDisplayName": "Read and change teams' settings",
        "value": "TeamSettings.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Read the members of teams, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read the members of teams",
        "id": "2497278c-d82d-46a2-b1ce-39d4cdde5570",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read the members of teams, on your behalf.",
        "userConsentDisplayName": "Read the members of teams",
        "value": "TeamMember.Read.All"
    },
    {
        "adminConsentDescription": "Add and remove members from teams, on behalf of the signed-in user. Also allows changing a member's role, for example from owner to non-owner.",
        "adminConsentDisplayName": "Add and remove members from teams",
        "id": "4a06efd2-f825-4e34-813e-82a57b03d1ee",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Add and remove members from teams, on your behalf. Also allows changing a member's role, for example from owner to non-owner.",
        "userConsentDisplayName": "Add and remove members from teams and channels",
        "value": "TeamMember.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read consent requests and approvals on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read consent requests",
        "id": "f3bfad56-966e-4590-a536-82ecf548ac1e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read consent requests and approvals, on your behalf.",
        "userConsentDisplayName": "Read consent requests",
        "value": "ConsentRequest.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read app consent requests and approvals, and deny or approve those requests on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write consent requests",
        "id": "497d9dfa-3bd1-481a-baab-90895e54568c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read app consent requests for your approval, and deny or approve those request on your behalf.",
        "userConsentDisplayName": "Read and write consent requests",
        "value": "ConsentRequest.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's consent requests policy on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write consent request policy",
        "id": "4d135e65-66b8-41a8-9f8b-081452c91774",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's consent request policy on your behalf.",
        "userConsentDisplayName": "Read and write consent request policy",
        "value": "Policy.ReadWrite.ConsentRequest"
    },
    {
        "adminConsentDescription": "Allows the app to read presence information on behalf of the signed-in user. Presence information includes activity, availability, status note, calendar out-of-office message, timezone and location.",
        "adminConsentDisplayName": "Read user's presence information",
        "id": "76bc735e-aecd-4a1d-8b4c-2b915deabb79",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your presence information on your behalf. Presence information includes activity, availability, status note, calendar out-of-office message, timezone and location.",
        "userConsentDisplayName": "Read your presence information",
        "value": "Presence.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read presence information of all users in the directory on behalf of the signed-in user. Presence information includes activity, availability, status note, calendar out-of-office message, timezone and location.",
        "adminConsentDisplayName": "Read presence information of all users in your organization",
        "id": "9c7a330d-35b3-4aa1-963d-cb2b9f927841",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read presence information of all users in the directory on your behalf. Presence information includes activity, availability, status note, calendar out-of-office message, timezone and location.",
        "userConsentDisplayName": "Read presence information of all users in your organization",
        "value": "Presence.Read.All"
    },
    {
        "adminConsentDescription": "Read the members of channels, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read the members of channels",
        "id": "2eadaff8-0bce-4198-a6b9-2cfc35a30075",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read the members of channels, on your behalf.",
        "userConsentDisplayName": "Read the members of teams and channels",
        "value": "ChannelMember.Read.All"
    },
    {
        "adminConsentDescription": "Add and remove members from channels, on behalf of the signed-in user. Also allows changing a member's role, for example from owner to non-owner.",
        "adminConsentDisplayName": "Add and remove members from channels",
        "id": "0c3e411a-ce45-4cd1-8f30-f99a3efa7b11",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Add and remove members from channels, on your behalf. Also allows changing a member's role, for example from owner to non-owner.",
        "userConsentDisplayName": "Add and remove members from teams and channels",
        "value": "ChannelMember.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the authentication flow policies, on behalf of the signed-in user. ",
        "adminConsentDisplayName": "Read and write authentication flow policies",
        "id": "edb72de9-4252-4d03-a925-451deef99db7",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the authentication flow policies for your tenant, on your behalf.",
        "userConsentDisplayName": "Read and write your authentication flow policies",
        "value": "Policy.ReadWrite.AuthenticationFlows"
    },
    {
        "adminConsentDescription": "Allows an app to read a channel's messages in Microsoft Teams, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user channel messages",
        "id": "767156cb-16ae-4d10-8f8b-41b657c8c8c8",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read a channel's messages in Microsoft Teams, on your behalf.",
        "userConsentDisplayName": "Read your channel messages",
        "value": "ChannelMessage.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the apps in the app catalogs.",
        "adminConsentDisplayName": "Read all app catalogs",
        "id": "88e58d74-d3df-44f3-ad47-e89edf4472e4",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read apps in the app catalogs.",
        "userConsentDisplayName": "Read all app catalogs",
        "value": "AppCatalog.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the authentication method policies, on behalf of the signed-in user.\u00a0",
        "adminConsentDisplayName": "Read and write authentication method policies",
        "id": "7e823077-d88e-468f-a337-e18f1f0e6c7c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the authentication method policies for your tenant, on your behalf.",
        "userConsentDisplayName": "Read and write your authentication method policies ",
        "value": "Policy.ReadWrite.AuthenticationMethod"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's authorization policy on behalf of the signed-in user.  For example, authorization policies can control some of the permissions that the out-of-the-box user role has by default.",
        "adminConsentDisplayName": "Read and write your organization's authorization policy",
        "id": "edd3c878-b384-41fd-95ad-e7407dd775be",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's authorization policy on your behalf. For example, authorization policies can control some of the permissions that the out-of-the-box user role has by default.",
        "userConsentDisplayName": "Read and write your organization's authorization policy",
        "value": "Policy.ReadWrite.Authorization"
    },
    {
        "adminConsentDescription": "Allows the app to read policies related to consent and permission grants for applications, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read consent and permission grant policies",
        "id": "414de6ea-2d92-462f-b120-6e2a809a6d01",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read policies related to consent and permission grants for applications, on your behalf.",
        "userConsentDisplayName": "Read consent and permission grant policies",
        "value": "Policy.Read.PermissionGrant"
    },
    {
        "adminConsentDescription": "Allows the app to manage policies related to consent and permission grants for applications, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage consent and permission grant policies",
        "id": "2672f8bb-fd5e-42e0-85e1-ec764dd2614e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage policies related to consent and permission grants for applications, on behalf of the signed-in user.",
        "userConsentDisplayName": "Manage consent and permission grant policies",
        "value": "Policy.ReadWrite.PermissionGrant"
    },
    {
        "adminConsentDescription": "Allows the application to create (register) printers on behalf of the signed-in user.\u00a0",
        "adminConsentDisplayName": "Register printers\u202f\u00a0",
        "id": "90c30bed-6fd1-4279-bf39-714069619721",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to create (register) printers on your behalf.\u00a0",
        "userConsentDisplayName": "Register printers\u202f\u00a0",
        "value": "Printer.Create"
    },
    {
        "adminConsentDescription": "Allows the application to create (register), read, update, and delete (unregister) printers on behalf of the signed-in user.\u00a0",
        "adminConsentDisplayName": "Register, read, update, and unregister printers",
        "id": "93dae4bd-43a1-4a23-9a1a-92957e1d9121",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to create (register), read, update, and delete (unregister) printers on your behalf.\u00a0\u00a0",
        "userConsentDisplayName": "Register, read, update, and unregister printers",
        "value": "Printer.FullControl.All"
    },
    {
        "adminConsentDescription": "Allows the application to read printers on behalf of the signed-in user.\u00a0",
        "adminConsentDisplayName": "Read printers",
        "id": "3a736c8a-018e-460a-b60c-863b2683e8bf",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read printers on your behalf.\u00a0",
        "userConsentDisplayName": "Read printers",
        "value": "Printer.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to read and update printers on behalf of the signed-in user.\u00a0Does not allow creating (registering) or deleting (unregistering) printers.",
        "adminConsentDisplayName": "Read and update printers",
        "id": "89f66824-725f-4b8f-928e-e1c5258dc565",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and update printers on your behalf.\u00a0Does not allow creating (registering) or deleting (unregistering) printers.",
        "userConsentDisplayName": "Read and update printers",
        "value": "Printer.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to read printer shares on behalf of the signed-in user.\u00a0",
        "adminConsentDisplayName": "Read printer shares",
        "id": "ed11134d-2f3f-440d-a2e1-411efada2502",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the application to read printer shares on your behalf.\u00a0",
        "userConsentDisplayName": "Read printer shares",
        "value": "PrinterShare.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to read and update printer shares on behalf of the signed-in user.\u00a0",
        "adminConsentDisplayName": "Read and write printer shares",
        "id": "06ceea37-85e2-40d7-bec3-91337a46038f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and update printer shares on your behalf.\u00a0",
        "userConsentDisplayName": "Read and update printer shares",
        "value": "PrinterShare.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to read the metadata and document content of print jobs that the signed-in user created.",
        "adminConsentDisplayName": "Read user's print jobs",
        "id": "248f5528-65c0-4c88-8326-876c7236df5e",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the application to read the metadata and document content of print jobs that you created.",
        "userConsentDisplayName": "Read your print jobs",
        "value": "PrintJob.Read"
    },
    {
        "adminConsentDescription": "Allows the application to read the metadata and document content of print jobs on behalf of the signed-in user.\u00a0",
        "adminConsentDisplayName": "Read print jobs",
        "id": "afdd6933-a0d8-40f7-bd1a-b5d778e8624b",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read the metadata and document content of print jobs on your behalf.\u00a0",
        "userConsentDisplayName": "Read print jobs",
        "value": "PrintJob.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to read the metadata of print jobs that the signed-in user created. Does not allow access to print job document content.",
        "adminConsentDisplayName": "Read basic information of user's print jobs",
        "id": "6a71a747-280f-4670-9ca0-a9cbf882b274",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the application to read the metadata of print jobs that you created. Does not allow access to print job document content.",
        "userConsentDisplayName": "Read basic information of your print jobs",
        "value": "PrintJob.ReadBasic"
    },
    {
        "adminConsentDescription": "Allows the application to read the metadata of print jobs on behalf of the signed-in user.\u00a0Does not allow access to print job document content.",
        "adminConsentDisplayName": "Read basic information of print jobs",
        "id": "04ce8d60-72ce-4867-85cf-6d82f36922f3",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read the metadata of print jobs on your behalf.\u00a0Does not allow access to print job document content.",
        "userConsentDisplayName": "Read basic information of print jobs",
        "value": "PrintJob.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Allows the application to read and update the metadata and document content of print jobs that the signed-in user created.",
        "adminConsentDisplayName": "Read and write user's print jobs",
        "id": "b81dd597-8abb-4b3f-a07a-820b0316ed04",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the application to read and update the metadata and document content of print jobs that you created.",
        "userConsentDisplayName": "Read and update your print jobs",
        "value": "PrintJob.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the application to read and update the metadata and document content of print jobs on behalf of the signed-in user.\u00a0",
        "adminConsentDisplayName": "Read and write print jobs",
        "id": "036b9544-e8c5-46ef-900a-0646cc42b271",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and update the metadata and document content of print jobs on your behalf.\u00a0",
        "userConsentDisplayName": "Read and update print jobs",
        "value": "PrintJob.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to read and update the metadata of print jobs that the signed-in user created. Does not allow access to print job document content.",
        "adminConsentDisplayName": "Read and write basic information of user's print jobs",
        "id": "6f2d22f2-1cb6-412c-a17c-3336817eaa82",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the application to read and update the metadata of print jobs that you created. Does not allow access to print job document content.",
        "userConsentDisplayName": "Read and write basic information of your print jobs",
        "value": "PrintJob.ReadWriteBasic"
    },
    {
        "adminConsentDescription": "Allows the application to read and update the metadata of print jobs on behalf of the signed-in user.\u00a0Does not allow access to print job document content.",
        "adminConsentDisplayName": "Read and write basic information of print jobs",
        "id": "3a0db2f6-0d2a-4c19-971b-49109b19ad3d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and update the metadata of print jobs on your behalf.\u00a0Does not allow access to print job document content.",
        "userConsentDisplayName": "Read and write basic information of print jobs",
        "value": "PrintJob.ReadWriteBasic.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's device configuration policies on behalf of the signed-in user.  For example, device registration policy can limit initial provisioning controls using quota restrictions, additional authentication and authorization checks.",
        "adminConsentDisplayName": "Read and write your organization's device configuration policies",
        "id": "40b534c3-9552-4550-901b-23879c90bcf9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's device configuration policies on your behalf.  For example, device registration policy can limit initial provisioning controls using quota restrictions, additional authentication and authorization checks.",
        "userConsentDisplayName": "Read and write your organization's device configuration policies",
        "value": "Policy.ReadWrite.DeviceConfiguration"
    },
    {
        "adminConsentDescription": "Allows the app to submit application packages to the catalog and cancel submissions that are pending review on behalf of the signed-in user.",
        "adminConsentDisplayName": "Submit application packages to the catalog and cancel pending submissions",
        "id": "3db89e36-7fa6-4012-b281-85f3d9d9fd2e",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to submit application packages to the catalog and cancel submissions that are pending review on your behalf.",
        "userConsentDisplayName": "Submit application packages to your organization's catalog and cancel pending submissions",
        "value": "AppCatalog.Submit"
    },
    {
        "adminConsentDescription": "Allows the app to read the Teams apps that are installed in chats the signed-in user can access. Does not give the ability to read application-specific settings.",
        "adminConsentDisplayName": "Read installed Teams apps in chats",
        "id": "bf3fbf03-f35f-4e93-963e-47e4d874c37a",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read the Teams apps that are installed in chats that you can access. Does not give the ability to read application-specific settings.",
        "userConsentDisplayName": "Read installed Teams apps in chats",
        "value": "TeamsAppInstallation.ReadForChat"
    },
    {
        "adminConsentDescription": "Allows the app to read the Teams apps that are installed in teams the signed-in user can access. Does not give the ability to read application-specific settings.",
        "adminConsentDisplayName": "Read installed Teams apps in teams",
        "id": "5248dcb1-f83b-4ec3-9f4d-a4428a961a72",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the Teams apps that are installed in teams that you can access. Does not give the ability to read application-specific settings.",
        "userConsentDisplayName": "Read installed Teams apps in teams",
        "value": "TeamsAppInstallation.ReadForTeam"
    },
    {
        "adminConsentDescription": "Allows the app to read the Teams apps that are installed for the signed-in user. Does not give the ability to read application-specific settings.",
        "adminConsentDisplayName": "Read user's installed Teams apps",
        "id": "c395395c-ff9a-4dba-bc1f-8372ba9dca84",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read the Teams apps that are installed for you. Does not give the ability to read application-specific settings.",
        "userConsentDisplayName": "Read your installed Teams apps",
        "value": "TeamsAppInstallation.ReadForUser"
    },
    {
        "adminConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps in teams the signed-in user can access. Does not give the ability to read application-specific settings.",
        "adminConsentDisplayName": "Manage installed Teams apps in teams",
        "id": "2e25a044-2580-450d-8859-42eeb6e996c0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps in teams you can access. Does not give the ability to read application-specific settings.",
        "userConsentDisplayName": "Manage installed Teams apps in teams",
        "value": "TeamsAppInstallation.ReadWriteForTeam"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself in chats the signed-in user can access.",
        "adminConsentDisplayName": "Allow the Teams app to manage itself in chats",
        "id": "0ce33576-30e8-43b7-99e5-62f8569a4002",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself in chats you can access.",
        "userConsentDisplayName": "Allow the Teams app to manage itself in chats",
        "value": "TeamsAppInstallation.ReadWriteSelfForChat"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself for the signed-in user.",
        "adminConsentDisplayName": "Allow the Teams app to manage itself for a user",
        "id": "207e0cb1-3ce7-4922-b991-5a760c346ebc",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself for you.",
        "userConsentDisplayName": "Allow the Teams app to manage itself for you",
        "value": "TeamsAppInstallation.ReadWriteSelfForUser"
    },
    {
        "adminConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps installed for the signed-in user. Does not give the ability to read application-specific settings.",
        "adminConsentDisplayName": "Manage user's installed Teams apps",
        "id": "093f8818-d05f-49b8-95bc-9d2a73e9a43c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps installed for you. Does not give the ability to read application-specific settings.",
        "userConsentDisplayName": "Manage your installed Teams apps",
        "value": "TeamsAppInstallation.ReadWriteForUser"
    },
    {
        "adminConsentDescription": "Allows the app to create teams on behalf of the signed-in user.",
        "adminConsentDisplayName": "Create teams",
        "id": "7825d5d6-6049-4ce7-bdf6-3b8d53f4bcd0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to create teams on your behalf.\u00a0",
        "userConsentDisplayName": "Create teams",
        "value": "Team.Create"
    },
    {
        "adminConsentDescription": "Add and remove members from all teams, on behalf of the signed-in user. Does not allow adding or removing a member with the owner role. Additionally, does not allow the app to elevate an existing member to the owner role.",
        "adminConsentDisplayName": "Add and remove members with non-owner role for all teams",
        "id": "2104a4db-3a2f-4ea0-9dba-143d457dc666",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Add and remove members from all teams, on your behalf. Does not allow adding or removing a member with the owner role. Additionally, does not allow the app to elevate an existing member to the owner role.",
        "userConsentDisplayName": "Add and remove members with non-owner role for all teams",
        "value": "TeamMember.ReadWriteNonOwnerRole.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the term store data that the signed-in user has access to. This includes all sets, groups and terms in the term store.",
        "adminConsentDisplayName": "Read term store data",
        "id": "297f747b-0005-475b-8fef-c890f5152b38",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the term store data that you have access to. This includes all sets, groups and terms in the term store.",
        "userConsentDisplayName": "Read term store data",
        "value": "TermStore.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read or modify data that the signed-in user has access to.\u00a0This includes all sets, groups and terms in the term store.",
        "adminConsentDisplayName": "Read and write term store data",
        "id": "6c37c71d-f50f-4bff-8fd3-8a41da390140",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read or modify data that you have access to. This includes all sets, groups and terms in the term store.",
        "userConsentDisplayName": "Read and write term store data",
        "value": "TermStore.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your tenant's service announcement messages on behalf of the signed-in user. Messages may include information about new or changed features.",
        "adminConsentDisplayName": "Read service announcement messages",
        "id": "eda39fa6-f8cf-4c3c-a909-432c683e4c9b",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your tenant's service announcement messages on your behalf. Messages may include information about new or changed features.",
        "userConsentDisplayName": "Read service messages",
        "value": "ServiceMessage.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your tenant's service health information on behalf of the signed-in user. Health information may include service issues or service health overviews.",
        "adminConsentDisplayName": "Read service health",
        "id": "55896846-df78-47a7-aa94-8d3d4442ca7f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your tenant's service health information on your behalf.Health information may include service issues or service health overviews.",
        "userConsentDisplayName": "Read service health",
        "value": "ServiceHealth.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all the short notes a sign-in user has access to.",
        "adminConsentDisplayName": "Read short notes of the signed-in user",
        "id": "50f66e47-eb56-45b7-aaa2-75057d9afe08",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your short notes.",
        "userConsentDisplayName": "Read your short notes",
        "value": "ShortNotes.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read, create, edit, and delete short notes of a signed-in user.",
        "adminConsentDisplayName": "Read, create, edit, and delete short notes of the signed-in user",
        "id": "328438b7-4c01-4c07-a840-e625a749bb89",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, create, edit, and delete your short notes.",
        "userConsentDisplayName": "Read, create, edit, and delete your short notes",
        "value": "ShortNotes.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's conditional access policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read your organization's conditional access policies",
        "id": "633e0fce-8c58-4cfb-9495-12bbd5a24f7c",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your organization's conditional access policies on your behalf.",
        "userConsentDisplayName": "Read your organization's conditional access policies",
        "value": "Policy.Read.ConditionalAccess"
    },
    {
        "adminConsentDescription": "Allows the app to read the role-based access control (RBAC) settings for all RBAC providers, on behalf of the signed-in user.  This includes reading role definitions and role assignments.",
        "adminConsentDisplayName": "Read role management data for all RBAC providers",
        "id": "48fec646-b2ba-4019-8681-8eb31435aded",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the role-based access control (RBAC) settings for all RBAC providers, on your behalf.  This includes reading role definitions and role assignments.",
        "userConsentDisplayName": "Read role management data for all RBAC providers",
        "value": "RoleManagement.Read.All"
    },
    {
        "adminConsentDescription": "Allows an app to send one-to-one and group chat messages in Microsoft Teams, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Send user chat messages",
        "id": "116b7235-7cc6-461e-b163-8e55691d839e",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to send one-to-one and group chat messages in Microsoft Teams, on your behalf.",
        "userConsentDisplayName": "Send chat messages",
        "value": "ChatMessage.Send"
    },
    {
        "adminConsentDescription": "Allows an app to read the members and descriptions of one-to-one and group chat threads, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read names and members of user chat threads",
        "id": "9547fcb5-d03f-419d-9948-5928bbf71b0f",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read the members and descriptions of one-to-one and group chat threads, on your behalf.",
        "userConsentDisplayName": "Read names and members of your chat threads",
        "value": "Chat.ReadBasic"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the properties of Cloud PCs on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write Cloud PCs",
        "id": "9d77138f-f0e2-47ba-ab33-cd246c8b79d1",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the properties of Cloud PCs, on your behalf.",
        "userConsentDisplayName": "Read and write Cloud PCs",
        "value": "CloudPC.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the properties of Cloud PCs on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read Cloud PCs",
        "id": "5252ec4e-fd40-4d92-8c68-89dd1d3c6110",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read the properties of Cloud PCs, on your behalf.",
        "userConsentDisplayName": "Read Cloud PCs",
        "value": "CloudPC.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps in chats the signed-in user can access. Does not give the ability to read application-specific settings.",
        "adminConsentDisplayName": "Manage installed Teams apps in chats",
        "id": "aa85bf13-d771-4d5d-a9e6-bca04ce44edf",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps in chats you can access. Does not give the ability to read application-specific settings.",
        "userConsentDisplayName": "Manage installed Teams apps in chats",
        "value": "TeamsAppInstallation.ReadWriteForChat"
    },
    {
        "adminConsentDescription": "Allows the app to create, read, update, and delete the signed-in user's tasks and task lists, including any shared with the user.",
        "adminConsentDisplayName": "Create, read, update, and delete user\u2019s tasks and task lists",
        "id": "2219042f-cab5-40cc-b0d2-16b1540b4c5f",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to create, read, update, and delete your tasks and task lists, including any shared with you.",
        "userConsentDisplayName": "Create, read, update, and delete your tasks and task lists",
        "value": "Tasks.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read the signed-in user\u2019s tasks and task lists, including any shared with the user. Doesn't include permission to create, delete, or update anything.",
        "adminConsentDisplayName": "Read user's tasks and task lists",
        "id": "f45671fb-e0fe-4b4b-be20-3d3ce43f1bcb",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your tasks and task lists, including any shared with you. Doesn't include permission to create, delete, or update anything.",
        "userConsentDisplayName": "Read your tasks and task lists",
        "value": "Tasks.Read"
    },
    {
        "adminConsentDescription": "Allows an app to read one-to-one and group chat messages, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user chat messages",
        "id": "cdcdac3a-fd45-410d-83ef-554db620e5c7",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read one-to-one or group chat messages in Microsoft Teams, on your behalf.",
        "userConsentDisplayName": "Read user chat messages",
        "value": "ChatMessage.Read"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall all tabs in chats the signed-in user can access.",
        "adminConsentDisplayName": "Allow the Teams app to manage all tabs in chats",
        "id": "ee928332-e9c2-4747-b4a0-f8c164b68de6",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall all tabs in chats you can access.",
        "userConsentDisplayName": "Allow the Teams app to manage all tabs in chats",
        "value": "TeamsTab.ReadWriteForChat"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall all tabs to teams the signed-in user can access.",
        "adminConsentDisplayName": "Allow the Teams app to manage all tabs in teams",
        "id": "c975dd04-a06e-4fbb-9704-62daad77bb49",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall all tabs to teams you can access.",
        "userConsentDisplayName": "Allow the app to manage all tabs in teams",
        "value": "TeamsTab.ReadWriteForTeam"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall all tabs for the signed-in user.",
        "adminConsentDisplayName": "Allow the Teams app to manage all tabs for a user",
        "id": "c37c9b61-7762-4bff-a156-afc0005847a0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall all tabs for you.",
        "userConsentDisplayName": "Allow the Teams app to manage all tabs for you",
        "value": "TeamsTab.ReadWriteForUser"
    },
    {
        "adminConsentDescription": "Allows the app to read the API connectors used in user authentication flows, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read API connectors for authentication flows",
        "id": "1b6ff35f-31df-4332-8571-d31ea5a4893f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the API connectors used in user authentication flows, on your behalf.",
        "userConsentDisplayName": "Read API connectors for authentication flows",
        "value": "APIConnectors.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, create and manage the API connectors used in user authentication flows, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write API connectors for authentication flows",
        "id": "c67b52c5-7c69-48b6-9d48-7b3af3ded914",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, create and manage the API connectors used in user authentication flows, on your behalf.",
        "userConsentDisplayName": "Read and write API connectors for authentication flows",
        "value": "APIConnectors.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Read the members of chats, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read the members of chats",
        "id": "c5a9e2b1-faf6-41d4-8875-d381aa549b24",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read the members of chats, on your behalf.",
        "userConsentDisplayName": "Read the members of chats",
        "value": "ChatMember.Read"
    },
    {
        "adminConsentDescription": "Add and remove members from chats, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Add and remove members from chats",
        "id": "dea13482-7ea6-488f-8b98-eb5bbecf033d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Add and remove members from chats, on your behalf.",
        "userConsentDisplayName": "Add and remove members from chats",
        "value": "ChatMember.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to create chats on behalf of the signed-in user.",
        "adminConsentDisplayName": "Create chats",
        "id": "38826093-1258-4dea-98f0-00003be2b8d0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to create chats on your behalf.\u00a0",
        "userConsentDisplayName": "Create chats",
        "value": "Chat.Create"
    },
    {
        "adminConsentDescription": "Allows the application to read and write tenant-wide print settings on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write tenant-wide print settings",
        "id": "9ccc526a-c51c-4e5c-a1fd-74726ef50b8f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and write tenant-wide print settings on your behalf.",
        "userConsentDisplayName": "Read and write tenant-wide print settings",
        "value": "PrintSettings.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to read tenant-wide print settings on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read tenant-wide print settings",
        "id": "490f32fd-d90f-4dd7-a601-ff6cdc1a3f6c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read tenant-wide print settings on your behalf.",
        "userConsentDisplayName": "Read tenant-wide print settings",
        "value": "PrintSettings.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to read and write print connectors on behalf of the signed-in user. ",
        "adminConsentDisplayName": "Read and write print connectors",
        "id": "79ef9967-7d59-4213-9c64-4b10687637d8",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and write print connectors on your behalf.",
        "userConsentDisplayName": "Read and write print connectors",
        "value": "PrintConnector.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to read print connectors on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read print connectors",
        "id": "d69c2d6d-4f72-4f99-a6b9-663e32f8cf68",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read print connectors on your behalf.",
        "userConsentDisplayName": "Read print connectors",
        "value": "PrintConnector.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to read basic information about printer shares on behalf of the signed-in user. Does not allow reading access control information.",
        "adminConsentDisplayName": "Read basic information about printer shares",
        "id": "5fa075e9-b951-4165-947b-c63396ff0a37",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the application to read basic information about printer shares on your behalf.",
        "userConsentDisplayName": "Read basic information about printer shares",
        "value": "PrinterShare.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Allows the application to create print jobs on behalf of the signed-in user and upload document content to print jobs that the signed-in user created.",
        "adminConsentDisplayName": "Create print jobs",
        "id": "21f0d9c0-9f13-48b3-94e0-b6b231c7d320",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the application to create print jobs on your behalf and upload document content to print jobs  that you created.",
        "userConsentDisplayName": "Create your print jobs",
        "value": "PrintJob.Create"
    },
    {
        "adminConsentDescription": "Allows the app to manage self-service entitlement management resources on behalf of the signed-in user.  This includes operations such as requesting access and approving access of others.",
        "adminConsentDisplayName": "Read and write entitlement management resources related to self-service operations",
        "id": "e9fdcbbb-8807-410f-b9ec-8d5468c7c2ac",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to create and manage self-service entitlement management resources that you have access to.  This includes operations such as requesting access and approving access for others.",
        "userConsentDisplayName": "Read and write self-service entitlement management resources",
        "value": "EntitlementMgmt-SubjectAccess.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read Azure AD recommendations, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read Azure AD recommendations",
        "id": "34d3bd24-f6a6-468c-b67c-0c365c1d6410",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read Azure AD recommendations, on your behalf.",
        "userConsentDisplayName": "Read Azure AD recommendations",
        "value": "DirectoryRecommendations.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to list and query user profile information associated with the current tenant on behalf of the signed-in user.\u00a0 It also permits the application to export and remove external user data (e.g. customer content or system-generated logs), associated with the current tenant on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read shared cross-tenant user profile and export or delete data",
        "id": "eed0129d-dc60-4f30-8641-daf337a39ffd",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to list and query shared user profile information associated with the current tenant on your behalf.\u00a0 It also permits the application to export and remove your external user data (e.g. customer content or system-generated logs), associated with the current tenant on your behalf.",
        "userConsentDisplayName": "Read shared cross-tenant user profile and export or delete data",
        "value": "CrossTenantUserProfileSharing.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to manage restricted resources based on the other permissions granted to the app, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage restricted resources in the directory",
        "id": "cba5390f-ed6a-4b7f-b657-0efc2210ed20",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage restricted resources based on the other permissions granted to the app, on your behalf.",
        "userConsentDisplayName": "Manage restricted resources in the directory",
        "value": "Directory.Write.Restricted"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's threat submission policies on behalf of the signed-in user. Also allows the app to create new threat submission policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all threat submission policies",
        "id": "059e5840-5353-4c68-b1da-666a033fc5e8",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization's threat submission policies  on your behalf. Also allows the app to create new threat submission policies  on your behalf.",
        "userConsentDisplayName": "Read and write all threat submission policies",
        "value": "ThreatSubmissionPolicy.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to fully manage all data associated with the business scenarios it owns. Data access and changes will be attributed to the signed-in user.",
        "adminConsentDisplayName": "Read and write all data for business scenarios this app creates or owns",
        "id": "19932d57-2952-4c60-8634-3655c79fc527",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to fully manage all data associated with the business scenarios it owns. These changes will be attributed to you.",
        "userConsentDisplayName": "Read and write data for business scenarios this app creates or owns",
        "value": "BusinessScenarioData.ReadWrite.OwnedBy"
    },
    {
        "adminConsentDescription": "Allows an application to read virtual appointments for the signed-in user. Only an organizer or participant user can read their virtual appointments.\u202f\u00a0",
        "adminConsentDisplayName": "Read a user's virtual appointments",
        "id": "27470298-d3b8-4b9c-aad4-6334312a3eac",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read virtual appointments on your behalf.\u202f\u202f",
        "userConsentDisplayName": "Read your virtual appointments\u202f",
        "value": "VirtualAppointment.Read"
    },
    {
        "adminConsentDescription": "Allows an app to read the browser site lists configured for your organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read browser site lists for your organization",
        "id": "fb9be2b7-a7fc-4182-aec1-eda4597c43d5",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read the browser site lists configured for your organization, on your behalf.",
        "userConsentDisplayName": "Read browser site lists for your organization",
        "value": "BrowserSiteLists.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read Azure AD synchronization information, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all Azure AD synchronization data",
        "id": "7aa02aeb-824f-4fbe-a3f7-611f751f5b55",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read Azure AD synchronization information, on your behalf.",
        "userConsentDisplayName": "Read all Azure AD synchronization data",
        "value": "Synchronization.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write inbound data flows on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage inbound flow definitions",
        "id": "97044676-2cec-40ee-bd70-38df444c9e70",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write inbound data flows on your behalf.",
        "userConsentDisplayName": "Manage inbound flow definitions",
        "value": "IndustryData-InboundFlow.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read time-based eligibility schedules for access to Azure AD groups, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read eligibility schedules for access to Azure AD groups",
        "id": "8f44f93d-ecef-46ae-a9bf-338508d44d6b",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read time-based eligibility schedules for access to Azure AD groups, on your behalf.",
        "userConsentDisplayName": "Read eligibility schedules for access to Azure AD groups",
        "value": "PrivilegedEligibilitySchedule.Read.AzureADGroup"
    },
    {
        "adminConsentDescription": "Allows the app to read data for the learner's self-initiated courses in the organization's directory, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user's self-initiated courses",
        "id": "f6403ef7-4a96-47be-a190-69ba274c3f11",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read data for your self-initiated courses in the organization's directory, on your behalf.",
        "userConsentDisplayName": "Read your self-initiated courses",
        "value": "LearningSelfInitiatedCourse.Read"
    },
    {
        "adminConsentDescription": "Allows an app to read all question and answer sets that the signed-in user can access.",
        "adminConsentDisplayName": "Read all Questions and Answers that the user can access.",
        "id": "f73fa04f-b9a5-4df9-8843-993ce928925e",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read all question and answer sets that you can access.",
        "userConsentDisplayName": "Read all Questions and Answers that you can access.",
        "value": "QnA.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to read and write tenant-wide people settings on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write tenant-wide people settings",
        "id": "e67e6727-c080-415e-b521-e3f35d5248e9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and write tenant-wide people settings on your behalf.",
        "userConsentDisplayName": "Read and write tenant-wide people settings",
        "value": "PeopleSettings.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to list and query any shared user profile information associated with the current tenant on behalf of the signed-in user.\u00a0 It also permits the application to export and remove external user data (e.g. customer content or system-generated logs), for any user associated with the current tenant on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all shared cross-tenant user profiles and export or delete their data",
        "id": "64dfa325-cbf8-48e3-938d-51224a0cac01",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to list and query any shared user profile information associated with the current tenant on your behalf.\u00a0 It also permits the application to export and remove external user data (e.g. customer content or system-generated logs), for any user associated with the current tenant on your behalf.",
        "userConsentDisplayName": "Read any shared cross-tenant user profiles and export or delete data",
        "value": "CrossTenantUserProfileSharing.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the threat submissions and threat submission policies owned by the signed-in user.",
        "adminConsentDisplayName": "Read threat submissions",
        "id": "fd5353c6-26dd-449f-a565-c4e16b9fce78",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read the threat submissions and threat submission policies that you own on your behalf.",
        "userConsentDisplayName": "Read threat submissions",
        "value": "ThreatSubmission.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read the threat submissions and threat submission policies owned by the signed-in user. Also allows the app to create new threat submissions on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write threat submissions",
        "id": "68a3156e-46c9-443c-b85c-921397f082b5",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read the threat submissions and threat submission policies that you own. Also allows the app to create new threat submissions on your behalf.",
        "userConsentDisplayName": "Read and write threat submissions",
        "value": "ThreatSubmission.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read device local credential properties including passwords, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read device local credential passwords",
        "id": "280b3b69-0437-44b1-bc20-3b2fca1ee3e9",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read device local credential properties including passwords, on your behalf.",
        "userConsentDisplayName": "Read device local credential passwords",
        "value": "DeviceLocalCredential.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all recordings of online meetings, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all recordings of online meetings.",
        "id": "190c2bb6-1fdd-4fec-9aa2-7d571b5e1fe3",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all recordings of online meetings, on your behalf.\u00a0",
        "userConsentDisplayName": "Read all recordings of online meetings.\u00a0",
        "value": "OnlineMeetingRecording.Read.All"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself in teams the signed-in user can access, and manage its permission grants for accessing those specific teams' data.",
        "adminConsentDisplayName": "Allow the Teams app to manage itself and its permission grants in teams",
        "id": "4a6bbf29-a0e1-4a4d-a7d1-cef17f772975",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself in teams the signed-in user can access, and manage its permission grants for accessing those specific teams' data.",
        "userConsentDisplayName": "Allow the Teams app to manage itself and its permission grants in teams",
        "value": "TeamsAppInstallation.ReadWriteAndConsentSelfForTeam"
    },
    {
        "adminConsentDescription": "Allows the app to configure the Azure AD synchronization service, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all Azure AD synchronization data",
        "id": "7bb27fa3-ea8f-4d67-a916-87715b6188bd",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to configure the Azure AD synchronization service, on your behalf.",
        "userConsentDisplayName": "Read and write all Azure AD synchronization data",
        "value": "Synchronization.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read inbound data flows on behalf of the signed-in user.",
        "adminConsentDisplayName": "View inbound flow definitions",
        "id": "cb0774da-a605-42af-959c-32f438fb38f4",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read inbound data flows on your behalf.",
        "userConsentDisplayName": "View inbound flow definitions",
        "value": "IndustryData-InboundFlow.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to read and update the organization's external identities policy on behalf of the signed-in user.  For example, external identities policy controls if users invited to access resources in your organization via B2B collaboration or B2B direct connect are allowed to self-service leave.",
        "adminConsentDisplayName": "Read and write your organization's external identities policy",
        "id": "b5219784-1215-45b5-b3f1-88fe1081f9c0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and update the organization's external identities policy on your behalf.  For example, external identities policy controls if users invited to access resources in your organization via B2B collaboration or B2B direct connect are allowed to self-service leave.",
        "userConsentDisplayName": "Read and write your organization's external identities policy",
        "value": "Policy.ReadWrite.ExternalIdentities"
    },
    {
        "adminConsentDescription": "Allows the app to read time-based assignment schedules for access to Azure AD groups, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read assignment schedules for access to Azure AD groups",
        "id": "02a32cc4-7ab5-4b58-879a-0586e0f7c495",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read time-based assignment schedules for access to Azure AD groups, on your behalf.",
        "userConsentDisplayName": "Read assignment schedules for access to Azure AD groups",
        "value": "PrivilegedAssignmentSchedule.Read.AzureADGroup"
    },
    {
        "adminConsentDescription": "Allows the application to obtain basic tenant information about another target tenant within the Azure AD ecosystem on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read cross-tenant basic information",
        "id": "81594d25-e88e-49cf-ac8c-fecbff49f994",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to obtain basic tenant information about another target tenant within the Azure AD ecosystem on your behalf.",
        "userConsentDisplayName": "Read cross-tenant basic information",
        "value": "CrossTenantInformation.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's authentication event listeners on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read your organization's authentication event listeners",
        "id": "f7dd3bed-5eec-48da-bc73-1c0ef50bc9a1",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization's authentication event listeners on your behalf.",
        "userConsentDisplayName": "Read your organization's authentication event listeners",
        "value": "EventListener.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read device local credential properties excluding passwords, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read device local credential properties",
        "id": "9917900e-410b-4d15-846e-42a357488545",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read device local credential properties excluding passwords, on your behalf.",
        "userConsentDisplayName": "Read device local credential properties",
        "value": "DeviceLocalCredential.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the Teams app settings on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read Teams app settings",
        "id": "44e060c4-bbdc-4256-a0b9-dcc0396db368",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read the Teams app settings on your behalf.",
        "userConsentDisplayName": "Read Teams app settings",
        "value": "TeamworkAppSettings.Read.All"
    },
    {
        "adminConsentDescription": "Allows\u00a0the\u00a0app\u00a0to\u00a0manage learning\u00a0content\u00a0in\u00a0the\u00a0organization's\u00a0directory, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage\u00a0learning\u00a0content",
        "id": "53cec1c4-a65f-4981-9dc1-ad75dbf1c077",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows\u00a0the\u00a0app\u00a0to\u00a0manage learning\u00a0content\u00a0in\u00a0the\u00a0organization's\u00a0directory, on your behalf.",
        "userConsentDisplayName": "Manage learning content",
        "value": "LearningContent.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to create, update, read, and delete data for the learning provider in the organization's directory, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage\u00a0learning\u00a0provider",
        "id": "40c2eb57-abaf-49f5-9331-e90fd01f7130",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows\u00a0the\u00a0app\u00a0to\u00a0create, update, read, and delete\u00a0data\u00a0for\u00a0the learning\u00a0provider\u00a0in\u00a0the organization's\u00a0directory, on your behalf.",
        "userConsentDisplayName": "Manage learning provider",
        "value": "LearningProvider.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the configurations of your organization's business scenarios, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write business scenario configurations",
        "id": "755e785b-b658-446f-bb22-5a46abd029ea",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the configurations of your organization's business scenarios, on your behalf.",
        "userConsentDisplayName": "Read and write business scenario configurations",
        "value": "BusinessScenarioConfig.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the lifecycle information like employeeLeaveDateTime of users in your organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all users' lifecycle information",
        "id": "ed8d2a04-0374-41f1-aefe-da8ac87ccc87",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the lifecycle information like employeeLeaveDateTime of users in your organization, on behalf of the signed-in user.",
        "userConsentDisplayName": "Read all users' lifecycle information",
        "value": "User-LifeCycleInfo.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps in chats the signed-in user can access. Gives the ability to manage permission grants for accessing those specific chats' data.",
        "adminConsentDisplayName": "Manage installed Teams apps in chats",
        "id": "e1408a66-8f82-451b-a2f3-3c3e38f7413f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps in chats the signed-in user can access. Gives the ability to manage permission grants for accessing those specific chats' data.",
        "userConsentDisplayName": "Manage installation and permission grants of Teams apps in chats",
        "value": "TeamsAppInstallation.ReadWriteAndConsentForChat"
    },
    {
        "adminConsentDescription": "Allows an app to read and write the browser site lists configured for your organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write browser site lists for your organization",
        "id": "83b34c85-95bf-497b-a04e-b58eca9d49d0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows an app to read and write the browser site lists configured for your organization, on your behalf.",
        "userConsentDisplayName": "Read and write browser site lists for your organization",
        "value": "BrowserSiteLists.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read data connectors on behalf of the signed-in user.",
        "adminConsentDisplayName": "View data connector definitions",
        "id": "d19c0de5-7ecb-4aba-b090-da35ebcd5425",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read data connectors on your behalf.",
        "userConsentDisplayName": "View data connector definitions",
        "value": "IndustryData-DataConnector.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write data connectors on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage data connector definitions",
        "id": "5ce933ac-3997-4280-aed0-cc072e5c062a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write data connectors on your behalf.",
        "userConsentDisplayName": "Manage data connector definitions",
        "value": "IndustryData-DataConnector.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read current and previous IndustryData runs on behalf of the signed-in user.",
        "adminConsentDisplayName": "View current and previous runs",
        "id": "92685235-50c4-4702-b2c8-36043db6fa79",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read current and previous IndustryData runs on your behalf.",
        "userConsentDisplayName": "View current and previous runs",
        "value": "IndustryData-Run.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write all on-premises directory synchronization information for the organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all on-premises directory synchronization information",
        "id": "c2d95988-7604-4ba1-aaed-38a5f82a51c7",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write all on-premises directory synchronization information for the organization, on your behalf.",
        "userConsentDisplayName": "Read and write all on-premises directory synchronization information",
        "value": "OnPremDirectorySynchronization.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, create, and delete time-based assignment schedules for access to Azure AD groups, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read, create, and delete assignment schedules for access to Azure AD groups",
        "id": "06dbc45d-6708-4ef0-a797-f797ee68bf4b",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, create, and delete time-based assignment schedules for access to Azure AD groups, on your behalf.",
        "userConsentDisplayName": "Read, create, and delete assignment schedules for access to Azure AD groups",
        "value": "PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup"
    },
    {
        "adminConsentDescription": "Allows the application to list and query user profile information associated with the current tenant on behalf of the signed-in user.\u00a0 It also permits the application to export external user data (e.g. customer content or system-generated logs), associated with the current tenant on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read shared cross-tenant user profile and export data",
        "id": "cb1ba48f-d22b-4325-a07f-74135a62ee41",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to list and query shared user profile information associated with the current tenant on your behalf.\u00a0 It also permits the application to export your external user data (e.g. customer content or system-generated logs), associated with the current tenant on your behalf.",
        "userConsentDisplayName": "Read shared cross-tenant user profile and export data",
        "value": "CrossTenantUserProfileSharing.Read"
    },
    {
        "adminConsentDescription": "Allows the app to enable and disable users' accounts, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Enable and disable user accounts",
        "id": "f92e74e7-2563-467f-9dd0-902688cb5863",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to enable and disable users' accounts, on your behalf.",
        "userConsentDisplayName": "Enable and disable user accounts",
        "value": "User.EnableDisableAccount.All"
    },
    {
        "adminConsentDescription": "Allows the app to read admin report settings, such as whether to display concealed information in reports, on behalf of the signed-in user",
        "adminConsentDisplayName": "Read admin report settings",
        "id": "84fac5f4-33a9-4100-aa38-a20c6d29e5e7",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read admin report settings, such as whether to display concealed information in reports, on your behalf.",
        "userConsentDisplayName": "Read admin report settings",
        "value": "ReportSettings.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all data associated with the business scenarios it owns. Data access will be attributed to the signed-in user.",
        "adminConsentDisplayName": "Read all data for business scenarios this app creates or owns",
        "id": "25b265c4-5d34-4e44-952d-b567f6d3b96d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all data associated with the business scenarios it owns. Data access will be attributed to you.",
        "userConsentDisplayName": "Read data for business scenarios this app creates or owns",
        "value": "BusinessScenarioData.Read.OwnedBy"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's security defaults policy on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write your organization's security defaults policy",
        "id": "0b2a744c-2abf-4f1e-ad7e-17a087e2be99",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's security defaults policy on your behalf.",
        "userConsentDisplayName": "Read and write your organization's security defaults policy",
        "value": "Policy.ReadWrite.SecurityDefaults"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the lifecycle information like employeeLeaveDateTime of users in your organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all users' lifecycle information",
        "id": "7ee7473e-bd4b-4c9f-987c-bd58481f5fa2",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the lifecycle information like employeeLeaveDateTime of users in your organization, on behalf of the signed-in user.",
        "userConsentDisplayName": "Read and write all users' lifecycle information",
        "value": "User-LifeCycleInfo.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps in teams the signed-in user can access. Gives the ability to manage permission grants for accessing those specific teams' data.",
        "adminConsentDisplayName": "Manage installed Teams apps in teams",
        "id": "946349d5-2a9d-4535-abc0-7beeacaedd1d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, install, upgrade, and uninstall Teams apps in teams the signed-in user can access. Gives the ability to manage permission grants for accessing those specific teams' data.",
        "userConsentDisplayName": "Manage installation and permission grants of Teams apps in teams",
        "value": "TeamsAppInstallation.ReadWriteAndConsentForTeam"
    },
    {
        "adminConsentDescription": "Allows the app to read, create, and delete time-based eligibility schedules for access to Azure AD groups, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read, create, and delete eligibility schedules for access to Azure AD groups",
        "id": "ba974594-d163-484e-ba39-c330d5897667",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read, create, and delete time-based eligibility schedules for access to Azure AD groups, on your behalf.",
        "userConsentDisplayName": "Read, create, and delete eligibility schedules for access to Azure AD groups",
        "value": "PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup"
    },
    {
        "adminConsentDescription": "Allows the app to read data for the learner's assignments in the organization's directory, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read user's assignments",
        "id": "ac08cdae-e845-41db-adf9-5899a0ec9ef6",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read data for your assignments in the organization's directory, on your behalf.",
        "userConsentDisplayName": "Read your assignments",
        "value": "LearningAssignedCourse.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read and manage the role-based access control (RBAC) settings for your organization's Exchange Online service, on behalf of the signed-in user. This includes reading, creating, updating, and deleting Exchange management role definitions, role groups, role group membership, role assignments, management scopes, and role assignment policies.",
        "adminConsentDisplayName": "Read and write Exchange Online RBAC configuration",
        "id": "c1499fe0-52b1-4b22-bed2-7a244e0e879f",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and manage the role-based access control (RBAC) settings for your organization's Exchange Online service, on your behalf. This includes reading, creating, updating, and deleting Exchange management role definitions, role groups, role group membership, role assignments, management scopes, and role assignment policies.",
        "userConsentDisplayName": "Read and write Exchange Online RBAC configuration",
        "value": "RoleManagement.ReadWrite.Exchange"
    },
    {
        "adminConsentDescription": "Allows the app to read the configurations applicable to the signed-in user for protecting organizational data, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read configurations for protecting organizational data applicable to the user",
        "id": "12f4bffb-b598-413c-984b-db99728f8b54",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the configurations applicable to you for protecting organizational data, on your behalf.",
        "userConsentDisplayName": "Read configurations for protecting organizational data applicable to you",
        "value": "InformationProtectionConfig.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read virtual events created by the you",
        "adminConsentDisplayName": "Read your virtual events",
        "id": "6b616635-ae58-433a-a918-8c45e4f304dc",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read virtual events created by the you",
        "userConsentDisplayName": "Read your virtual events",
        "value": "VirtualEvent.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read and update Azure AD recommendations, on behalf of the signed-in user. ",
        "adminConsentDisplayName": "Read and update Azure AD recommendations",
        "id": "f37235e8-90a0-4189-93e2-e55b53867ccd",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and update Azure AD recommendations, on your behalf.",
        "userConsentDisplayName": "Read and update Azure AD recommendations",
        "value": "DirectoryRecommendations.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's threat submissions and threat submission policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all threat submissions",
        "id": "7083913a-4966-44b6-9886-c5822a5fd910",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization's threat submissions and threat submission policies on your behalf.",
        "userConsentDisplayName": "Read all threat submissions",
        "value": "ThreatSubmission.Read.All"
    },
    {
        "adminConsentDescription": "Read email metadata and security detection details on behalf of the signed in user.",
        "adminConsentDisplayName": "Read metadata and detection details for emails in your organization",
        "id": "53e6783e-b127-4a35-ab3a-6a52d80a9077",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read email metadata and security detection details on your behalf.",
        "userConsentDisplayName": "Read metadata and detection details for emails in your organization",
        "value": "SecurityAnalyzedMessage.Read.All"
    },
    {
        "adminConsentDescription": "Read email metadata, security detection details, and execute remediation actions like deleting an email, on behalf of the signed in user.",
        "adminConsentDisplayName": "Read metadata, detection details, and execute remediation actions on emails in your organization",
        "id": "48eb8c83-6e58-46e7-a6d3-8805822f5940",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Read email metadata, security detection details, and execute remediation actions like deleting an email, on your behalf.",
        "userConsentDisplayName": "Read metadata, detection details, and execute remediation actions on emails in your organization",
        "value": "SecurityAnalyzedMessage.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read learning content in the organization's directory, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read learning content",
        "id": "ea4c1fd9-6a9f-4432-8e5d-86e06cc0da77",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read learning content in the organization's directory, on your behalf.",
        "userConsentDisplayName": "Read learning content",
        "value": "LearningContent.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read data for the learning provider in the organization's directory, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read learning provider",
        "id": "dd8ce36f-9245-45ea-a99e-8ac398c22861",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows\u00a0the\u00a0app\u00a0to\u00a0read\u00a0data\u00a0for\u00a0the learning\u00a0provider\u00a0in\u00a0the organization's\u00a0directory, on your behalf.",
        "userConsentDisplayName": "Read learning provider",
        "value": "LearningProvider.Read"
    },
    {
        "adminConsentDescription": "Allows the app to read the configurations of your organization's business scenarios, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read business scenario configurations",
        "id": "d16480b2-e469-4118-846b-d3d177327bee",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the configurations of your organization's business scenarios, on your behalf.",
        "userConsentDisplayName": "Read business scenario configurations",
        "value": "BusinessScenarioConfig.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to create, update, list, read and delete all workflows, tasks and related lifecycle workflows resources on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all lifecycle workflows resources",
        "id": "84b9d731-7db8-4454-8c90-fd9e95350179",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to create, update, list, read and delete all workflows, tasks and related lifecycle workflows resources on your behalf.",
        "userConsentDisplayName": "Read and write all lifecycle workflows resources",
        "value": "LifecycleWorkflows.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's branches for network access on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write properties of branches for network access",
        "id": "b8a36cc2-b810-461a-baa4-a7281e50bd5c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's branches for network access on your behalf.",
        "userConsentDisplayName": "Read and write properties of branches for network access",
        "value": "NetworkAccessBranch.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows an app to read all bookmarks that the signed-in user can access.",
        "adminConsentDisplayName": "Read all bookmarks that the user can access",
        "id": "98b17b35-f3b1-4849-a85f-9f13733002f0",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read all bookmarks you can access.",
        "userConsentDisplayName": "Read all bookmarks that you have access to",
        "value": "Bookmark.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read basic Industry Data service and resource information on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read basic Industry Data service and resource definitions",
        "id": "60382b96-1f5e-46ea-a544-0407e489e588",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read Industry Data basic service and resource information on your behalf.",
        "userConsentDisplayName": "Read basic Industry Data service and resource definitions",
        "value": "IndustryData.ReadBasic.All"
    },
    {
        "adminConsentDescription": "Allows the app to read reference definitions on behalf of the signed-in user.",
        "adminConsentDisplayName": "View reference definitions",
        "id": "a3f96ffe-cb84-40a8-ac85-582d7ef97c2a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read reference definitions on your behalf.",
        "userConsentDisplayName": "View reference definitions",
        "value": "IndustryData-ReferenceDefinition.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read source system definitions on behalf of the signed-in user.",
        "adminConsentDisplayName": "View source system definitions",
        "id": "49b7016c-89ae-41e7-bd6f-b7170c5490bf",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read source system definitions on your behalf.",
        "userConsentDisplayName": "View source system definitions",
        "value": "IndustryData-SourceSystem.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read time period definitions on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read time period definitions",
        "id": "c9d51f28-8ccd-42b2-a836-fd8fe9ebf2ae",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read time period definitions on your behalf.",
        "userConsentDisplayName": "Read time period definitions",
        "value": "IndustryData-TimePeriod.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write time period definitions on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage time period definitions",
        "id": "b6d56528-3032-4f9d-830f-5a24a25e6661",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write time period definitions on your behalf.",
        "userConsentDisplayName": "Manage time period definitions",
        "value": "IndustryData-TimePeriod.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write other apps' remote desktop security configuration, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write the remote desktop security configuration for apps",
        "id": "ffa91d43-2ad8-45cc-b592-09caddeb24bb",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write other apps' remote desktop security configuration, on your behalf.",
        "userConsentDisplayName": "Read and write the remote desktop security configuration for apps",
        "value": "Application-RemoteDesktopConfig.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all on-premises directory synchronization information for the organization, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all on-premises directory synchronization information",
        "id": "f6609722-4100-44eb-b747-e6ca0536989d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all on-premises directory synchronization information for the organization, on your behalf.",
        "userConsentDisplayName": "Read all on-premises directory synchronization information",
        "value": "OnPremDirectorySynchronization.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the role-based access control (RBAC) alerts for your company's directory, on behalf of the signed-in user. This includes reading alert statuses, alert definitions, alert configurations and incidents that lead to an alert.",
        "adminConsentDisplayName": "Read all alert data for your company's directory",
        "id": "cce71173-f76d-446e-97ff-efb2d82e11b1",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the role-based access control (RBAC) alerts for your company's directory, on your behalf. This includes reading alert statuses, alert definitions, alert configurations and incidents that lead to an alert.",
        "userConsentDisplayName": "Read all alert data for your company's directory",
        "value": "RoleManagementAlert.Read.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the billing configuration on all applications on behalf of the signed-in user. ",
        "adminConsentDisplayName": "Read and write application billing configuration",
        "id": "2bf6d319-dfca-4c22-9879-f88dcfaee6be",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the billing configuration on all applications on your behalf",
        "userConsentDisplayName": "Read and write application billing configuration",
        "value": "BillingConfiguration.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the application to read and change the tenant-level settings of SharePoint and OneDrive on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and change SharePoint and OneDrive tenant settings",
        "id": "aa07f155-3612-49b8-a147-6c590df35536",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read and change the tenant-level settings of SharePoint and OneDrive on your behalf.",
        "userConsentDisplayName": "Read and change SharePoint and OneDrive tenant settings",
        "value": "SharePointTenantSettings.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read or write your organization's authentication event listeners on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write your organization's authentication event listeners",
        "id": "d11625a6-fe21-4fc6-8d3d-063eba5525ad",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read or write your organization's authentication event listeners on your behalf.",
        "userConsentDisplayName": "Read and write your organization's authentication event listeners",
        "value": "EventListener.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write the Teams app settings on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write Teams app settings",
        "id": "87c556f0-2bd9-4eed-bd74-5dd8af6eaf7e",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write the Teams app settings on your behalf.",
        "userConsentDisplayName": "Read and write Teams app settings",
        "value": "TeamworkAppSettings.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all authentication context information in your organization on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all authentication context information",
        "id": "57b030f1-8c35-469c-b0d9-e4a077debe70",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all authentication context information in your organization on your behalf.",
        "userConsentDisplayName": "Read all authentication context information",
        "value": "AuthenticationContext.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and update all authentication context information in your organization on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write all authentication context information",
        "id": "ba6d575a-1344-4516-b777-1404f5593057",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and update all authentication context information in your organization on your behalf.",
        "userConsentDisplayName": "Read and write all authentication context information",
        "value": "AuthenticationContext.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and update admin report settings, such as whether to display concealed information in reports, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write admin report settings",
        "id": "b955410e-7715-4a88-a940-dfd551018df3",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and update admin report settings, such as whether to display concealed information in reports, on your behalf.",
        "userConsentDisplayName": "Read and write admin report settings",
        "value": "ReportSettings.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read the configurations of business scenarios it owns, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read business scenario configurations this app creates or owns",
        "id": "c47e7b6e-d6f1-4be9-9ffd-1e00f3e32892",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the configurations of business scenarios it owns, on your behalf.",
        "userConsentDisplayName": "Read business scenario configurations this app creates or owns",
        "value": "BusinessScenarioConfig.Read.OwnedBy"
    },
    {
        "adminConsentDescription": "Allows an application to read and write virtual appointments for the signed-in user. Only an organizer or participant user can read and write their virtual appointments.\u202f",
        "adminConsentDisplayName": "Read and write a user's virtual appointments\u202f\u00a0",
        "id": "2ccc2926-a528-4b17-b8bb-860eed29d64c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write virtual appointments on your behalf.\u202f\u00a0",
        "userConsentDisplayName": "Read and write your virtual appointments",
        "value": "VirtualAppointment.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows the app to list and read all workflows, tasks and related lifecycle workflows resources on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all lifecycle workflows resources",
        "id": "9bcb9916-765a-42af-bf77-02282e26b01a",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to list and read all workflows, tasks and related lifecycle workflows resources on your behalf.",
        "userConsentDisplayName": "Read all lifecycle workflows resources",
        "value": "LifecycleWorkflows.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write your organization's security and routing network access policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write security and routing policies for network access",
        "id": "b1fbad0f-ef6e-42ed-8676-bca7fa3e7291",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write your organization's security and routing network access policies on your behalf.",
        "userConsentDisplayName": "Read and write security and routing policies for network access",
        "value": "NetworkAccessPolicy.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and manage the role-based access control (RBAC) alerts for your company's directory, on behalf of the signed-in user. This includes managing alert settings, initiating alert scans, dimissing alerts, remediating alert incidents, and reading alert statuses, alert definitions, alert configurations and incidents that lead to an alert.",
        "adminConsentDisplayName": "Read all alert data, configure alerts, and take actions on all alerts for your company's directory",
        "id": "435644c6-a5b1-40bf-8f52-fe8e5b53e19c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and manage the role-based access control (RBAC) alerts for your company's directory, on your behalf. This includes managing alert settings, initiating alert scans, dimissing alerts, remediating alert incidents, and reading alert statuses, alert definitions, alert configurations and incidents that lead to an alert.",
        "userConsentDisplayName": "Read all alert data, configure alerts, and take actions on all alerts for your company's directory",
        "value": "RoleManagementAlert.ReadWrite.Directory"
    },
    {
        "adminConsentDescription": "Allows the app to read the role-based access control (RBAC) settings for your organization's Exchange Online service, on behalf of the signed-in user. This includes reading Exchange management role definitions, role groups, role group membership, role assignments, management scopes, and role assignment policies.",
        "adminConsentDisplayName": "Read Exchange Online RBAC configuration",
        "id": "3bc15058-7858-4141-b24f-ae43b4e80b52",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read the role-based access control (RBAC) settings for your organization's Exchange Online service, on your behalf. This includes reading Exchange management role definitions, role groups, role group membership, role assignments, management scopes, and role assignment policies.",
        "userConsentDisplayName": "Read Exchange Online RBAC configuration",
        "value": "RoleManagement.Read.Exchange"
    },
    {
        "adminConsentDescription": "Allows the application to read tenant-wide people settings on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read tenant-wide people settings",
        "id": "ec762c5f-388b-4b16-8693-ac1efbc611bc",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read tenant-wide people settings on your behalf.",
        "userConsentDisplayName": "Read tenant-wide people settings",
        "value": "PeopleSettings.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to list and query any shared user profile information associated with the current tenant on behalf of the signed-in user.\u00a0 It also permits the application to export external user data (e.g. customer content or system-generated logs), for any user associated with the current tenant on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all shared cross-tenant user profiles and export their data",
        "id": "759dcd16-3c90-463c-937e-abf89f991c18",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to list and query any shared user profile information associated with the current tenant on your behalf.\u00a0 It also permits the application to export external user data (e.g. customer content or system-generated logs), for any user associated with the current tenant on your behalf.",
        "userConsentDisplayName": "Read any shared cross-tenant user profiles and export data",
        "value": "CrossTenantUserProfileSharing.Read.All"
    },
    {
        "adminConsentDescription": "Allows the application to read the tenant-level settings in SharePoint and OneDrive on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read SharePoint and OneDrive tenant settings",
        "id": "2ef70e10-5bfd-4ede-a5f6-67720500b258",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the application to read the tenant-level settings in SharePoint and OneDrive on your behalf.",
        "userConsentDisplayName": "Read SharePoint and OneDrive tenant settings",
        "value": "SharePointTenantSettings.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read or write your organization's custom authentication extensions on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write your organization's custom authentication extensions",
        "id": "8dfcf82f-15d0-43b3-bc78-a958a13a5792",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read or write your organization's custom authentication extensions on your behalf.",
        "userConsentDisplayName": "Read and write your organization's custom authentication extensions",
        "value": "CustomAuthenticationExtension.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows an app to manage license assignments for users and groups, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage all license assignments",
        "id": "f55016cc-149c-447e-8f21-7cf3ec1d6350",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to manage all license assignments, on your behalf.",
        "userConsentDisplayName": "Manage all license assignments",
        "value": "LicenseAssignment.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read mail the signed-in user can access, including their own and shared mail, except for body, bodyPreview, uniqueBody, attachments, extensions, and any extended properties.",
        "adminConsentDisplayName": "Read user and shared basic mail",
        "id": "b11fa0e7-fdb7-4dc9-b1f1-59facd463480",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read mail you can access, including shared mail except body, previewBody, uniqueBody, attachments, extensions, and any extended properties. ",
        "userConsentDisplayName": "Read basic mail you can access",
        "value": "Mail.ReadBasic.Shared"
    },
    {
        "adminConsentDescription": "Allows the app to create new business scenarios and fully manage the configurations of scenarios it owns, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read and write business scenario configurations this app creates or owns",
        "id": "b3b7fcff-b4d4-4230-bf6f-90bd91285395",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to create new business scenarios and fully manage the configurations of scenarios it owns, on your behalf.",
        "userConsentDisplayName": "Read and write business scenario configurations this app creates or owns",
        "value": "BusinessScenarioConfig.ReadWrite.OwnedBy"
    },
    {
        "adminConsentDescription": "Allows the app to delete and recover deleted chats, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Delete and recover deleted chats",
        "id": "bb64e6fc-6b6d-4752-aea0-dd922dbba588",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to delete and recover deleted chats, on your behalf.",
        "userConsentDisplayName": "Delete and recover deleted chats",
        "value": "Chat.ManageDeletion.All"
    },
    {
        "adminConsentDescription": "Allows an app to read all acronyms that the signed-in user can access.",
        "adminConsentDisplayName": "Read all acronyms that the user can access",
        "id": "9084c10f-a2d6-4713-8732-348def50fe02",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read all acronyms you can access.",
        "userConsentDisplayName": "Read all acronyms that you have access to",
        "value": "Acronym.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write source system definitions on behalf of the signed-in user.",
        "adminConsentDisplayName": "Manage source system definitions",
        "id": "9599f005-05d6-4ea7-b1b1-4929768af5d0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write source system definitions on your behalf.",
        "userConsentDisplayName": "Manage source system definitions",
        "value": "IndustryData-SourceSystem.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's custom authentication extensions on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read your oganization's custom authentication extensions",
        "id": "b2052569-c98c-4f36-a5fb-43e5c111e6d0",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read your organization's custom authentication extensions on your behalf.",
        "userConsentDisplayName": "Read your organization's custom authentication extensions",
        "value": "CustomAuthenticationExtension.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read all transcripts of online meetings, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all transcripts of online meetings. ",
        "id": "30b87d18-ebb1-45db-97f8-82ccb1f0190c",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read all transcripts of online meetings, on your behalf.",
        "userConsentDisplayName": "Read all transcripts of online meetings.",
        "value": "OnlineMeetingTranscript.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read and write channel messages, on behalf of the signed-in user. This doesn't allow the app to edit the policyViolation of a channel message.",
        "adminConsentDisplayName": "Read and write user channel messages",
        "id": "5922d31f-46c8-4404-9eaf-2117e390a8a4",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read and write channel messages, on your behalf. This doesn't allow the app to edit the policyViolation of a channel message.",
        "userConsentDisplayName": "Read and write user channel messages",
        "value": "ChannelMessage.ReadWrite"
    },
    {
        "adminConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself in chats the signed-in user can access, and manage its permission grants for accessing those specific chats' data.",
        "adminConsentDisplayName": "Allow the Teams app to manage itself and its permission grants in chats",
        "id": "a0e0e18b-8fb2-458f-8130-da2d7cab9c75",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows a Teams app to read, install, upgrade, and uninstall itself in chats the signed-in user can access, and manage its permission grants for accessing those specific chats' data.",
        "userConsentDisplayName": "Allow the Teams app to manage itself and its permission grants in chats",
        "value": "TeamsAppInstallation.ReadWriteAndConsentSelfForChat"
    },
    {
        "adminConsentDescription": "Allows the app to read events in user calendars, except for properties such as body, attachments, and extensions.",
        "adminConsentDisplayName": "Read basic details of user calendars",
        "id": "662d75ba-a364-42ad-adee-f5f880ea4878",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read events in your calendars, except for properties such as body, attachments, and extensions.",
        "userConsentDisplayName": "Read basic details of your calendars",
        "value": "Calendars.ReadBasic"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's security and routing network access policies on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read security and routing policies for network access",
        "id": "ba22922b-752c-446f-89d7-a2d92398fceb",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your organization's security and routing network access policies on your behalf.",
        "userConsentDisplayName": "Read security and routing policies for network access",
        "value": "NetworkAccessPolicy.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to read your organization's branches for network access on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read properties of branches for network access",
        "id": "4051c7fc-b429-4804-8d80-8f1f8c24a6f7",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read your organization's branches for network access on your behalf.",
        "userConsentDisplayName": "Read properties of branches for network access",
        "value": "NetworkAccessBranch.Read.All"
    },
    {
        "adminConsentDescription": "Allows the app to upload data files to a data connector on behalf of the signed-in user.",
        "adminConsentDisplayName": "Upload files to a data connector",
        "id": "fc47391d-ab2c-410f-9059-5600f7af660d",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to upload data files to a data connector on your behalf.",
        "userConsentDisplayName": "Upload files to a data connector",
        "value": "IndustryData-DataConnector.Upload"
    },
    {
        "adminConsentDescription": "Allows the app to read, create, and update attack simulation and training data for an organization for the signed-in user.",
        "adminConsentDisplayName": "Read, create, and update attack simulation data of an organization",
        "id": "27608d7c-2c66-4cad-a657-951d575f5a60",
        "isEnabled": True,
        "type": "User",
        "userConsentDescription": "Allows the app to read, create, and update attack simulation and training data for an organization on your behalf.",
        "userConsentDisplayName": "Read, create, and update attack simulation data of an organization",
        "value": "AttackSimulation.ReadWrite.All"
    },
    {
        "adminConsentDescription": "Allows the app to read threat intelligence information, such as indicators, observations, and articles, on behalf of the signed-in user.",
        "adminConsentDisplayName": "Read all threat intelligence information",
        "id": "f266d9c0-ccb9-4fb8-a228-01ac0d8d6627",
        "isEnabled": True,
        "type": "Admin",
        "userConsentDescription": "Allows the app to read threat intelligence information, such as indicators, observations, and articles, on your behalf.",
        "userConsentDisplayName": "Read threat intelligence Information",
        "value": "ThreatIntelligence.Read.All"
    }
]