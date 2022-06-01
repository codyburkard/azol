graph_permission_map = {
    "0121dc95-1b9f-4aed-8bac-58c5ac466691": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Add and remove members from all teams, without a signed-in user. Also allows changing a team member's role, for example from owner to non-owner.",
        "displayName": "Add and remove members from all teams",
        "id": "0121dc95-1b9f-4aed-8bac-58c5ac466691",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamMember.ReadWrite.All"
    },
    "01c0a623-fc9b-48e9-b794-0756f8e8f067": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's conditional access policies, without a signed-in user.",
        "displayName": "Read and write your organization's conditional access policies",
        "id": "01c0a623-fc9b-48e9-b794-0756f8e8f067",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.ConditionalAccess"
    },
    "01d4889c-1287-42c6-ac1f-5d1e02578ef6": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all files in all site collections without a signed in user.",
        "displayName": "Read files in all site collections",
        "id": "01d4889c-1287-42c6-ac1f-5d1e02578ef6",
        "isEnabled": True,
        "origin": "Application",
        "value": "Files.Read.All"
    },
    "01e37dc9-c035-40bd-b438-b2879c4870a6": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD groups in your organization, without a signed-in user.",
        "displayName": "Read privileged access to Azure AD groups",
        "id": "01e37dc9-c035-40bd-b438-b2879c4870a6",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedAccess.Read.AzureADGroup"
    },
    "025d3225-3f02-4882-b4c0-cd5b541a4e80": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and manage the role-based access control (RBAC) settings for your organization's Exchange Online service, without a signed-in user. This includes reading, creating, updating, and deleting Exchange management role definitions, role groups, role group membership, role assignments, management scopes, and role assignment policies.",
        "displayName": "Read and write Exchange Online RBAC configuration",
        "id": "025d3225-3f02-4882-b4c0-cd5b541a4e80",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagement.ReadWrite.Exchange"
    },
    "031a549a-bb80-49b6-8032-2068448c6a3c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the Cloud PC role-based access control (RBAC) settings, without a signed-in user.",
        "displayName": "Read Cloud PC RBAC settings",
        "id": "031a549a-bb80-49b6-8032-2068448c6a3c",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagement.Read.CloudPC"
    },
    "03cc4f92-788e-4ede-b93f-199424d144a5": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and update the organization's external identities policy without a signed-in user.  For example, external identities policy controls if users invited to access resources in your organization via B2B collaboration or B2B direct connect are allowed to self-service leave.",
        "displayName": "Read and write your organization's external identities policy",
        "id": "03cc4f92-788e-4ede-b93f-199424d144a5",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.ExternalIdentities"
    },
    "04c55753-2244-4c25-87fc-704ab82a4f69": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read email metadata and security detection details, and execute remediation actions like deleting an email, without a signed-in user.",
        "displayName": "Read metadata, detection details, and execute remediation actions on all emails in your organization",
        "id": "04c55753-2244-4c25-87fc-704ab82a4f69",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityAnalyzedMessage.ReadWrite.All"
    },
    "0591bafd-7c1c-4c30-a2a5-2b9aacb1dfe8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allow the app to read the management data for Teams devices, without a signed-in user.",
        "displayName": "Read Teams devices",
        "id": "0591bafd-7c1c-4c30-a2a5-2b9aacb1dfe8",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamworkDevice.Read.All"
    },
    "06a5fe6d-c49d-46a7-b082-56b1b14103c7": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read Microsoft Intune service properties including device enrollment and third party service connection configuration, without a signed-in user.",
        "displayName": "Read Microsoft Intune configuration",
        "id": "06a5fe6d-c49d-46a7-b082-56b1b14103c7",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementServiceConfig.Read.All"
    },
    "06b708a9-e830-4db3-a914-8e69da51d44f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to manage permission grants for application permissions to any API (including Microsoft Graph) and application assignments for any app, without a signed-in user.",
        "displayName": "Manage app permission grants and app role assignments",
        "id": "06b708a9-e830-4db3-a914-8e69da51d44f",
        "isEnabled": True,
        "origin": "Application",
        "value": "AppRoleAssignment.ReadWrite.All"
    },
    "089fe4d0-434a-44c5-8827-41ba8a0b17f5": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all contacts in all mailboxes without a signed-in user.",
        "displayName": "Read contacts in all mailboxes",
        "id": "089fe4d0-434a-44c5-8827-41ba8a0b17f5",
        "isEnabled": True,
        "origin": "Application",
        "value": "Contacts.Read"
    },
    "09850681-111b-4a89-9bed-3f2cae46d706": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to invite guest users to the organization, without a signed-in user.",
        "displayName": "Invite guest users to the organization",
        "id": "09850681-111b-4a89-9bed-3f2cae46d706",
        "isEnabled": True,
        "origin": "Application",
        "value": "User.Invite.All"
    },
    "0b57845e-aa49-4e6f-8109-ce654fffa618": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, view, update and delete on-premises published resources, on-premises agents and agent groups, as part of a hybrid identity configuration, without a signed in user.",
        "displayName": "Manage on-premises published resources",
        "id": "0b57845e-aa49-4e6f-8109-ce654fffa618",
        "isEnabled": True,
        "origin": "Application",
        "value": "OnPremisesPublishingProfiles.ReadWrite.All"
    },
    "0c0bf378-bf22-4481-8f81-9e89a9b4960a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create or delete document libraries and lists in all site collections without a signed in user.",
        "displayName": "Create, edit, and delete items and lists in all site collections",
        "id": "0c0bf378-bf22-4481-8f81-9e89a9b4960a",
        "isEnabled": True,
        "origin": "Application",
        "value": "Sites.Manage.All"
    },
    "0c458cef-11f3-48c2-a568-c66751c238c0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all the OneNote notebooks in your organization, without a signed-in user.",
        "displayName": "Read and write all OneNote notebooks",
        "id": "0c458cef-11f3-48c2-a568-c66751c238c0",
        "isEnabled": True,
        "origin": "Application",
        "value": "Notes.ReadWrite.All"
    },
    "0c7d31ec-31ca-4f58-b6ec-9950b6b0de69": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all the short notes without a signed-in user.",
        "displayName": "Read all users' short notes",
        "id": "0c7d31ec-31ca-4f58-b6ec-9950b6b0de69",
        "isEnabled": True,
        "origin": "Application",
        "value": "ShortNotes.Read.All"
    },
    "0d22204b-6cad-4dd0-8362-3e3f2ae699d9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update and delete all\u00a0class assignments with grades for all users without a signed-in user.",
        "displayName": "Create, read, update and delete all\u00a0class assignments with grades",
        "id": "0d22204b-6cad-4dd0-8362-3e3f2ae699d9",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduAssignments.ReadWrite.All"
    },
    "0d412a8c-a06c-439f-b3ec-8abcf54d2f96": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read a limited subset of properties from both the structure of schools and classes in the organization's roster and education-specific information about all users. Includes name, status, role, email address and photo.",
        "displayName": "Read a limited subset of the organization's roster",
        "id": "0d412a8c-a06c-439f-b3ec-8abcf54d2f96",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduRoster.ReadBasic.All"
    },
    "0e778b85-fefa-466d-9eec-750569d92122": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write search configurations, without a signed-in user.",
        "displayName": "Read and write your organization's search configuration",
        "id": "0e778b85-fefa-466d-9eec-750569d92122",
        "isEnabled": True,
        "origin": "Application",
        "value": "SearchConfiguration.ReadWrite.All"
    },
    "0e9eea12-4f01-45f6-9b8d-3ea4c8144158": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and update all Azure AD recommendations, without a signed-in user. ",
        "displayName": "Read and update all Azure AD recommendations",
        "id": "0e9eea12-4f01-45f6-9b8d-3ea4c8144158",
        "isEnabled": True,
        "origin": "Application",
        "value": "DirectoryRecommendations.ReadWrite.All"
    },
    "0edf5e9e-4ce8-468a-8432-d08631d18c43": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read or write your organization's authentication event listeners without a signed-in user.",
        "displayName": "Read and write all authentication event listeners",
        "id": "0edf5e9e-4ce8-468a-8432-d08631d18c43",
        "isEnabled": True,
        "origin": "Application",
        "value": "EventListener.ReadWrite.All"
    },
    "11059518-d6a6-4851-98ed-509268489c4a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and manage all role-based access control (RBAC) alerts for your company's directory, without a signed-in user. This includes managing alert settings, initiating alert scans, dimissing alerts, remediating alert incidents, and reading alert statuses, alert definitions, alert configurations and incidents that lead to an alert.",
        "displayName": "Read all alert data, configure alerts, and take actions on all alerts for your company's directory",
        "id": "11059518-d6a6-4851-98ed-509268489c4a",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagementAlert.ReadWrite.Directory"
    },
    "1138cb37-bd11-4084-a2b7-9f71582aeddb": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write all device properties without a signed in user.  Does not allow device creation, device deletion or update of device alternative security identifiers.",
        "displayName": "Read and write devices",
        "id": "1138cb37-bd11-4084-a2b7-9f71582aeddb",
        "isEnabled": True,
        "origin": "Application",
        "value": "Device.ReadWrite.All"
    },
    "12338004-21f4-4896-bf5e-b75dfaf1016d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write custom security attribute definitions for the tenant without a signed in user.",
        "displayName": "Read and write custom security attribute definitions",
        "id": "12338004-21f4-4896-bf5e-b75dfaf1016d",
        "isEnabled": True,
        "origin": "Application",
        "value": "CustomSecAttributeDefinition.ReadWrite.All"
    },
    "1260ad83-98fb-4785-abbb-d6cc1806fd41": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read consent requests and approvals without a signed-in user.",
        "displayName": "Read all consent requests",
        "id": "1260ad83-98fb-4785-abbb-d6cc1806fd41",
        "isEnabled": True,
        "origin": "Application",
        "value": "ConsentRequest.Read.All"
    },
    "134fd756-38ce-4afd-ba33-e9623dbe66c2": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read administrative units and administrative unit membership without a signed-in user.",
        "displayName": "Read all administrative units",
        "id": "134fd756-38ce-4afd-ba33-e9623dbe66c2",
        "isEnabled": True,
        "origin": "Application",
        "value": "AdministrativeUnit.Read.All"
    },
    "14f49b9f-4bf2-4d24-b80e-b27ec58409bd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all configurations applicable to users for protecting organizational data, without a signed-in user.",
        "displayName": "Read all configurations for protecting organizational data applicable to users",
        "id": "14f49b9f-4bf2-4d24-b80e-b27ec58409bd",
        "isEnabled": True,
        "origin": "Application",
        "value": "InformationProtectionConfig.Read.All"
    },
    "18228521-a591-40f1-b215-5fad4488c117": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, update, delete and perform actions on access reviews, reviewers, decisions and settings in the organization for group and app memberships, without a signed-in user.",
        "displayName": "Manage access reviews for group and app memberships",
        "id": "18228521-a591-40f1-b215-5fad4488c117",
        "isEnabled": True,
        "origin": "Application",
        "value": "AccessReview.ReadWrite.Membership"
    },
    "18a4783c-866b-4cc7-a460-3d5e5662c884": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create other applications, and fully manage those applications (read, update, update application secrets and delete), without a signed-in user. \u00a0It cannot update any apps that it is not an owner of.",
        "displayName": "Manage apps that this app creates or owns",
        "id": "18a4783c-866b-4cc7-a460-3d5e5662c884",
        "isEnabled": True,
        "origin": "Application",
        "value": "Application.ReadWrite.OwnedBy"
    },
    "1914711b-a1cb-4793-b019-c2ce0ed21b8c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all external connections without a signed-in user.",
        "displayName": "Read all external connections",
        "id": "1914711b-a1cb-4793-b019-c2ce0ed21b8c",
        "isEnabled": True,
        "origin": "Application",
        "value": "ExternalConnection.Read.All"
    },
    "197ee4e9-b993-4066-898f-d6aecc55125b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all the indicators for your organization, without a signed-in user.",
        "displayName": "Read all threat indicators",
        "id": "197ee4e9-b993-4066-898f-d6aecc55125b",
        "isEnabled": True,
        "origin": "Application",
        "value": "ThreatIndicators.Read.All"
    },
    "19b94e34-907c-4f43-bde9-38b1909ed408": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and change the tenant-level settings of SharePoint and OneDrive, without a signed-in user.",
        "displayName": "Read and change SharePoint and OneDrive tenant settings",
        "id": "19b94e34-907c-4f43-bde9-38b1909ed408",
        "isEnabled": True,
        "origin": "Application",
        "value": "SharePointTenantSettings.ReadWrite.All"
    },
    "19da66cb-0fb0-4390-b071-ebc76a349482": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read published sensitivity labels and label policy settings for the entire organization or a specific user, without a signed in user.",
        "displayName": "Read all published labels and label policies for an organization.",
        "id": "19da66cb-0fb0-4390-b071-ebc76a349482",
        "isEnabled": True,
        "origin": "Application",
        "value": "InformationProtectionPolicy.Read.All"
    },
    "19dbc75e-c2e2-444c-a770-ec69d8559fc7": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write data in your organization's directory, such as users, and groups, without a signed-in user.  Does not allow user or group deletion.",
        "displayName": "Read and write directory data",
        "id": "19dbc75e-c2e2-444c-a770-ec69d8559fc7",
        "isEnabled": True,
        "origin": "Application",
        "value": "Directory.ReadWrite.All"
    },
    "1b0c317f-dd31-4305-9932-259a8b6e8099": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's user flows, without a signed-in user.",
        "displayName": "Read all identity user flows",
        "id": "1b0c317f-dd31-4305-9932-259a8b6e8099",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityUserFlow.Read.All"
    },
    "1b620472-6534-4fe6-9df2-4680e8aa28ec": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your tenant's service announcement messages, without a signed-in user. Messages may include information about new or changed features.",
        "displayName": "Read service messages",
        "id": "1b620472-6534-4fe6-9df2-4680e8aa28ec",
        "isEnabled": True,
        "origin": "Application",
        "value": "ServiceMessage.Read.All"
    },
    "1bfefb4e-e0b5-418b-a88f-73c46d2cc8e9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update and delete applications and service principals without a signed-in user.  Does not allow management of consent grants.",
        "displayName": "Read and write all applications",
        "id": "1bfefb4e-e0b5-418b-a88f-73c46d2cc8e9",
        "isEnabled": True,
        "origin": "Application",
        "value": "Application.ReadWrite.All"
    },
    "1c1b4c8e-3cc7-4c58-8470-9b92c9d5848b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all one-to-one or group chat messages in Microsoft Teams for chats where the associated Teams application is installed, without a signed-in user.",
        "displayName": "Read all chat messages for chats where the associated Teams application is installed.",
        "id": "1c1b4c8e-3cc7-4c58-8470-9b92c9d5848b",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.Read.WhereInstalled"
    },
    "1c6e93a6-28e2-4cbb-9f64-1a46a821124d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's security defaults policy, without a signed-in user.",
        "displayName": "Read and write your organization's security defaults policy",
        "id": "1c6e93a6-28e2-4cbb-9f64-1a46a821124d",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.SecurityDefaults"
    },
    "1dccb351-c4e4-4e09-a8d1-7a9ecbf027cc": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all virtual events without a signed-in user.",
        "displayName": "Read all users' virtual events",
        "id": "1dccb351-c4e4-4e09-a8d1-7a9ecbf027cc",
        "isEnabled": True,
        "origin": "Application",
        "value": "VirtualEvent.Read.All"
    },
    "1dfe531a-24a6-4f1b-80f4-7a0dc5a0a171": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, create and manage the API connectors used in user authentication flows, without a signed-in user.",
        "displayName": "Read and write API connectors for authentication flows",
        "id": "1dfe531a-24a6-4f1b-80f4-7a0dc5a0a171",
        "isEnabled": True,
        "origin": "Application",
        "value": "APIConnectors.ReadWrite.All"
    },
    "1e4be56c-312e-42b8-a2c9-009600d732c0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall itself for any team, without a signed-in user, and manage its permission grants for accessing those specific teams' data.",
        "displayName": "Allow the Teams app to manage itself and its permission grants for all teams",
        "id": "1e4be56c-312e-42b8-a2c9-009600d732c0",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteAndConsentSelfForTeam.All"
    },
    "1f615aea-6bf9-4b05-84bd-46388e138537": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the Teams apps that are installed in any team, without a signed-in user. Does not give the ability to read application-specific settings.",
        "displayName": "Read installed Teams apps for all teams",
        "id": "1f615aea-6bf9-4b05-84bd-46388e138537",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadForTeam.All"
    },
    "202bf709-e8e6-478e-bcfd-5d63c50b68e3": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to manage workforce integrations to synchronize data from Microsoft Teams Shifts, without a signed-in user.",
        "displayName": "Read and write workforce integrations",
        "id": "202bf709-e8e6-478e-bcfd-5d63c50b68e3",
        "isEnabled": True,
        "origin": "Application",
        "value": "WorkforceIntegration.ReadWrite.All"
    },
    "2044e4f1-e56c-435b-925c-44cd8f6ba89a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write feature rollout policies without a signed-in user. Includes abilities to assign and remove users and groups to rollout of a specific feature.",
        "displayName": "Read and write feature rollout policies",
        "id": "2044e4f1-e56c-435b-925c-44cd8f6ba89a",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.FeatureRollout"
    },
    "214e810f-fda8-4fd7-a475-29461495eb00": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows custom authentication extensions associated with the app to receive HTTP requests triggered by an authentication event. The request can include information about a user, client and resource service principals, and other information about the authentication.",
        "displayName": "Receive custom authentication extension HTTP requests",
        "id": "214e810f-fda8-4fd7-a475-29461495eb00",
        "isEnabled": True,
        "origin": "Application",
        "value": "CustomAuthenticationExtension.Receive.Payload"
    },
    "21792b6c-c986-4ffc-85de-df9da54b52fa": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create threat indicators, and fully manage those threat indicators (read, update and delete), without a signed-in user. \u00a0It cannot update any threat indicators it does not own.",
        "displayName": "Manage threat indicators this app creates or owns",
        "id": "21792b6c-c986-4ffc-85de-df9da54b52fa",
        "isEnabled": True,
        "origin": "Application",
        "value": "ThreatIndicators.ReadWrite.OwnedBy"
    },
    "2280dda6-0bfd-44ee-a2f4-cb867cfc4c1e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Get a list of all teams, without a signed-in user.",
        "displayName": "Get a list of all teams",
        "id": "2280dda6-0bfd-44ee-a2f4-cb867cfc4c1e",
        "isEnabled": True,
        "origin": "Application",
        "value": "Team.ReadBasic.All"
    },
    "230c1aed-a721-4c5d-9cb4-a90514e508ef": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read all service usage reports without a signed-in user.  Services that provide usage reports include Office 365 and Azure Active Directory.",
        "displayName": "Read all usage reports",
        "id": "230c1aed-a721-4c5d-9cb4-a90514e508ef",
        "isEnabled": True,
        "origin": "Application",
        "value": "Reports.Read.All"
    },
    "236c1cbd-1187-427f-b0f5-b1852454973b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, update, read and delete all assignments in the organization's directory, without a signed-in user.",
        "displayName": "Read and write all assignments",
        "id": "236c1cbd-1187-427f-b0f5-b1852454973b",
        "isEnabled": True,
        "origin": "Application",
        "value": "LearningAssignedCourse.ReadWrite.All"
    },
    "23fc2474-f741-46ce-8465-674744c5c361": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create teams without a signed-in user.\u00a0",
        "displayName": "Create teams",
        "id": "23fc2474-f741-46ce-8465-674744c5c361",
        "isEnabled": True,
        "origin": "Application",
        "value": "Team.Create"
    },
    "242607bd-1d2c-432c-82eb-bdb27baa23ab": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read all team's settings, without a signed-in user.",
        "displayName": "Read all teams' settings",
        "id": "242607bd-1d2c-432c-82eb-bdb27baa23ab",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamSettings.Read.All"
    },
    "243333ab-4d21-40cb-a475-36241daa0842": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the properties of devices managed by Microsoft Intune, without a signed-in user. Does not allow high impact operations such as remote wipe and password reset on the device\u2019s owner",
        "displayName": "Read and write Microsoft Intune devices",
        "id": "243333ab-4d21-40cb-a475-36241daa0842",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementManagedDevices.ReadWrite.All"
    },
    "243cded2-bd16-4fd6-a953-ff8177894c3d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read and write the names, descriptions, and settings of all channels, without a signed-in user.",
        "displayName": "Read and write the names, descriptions, and settings of all channels",
        "id": "243cded2-bd16-4fd6-a953-ff8177894c3d",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChannelSettings.ReadWrite.All"
    },
    "246dd0d5-5bd0-4def-940b-0421030a5b68": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all your organization's policies without a signed in user.",
        "displayName": "Read your organization's policies",
        "id": "246dd0d5-5bd0-4def-940b-0421030a5b68",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.Read.All"
    },
    "25f85f3c-f66c-4205-8cd5-de92dd7f0cec": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write all authentication flow policies for the tenant, without a signed-in user.",
        "displayName": "Read and write authentication flow policies",
        "id": "25f85f3c-f66c-4205-8cd5-de92dd7f0cec",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.AuthenticationFlows"
    },
    "274d0592-d1b6-44bd-af1d-26d259bcb43a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and manage the Cloud PC role-based access control (RBAC) settings, without a signed-in user. This includes reading and managing Cloud PC role definitions and memberships.",
        "displayName": "Read and write all Cloud PC RBAC settings",
        "id": "274d0592-d1b6-44bd-af1d-26d259bcb43a",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagement.ReadWrite.CloudPC"
    },
    "284383ee-7f6e-4e40-a2a8-e85dcb029101": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to place outbound calls to a single user and transfer calls to users in your organization\u2019s directory, without a signed-in user.",
        "displayName": "Initiate outgoing 1 to 1 calls from the app",
        "id": "284383ee-7f6e-4e40-a2a8-e85dcb029101",
        "isEnabled": True,
        "origin": "Application",
        "value": "Calls.Initiate.All"
    },
    "287bd98c-e865-4e8c-bade-1a85523195b9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create protected content without a signed-in user. ",
        "displayName": "Create protected content",
        "id": "287bd98c-e865-4e8c-bade-1a85523195b9",
        "isEnabled": True,
        "origin": "Application",
        "value": "InformationProtectionContent.Write.All"
    },
    "292d869f-3427-49a8-9dab-8c70152b74e9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the organization and related resources, without a signed-in user.\u00a0Related resources include things like subscribed skus and tenant branding information.",
        "displayName": "Read and write organization information",
        "id": "292d869f-3427-49a8-9dab-8c70152b74e9",
        "isEnabled": True,
        "origin": "Application",
        "value": "Organization.ReadWrite.All"
    },
    "294ce7c9-31ba-490a-ad7d-97a7d075e4ed": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read and write all chat messages in Microsoft Teams, without a signed-in user.",
        "displayName": "Read and write all chat messages",
        "id": "294ce7c9-31ba-490a-ad7d-97a7d075e4ed",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.ReadWrite.All"
    },
    "29c18626-4985-4dcd-85c0-193eef327366": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write all authentication method policies for the tenant, without a signed-in user.\u00a0",
        "displayName": "Read and write all authentication method policies\u00a0",
        "id": "29c18626-4985-4dcd-85c0-193eef327366",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.AuthenticationMethod"
    },
    "2a60023f-3219-47ad-baa4-40e17cd02a1d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and update all admin report settings, such as whether to display concealed information in reports, without a signed-in user.",
        "displayName": "Read and write all admin report settings",
        "id": "2a60023f-3219-47ad-baa4-40e17cd02a1d",
        "isEnabled": True,
        "origin": "Application",
        "value": "ReportSettings.ReadWrite.All"
    },
    "2f3e6f8c-093b-4c57-a58b-ba5ce494a169": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read terms of use agreements, without a signed in user.",
        "displayName": "Read all terms of use agreements",
        "id": "2f3e6f8c-093b-4c57-a58b-ba5ce494a169",
        "isEnabled": True,
        "origin": "Application",
        "value": "Agreement.Read.All"
    },
    "2f51be20-0bb4-4fed-bf7b-db946066c75e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the properties of devices managed by Microsoft Intune, without a signed-in user.",
        "displayName": "Read Microsoft Intune devices",
        "id": "2f51be20-0bb4-4fed-bf7b-db946066c75e",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementManagedDevices.Read.All"
    },
    "2f6817f8-7b12-4f0f-bc18-eeaf60705a9e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to request and manage time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD groups in your organization, without a signed-in user.",
        "displayName": "Read and write privileged access to Azure AD groups",
        "id": "2f6817f8-7b12-4f0f-bc18-eeaf60705a9e",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedAccess.ReadWrite.AzureADGroup"
    },
    "3011c876-62b7-4ada-afa2-506cbbecc68c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to enable and disable users' accounts, without a signed-in user.",
        "displayName": "Enable and disable user accounts",
        "id": "3011c876-62b7-4ada-afa2-506cbbecc68c",
        "isEnabled": True,
        "origin": "Application",
        "value": "User.EnableDisableAccount.All"
    },
    "305f6ba2-049a-4b1b-88bb-fe7e08758a00": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read inbound data flows without a signed-in user.",
        "displayName": "View inbound flow definitions",
        "id": "305f6ba2-049a-4b1b-88bb-fe7e08758a00",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-InboundFlow.Read.All"
    },
    "306785c5-c09b-4ba0-a4ee-023f3da165cb": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to list and query any shared user profile information associated with the current tenant without a signed-in user.\u00a0 It also permits the application to export and remove external user data (e.g. customer content or system-generated logs), for any user associated with the current tenant without a signed-in user.",
        "displayName": "Read all shared cross-tenant user profiles and export or delete their data",
        "id": "306785c5-c09b-4ba0-a4ee-023f3da165cb",
        "isEnabled": True,
        "origin": "Application",
        "value": "CrossTenantUserProfileSharing.ReadWrite.All"
    },
    "31e08e0a-d3f7-4ca2-ac39-7343fb83e8ad": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, update, and delete policies for privileged role-based access control (RBAC) assignments of your company's directory, without a signed-in user.",
        "displayName": "Read, update, and delete all policies for privileged role assignments of your company's directory",
        "id": "31e08e0a-d3f7-4ca2-ac39-7343fb83e8ad",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagementPolicy.ReadWrite.Directory"
    },
    "332a536c-c7ef-4017-ab91-336970924f0d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read documents and list items in all site collections without a signed in user.",
        "displayName": "Read items in all site collections ",
        "id": "332a536c-c7ef-4017-ab91-336970924f0d",
        "isEnabled": True,
        "origin": "Application",
        "value": "Sites.Read.All"
    },
    "338163d7-f101-4c92-94ba-ca46fe52447c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's cross tenant access policies without a signed-in user.",
        "displayName": "Read and write your organization's cross tenant access policies",
        "id": "338163d7-f101-4c92-94ba-ca46fe52447c",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.CrossTenantAccess"
    },
    "34bf0e97-1971-4929-b999-9e2442d941d7": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write to all security incidents, without a signed-in user.",
        "displayName": "Read and write to all security incidents",
        "id": "34bf0e97-1971-4929-b999-9e2442d941d7",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityIncident.ReadWrite.All"
    },
    "34c37bc0-2b40-4d5e-85e1-2365cd256d79": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write all external connections without a signed-in user.",
        "displayName": "Read and write all external connections",
        "id": "34c37bc0-2b40-4d5e-85e1-2365cd256d79",
        "isEnabled": True,
        "origin": "Application",
        "value": "ExternalConnection.ReadWrite.All"
    },
    "35930dcf-aceb-4bd1-b99a-8ffed403c974": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Add and remove members from all channels, without a signed-in user. Also allows changing a member's role, for example from owner to non-owner.",
        "displayName": "Add and remove members from all channels",
        "id": "35930dcf-aceb-4bd1-b99a-8ffed403c974",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChannelMember.ReadWrite.All"
    },
    "37730810-e9ba-4e46-b07e-8ca78d182097": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's conditional access policies, without a signed-in user.",
        "displayName": "Read your organization's conditional access policies",
        "id": "37730810-e9ba-4e46-b07e-8ca78d182097",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.Read.ConditionalAccess"
    },
    "381f742f-e1f8-4309-b4ab-e3d91ae4c5c1": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the authentication context information in your organization without a signed-in user.",
        "displayName": "Read all authentication context information",
        "id": "381f742f-e1f8-4309-b4ab-e3d91ae4c5c1",
        "isEnabled": True,
        "origin": "Application",
        "value": "AuthenticationContext.Read.All"
    },
    "38c3d6ee-69ee-422f-b954-e17819665354": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allow the app to read or write items in all external datasets that the app is authorized to access",
        "displayName": "Read and write items in external datasets",
        "id": "38c3d6ee-69ee-422f-b954-e17819665354",
        "isEnabled": True,
        "origin": "Application",
        "value": "ExternalItem.ReadWrite.All"
    },
    "38d9df27-64da-44fd-b7c5-a6fbac20248f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": " Allows the app to read authentication methods of all users in your organization, without a signed-in user.                       Authentication methods include things like a user\u2019s phone numbers and Authenticator app settings. This does not allow the                      app to see secret information like passwords, or to sign-in or otherwise use the authentication methods.",
        "displayName": " Read all users' authentication methods",
        "id": "38d9df27-64da-44fd-b7c5-a6fbac20248f",
        "isEnabled": True,
        "origin": "Application",
        "value": "UserAuthenticationMethod.Read.All"
    },
    "39ae4a24-1ef0-49e8-9d63-2a66f5c39edd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's network access braches, without a signed-in user.",
        "displayName": "Read properties of all branches for network access",
        "id": "39ae4a24-1ef0-49e8-9d63-2a66f5c39edd",
        "isEnabled": True,
        "origin": "Application",
        "value": "NetworkAccessBranch.Read.All"
    },
    "3aeca27b-ee3a-4c2b-8ded-80376e2134a4": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all the OneNote notebooks in your organization, without a signed-in user.",
        "displayName": "Read all OneNote notebooks",
        "id": "3aeca27b-ee3a-4c2b-8ded-80376e2134a4",
        "isEnabled": True,
        "origin": "Application",
        "value": "Notes.Read.All"
    },
    "3b37c5a4-1226-493d-bec3-5d6c6b866f3f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read custom security attribute assignments for all principals in the tenant without a signed in user.",
        "displayName": "Read custom security attribute assignments",
        "id": "3b37c5a4-1226-493d-bec3-5d6c6b866f3f",
        "isEnabled": True,
        "origin": "Application",
        "value": "CustomSecAttributeAssignment.Read.All"
    },
    "3b4349e1-8cf5-45a3-95b7-69d1751d3e6a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the properties of Cloud PCs, without a signed-in user.",
        "displayName": "Read and write Cloud PCs",
        "id": "3b4349e1-8cf5-45a3-95b7-69d1751d3e6a",
        "isEnabled": True,
        "origin": "Application",
        "value": "CloudPC.ReadWrite.All"
    },
    "3b55498e-47ec-484f-8136-9013221c06a9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read the members of all channels, without a signed-in user.",
        "displayName": "Read the members of all channels",
        "id": "3b55498e-47ec-484f-8136-9013221c06a9",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChannelMember.Read.All"
    },
    "3be0012a-cc4e-426b-895b-f9c836bf6381": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the remote desktop security configuration for all apps in your organization, without a signed-in user.",
        "displayName": "Read and write the remote desktop security configuration for all apps",
        "id": "3be0012a-cc4e-426b-895b-f9c836bf6381",
        "isEnabled": True,
        "origin": "Application",
        "value": "Application-RemoteDesktopConfig.ReadWrite.All"
    },
    "3c42dec6-49e8-4a0a-b469-36cff0d9da93": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs for any user, without a signed-in user.",
        "displayName": "Allow the Teams app to manage only its own tabs for all users",
        "id": "3c42dec6-49e8-4a0a-b469-36cff0d9da93",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.ReadWriteSelfForUser.All"
    },
    "405a51b5-8d8d-430b-9842-8be4b0e9f324": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to export data (e.g. customer content or system-generated logs), associated with any user in your company, when the app is used by a privileged user (e.g. a Company Administrator).",
        "displayName": "Export user's data",
        "id": "405a51b5-8d8d-430b-9842-8be4b0e9f324",
        "isEnabled": True,
        "origin": "Application",
        "value": "User.Export.All"
    },
    "40f97065-369a-49f4-947c-6a255697ae91": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read user's mailbox settings without a signed-in user. Does not include permission to send mail.",
        "displayName": "Read all user mailbox settings",
        "id": "40f97065-369a-49f4-947c-6a255697ae91",
        "isEnabled": True,
        "origin": "Application",
        "value": "MailboxSettings.Read"
    },
    "41202f2c-f7ab-45be-b001-85c9728b9d69": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, create, and delete time-based assignment schedules for access to Azure AD groups, without a signed-in user.",
        "displayName": "Read, create, and delete assignment schedules for access to Azure AD groups",
        "id": "41202f2c-f7ab-45be-b001-85c9728b9d69",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup"
    },
    "425b4b59-d5af-45c8-832f-bb0b7402348a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall all tabs for any user, without a signed-in user.",
        "displayName": "Allow the app to manage all tabs for all users",
        "id": "425b4b59-d5af-45c8-832f-bb0b7402348a",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.ReadWriteForUser.All"
    },
    "4437522e-9a86-4a41-a7da-e380edd4a97d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Add and remove members from all teams, without a signed-in user. Does not allow adding or removing a member with the owner role. Additionally, does not allow the app to elevate an existing member to the owner role.",
        "displayName": "Add and remove members with non-owner role for all teams",
        "id": "4437522e-9a86-4a41-a7da-e380edd4a97d",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamMember.ReadWriteNonOwnerRole.All"
    },
    "444d6fcb-b738-41e5-b103-ac4f2a2628a3": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows\u00a0the\u00a0app\u00a0to\u00a0manage all learning\u00a0content\u00a0in\u00a0the\u00a0organization's\u00a0directory, without a signed-in user.",
        "displayName": "Manage all\u00a0learning\u00a0content",
        "id": "444d6fcb-b738-41e5-b103-ac4f2a2628a3",
        "isEnabled": True,
        "origin": "Application",
        "value": "LearningContent.ReadWrite.All"
    },
    "44e666d1-d276-445b-a5fc-8815eeb81d55": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update and delete all users\u2019 tasks and task lists in your organization, without a signed-in user",
        "displayName": "Read and write all users\u2019 tasks and tasklists",
        "id": "44e666d1-d276-445b-a5fc-8815eeb81d55",
        "isEnabled": True,
        "origin": "Application",
        "value": "Tasks.ReadWrite.All"
    },
    "456b71a7-0ee0-4588-9842-c123fcc8f664": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and update print task definitions without a signed-in user.\u00a0",
        "displayName": "Read, write and update print task definitions",
        "id": "456b71a7-0ee0-4588-9842-c123fcc8f664",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrintTaskDefinition.ReadWrite.All"
    },
    "45bbb07e-7321-4fd7-a8f6-3ff27e6a81c8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read call records for all calls and online meetings without a signed-in user.",
        "displayName": "Read all call records",
        "id": "45bbb07e-7321-4fd7-a8f6-3ff27e6a81c8",
        "isEnabled": True,
        "origin": "Application",
        "value": "CallRecords.Read.All"
    },
    "45cc0394-e837-488b-a098-1918f48d186c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all security incidents, without a signed-in user.",
        "displayName": "Read all security incidents",
        "id": "45cc0394-e837-488b-a098-1918f48d186c",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityIncident.Read.All"
    },
    "467524fc-ed22-4356-a910-af61191e3503": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read data for all self-initiated courses in the organization's directory, without a signed-in user.",
        "displayName": "Read all self-initiated courses",
        "id": "467524fc-ed22-4356-a910-af61191e3503",
        "isEnabled": True,
        "origin": "Application",
        "value": "LearningSelfInitiatedCourse.Read.All"
    },
    "46890524-499a-4bb2-ad64-1476b4f3e1cf": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read the names and settings of tabs inside any team in Microsoft Teams, without a signed-in user. This does not give access to the content inside the tabs. ",
        "displayName": "Read tabs in Microsoft Teams.",
        "id": "46890524-499a-4bb2-ad64-1476b4f3e1cf",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.Read.All"
    },
    "472e4a4d-bb4a-4026-98d1-0b0d74cb74a5": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all security alerts, without a signed-in user.",
        "displayName": "Read all security alerts",
        "id": "472e4a4d-bb4a-4026-98d1-0b0d74cb74a5",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityAlert.Read.All"
    },
    "475ebe88-f071-4bd7-af2b-642952bd4986": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the Teams app settings without a signed-in user.",
        "displayName": "Read Teams app settings",
        "id": "475ebe88-f071-4bd7-af2b-642952bd4986",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamworkAppSettings.Read.All"
    },
    "483bed4a-2ad3-4361-a73b-c83ccdbdc53c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the role-based access control (RBAC) settings for your company's directory, without a signed-in user.  This includes reading directory role templates, directory roles and memberships.",
        "displayName": "Read all directory RBAC settings",
        "id": "483bed4a-2ad3-4361-a73b-c83ccdbdc53c",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagement.Read.Directory"
    },
    "498476ce-e0fe-48b0-b801-37ba7e2685c6": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the organization and related resources, without a signed-in user.\u00a0Related resources include things like subscribed skus and tenant branding information.",
        "displayName": "Read organization information",
        "id": "498476ce-e0fe-48b0-b801-37ba7e2685c6",
        "isEnabled": True,
        "origin": "Application",
        "value": "Organization.Read.All"
    },
    "49981c42-fd7b-4530-be03-e77b21aed25e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create tabs in any team in Microsoft Teams, without a signed-in user. This does not grant the ability to read, modify or delete tabs after they are created, or give access to the content inside the tabs.",
        "displayName": "Create tabs in Microsoft Teams.",
        "id": "49981c42-fd7b-4530-be03-e77b21aed25e",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.Create"
    },
    "4a771c9a-1cf2-4609-b88e-3d3e02d539cd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write trust framework key set properties without a signed-in user.",
        "displayName": "Read and write trust framework key sets",
        "id": "4a771c9a-1cf2-4609-b88e-3d3e02d539cd",
        "isEnabled": True,
        "origin": "Application",
        "value": "TrustFrameworkKeySet.ReadWrite.All"
    },
    "4c277553-8a09-487b-8023-29ee378d8324": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to place outbound calls to multiple users and add participants to meetings in your organization, without a signed-in user.",
        "displayName": "Initiate outgoing group calls from the app",
        "id": "4c277553-8a09-487b-8023-29ee378d8324",
        "isEnabled": True,
        "origin": "Application",
        "value": "Calls.InitiateGroupCall.All"
    },
    "4c37e1b6-35a1-43bf-926a-6f30f2cdf585": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all\u00a0class assignments with grades for all users without a signed-in user.",
        "displayName": "Read all class assignments with grades",
        "id": "4c37e1b6-35a1-43bf-926a-6f30f2cdf585",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduAssignments.Read.All"
    },
    "4cdc2547-9148-4295-8d11-be0db1391d6b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD built-in and custom administrative roles in your organization, without a signed-in user.",
        "displayName": "Read privileged access to Azure AD roles",
        "id": "4cdc2547-9148-4295-8d11-be0db1391d6b",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedAccess.Read.AzureAD"
    },
    "4d02b0cc-d90b-441f-8d82-4fb55c34d6bb": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to update Microsoft Teams channel messages by patching a set of Data Loss Prevention (DLP) policy violation properties to handle the output of DLP processing.",
        "displayName": "Flag channel messages for violating policy",
        "id": "4d02b0cc-d90b-441f-8d82-4fb55c34d6bb",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChannelMessage.UpdatePolicyViolation.All"
    },
    "4e774092-a092-48d1-90bd-baad67c7eb47": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to send, read, update and delete user\u2019s notifications, without a signed-in user.",
        "displayName": "Deliver and manage all user's notifications",
        "id": "4e774092-a092-48d1-90bd-baad67c7eb47",
        "isEnabled": True,
        "origin": "Application",
        "value": "UserNotification.ReadWrite.CreatedByApp"
    },
    "4f5ac95f-62fd-472c-b60f-125d24ca0bc5": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read basic service and resource information without a signed-in user.",
        "displayName": "View basic service and resource information",
        "id": "4f5ac95f-62fd-472c-b60f-125d24ca0bc5",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData.ReadBasic.All"
    },
    "50180013-6191-4d1e-a373-e590ff4e66af": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read eDiscovery objects such as cases, custodians, review sets and other related objects without a signed-in user.",
        "displayName": "Read all eDiscovery objects",
        "id": "50180013-6191-4d1e-a373-e590ff4e66af",
        "isEnabled": True,
        "origin": "Application",
        "value": "eDiscovery.Read.All"
    },
    "50483e42-d915-4231-9639-7fdb7fd190e5": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and write authentication methods of all users in your organization, without a signed-in user.                       Authentication methods include things like a user\u2019s phone numbers and Authenticator app settings. This                      does not allow the app to see secret information like passwords, or to sign-in or otherwise use the authentication methods",
        "displayName": "Read and write all users' authentication methods ",
        "id": "50483e42-d915-4231-9639-7fdb7fd190e5",
        "isEnabled": True,
        "origin": "Application",
        "value": "UserAuthenticationMethod.ReadWrite.All"
    },
    "5114b07b-2898-4de7-a541-53b0004e2e13": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and update the metadata and document content of print jobs without a signed-in user.",
        "displayName": "Read and write print jobs",
        "id": "5114b07b-2898-4de7-a541-53b0004e2e13",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrintJob.ReadWrite.All"
    },
    "5256681e-b7f6-40c0-8447-2d9db68797a0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read service principal endpoints",
        "displayName": "Read service principal endpoints",
        "id": "5256681e-b7f6-40c0-8447-2d9db68797a0",
        "isEnabled": True,
        "origin": "Application",
        "value": "ServicePrincipalEndpoint.Read.All"
    },
    "535e6066-2894-49ef-ab33-e2c6d064bb81": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read data for all assignments in the organization's directory, without a signed-in user.",
        "displayName": "Read all assignments",
        "id": "535e6066-2894-49ef-ab33-e2c6d064bb81",
        "isEnabled": True,
        "origin": "Application",
        "value": "LearningAssignedCourse.Read.All"
    },
    "57257249-34ce-4810-a8a2-a03adf0c5693": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Add and remove members from all chats, without a signed-in user.",
        "displayName": "Add and remove members from all chats",
        "id": "57257249-34ce-4810-a8a2-a03adf0c5693",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChatMember.ReadWrite.All"
    },
    "57878358-37f4-4d3a-8c20-4816e0d457b1": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and update the metadata of print jobs without a signed-in user.\u00a0Does not allow access to print job document content.",
        "displayName": "Read and write basic information for print jobs",
        "id": "57878358-37f4-4d3a-8c20-4816e0d457b1",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrintJob.ReadWriteBasic.All"
    },
    "58a52f47-9e36-4b17-9ebe-ce4ef7f3e6c8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to perform advanced operations like redirecting a print job to another printer without a signed-in user. Also allows the application to read and update the metadata of print jobs.",
        "displayName": "Perform advanced operations on print jobs",
        "id": "58a52f47-9e36-4b17-9ebe-ce4ef7f3e6c8",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrintJob.Manage.All"
    },
    "58ca0d9a-1575-47e1-a3cb-007ef2e4583b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the properties relating to the Microsoft Intune Role-Based Access Control (RBAC) settings, without a signed-in user.",
        "displayName": "Read Microsoft Intune RBAC settings",
        "id": "58ca0d9a-1575-47e1-a3cb-007ef2e4583b",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementRBAC.Read.All"
    },
    "59a6b24b-4225-4393-8165-ebaec5f55d7a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read all channel names and channel descriptions, without a signed-in user.",
        "displayName": "Read the names and descriptions  of all channels",
        "id": "59a6b24b-4225-4393-8165-ebaec5f55d7a",
        "isEnabled": True,
        "origin": "Application",
        "value": "Channel.ReadBasic.All"
    },
    "5ac13192-7ace-4fcf-b828-1a26f28068ee": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write Microsoft Intune service properties including device enrollment and third party service connection configuration, without a signed-in user.",
        "displayName": "Read and write Microsoft Intune configuration",
        "id": "5ac13192-7ace-4fcf-b828-1a26f28068ee",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementServiceConfig.ReadWrite.All"
    },
    "5b07b0dd-2377-4e44-a38d-703f09a0dc3c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to perform remote high impact actions such as wiping the device or resetting the passcode on devices managed by Microsoft Intune, without a signed-in user.",
        "displayName": "Perform user-impacting remote actions on Microsoft Intune devices",
        "id": "5b07b0dd-2377-4e44-a38d-703f09a0dc3c",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementManagedDevices.PrivilegedOperations.All"
    },
    "5b567255-7703-4780-807c-7be8301ae99b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read group properties and memberships, and read\u00a0conversations for all groups, without a signed-in user.",
        "displayName": "Read all groups",
        "id": "5b567255-7703-4780-807c-7be8301ae99b",
        "isEnabled": True,
        "origin": "Application",
        "value": "Group.Read.All"
    },
    "5ba43d2f-fa88-4db2-bd1c-a67c5f0fb1ce": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read Azure AD synchronization information, without a signed-in user.",
        "displayName": "Read all Azure AD synchronization data. ",
        "id": "5ba43d2f-fa88-4db2-bd1c-a67c5f0fb1ce",
        "isEnabled": True,
        "origin": "Application",
        "value": "Synchronization.Read.All"
    },
    "5c505cf4-8424-4b8e-aa14-ee06e3bb23e3": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, update, list, read and delete all workflows, tasks and related lifecycle workflows resources without a signed-in user.",
        "displayName": "Read and write all lifecycle workflows resources",
        "id": "5c505cf4-8424-4b8e-aa14-ee06e3bb23e3",
        "isEnabled": True,
        "origin": "Application",
        "value": "LifecycleWorkflows.ReadWrite.All"
    },
    "5dad17ba-f6cc-4954-a5a2-a0dcc95154f0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, install, upgrade, and uninstall Teams apps in any team, without a signed-in user. Does not give the ability to read application-specific settings.",
        "displayName": "Manage Teams apps for all teams",
        "id": "5dad17ba-f6cc-4954-a5a2-a0dcc95154f0",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteForTeam.All"
    },
    "5df6fe86-1be0-44eb-b916-7bd443a71236": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read time-based assignment and just-in-time elevation of user privileges to audit Azure resources in your organization, without a signed-in user.",
        "displayName": "Read privileged access to Azure resources",
        "id": "5df6fe86-1be0-44eb-b916-7bd443a71236",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedAccess.Read.AzureResources"
    },
    "5e0edab9-c148-49d0-b423-ac253e121825": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read security actions, without a signed-in user.",
        "displayName": "Read your organization's security actions",
        "id": "5e0edab9-c148-49d0-b423-ac253e121825",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityActions.Read.All"
    },
    "5eb59dd3-1da2-4329-8733-9dabdc435916": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update, and delete administrative units and manage administrative unit membership without a signed-in user.",
        "displayName": "Read and write all administrative units",
        "id": "5eb59dd3-1da2-4329-8733-9dabdc435916",
        "isEnabled": True,
        "origin": "Application",
        "value": "AdministrativeUnit.ReadWrite.All"
    },
    "5facf0c1-8979-4e95-abcf-ff3d079771c0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to manage license assignments for users and groups, without a signed-in user.",
        "displayName": "Manage all license assignments",
        "id": "5facf0c1-8979-4e95-abcf-ff3d079771c0",
        "isEnabled": True,
        "origin": "Application",
        "value": "LicenseAssignment.ReadWrite.All"
    },
    "607c7344-0eed-41e5-823a-9695ebe1b7b0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all risky service principal information for your organization, without a signed-in user.",
        "displayName": "Read all identity risky service principal information",
        "id": "607c7344-0eed-41e5-823a-9695ebe1b7b0",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityRiskyServicePrincipal.Read.All"
    },
    "60a901ed-09f7-4aa5-a16e-7dd3d6f9de36": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, update, delete and perform actions on programs and program controls in the organization, without a signed-in user.",
        "displayName": "Manage all programs",
        "id": "60a901ed-09f7-4aa5-a16e-7dd3d6f9de36",
        "isEnabled": True,
        "origin": "Application",
        "value": "ProgramControl.ReadWrite.All"
    },
    "6163d4f4-fbf8-43da-a7b4-060fe85ed148": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall all tabs in any team, without a signed-in user.",
        "displayName": "Allow the Teams app to manage all tabs for all teams",
        "id": "6163d4f4-fbf8-43da-a7b4-060fe85ed148",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.ReadWriteForTeam.All"
    },
    "618b6020-bca8-4de6-99f6-ef445fa4d857": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, create, and delete time-based eligibility schedules for access to Azure AD groups, without a signed-in user.",
        "displayName": "Read, create, and delete eligibility schedules for access to Azure AD groups",
        "id": "618b6020-bca8-4de6-99f6-ef445fa4d857",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup"
    },
    "62a82d76-70ea-41e2-9197-370581804d09": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create groups, read all group properties and memberships, update group properties and memberships, and delete groups. Also allows the app to read and write conversations. All of these operations can be performed by the app without a signed-in user.",
        "displayName": "Read and write all groups",
        "id": "62a82d76-70ea-41e2-9197-370581804d09",
        "isEnabled": True,
        "origin": "Application",
        "value": "Group.ReadWrite.All"
    },
    "6323133e-1f6e-46d4-9372-ac33a0870636": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all available Teams Templates, without a signed-user.",
        "displayName": "Read all available Teams Templates",
        "id": "6323133e-1f6e-46d4-9372-ac33a0870636",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamTemplates.Read.All"
    },
    "65319a09-a2be-469d-8782-f6b07debf789": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read or write your organization's user flows, without a signed-in user.",
        "displayName": "Read and write all identity user flows",
        "id": "65319a09-a2be-469d-8782-f6b07debf789",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityUserFlow.ReadWrite.All"
    },
    "656f6061-f9fe-4807-9708-6a2e0934df76": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and update identity risky user information for your organization without a signed-in user. \u00a0Update operations include dismissing risky users.",
        "displayName": "Read and write all risky user information",
        "id": "656f6061-f9fe-4807-9708-6a2e0934df76",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityRiskyUser.ReadWrite.All"
    },
    "658aa5d8-239f-45c4-aa12-864f4fc7e490": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the memberships of hidden groups and administrative units without a signed-in user.",
        "displayName": "Read all hidden memberships",
        "id": "658aa5d8-239f-45c4-aa12-864f4fc7e490",
        "isEnabled": True,
        "origin": "Application",
        "value": "Member.Read.Hidden"
    },
    "660b7406-55f1-41ca-a0ed-0b035e182f3e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read the members of all teams, without a signed-in user.",
        "displayName": "Read the members of all teams",
        "id": "660b7406-55f1-41ca-a0ed-0b035e182f3e",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamMember.Read.All"
    },
    "6918b873-d17a-4dc1-b314-35f528134491": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update, and delete all contacts in all mailboxes without a signed-in user.",
        "displayName": "Read and write contacts in all mailboxes",
        "id": "6918b873-d17a-4dc1-b314-35f528134491",
        "isEnabled": True,
        "origin": "Application",
        "value": "Contacts.ReadWrite"
    },
    "6931bccd-447a-43d1-b442-00a195474933": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update, and delete user's mailbox settings without a signed-in user. Does not include permission to send mail.",
        "displayName": "Read and write all user mailbox settings",
        "id": "6931bccd-447a-43d1-b442-00a195474933",
        "isEnabled": True,
        "origin": "Application",
        "value": "MailboxSettings.ReadWrite"
    },
    "693c5e45-0940-467d-9b8a-1022fb9d42ef": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read basic mail properties in all mailboxes without a signed-in user. Includes all properties except body, previewBody, attachments and any extended properties.",
        "displayName": "Read basic mail in all mailboxes",
        "id": "693c5e45-0940-467d-9b8a-1022fb9d42ef",
        "isEnabled": True,
        "origin": "Application",
        "value": "Mail.ReadBasic.All"
    },
    "6a118a39-1227-45d4-af0c-ea7b40d210bc": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Delete channels in any team, without a signed-in user.",
        "displayName": "Delete channels",
        "id": "6a118a39-1227-45d4-af0c-ea7b40d210bc",
        "isEnabled": True,
        "origin": "Application",
        "value": "Channel.Delete.All"
    },
    "6b7d71aa-70aa-4810-a8d9-5d9fb2830017": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all 1-to-1 or group chat messages in Microsoft Teams.",
        "displayName": "Read all chat messages",
        "id": "6b7d71aa-70aa-4810-a8d9-5d9fb2830017",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.Read.All"
    },
    "6be147d2-ea4f-4b5a-a3fa-3eab6f3c140a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read basic mail properties in all mailboxes without a signed-in user. Includes all properties except body, previewBody, attachments and any extended properties.",
        "displayName": "Read basic mail in all mailboxes",
        "id": "6be147d2-ea4f-4b5a-a3fa-3eab6f3c140a",
        "isEnabled": True,
        "origin": "Application",
        "value": "Mail.ReadBasic"
    },
    "6c0257fd-cffe-415b-8239-2d0d70fdaa9c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the data associated with the business scenarios it owns, without a signed-in user.",
        "displayName": "Read data for all business scenarios this app creates or owns",
        "id": "6c0257fd-cffe-415b-8239-2d0d70fdaa9c",
        "isEnabled": True,
        "origin": "Application",
        "value": "BusinessScenarioData.Read.OwnedBy"
    },
    "6e0a958b-b7fc-4348-b7c4-a6ab9fd3dd0e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all\u00a0class assignments without grades for all users without a signed-in user.",
        "displayName": "Read all class assignments without grades",
        "id": "6e0a958b-b7fc-4348-b7c4-a6ab9fd3dd0e",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduAssignments.ReadBasic.All"
    },
    "6e472fd1-ad78-48da-a0f0-97ab2c6b769e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the identity risk event information for your organization without a signed in user.",
        "displayName": "Read all identity risk event information",
        "id": "6e472fd1-ad78-48da-a0f0-97ab2c6b769e",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityRiskEvent.Read.All"
    },
    "6e74eff9-4a21-45d6-bc03-3a20f61f8281": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, install, upgrade, and uninstall Teams apps in any chat, without a signed-in user. Gives the ability to manage permission grants for accessing those specific chats' data.",
        "displayName": "Manage installation and permission grants of Teams apps for all chats",
        "id": "6e74eff9-4a21-45d6-bc03-3a20f61f8281",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteAndConsentForChat.All"
    },
    "6e98f277-b046-4193-a4f2-6bf6a78cd491": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read Bookings appointments, businesses, customers, services, and staff without a signed-in user.  ",
        "displayName": "Read all Bookings related resources.",
        "id": "6e98f277-b046-4193-a4f2-6bf6a78cd491",
        "isEnabled": True,
        "origin": "Application",
        "value": "Bookings.Read.All"
    },
    "6ee891c3-74a4-4148-8463-0c834375dfaf": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read reference definitions without a signed-in user.",
        "displayName": "View reference definitions",
        "id": "6ee891c3-74a4-4148-8463-0c834375dfaf",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-ReferenceDefinition.Read.All"
    },
    "6f9d5abc-2db6-400b-a267-7de22a40fb87": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to request and manage time-based assignment and just-in-time elevation of Azure resources (like your subscriptions, resource groups, storage, compute) in your organization, without a signed-in user.",
        "displayName": "Read and write privileged access to Azure resources",
        "id": "6f9d5abc-2db6-400b-a267-7de22a40fb87",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedAccess.ReadWrite.AzureResources"
    },
    "70dec828-f620-4914-aa83-a29117306807": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all users' teamwork activity feed, without a signed-in user.",
        "displayName": "Read all users' teamwork activity feed",
        "id": "70dec828-f620-4914-aa83-a29117306807",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsActivity.Read.All"
    },
    "73a45059-f39c-4baf-9182-4954ac0e55cf": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall itself for any chat, without a signed-in user.",
        "displayName": "Allow the Teams app to manage itself for all chats",
        "id": "73a45059-f39c-4baf-9182-4954ac0e55cf",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteSelfForChat.All"
    },
    "741f803b-c850-494e-b5df-cde7c675a1ca": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and update user profiles without a signed in user.",
        "displayName": "Read and write all users' full profiles",
        "id": "741f803b-c850-494e-b5df-cde7c675a1ca",
        "isEnabled": True,
        "origin": "Application",
        "value": "User.ReadWrite.All"
    },
    "7438b122-aefc-4978-80ed-43db9fcc7715": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's devices' configuration information without a signed-in user.",
        "displayName": "Read all devices",
        "id": "7438b122-aefc-4978-80ed-43db9fcc7715",
        "isEnabled": True,
        "origin": "Application",
        "value": "Device.Read.All"
    },
    "74ef0291-ca83-4d02-8c7e-d2391e6a444f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, install, upgrade, and uninstall Teams apps for any user, without a signed-in user. Does not give the ability to read application-specific settings.",
        "displayName": "Manage Teams apps for all users",
        "id": "74ef0291-ca83-4d02-8c7e-d2391e6a444f",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteForUser.All"
    },
    "75359482-378d-4052-8f01-80520e7db3cd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, create, update and delete all files in all site collections without a signed in user. ",
        "displayName": "Read and write files in all site collections",
        "id": "75359482-378d-4052-8f01-80520e7db3cd",
        "isEnabled": True,
        "origin": "Application",
        "value": "Files.ReadWrite.All"
    },
    "7654ed61-8965-4025-846a-0856ec02b5b0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, update, read and delete all self-initiated courses in the organization's directory, without a signed-in user.",
        "displayName": "Read and write all self-initiated courses",
        "id": "7654ed61-8965-4025-846a-0856ec02b5b0",
        "isEnabled": True,
        "origin": "Application",
        "value": "LearningSelfInitiatedCourse.ReadWrite.All"
    },
    "77c863fd-06c0-47ce-a7eb-49773e89d319": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's directory access review default policy without a signed-in user.",
        "displayName": "Read and write your organization's directory access review default policy",
        "id": "77c863fd-06c0-47ce-a7eb-49773e89d319",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.AccessReview"
    },
    "78145de6-330d-4800-a6ce-494ff2d33d07": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the properties, group assignments and status of apps, app configurations and app protection policies managed by Microsoft Intune, without a signed-in user.",
        "displayName": "Read and write Microsoft Intune apps",
        "id": "78145de6-330d-4800-a6ce-494ff2d33d07",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementApps.ReadWrite.All"
    },
    "798ee544-9d2d-430c-a058-570e29e34338": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read events of all calendars without a signed-in user.",
        "displayName": "Read calendars in all mailboxes",
        "id": "798ee544-9d2d-430c-a058-570e29e34338",
        "isEnabled": True,
        "origin": "Application",
        "value": "Calendars.Read"
    },
    "79a677f7-b79d-40d0-a36a-3e6f8688dd7a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's trust framework policies without a signed in user.",
        "displayName": "Read and write your organization's trust framework policies",
        "id": "79a677f7-b79d-40d0-a36a-3e6f8688dd7a",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.TrustFramework"
    },
    "79c02f5b-bd4f-4713-bc2c-a8a4a66e127b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allow the app to read and write the management data for Teams devices, without a signed-in user.",
        "displayName": "Read and write Teams devices",
        "id": "79c02f5b-bd4f-4713-bc2c-a8a4a66e127b",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamworkDevice.ReadWrite.All"
    },
    "79c261e0-fe76-4144-aad5-bdc68fbe4037": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your tenant's service health information, without a signed-in user. Health information may include service issues or service health overviews.",
        "displayName": "Read service health",
        "id": "79c261e0-fe76-4144-aad5-bdc68fbe4037",
        "isEnabled": True,
        "origin": "Application",
        "value": "ServiceHealth.Read.All"
    },
    "7a6ee1e7-141e-4cec-ae74-d9db155731ff": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the properties, group assignments and status of apps, app configurations and app protection policies managed by Microsoft Intune, without a signed-in user.",
        "displayName": "Read Microsoft Intune apps",
        "id": "7a6ee1e7-141e-4cec-ae74-d9db155731ff",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementApps.Read.All"
    },
    "7a7cffad-37d2-4f48-afa4-c6ab129adcc2": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all external items without a signed-in user.",
        "displayName": "Read all external items",
        "id": "7a7cffad-37d2-4f48-afa4-c6ab129adcc2",
        "isEnabled": True,
        "origin": "Application",
        "value": "ExternalItem.Read.All"
    },
    "7ab1d382-f21e-4acd-a863-ba3e13f7da61": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read data in your organization's directory, such as users, groups and apps, without a signed-in user.",
        "displayName": "Read directory data",
        "id": "7ab1d382-f21e-4acd-a863-ba3e13f7da61",
        "isEnabled": True,
        "origin": "Application",
        "value": "Directory.Read.All"
    },
    "7ab52c2f-a2ee-4d98-9ebc-725e3934aae2": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read data connectors without a signed-in user.",
        "displayName": "View data connector definitions",
        "id": "7ab52c2f-a2ee-4d98-9ebc-725e3934aae2",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-DataConnector.Read.All"
    },
    "7afa7744-a782-4a32-b8c2-e3db637e8de7": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write time period definitions without a signed-in user.",
        "displayName": "Manage time period definitions",
        "id": "7afa7744-a782-4a32-b8c2-e3db637e8de7",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-TimePeriod.ReadWrite.All"
    },
    "7b2449af-6ccd-4f4d-9f78-e550c193f0d1": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all channel messages in Microsoft Teams",
        "displayName": "Read all channel messages",
        "id": "7b2449af-6ccd-4f4d-9f78-e550c193f0d1",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChannelMessage.Read.All"
    },
    "7b2ebf90-d836-437f-b90d-7b62722c4456": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all schedules, schedule groups, shifts and associated entities in the Teams or Shifts application without a signed-in user.",
        "displayName": "Read all schedule items",
        "id": "7b2ebf90-d836-437f-b90d-7b62722c4456",
        "isEnabled": True,
        "origin": "Application",
        "value": "Schedule.Read.All"
    },
    "7c55c952-b095-4c23-a522-022bce4cc1e3": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read time period definitions without a signed-in user.",
        "displayName": "Read time period definitions",
        "id": "7c55c952-b095-4c23-a522-022bce4cc1e3",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-TimePeriod.Read.All"
    },
    "7c67316a-232a-4b84-be22-cea2c0906404": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to list and read all workflows, tasks and related lifecycle workflows resources without a signed-in user.",
        "displayName": "Read all lifecycle workflows resources",
        "id": "7c67316a-232a-4b84-be22-cea2c0906404",
        "isEnabled": True,
        "origin": "Application",
        "value": "LifecycleWorkflows.Read.All"
    },
    "7c9db06a-ec2d-4e7b-a592-5a1e30992566": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read the state and settings of all Microsoft education apps.",
        "displayName": "Read Education app settings",
        "id": "7c9db06a-ec2d-4e7b-a592-5a1e30992566",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduAdministration.Read.All"
    },
    "7d866958-e06e-4dd6-91c6-a086b3f5cfeb": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write source system definitions without a signed-in user.",
        "displayName": "Manage source system definitions",
        "id": "7d866958-e06e-4dd6-91c6-a086b3f5cfeb",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-SourceSystem.ReadWrite.All"
    },
    "7dd1be58-6e76-4401-bf8d-31d1e8180d5b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write all Windows update deployment settings for the organization without a signed-in user.",
        "displayName": "Read and write all Windows update deployment settings",
        "id": "7dd1be58-6e76-4401-bf8d-31d1e8180d5b",
        "isEnabled": True,
        "origin": "Application",
        "value": "WindowsUpdates.ReadWrite.All"
    },
    "7e05723c-0bb0-42da-be95-ae9f08a6e53c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write all domain properties without a signed in user. \u00a0Also allows the app to add, \u00a0verify and remove domains.",
        "displayName": "Read and write domains",
        "id": "7e05723c-0bb0-42da-be95-ae9f08a6e53c",
        "isEnabled": True,
        "origin": "Application",
        "value": "Domain.ReadWrite.All"
    },
    "7e847308-e030-4183-9899-5235d7270f58": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to update Microsoft Teams 1-to-1 or group chat messages by patching a set of Data Loss Prevention (DLP) policy violation properties to handle the output of DLP processing.",
        "displayName": "Flag chat messages for violating policy",
        "id": "7e847308-e030-4183-9899-5235d7270f58",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.UpdatePolicyViolation.All"
    },
    "810c84a8-4a9e-49e6-bf7d-12d183f40d01": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read mail in all mailboxes without a signed-in user.",
        "displayName": "Read mail in all mailboxes",
        "id": "810c84a8-4a9e-49e6-bf7d-12d183f40d01",
        "isEnabled": True,
        "origin": "Application",
        "value": "Mail.Read"
    },
    "8116ae0f-55c2-452d-9944-d18420f5b2c8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write external items without a signed-in user. The app can only read external items of the connection that it is authorized to.",
        "displayName": "Read and write external items",
        "id": "8116ae0f-55c2-452d-9944-d18420f5b2c8",
        "isEnabled": True,
        "origin": "Application",
        "value": "ExternalItem.ReadWrite.OwnedBy"
    },
    "8137102d-ec16-4191-aaf8-7aeda8026183": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's network access braches, without a signed-in user.",
        "displayName": "Read and write properties of all branches for network access",
        "id": "8137102d-ec16-4191-aaf8-7aeda8026183",
        "isEnabled": True,
        "origin": "Application",
        "value": "NetworkAccessBranch.ReadWrite.All"
    },
    "818ba5bd-5b3e-4fe0-bbe6-aa4686669073": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read names and members of all one-to-one and group chats in Microsoft Teams where the associated Teams application is installed, without a signed-in user.",
        "displayName": "Read names and members of all chat threads where the associated Teams application is installed.",
        "id": "818ba5bd-5b3e-4fe0-bbe6-aa4686669073",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.ReadBasic.WhereInstalled"
    },
    "8349ca94-3061-44d5-9bfb-33774ea5e4f9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read and write all browser site lists configured for your organization, without a signed-in user.",
        "displayName": "Read and write all browser site lists for your organization",
        "id": "8349ca94-3061-44d5-9bfb-33774ea5e4f9",
        "isEnabled": True,
        "origin": "Application",
        "value": "BrowserSiteLists.ReadWrite.All"
    },
    "8387eaa4-1a3c-41f5-b261-f888138e6041": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows\u00a0the\u00a0app\u00a0to\u00a0read\u00a0and\u00a0write subject\u00a0rights requests\u00a0without a signed in user.",
        "displayName": "Read\u00a0and\u00a0write\u00a0all subject\u00a0rights requests",
        "id": "8387eaa4-1a3c-41f5-b261-f888138e6041",
        "isEnabled": True,
        "origin": "Application",
        "value": "SubjectRightsRequest.ReadWrite.All"
    },
    "83cded22-8297-4ff6-a7fa-e97e9545a259": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all presence information and write activity and availability of all users in the directory without a signed-in user. Presence information includes activity, availability, status note, calendar out-of-office message, time zone and location.",
        "displayName": "Read and write presence information for all users",
        "id": "83cded22-8297-4ff6-a7fa-e97e9545a259",
        "isEnabled": True,
        "origin": "Application",
        "value": "Presence.ReadWrite.All"
    },
    "83d4163d-a2d8-4d3b-9695-4ae3ca98f888": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read the tenant-level settings of SharePoint and OneDrive, without a signed-in user.",
        "displayName": "Read SharePoint and OneDrive tenant settings",
        "id": "83d4163d-a2d8-4d3b-9695-4ae3ca98f888",
        "isEnabled": True,
        "origin": "Application",
        "value": "SharePointTenantSettings.Read.All"
    },
    "842c284c-763d-4a97-838d-79787d129bab": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, create, edit, and delete all the short notes without a signed-in user.",
        "displayName": "Read, create, edit, and delete all users' short notes",
        "id": "842c284c-763d-4a97-838d-79787d129bab",
        "isEnabled": True,
        "origin": "Application",
        "value": "ShortNotes.ReadWrite.All"
    },
    "854d9ab1-6657-4ec8-be45-823027bcd009": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to request and manage time-based assignment and just-in-time elevation (including scheduled elevation) of Azure AD built-in and custom administrative roles in your organization, without a signed-in user.",
        "displayName": "Read and write privileged access to Azure AD roles",
        "id": "854d9ab1-6657-4ec8-be45-823027bcd009",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedAccess.ReadWrite.AzureAD"
    },
    "8556a004-db57-4d7a-8b82-97a13428e96f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the lifecycle information like employeeLeaveDateTime of users in your organization, without a signed-in user.",
        "displayName": "Read all users' lifecycle information",
        "id": "8556a004-db57-4d7a-8b82-97a13428e96f",
        "isEnabled": True,
        "origin": "Application",
        "value": "User-LifeCycleInfo.Read.All"
    },
    "86632667-cd15-4845-ad89-48a88e8412e1": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's threat submissions and to view threat submission policies without a signed-in user.",
        "displayName": "Read all of the organization's threat submissions",
        "id": "86632667-cd15-4845-ad89-48a88e8412e1",
        "isEnabled": True,
        "origin": "Application",
        "value": "ThreatSubmission.Read.All"
    },
    "8740813e-d8aa-4204-860e-2a0f8f84dbc8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all learning content in the organization's directory, without a signed-in user.",
        "displayName": "Read all learning content",
        "id": "8740813e-d8aa-4204-860e-2a0f8f84dbc8",
        "isEnabled": True,
        "origin": "Application",
        "value": "LearningContent.Read.All"
    },
    "883ea226-0bf2-4a8f-9f9d-92c9162a727d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allow the application to access a subset of site collections without a signed in user.\u00a0\u00a0The specific site collections and the permissions granted will be configured in SharePoint Online.",
        "displayName": "Access selected site collections",
        "id": "883ea226-0bf2-4a8f-9f9d-92c9162a727d",
        "isEnabled": True,
        "origin": "Application",
        "value": "Sites.Selected"
    },
    "884b599e-4d48-43a5-ba94-15c414d00588": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read device local credential properties including passwords, without a signed-in user.",
        "displayName": "Read device local credential passwords",
        "id": "884b599e-4d48-43a5-ba94-15c414d00588",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceLocalCredential.Read.All"
    },
    "88bb2658-5d9e-454f-aacd-a3933e079526": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's custom authentication extensions without a signed-in user.",
        "displayName": "Read all custom authentication extensions",
        "id": "88bb2658-5d9e-454f-aacd-a3933e079526",
        "isEnabled": True,
        "origin": "Application",
        "value": "CustomAuthenticationExtension.Read.All"
    },
    "89c8469c-83ad-45f7-8ff2-6e3d4285709e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to update service principal endpoints",
        "displayName": "Read and update service principal endpoints",
        "id": "89c8469c-83ad-45f7-8ff2-6e3d4285709e",
        "isEnabled": True,
        "origin": "Application",
        "value": "ServicePrincipalEndpoint.ReadWrite.All"
    },
    "8a3d36bf-cb46-4bcc-bec9-8d92829dab84": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's network access policies, without a signed-in user.",
        "displayName": "Read all security and routing policies for network access",
        "id": "8a3d36bf-cb46-4bcc-bec9-8d92829dab84",
        "isEnabled": True,
        "origin": "Application",
        "value": "NetworkAccessPolicy.Read.All"
    },
    "8b919d44-6192-4f3d-8a3b-f86f8069ae3c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to list and query any shared user profile information associated with the current tenant without a signed-in user.\u00a0 It also permits the application to export external user data (e.g. customer content or system-generated logs), for any user associated with the current tenant without a signed-in user.",
        "displayName": "Read all shared cross-tenant user profiles and export their data",
        "id": "8b919d44-6192-4f3d-8a3b-f86f8069ae3c",
        "isEnabled": True,
        "origin": "Application",
        "value": "CrossTenantUserProfileSharing.Read.All"
    },
    "8ba4a692-bc31-4128-9094-475872af8a53": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read events of all calendars, except for properties such as body, attachments, and extensions, without a signed-in user.",
        "displayName": "Read basic details of calendars in all mailboxes ",
        "id": "8ba4a692-bc31-4128-9094-475872af8a53",
        "isEnabled": True,
        "origin": "Application",
        "value": "Calendars.ReadBasic.All"
    },
    "8c0aed2c-0c61-433d-b63c-6370ddc73248": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read all acronyms without a signed-in user.",
        "displayName": "Read all acronyms",
        "id": "8c0aed2c-0c61-433d-b63c-6370ddc73248",
        "isEnabled": True,
        "origin": "Application",
        "value": "Acronym.Read.All"
    },
    "8e8e4742-1d95-4f68-9d56-6ee75648c72a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to manage permission grants for delegated permissions exposed by any API (including Microsoft Graph), without a signed-in user.",
        "displayName": "Manage all delegated permission grants",
        "id": "8e8e4742-1d95-4f68-9d56-6ee75648c72a",
        "isEnabled": True,
        "origin": "Application",
        "value": "DelegatedPermissionGrant.ReadWrite.All"
    },
    "908de74d-f8b2-4d6b-a9ed-2a17b3b78179": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall itself to any user, without a signed-in user.",
        "displayName": "Allow the app to manage itself for all users",
        "id": "908de74d-f8b2-4d6b-a9ed-2a17b3b78179",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteSelfForUser.All"
    },
    "90db2b9a-d928-4d33-a4dd-8442ae3d41e4": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization\u2019s identity (authentication) providers\u2019 properties without a signed in user.",
        "displayName": "Read and write identity providers",
        "id": "90db2b9a-d928-4d33-a4dd-8442ae3d41e4",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityProvider.ReadWrite.All"
    },
    "913b9306-0ce1-42b8-9137-6a7df690a760": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read company places (conference rooms and room lists) for calendar events and other applications, without a signed-in user.",
        "displayName": "Read all company places",
        "id": "913b9306-0ce1-42b8-9137-6a7df690a760",
        "isEnabled": True,
        "origin": "Application",
        "value": "Place.Read.All"
    },
    "91c32b81-0ef0-453f-a5c7-4ce2e562f449": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs in any team, without a signed-in user.",
        "displayName": "Allow the Teams app to manage only its own tabs for all teams",
        "id": "91c32b81-0ef0-453f-a5c7-4ce2e562f449",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.ReadWriteSelfForTeam.All"
    },
    "9241abd9-d0e6-425a-bd4f-47ba86e767a4": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write properties of Microsoft Intune-managed device configuration and device compliance policies and their assignment to groups, without a signed-in user.",
        "displayName": "Read and write Microsoft Intune device configuration and policies",
        "id": "9241abd9-d0e6-425a-bd4f-47ba86e767a4",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementConfiguration.ReadWrite.All"
    },
    "925f1248-0f97-47b9-8ec8-538c54e01325": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the lifecycle information like employeeLeaveDateTime of users in your organization, without a signed-in user.",
        "displayName": "Read and write all users' lifecycle information",
        "id": "925f1248-0f97-47b9-8ec8-538c54e01325",
        "isEnabled": True,
        "origin": "Application",
        "value": "User-LifeCycleInfo.ReadWrite.All"
    },
    "926a6798-b100-4a20-a22f-a4918f13951d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's threat submission policies without a signed-in user. Also allows the app to create new threat submission polices without a signed-in user.",
        "displayName": "Read and write all of the organization's threat submission policies",
        "id": "926a6798-b100-4a20-a22f-a4918f13951d",
        "isEnabled": True,
        "origin": "Application",
        "value": "ThreatSubmissionPolicy.ReadWrite.All"
    },
    "93283d0a-6322-4fa8-966b-8c121624760d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read attack simulation and training data for an organization without a signed-in user.",
        "displayName": "Read attack simulation data of an organization",
        "id": "93283d0a-6322-4fa8-966b-8c121624760d",
        "isEnabled": True,
        "origin": "Application",
        "value": "AttackSimulation.Read.All"
    },
    "9334c44b-a7c6-4350-8036-6bf8e02b4c1f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to upload data files to a data connector without a signed-in user.",
        "displayName": "Upload files to a data connector",
        "id": "9334c44b-a7c6-4350-8036-6bf8e02b4c1f",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-DataConnector.Upload"
    },
    "93e7c9e4-54c5-4a41-b796-f2a5adaacda7": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the members of all chats where the associated Teams application is installed, without a signed-in user.",
        "displayName": "Read the members of all chats where the associated Teams application is installed.",
        "id": "93e7c9e4-54c5-4a41-b796-f2a5adaacda7",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChatMember.Read.WhereInstalled"
    },
    "9492366f-7969-46a4-8d15-ed1a20078fff": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update, and delete documents and list items in all site collections without a signed in user.",
        "displayName": "Read and write items in all site collections",
        "id": "9492366f-7969-46a4-8d15-ed1a20078fff",
        "isEnabled": True,
        "origin": "Application",
        "value": "Sites.ReadWrite.All"
    },
    "9709bb33-4549-49d4-8ed9-a8f65e45bb0f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read printers without a signed-in user.\u00a0",
        "displayName": "Read printers",
        "id": "9709bb33-4549-49d4-8ed9-a8f65e45bb0f",
        "isEnabled": True,
        "origin": "Application",
        "value": "Printer.Read.All"
    },
    "9769393e-5a9f-4302-9e3d-7e018ecb64a7": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read and write Bookings appointments and customers, and additionally allows reading businesses, services, and staff without a signed-in user. ",
        "displayName": "Read and write all Bookings related resources.",
        "id": "9769393e-5a9f-4302-9e3d-7e018ecb64a7",
        "isEnabled": True,
        "origin": "Application",
        "value": "BookingsAppointment.ReadWrite.All"
    },
    "98830695-27a2-44f7-8c18-0c3ebc9698f6": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read memberships and basic group properties for all groups without a signed-in user.",
        "displayName": "Read all group memberships",
        "id": "98830695-27a2-44f7-8c18-0c3ebc9698f6",
        "isEnabled": True,
        "origin": "Application",
        "value": "GroupMember.Read.All"
    },
    "999f8c63-0a38-4f1b-91fd-ed1947bdd1a9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's consent requests policy without a signed-in user.",
        "displayName": "Read and write your organization's consent request policy",
        "id": "999f8c63-0a38-4f1b-91fd-ed1947bdd1a9",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.ConsentRequest"
    },
    "9a5d68dd-52b0-4cc2-bd40-abcf44ac3a30": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all applications and service principals without a signed-in user.",
        "displayName": "Read all applications",
        "id": "9a5d68dd-52b0-4cc2-bd40-abcf44ac3a30",
        "isEnabled": True,
        "origin": "Application",
        "value": "Application.Read.All"
    },
    "9acd699f-1e81-4958-b001-93b1d2506e19": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write access packages and related entitlement management resources without a signed-in user.",
        "displayName": "Read and write all entitlement management resources",
        "id": "9acd699f-1e81-4958-b001-93b1d2506e19",
        "isEnabled": True,
        "origin": "Application",
        "value": "EntitlementManagement.ReadWrite.All"
    },
    "9b50c33d-700f-43b1-b2eb-87e89b703581": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to configure the Azure AD synchronization service, without a signed-in user.",
        "displayName": "Read and write all Azure AD synchronization data. ",
        "id": "9b50c33d-700f-43b1-b2eb-87e89b703581",
        "isEnabled": True,
        "origin": "Application",
        "value": "Synchronization.ReadWrite.All"
    },
    "9bc431c3-b8bc-4a8d-a219-40f10f92eff6": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Manage the state and settings of all Microsoft education apps.",
        "displayName": "Manage education app settings",
        "id": "9bc431c3-b8bc-4a8d-a219-40f10f92eff6",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduAdministration.ReadWrite.All"
    },
    "9c7abde0-eacd-4319-bf9e-35994b1a1717": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to delete and recover deleted chats, without a signed-in user.",
        "displayName": "Delete and recover deleted chats",
        "id": "9c7abde0-eacd-4319-bf9e-35994b1a1717",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.ManageDeletion.All"
    },
    "9ce09611-f4f7-4abd-a629-a05450422a97": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the Teams apps that are installed for any user, without a signed-in user. Does not give the ability to read application-specific settings.",
        "displayName": "Read installed Teams apps for all users",
        "id": "9ce09611-f4f7-4abd-a629-a05450422a97",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadForUser.All"
    },
    "9e19bae1-2623-4c4f-ab6e-2664615ff9a0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, install, upgrade, and uninstall Teams apps in any chat, without a signed-in user. Does not give the ability to read application-specific settings.",
        "displayName": "Manage Teams apps for all chats",
        "id": "9e19bae1-2623-4c4f-ab6e-2664615ff9a0",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteForChat.All"
    },
    "9e3f62cf-ca93-4989-b6ce-bf83c28f9fe8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and manage the role-based access control (RBAC) settings for your company's directory, without a signed-in user. This includes instantiating directory roles and managing directory role membership, and reading directory role templates, directory roles and memberships.",
        "displayName": "Read and write all directory RBAC settings",
        "id": "9e3f62cf-ca93-4989-b6ce-bf83c28f9fe8",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagement.ReadWrite.Directory"
    },
    "9e640839-a198-48fb-8b9a-013fd6f6cbcd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read policies related to consent and permission grants for applications, without a signed-in user.",
        "displayName": "Read consent and permission grant policies",
        "id": "9e640839-a198-48fb-8b9a-013fd6f6cbcd",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.Read.PermissionGrant"
    },
    "9e8be751-7eee-4c09-bcfd-d64f6b087fd8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the billing configuration on all applications without a signed-in user. ",
        "displayName": "Read and write application billing configuration",
        "id": "9e8be751-7eee-4c09-bcfd-d64f6b087fd8",
        "isEnabled": True,
        "origin": "Application",
        "value": "BillingConfiguration.ReadWrite.All"
    },
    "9f1b81a7-0223-4428-bfa4-0bcb5535f27d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read app consent requests and approvals, and deny or approve those requests without a signed-in user.",
        "displayName": "Read and write all consent requests",
        "id": "9f1b81a7-0223-4428-bfa4-0bcb5535f27d",
        "isEnabled": True,
        "origin": "Application",
        "value": "ConsentRequest.ReadWrite.All"
    },
    "9f62e4a2-a2d6-4350-b28b-d244728c4f86": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall its own tabs for any chat, without a signed-in user.",
        "displayName": "Allow the Teams app to manage only its own tabs for all chats",
        "id": "9f62e4a2-a2d6-4350-b28b-d244728c4f86",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.ReadWriteSelfForChat.All"
    },
    "9f67436c-5415-4e7f-8ac1-3014a7132630": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall itself in any team, without a signed-in user.",
        "displayName": "Allow the Teams app to manage itself for all teams",
        "id": "9f67436c-5415-4e7f-8ac1-3014a7132630",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteSelfForTeam.All"
    },
    "a2611786-80b3-417e-adaa-707d4261a5f0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all PSTN and direct routing call log data without a signed-in user.",
        "displayName": "Read PSTN and direct routing call log data",
        "id": "a2611786-80b3-417e-adaa-707d4261a5f0",
        "isEnabled": True,
        "origin": "Application",
        "value": "CallRecord-PstnCalls.Read.All"
    },
    "a267235f-af13-44dc-8385-c1dc93023186": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create new notifications in users' teamwork activity feeds without a signed in user. These notifications may not be discoverable or be held or governed by compliance policies.",
        "displayName": "Send a teamwork activity to any user",
        "id": "a267235f-af13-44dc-8385-c1dc93023186",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsActivity.Send"
    },
    "a3371ca5-911d-46d6-901c-42c8c7a937d8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write tags in Teams without a signed-in user.",
        "displayName": "Read and write tags in Teams",
        "id": "a3371ca5-911d-46d6-901c-42c8c7a937d8",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamworkTag.ReadWrite.All"
    },
    "a3410be2-8e48-4f32-8454-c29a7465209d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read the members of all chats, without a signed-in user.",
        "displayName": "Read the members of all chats",
        "id": "a3410be2-8e48-4f32-8454-c29a7465209d",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChatMember.Read.All"
    },
    "a402ca1c-2696-4531-972d-6e5ee4aa11ea": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to manage policies related to consent and permission grants for applications, without a signed-in user.",
        "displayName": "Manage consent and permission grant policies",
        "id": "a402ca1c-2696-4531-972d-6e5ee4aa11ea",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.PermissionGrant"
    },
    "a4a08342-c95d-476b-b943-97e100569c8d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all recordings of all online meetings, without a signed-in user.",
        "displayName": "Read all recordings of online meetings.",
        "id": "a4a08342-c95d-476b-b943-97e100569c8d",
        "isEnabled": True,
        "origin": "Application",
        "value": "OnlineMeetingRecording.Read.All"
    },
    "a4a80d8d-d283-4bd8-8504-555ec3870630": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all transcripts of all online meetings, without a signed-in user.",
        "displayName": "Read all transcripts of online meetings.",
        "id": "a4a80d8d-d283-4bd8-8504-555ec3870630",
        "isEnabled": True,
        "origin": "Application",
        "value": "OnlineMeetingTranscript.Read.All"
    },
    "a7a681dc-756e-4909-b988-f160edc6655f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to get direct access to media streams in a call, without a signed-in user.",
        "displayName": "Access media streams in a call as an app",
        "id": "a7a681dc-756e-4909-b988-f160edc6655f",
        "isEnabled": True,
        "origin": "Application",
        "value": "Calls.AccessMedia.All"
    },
    "a82116e5-55eb-4c41-a434-62fe8a61c773": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to have full control of all site collections without a signed in user.",
        "displayName": "Have full control of all site collections",
        "id": "a82116e5-55eb-4c41-a434-62fe8a61c773",
        "isEnabled": True,
        "origin": "Application",
        "value": "Sites.FullControl.All"
    },
    "a88eef72-fed0-4bf7-a2a9-f19df33f8b83": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and update the authentication context information in your organization without a signed-in user.",
        "displayName": "Read and write all authentication context information",
        "id": "a88eef72-fed0-4bf7-a2a9-f19df33f8b83",
        "isEnabled": True,
        "origin": "Application",
        "value": "AuthenticationContext.ReadWrite.All"
    },
    "a96d855f-016b-47d7-b51c-1218a98d791c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read and write tabs in any team in Microsoft Teams, without a signed-in user. This does not give access to the content inside the tabs.",
        "displayName": "Read and write tabs in Microsoft Teams.",
        "id": "a96d855f-016b-47d7-b51c-1218a98d791c",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.ReadWrite.All"
    },
    "a9e09520-8ed4-4cde-838e-4fdea192c227": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the properties of Cloud PCs, without a signed-in user.",
        "displayName": "Read Cloud PCs",
        "id": "a9e09520-8ed4-4cde-838e-4fdea192c227",
        "isEnabled": True,
        "origin": "Application",
        "value": "CloudPC.Read.All"
    },
    "ab5b445e-8f10-45f4-9c79-dd3f8062cc4e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the Teams app settings without a signed-in user.",
        "displayName": "Read and write Teams app settings",
        "id": "ab5b445e-8f10-45f4-9c79-dd3f8062cc4e",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamworkAppSettings.ReadWrite.All"
    },
    "ac3a2b8e-03a3-4da9-9ce0-cbe28bf1accd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read any data from Records Management, such as configuration, labels, and policies without the signed in user.",
        "displayName": "Read Records Management configuration,\u00a0labels and policies",
        "id": "ac3a2b8e-03a3-4da9-9ce0-cbe28bf1accd",
        "isEnabled": True,
        "origin": "Application",
        "value": "RecordsManagement.Read.All"
    },
    "ac6f956c-edea-44e4-bd06-64b1b4b9aec9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read the metadata and document content of print jobs without a signed-in user.\u00a0",
        "displayName": "Read print jobs",
        "id": "ac6f956c-edea-44e4-bd06-64b1b4b9aec9",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrintJob.Read.All"
    },
    "acc0fc4d-2cd6-4194-8700-1768d8423d86": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the configurations of business scenarios it owns, without a signed-in user.",
        "displayName": "Read all business scenario configurations this app creates or owns",
        "id": "acc0fc4d-2cd6-4194-8700-1768d8423d86",
        "isEnabled": True,
        "origin": "Application",
        "value": "BusinessScenarioConfig.Read.OwnedBy"
    },
    "ad73ce80-f3cd-40ce-b325-df12c33df713": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write all chat messages in Microsoft Teams for chats where the associated Teams application is installed, without a signed-in user.",
        "displayName": "Read and write all chat messages for chats where the associated Teams application is installed.",
        "id": "ad73ce80-f3cd-40ce-b325-df12c33df713",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.ReadWrite.WhereInstalled"
    },
    "ada977a5-b8b1-493b-9a91-66c206d76ecf": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read search configurations, without a signed-in user.",
        "displayName": "Read your organization's search configuration",
        "id": "ada977a5-b8b1-493b-9a91-66c206d76ecf",
        "isEnabled": True,
        "origin": "Application",
        "value": "SearchConfiguration.Read.All"
    },
    "ae73097b-cb2a-4447-b064-5d80f6093921": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all Azure AD recommendations, without a signed-in user. ",
        "displayName": "Read all Azure AD recommendations",
        "id": "ae73097b-cb2a-4447-b064-5d80f6093921",
        "isEnabled": True,
        "origin": "Application",
        "value": "DirectoryRecommendations.Read.All"
    },
    "b0afded3-3588-46d8-8b3d-9842eff778da": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and query your audit log activities, without a signed-in user.",
        "displayName": "Read all audit log data",
        "id": "b0afded3-3588-46d8-8b3d-9842eff778da",
        "isEnabled": True,
        "origin": "Application",
        "value": "AuditLog.Read.All"
    },
    "b0c13be0-8e20-4bc5-8c55-963c23a39ce9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, install, upgrade, and uninstall Teams apps in any team, without a signed-in user. Gives the ability to manage permission grants for accessing those specific teams' data.",
        "displayName": "Manage installation and permission grants of Teams apps for all teams",
        "id": "b0c13be0-8e20-4bc5-8c55-963c23a39ce9",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteAndConsentForTeam.All"
    },
    "b185aa14-d8d2-42c1-a685-0f5596613624": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read custom security attribute definitions for the tenant without a signed in user.",
        "displayName": "Read custom security attribute definitions",
        "id": "b185aa14-d8d2-42c1-a685-0f5596613624",
        "isEnabled": True,
        "origin": "Application",
        "value": "CustomSecAttributeDefinition.Read.All"
    },
    "b2620db1-3bf7-4c5b-9cb9-576d29eac736": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write eDiscovery objects such as cases, custodians, review sets and other related objects without a signed-in user.",
        "displayName": "Read and write all eDiscovery objects",
        "id": "b2620db1-3bf7-4c5b-9cb9-576d29eac736",
        "isEnabled": True,
        "origin": "Application",
        "value": "eDiscovery.ReadWrite.All"
    },
    "b2e060da-3baf-4687-9611-f4ebc0f0cbde": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read names and members of all one-to-one and group chats in Microsoft Teams, without a signed-in user.",
        "displayName": "Read names and members of all chat threads",
        "id": "b2e060da-3baf-4687-9611-f4ebc0f0cbde",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.ReadBasic.All"
    },
    "b48f7ac2-044d-4281-b02f-75db744d6f5f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read email metadata and security detection details, without a signed-in user.  ",
        "displayName": "Read metadata and detection details for all emails in your organization",
        "id": "b48f7ac2-044d-4281-b02f-75db744d6f5f",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityAnalyzedMessage.Read.All"
    },
    "b528084d-ad10-4598-8b93-929746b4d7d6": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read any user's scored list of relevant people, without a signed-in user. The list can include local contacts, contacts from social networking, your organization's directory, and people from recent communications (such as email and Skype).",
        "displayName": "Read all users' relevant people lists",
        "id": "b528084d-ad10-4598-8b93-929746b4d7d6",
        "isEnabled": True,
        "origin": "Application",
        "value": "People.Read.All"
    },
    "b5991872-94cf-4652-9765-29535087c6d8": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read tenant-wide print settings without a signed-in user.",
        "displayName": "Read tenant-wide print settings",
        "id": "b5991872-94cf-4652-9765-29535087c6d8",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrintSettings.Read.All"
    },
    "b633e1c5-b582-4048-a93e-9f11b44c7e96": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to send mail as any user without a signed-in user.",
        "displayName": "Send mail as any user",
        "id": "b633e1c5-b582-4048-a93e-9f11b44c7e96",
        "isEnabled": True,
        "origin": "Application",
        "value": "Mail.Send"
    },
    "b6890674-9dd5-4e42-bb15-5af07f541ae1": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and write tenant-wide people settings without a signed-in user.",
        "displayName": "Read and write all tenant-wide people settings",
        "id": "b6890674-9dd5-4e42-bb15-5af07f541ae1",
        "isEnabled": True,
        "origin": "Application",
        "value": "PeopleSettings.ReadWrite.All"
    },
    "b74fd6c4-4bde-488e-9695-eeb100e4907f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read\u00a0tags in Teams\u00a0without a signed-in user.",
        "displayName": "Read tags in Teams",
        "id": "b74fd6c4-4bde-488e-9695-eeb100e4907f",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamworkTag.Read.All"
    },
    "b7760610-0545-4e8a-9ec3-cce9e63db01c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to manage all schedules, schedule groups, shifts and associated entities in the Teams or Shifts application without a signed-in user.",
        "displayName": "Read and write all schedule items",
        "id": "b7760610-0545-4e8a-9ec3-cce9e63db01c",
        "isEnabled": True,
        "origin": "Application",
        "value": "Schedule.ReadWrite.All"
    },
    "b7f6385c-6ce6-4639-a480-e23c42ed9784": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's authentication event listeners without a signed-in user.",
        "displayName": "Read all authentication event listeners",
        "id": "b7f6385c-6ce6-4639-a480-e23c42ed9784",
        "isEnabled": True,
        "origin": "Application",
        "value": "EventListener.Read.All"
    },
    "b86848a7-d5b1-41eb-a9b4-54a4e6306e97": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the API connectors used in user authentication flows, without a signed-in user.",
        "displayName": "Read API connectors for authentication flows",
        "id": "b86848a7-d5b1-41eb-a9b4-54a4e6306e97",
        "isEnabled": True,
        "origin": "Application",
        "value": "APIConnectors.Read.All"
    },
    "b8bb2037-6e08-44ac-a4ea-4674e010e2a4": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and create online meetings as an application in your organization.",
        "displayName": "Read and create online meetings",
        "id": "b8bb2037-6e08-44ac-a4ea-4674e010e2a4",
        "isEnabled": True,
        "origin": "Application",
        "value": "OnlineMeetings.ReadWrite.All"
    },
    "b9bb2381-47a4-46cd-aafb-00cb12f68504": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all one-to-one and group chats messages in Microsoft Teams, without a signed-in user.",
        "displayName": "Read all chat messages",
        "id": "b9bb2381-47a4-46cd-aafb-00cb12f68504",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChatMessage.Read.All"
    },
    "ba1ba90b-2d8f-487e-9f16-80728d85bb5c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall itself for any chat, without a signed-in user, and manage its permission grants for accessing those specific chats' data.",
        "displayName": "Allow the Teams app to manage itself and its permission grants for all chats",
        "id": "ba1ba90b-2d8f-487e-9f16-80728d85bb5c",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadWriteAndConsentSelfForChat.All"
    },
    "bbea195a-4c47-4a4f-bff2-cba399e11698": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create new business scenarios and fully manage the configurations of scenarios it owns, without a signed-in user.",
        "displayName": "Read and write all business scenario configurations this app creates or owns",
        "id": "bbea195a-4c47-4a4f-bff2-cba399e11698",
        "isEnabled": True,
        "origin": "Application",
        "value": "BusinessScenarioConfig.ReadWrite.OwnedBy"
    },
    "bc167a60-39fe-4865-8b44-78400fc6ed03": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read source system definitions without a signed-in user.",
        "displayName": "View source system definitions",
        "id": "bc167a60-39fe-4865-8b44-78400fc6ed03",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-SourceSystem.Read.All"
    },
    "bdd80a03-d9bc-451d-b7c4-ce7c63fe3c8f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read and change all teams' settings, without a signed-in user.",
        "displayName": "Read and change all teams' settings",
        "id": "bdd80a03-d9bc-451d-b7c4-ce7c63fe3c8f",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamSettings.ReadWrite.All"
    },
    "be74164b-cff1-491c-8741-e671cb536e13": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's application configuration policies, without a signed-in user.  This includes policies such as activityBasedTimeoutPolicy, claimsMappingPolicy, homeRealmDiscoveryPolicy, tokenIssuancePolicy  and tokenLifetimePolicy.",
        "displayName": "Read and write your organization's application configuration policies",
        "id": "be74164b-cff1-491c-8741-e671cb536e13",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.ApplicationConfiguration"
    },
    "be95e614-8ef3-49eb-8464-1c9503433b86": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read all bookmarks without a signed-in user.",
        "displayName": "Read all bookmarks",
        "id": "be95e614-8ef3-49eb-8464-1c9503433b86",
        "isEnabled": True,
        "origin": "Application",
        "value": "Bookmark.Read.All"
    },
    "bf394140-e372-4bf9-a898-299cfc7564e5": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization\u2019s security events without a signed-in user.",
        "displayName": "Read your organization\u2019s security events",
        "id": "bf394140-e372-4bf9-a898-299cfc7564e5",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityEvents.Read.All"
    },
    "bf46a256-f47d-448f-ab78-f226fff08d40": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and write virtual appointments for all users, without a signed-in user. The app must also be authorized to access an individual user\u2019s data by the online meetings application access policy.",
        "displayName": "Read-write all virtual appointments for users, as authorized by online meetings app access policy",
        "id": "bf46a256-f47d-448f-ab78-f226fff08d40",
        "isEnabled": True,
        "origin": "Application",
        "value": "VirtualAppointment.ReadWrite.All"
    },
    "bf7b1a76-6e77-406b-b258-bf5c7720e98f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create groups without a signed-in user.",
        "displayName": "Create groups",
        "id": "bf7b1a76-6e77-406b-b258-bf5c7720e98f",
        "isEnabled": True,
        "origin": "Application",
        "value": "Group.Create"
    },
    "c1684f21-1984-47fa-9d61-2dc8c296bb70": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read online meeting details in your organization, without a signed-in user.",
        "displayName": "Read online meeting details",
        "id": "c1684f21-1984-47fa-9d61-2dc8c296bb70",
        "isEnabled": True,
        "origin": "Application",
        "value": "OnlineMeetings.Read.All"
    },
    "c2667967-7050-4e7e-b059-4cbbb3811d03": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read or write your organization's custom authentication extensions without a signed-in user.",
        "displayName": "Read and write all custom authentication extensions",
        "id": "c2667967-7050-4e7e-b059-4cbbb3811d03",
        "isEnabled": True,
        "origin": "Application",
        "value": "CustomAuthenticationExtension.ReadWrite.All"
    },
    "c529cfca-c91b-489c-af2b-d92990b66ce6": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, update and delete identities that are associated with a user's account, without a signed in user. This controls the identities users can sign-in with.",
        "displayName": "Manage all users' identities",
        "id": "c529cfca-c91b-489c-af2b-d92990b66ce6",
        "isEnabled": True,
        "origin": "Application",
        "value": "User.ManageIdentities.All"
    },
    "c5ee1f21-fc7f-4937-9af0-c91648ff9597": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read all browser site lists configured for your organization, without a signed-in user.",
        "displayName": "Read all browser site lists for your organization",
        "id": "c5ee1f21-fc7f-4937-9af0-c91648ff9597",
        "isEnabled": True,
        "origin": "Application",
        "value": "BrowserSiteLists.Read.All"
    },
    "c74fd47d-ed3c-45c3-9a9e-b8676de685d2": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read access packages and related entitlement management resources without a signed-in user.",
        "displayName": "Read all entitlement management resources",
        "id": "c74fd47d-ed3c-45c3-9a9e-b8676de685d2",
        "isEnabled": True,
        "origin": "Application",
        "value": "EntitlementManagement.Read.All"
    },
    "c769435f-f061-4d0b-8ff1-3d39870e5f85": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the role-based access control (RBAC) configuration for your organization's Exchange Online service, without a signed-in user. This includes reading Exchange management role definitions, role groups, role group membership, role assignments, management scopes, and role assignment policies.",
        "displayName": "Read Exchange Online RBAC configuration",
        "id": "c769435f-f061-4d0b-8ff1-3d39870e5f85",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagement.Read.Exchange"
    },
    "c7fbd983-d9aa-4fa7-84b8-17382c103bc4": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read role-based access control (RBAC) settings for all RBAC providers without a signed-in user. This includes reading role definitions and role assignments.",
        "displayName": "Read role management data for all RBAC providers",
        "id": "c7fbd983-d9aa-4fa7-84b8-17382c103bc4",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagement.Read.All"
    },
    "c9090d00-6101-42f0-a729-c41074260d47": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write terms of use agreements, without a signed in user.",
        "displayName": "Read and write all terms of use agreements",
        "id": "c9090d00-6101-42f0-a729-c41074260d47",
        "isEnabled": True,
        "origin": "Application",
        "value": "Agreement.ReadWrite.All"
    },
    "c97b873f-f59f-49aa-8a0e-52b32d762124": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Read all channel names, channel descriptions, and channel settings, without a signed-in user.",
        "displayName": "Read the names, descriptions, and settings of all channels",
        "id": "c97b873f-f59f-49aa-8a0e-52b32d762124",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChannelSettings.Read.All"
    },
    "cac88765-0581-4025-9725-5ebc13f729ee": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to obtain basic tenant information about another target tenant within the Azure AD ecosystem without a signed-in user.",
        "displayName": "Read cross-tenant basic information",
        "id": "cac88765-0581-4025-9725-5ebc13f729ee",
        "isEnabled": True,
        "origin": "Application",
        "value": "CrossTenantInformation.ReadBasic.All"
    },
    "cb8d6980-6bcb-4507-afec-ed6de3a2d798": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and update identity risky service principal for your organization, without a signed-in user.",
        "displayName": "Read and write all identity risky service principal information",
        "id": "cb8d6980-6bcb-4507-afec-ed6de3a2d798",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityRiskyServicePrincipal.ReadWrite.All"
    },
    "cbe6c7e4-09aa-4b8d-b3c3-2dbb59af4b54": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to sign digests for data without a signed-in user.",
        "displayName": "Sign digests for data",
        "id": "cbe6c7e4-09aa-4b8d-b3c3-2dbb59af4b54",
        "isEnabled": True,
        "origin": "Application",
        "value": "InformationProtectionContent.Sign.All"
    },
    "cc13eba4-8cd8-44c6-b4d4-f93237adce58": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to manage (create-update-terminate) Delegated Admin relationships with customers and role assignments to security groups for active Delegated Admin relationships without a signed-in user.",
        "displayName": "Manage Delegated Admin relationships with customers",
        "id": "cc13eba4-8cd8-44c6-b4d4-f93237adce58",
        "isEnabled": True,
        "origin": "Application",
        "value": "DelegatedAdminRelationship.ReadWrite.All"
    },
    "cc7e7635-2586-41d6-adaa-a8d3bcad5ee5": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the Teams apps that are installed in any chat, without a signed-in user. Does not give the ability to read application-specific settings.",
        "displayName": "Read installed Teams apps for all chats",
        "id": "cc7e7635-2586-41d6-adaa-a8d3bcad5ee5",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsAppInstallation.ReadForChat.All"
    },
    "cd4161cb-f098-48f8-a884-1eda9a42434c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read time-based assignment schedules for access to Azure AD groups, without a signed-in user.",
        "displayName": "Read assignment schedules for access to Azure AD groups",
        "id": "cd4161cb-f098-48f8-a884-1eda9a42434c",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedAssignmentSchedule.Read.AzureADGroup"
    },
    "d07a8cc0-3d51-4b77-b3b0-32704d1f69fa": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read access reviews, reviewers, decisions and settings in the organization, without a signed-in user.",
        "displayName": "Read all access reviews",
        "id": "d07a8cc0-3d51-4b77-b3b0-32704d1f69fa",
        "isEnabled": True,
        "origin": "Application",
        "value": "AccessReview.Read.All"
    },
    "d1808e82-ce13-47af-ae0d-f9b254e6d58a": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the structure of schools and classes in the organization's roster and education-specific information about all users to be read and written.",
        "displayName": "Read and write the organization's roster",
        "id": "d1808e82-ce13-47af-ae0d-f9b254e6d58a",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduRoster.ReadWrite.All"
    },
    "d1eec298-80f3-49b0-9efb-d90e224798ac": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to manage all users' shift schedule preferences without a signed-in user.",
        "displayName": "Read and write all user shift preferences",
        "id": "d1eec298-80f3-49b0-9efb-d90e224798ac",
        "isEnabled": True,
        "origin": "Application",
        "value": "UserShiftPreferences.ReadWrite.All"
    },
    "d4f67ec2-59b5-4bdc-b4af-d78f6f9c1954": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read virtual appointments for all users, without a signed-in user. The app must also be authorized to access an individual user\u2019s data by the online meetings application access policy.",
        "displayName": "Read all virtual appointments for users, as authorized by online meetings application access policy",
        "id": "d4f67ec2-59b5-4bdc-b4af-d78f6f9c1954",
        "isEnabled": True,
        "origin": "Application",
        "value": "VirtualAppointment.Read.All"
    },
    "d5fe8ce8-684c-4c83-a52c-46e882ce4be1": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the active role-based access control (RBAC) assignments and schedules for your company's directory, without a signed-in user. This includes reading directory role templates, and directory roles.",
        "displayName": "Read all active role assignments and role schedules for your company's directory",
        "id": "d5fe8ce8-684c-4c83-a52c-46e882ce4be1",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleAssignmentSchedule.Read.Directory"
    },
    "d72bdbf4-a59b-405c-8b04-5995895819ac": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization's threat submissions and threat submission policies without a signed-in user. Also allows the app to create new threat submissions without a signed-in user.",
        "displayName": "Read and write all of the organization's threat submissions",
        "id": "d72bdbf4-a59b-405c-8b04-5995895819ac",
        "isEnabled": True,
        "origin": "Application",
        "value": "ThreatSubmission.ReadWrite.All"
    },
    "d8e4ec18-f6c0-4620-8122-c8b1f2bf400e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read terms of use acceptance statuses, without a signed in user.",
        "displayName": "Read all terms of use acceptance statuses",
        "id": "d8e4ec18-f6c0-4620-8122-c8b1f2bf400e",
        "isEnabled": True,
        "origin": "Application",
        "value": "AgreementAcceptance.Read.All"
    },
    "d903a879-88e0-4c09-b0c9-82f6a1333f84": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization\u2019s security events without a signed-in user. Also allows the app to update editable properties in security events.",
        "displayName": "Read and update your organization\u2019s security events",
        "id": "d903a879-88e0-4c09-b0c9-82f6a1333f84",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityEvents.ReadWrite.All"
    },
    "d9c48af6-9ad9-47ad-82c3-63757137b9af": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create chats without a signed-in user.\u00a0",
        "displayName": "Create chats",
        "id": "d9c48af6-9ad9-47ad-82c3-63757137b9af",
        "isEnabled": True,
        "origin": "Application",
        "value": "Chat.Create"
    },
    "db06fb33-1953-4b7b-a2ac-f1e2c854f7ae": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and update identity risk detection information for your organization without a signed-in user. Update operations include confirming risk event detections.\u00a0",
        "displayName": "Read and write all risk detection information",
        "id": "db06fb33-1953-4b7b-a2ac-f1e2c854f7ae",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityRiskEvent.ReadWrite.All"
    },
    "db51be59-e728-414b-b800-e0f010df1a79": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read device local credential properties excluding passwords, without a signed-in user.",
        "displayName": "Read device local credential properties",
        "id": "db51be59-e728-414b-b800-e0f010df1a79",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceLocalCredential.ReadBasic.All"
    },
    "dbaae8cf-10b5-4b86-a4a1-f871c94c6695": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to list groups, read basic properties, read and update the membership of the groups this app has access to without a signed-in user. Group properties and owners cannot be updated and groups cannot be deleted.",
        "displayName": "Read and write all group memberships",
        "id": "dbaae8cf-10b5-4b86-a4a1-f871c94c6695",
        "isEnabled": True,
        "origin": "Application",
        "value": "GroupMember.ReadWrite.All"
    },
    "dbb9058a-0e50-45d7-ae91-66909b5d4664": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all domain properties without a signed-in user.",
        "displayName": "Read domains",
        "id": "dbb9058a-0e50-45d7-ae91-66909b5d4664",
        "isEnabled": True,
        "origin": "Application",
        "value": "Domain.Read.All"
    },
    "dc149144-f292-421e-b185-5953f2e98d7f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update, and delete apps in the app catalogs without a signed-in user.",
        "displayName": "Read and write to all app catalogs",
        "id": "dc149144-f292-421e-b185-5953f2e98d7f",
        "isEnabled": True,
        "origin": "Application",
        "value": "AppCatalog.ReadWrite.All"
    },
    "dc377aa6-52d8-4e23-b271-2a7ae04cedf3": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read properties of Microsoft Intune-managed device configuration and device compliance policies and their assignment to groups, without a signed-in user.",
        "displayName": "Read Microsoft Intune device configuration and policies",
        "id": "dc377aa6-52d8-4e23-b271-2a7ae04cedf3",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementConfiguration.Read.All"
    },
    "dc5007c0-2d7d-4c42-879c-2dab87571379": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the identity risky user information for your organization without a signed in user.",
        "displayName": "Read all identity risky user information",
        "id": "dc5007c0-2d7d-4c42-879c-2dab87571379",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityRiskyUser.Read.All"
    },
    "dd199f4a-f148-40a4-a2ec-f0069cc799ec": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, update, and delete policies for privileged role-based access control (RBAC) assignments of your company's directory, without a signed-in user.",
        "displayName": "Read, update, and delete all policies for privileged role assignments of your company's directory",
        "id": "dd199f4a-f148-40a4-a2ec-f0069cc799ec",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleAssignmentSchedule.ReadWrite.Directory"
    },
    "dd98c7f5-2d42-42d3-a0e4-633161547251": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to run hunting queries, without a signed-in user.",
        "displayName": "Run hunting queries",
        "id": "dd98c7f5-2d42-42d3-a0e4-633161547251",
        "isEnabled": True,
        "origin": "Application",
        "value": "ThreatHunting.Read.All"
    },
    "de023814-96df-4f53-9376-1e2891ef5a18": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all users' shift schedule preferences without a signed-in user.",
        "displayName": "Read all user shift preferences",
        "id": "de023814-96df-4f53-9376-1e2891ef5a18",
        "isEnabled": True,
        "origin": "Application",
        "value": "UserShiftPreferences.Read.All"
    },
    "de89b5e4-5b8f-48eb-8925-29c2b33bd8bd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write custom security attribute assignments for all principals in the tenant without a signed in user.",
        "displayName": "Read and write custom security attribute assignments",
        "id": "de89b5e4-5b8f-48eb-8925-29c2b33bd8bd",
        "isEnabled": True,
        "origin": "Application",
        "value": "CustomSecAttributeAssignment.ReadWrite.All"
    },
    "df01ed3b-eb61-4eca-9965-6b3d789751b2": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read online meeting artifacts in your organization, without a signed-in user.",
        "displayName": "Read online meeting artifacts",
        "id": "df01ed3b-eb61-4eca-9965-6b3d789751b2",
        "isEnabled": True,
        "origin": "Application",
        "value": "OnlineMeetingArtifact.Read.All"
    },
    "df021288-bdef-4463-88db-98f22de89214": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read user profiles without a signed in user.",
        "displayName": "Read all users' full profiles",
        "id": "df021288-bdef-4463-88db-98f22de89214",
        "isEnabled": True,
        "origin": "Application",
        "value": "User.Read.All"
    },
    "dfb0dd15-61de-45b2-be36-d6a69fba3c79": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create chat and channel messages, without a signed in user. The app specifies which user appears as the sender, and can backdate the message to appear as if it was sent long ago. The messages can be sent to any chat or channel in the organization.",
        "displayName": "Create chat and channel messages with anyone's identity and with any timestamp",
        "id": "dfb0dd15-61de-45b2-be36-d6a69fba3c79",
        "isEnabled": True,
        "origin": "Application",
        "value": "Teamwork.Migrate.All"
    },
    "e0ac9e1b-cb65-4fc5-87c5-1a8bc181f648": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the structure of schools and classes in the organization's roster and education-specific information about all users to be read.",
        "displayName": "Read the organization's roster",
        "id": "e0ac9e1b-cb65-4fc5-87c5-1a8bc181f648",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduRoster.Read.All"
    },
    "e0b77adb-e790-44a3-b0a0-257d06303687": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read threat intellgence information, such as indicators, observations, and and articles, without a signed in user.",
        "displayName": "Read all Threat Intelligence Information",
        "id": "e0b77adb-e790-44a3-b0a0-257d06303687",
        "isEnabled": True,
        "origin": "Application",
        "value": "ThreatIntelligence.Read.All"
    },
    "e125258e-8c8a-42a8-8f55-ab502afa52f3": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, create, and update attack simulation and training data for an organization without a signed-in user.",
        "displayName": "Read, create, and update all attack simulation data of an organization",
        "id": "e125258e-8c8a-42a8-8f55-ab502afa52f3",
        "isEnabled": True,
        "origin": "Application",
        "value": "AttackSimulation.ReadWrite.All"
    },
    "e12dae10-5a57-4817-b79d-dfbec5348930": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read apps in the app catalogs without a signed-in user.",
        "displayName": "Read all app catalogs",
        "id": "e12dae10-5a57-4817-b79d-dfbec5348930",
        "isEnabled": True,
        "origin": "Application",
        "value": "AppCatalog.Read.All"
    },
    "e1a88a34-94c4-4418-be12-c87b00e26bea": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all organizational contacts without a signed-in user.  These contacts are managed by the organization and are different from a user's personal contacts.",
        "displayName": "Read organizational contacts",
        "id": "e1a88a34-94c4-4418-be12-c87b00e26bea",
        "isEnabled": True,
        "origin": "Application",
        "value": "OrgContact.Read.All"
    },
    "e2a3a72e-5f79-4c64-b1b1-878b674786c9": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update, and delete mail in all mailboxes without a signed-in user. Does not include permission to send mail.",
        "displayName": "Read and write mail in all mailboxes",
        "id": "e2a3a72e-5f79-4c64-b1b1-878b674786c9",
        "isEnabled": True,
        "origin": "Application",
        "value": "Mail.ReadWrite"
    },
    "e321f0bb-e7f7-481e-bb28-e3b0b32d4bd0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read your organization\u2019s identity (authentication) providers\u2019 properties without a signed in user.",
        "displayName": "Read identity providers",
        "id": "e321f0bb-e7f7-481e-bb28-e3b0b32d4bd0",
        "isEnabled": True,
        "origin": "Application",
        "value": "IdentityProvider.Read.All"
    },
    "e32c2cd9-0124-4e44-88fc-772cd98afbdb": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to add and remove members from all chats where the associated Teams application is installed, without a signed-in user.",
        "displayName": "Add and remove members from all chats where the associated Teams application is installed.",
        "id": "e32c2cd9-0124-4e44-88fc-772cd98afbdb",
        "isEnabled": True,
        "origin": "Application",
        "value": "ChatMember.ReadWrite.WhereInstalled"
    },
    "e330c4f0-4170-414e-a55a-2f022ec2b57b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write the properties relating to the Microsoft Intune Role-Based Access Control (RBAC) settings, without a signed-in user.",
        "displayName": "Read and write Microsoft Intune RBAC settings",
        "id": "e330c4f0-4170-414e-a55a-2f022ec2b57b",
        "isEnabled": True,
        "origin": "Application",
        "value": "DeviceManagementRBAC.ReadWrite.All"
    },
    "e688c61f-d4c6-4d64-a197-3bcf6ba1d6ad": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write inbound data flows without a signed-in user.",
        "displayName": "Manage inbound flow definitions",
        "id": "e688c61f-d4c6-4d64-a197-3bcf6ba1d6ad",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-InboundFlow.ReadWrite.All"
    },
    "ea047cc2-df29-4f3e-83a3-205de61501ca": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all term store data, without a signed-in user. This includes all sets, groups and terms in the term store.",
        "displayName": "Read all term store data",
        "id": "ea047cc2-df29-4f3e-83a3-205de61501ca",
        "isEnabled": True,
        "origin": "Application",
        "value": "TermStore.Read.All"
    },
    "eb158f57-df43-4751-8b21-b8932adb3d34": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allow the application to create, update and delete any data from Records Management, such as configuration, labels, and policies without the signed in user.",
        "displayName": "Read and write Records Management configuration, labels and policies",
        "id": "eb158f57-df43-4751-8b21-b8932adb3d34",
        "isEnabled": True,
        "origin": "Application",
        "value": "RecordsManagement.ReadWrite.All"
    },
    "ed4fca05-be46-441f-9803-1873825f8fdb": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write to all security alerts, without a signed-in user.",
        "displayName": "Read and write to all security alerts",
        "id": "ed4fca05-be46-441f-9803-1873825f8fdb",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityAlert.ReadWrite.All"
    },
    "eda0971c-482e-4345-b28f-69c309cb8a34": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write data connectors without a signed-in user.",
        "displayName": "Manage data connector definitions",
        "id": "eda0971c-482e-4345-b28f-69c309cb8a34",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-DataConnector.ReadWrite.All"
    },
    "edb419d6-7edc-42a3-9345-509bfdf5d87c": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read time-based eligibility schedules for access to Azure AD groups, without a signed-in user.",
        "displayName": "Read eligibility schedules for access to Azure AD groups",
        "id": "edb419d6-7edc-42a3-9345-509bfdf5d87c",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrivilegedEligibilitySchedule.Read.AzureADGroup"
    },
    "ee1460f0-368b-4153-870a-4e1ca7e72c42": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows\u00a0the\u00a0app\u00a0to\u00a0read\u00a0subject\u00a0rights requests\u00a0without a\u00a0signed-in\u00a0user.",
        "displayName": "Read\u00a0all subject\u00a0rights requests",
        "id": "ee1460f0-368b-4153-870a-4e1ca7e72c42",
        "isEnabled": True,
        "origin": "Application",
        "value": "SubjectRightsRequest.Read.All"
    },
    "ee353f83-55ef-4b78-82da-555bfa2b4b95": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all admin report settings, such as whether to display concealed information in reports, without a signed-in user.",
        "displayName": "Read all admin report settings",
        "id": "ee353f83-55ef-4b78-82da-555bfa2b4b95",
        "isEnabled": True,
        "origin": "Application",
        "value": "ReportSettings.Read.All"
    },
    "ee49e170-1dd1-4030-b44c-61ad6e98f743": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read all question and answers, without a signed-in user.",
        "displayName": "Read all Question and Answers ",
        "id": "ee49e170-1dd1-4030-b44c-61ad6e98f743",
        "isEnabled": True,
        "origin": "Application",
        "value": "QnA.Read.All"
    },
    "eedb7fdd-7539-4345-a38b-4839e4a84cbd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read programs and program controls in the organization, without a signed-in user.",
        "displayName": "Read all programs",
        "id": "eedb7fdd-7539-4345-a38b-4839e4a84cbd",
        "isEnabled": True,
        "origin": "Application",
        "value": "ProgramControl.Read.All"
    },
    "ef02f2e7-e22d-4c77-8614-8f765683b86e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read tenant-wide people settings without a signed-in user.",
        "displayName": "Read all tenant-wide people settings",
        "id": "ef02f2e7-e22d-4c77-8614-8f765683b86e",
        "isEnabled": True,
        "origin": "Application",
        "value": "PeopleSettings.Read.All"
    },
    "ef31918f-2d50-4755-8943-b8638c0a077e": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all role-based access control (RBAC) alerts for your company's directory, without a signed-in user. This includes reading alert statuses, alert definitions, alert configurations and incidents that lead to an alert.",
        "displayName": "Read all alert data for your company's directory",
        "id": "ef31918f-2d50-4755-8943-b8638c0a077e",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagementAlert.Read.Directory"
    },
    "ef54d2bf-783f-4e0f-bca1-3210c0444d99": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update, and delete events of all calendars without a signed-in user.",
        "displayName": "Read and write calendars in all mailboxes",
        "id": "ef54d2bf-783f-4e0f-bca1-3210c0444d99",
        "isEnabled": True,
        "origin": "Application",
        "value": "Calendars.ReadWrite"
    },
    "ef5f7d5c-338f-44b0-86c3-351f46c8bb5f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, update, delete and perform actions on access reviews, reviewers, decisions and settings in the organization, without a signed-in user.",
        "displayName": "Manage all access reviews",
        "id": "ef5f7d5c-338f-44b0-86c3-351f46c8bb5f",
        "isEnabled": True,
        "origin": "Application",
        "value": "AccessReview.ReadWrite.All"
    },
    "f0c341be-8348-4989-8e43-660324294538": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's network access policies, without a signed-in user.",
        "displayName": "Read and write all security and routing policies for network access",
        "id": "f0c341be-8348-4989-8e43-660324294538",
        "isEnabled": True,
        "origin": "Application",
        "value": "NetworkAccessPolicy.ReadWrite.All"
    },
    "f10e1f91-74ed-437f-a6fd-d6ae88e26c1f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read all users\u2019 tasks and task lists in your organization, without a signed-in user.",
        "displayName": "Read all users\u2019 tasks and tasklist",
        "id": "f10e1f91-74ed-437f-a6fd-d6ae88e26c1f",
        "isEnabled": True,
        "origin": "Application",
        "value": "Tasks.Read.All"
    },
    "f12eb8d6-28e3-46e6-b2c0-b7e4dc69fc95": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read, edit or write all term store data, without a signed-in user. This includes all sets, groups and terms in the term store.",
        "displayName": "Read and write all term store data",
        "id": "f12eb8d6-28e3-46e6-b2c0-b7e4dc69fc95",
        "isEnabled": True,
        "origin": "Application",
        "value": "TermStore.ReadWrite.All"
    },
    "f20584af-9290-4153-9280-ff8bb2c0ea7f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to manage restricted resources based on the other permissions granted to the app, without a signed-in user.",
        "displayName": "Manage restricted resources in the directory",
        "id": "f20584af-9290-4153-9280-ff8bb2c0ea7f",
        "isEnabled": True,
        "origin": "Application",
        "value": "Directory.Write.Restricted"
    },
    "f2bf083f-0179-402a-bedb-b2784de8a49b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read or update security actions, without a signed-in user.",
        "displayName": "Read and update your organization's security actions",
        "id": "f2bf083f-0179-402a-bedb-b2784de8a49b",
        "isEnabled": True,
        "origin": "Application",
        "value": "SecurityActions.ReadWrite.All"
    },
    "f2d21f22-5d80-499e-91cc-0a8a4ce16f54": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to fully manage the data associated with the business scenarios it owns, without a signed-in user.",
        "displayName": "Read and write data for all business scenarios this app creates or owns",
        "id": "f2d21f22-5d80-499e-91cc-0a8a4ce16f54",
        "isEnabled": True,
        "origin": "Application",
        "value": "BusinessScenarioData.ReadWrite.OwnedBy"
    },
    "f3a65bd4-b703-46df-8f7e-0174fea562aa": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Create channels in any team, without a signed-in user.",
        "displayName": "Create channels",
        "id": "f3a65bd4-b703-46df-8f7e-0174fea562aa",
        "isEnabled": True,
        "origin": "Application",
        "value": "Channel.Create"
    },
    "f431331c-49a6-499f-be1c-62af19c34a9d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write external connections without a signed-in user. The app can only read and write external connections that it is authorized to, or it can create new external connections. ",
        "displayName": "Read and write external connections",
        "id": "f431331c-49a6-499f-be1c-62af19c34a9d",
        "isEnabled": True,
        "origin": "Application",
        "value": "ExternalConnection.ReadWrite.OwnedBy"
    },
    "f431cc63-a2de-48c4-8054-a34bc093af84": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to create, read, update and delete all\u00a0class assignments without grades for all users without a signed-in user.",
        "displayName": "Create, read, update and delete all\u00a0class assignments without grades",
        "id": "f431cc63-a2de-48c4-8054-a34bc093af84",
        "isEnabled": True,
        "origin": "Application",
        "value": "EduAssignments.ReadWriteBasic.All"
    },
    "f5b3f73d-6247-44df-a74c-866173fddab0": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read and update printers without a signed-in user. Does not allow creating (registering) or deleting (unregistering) printers.",
        "displayName": "Read and update printers",
        "id": "f5b3f73d-6247-44df-a74c-866173fddab0",
        "isEnabled": True,
        "origin": "Application",
        "value": "Printer.ReadWrite.All"
    },
    "f6b49018-60ab-4f81-83bd-22caeabfed2d": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to join group calls and scheduled meetings in your organization, without a signed-in user. \u00a0The app will be joined with the privileges of a directory user to meetings in your organization.",
        "displayName": "Join group calls and meetings as an app",
        "id": "f6b49018-60ab-4f81-83bd-22caeabfed2d",
        "isEnabled": True,
        "origin": "Application",
        "value": "Calls.JoinGroupCall.All"
    },
    "f6e9e124-4586-492f-adc0-c6f96e4823fd": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read details of delegated admin relationships with customers like access details (that includes roles) and the duration as well as specific role assignments to security groups without a signed-in user.",
        "displayName": "Read Delegated Admin relationships with customers",
        "id": "f6e9e124-4586-492f-adc0-c6f96e4823fd",
        "isEnabled": True,
        "origin": "Application",
        "value": "DelegatedAdminRelationship.Read.All"
    },
    "f6f5d10b-3024-4d1d-b674-aae4df4a1a73": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read current and previous IndustryData runs without a signed-in user.",
        "displayName": "View current and previous runs",
        "id": "f6f5d10b-3024-4d1d-b674-aae4df4a1a73",
        "isEnabled": True,
        "origin": "Application",
        "value": "IndustryData-Run.Read.All"
    },
    "f8f035bb-2cce-47fb-8bf5-7baf3ecbee48": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows an app to read your organization's threat assessment requests, without a signed-in user.",
        "displayName": "Read threat assessment requests",
        "id": "f8f035bb-2cce-47fb-8bf5-7baf3ecbee48",
        "isEnabled": True,
        "origin": "Application",
        "value": "ThreatAssessment.Read.All"
    },
    "fb221be6-99f2-473f-bd32-01c6a0e9ca3b": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and write your organization's authorization policy without a signed in user. For example, authorization policies can control some of the permissions that the out-of-the-box user role has by default.",
        "displayName": "Read and write your organization's authorization policy",
        "id": "fb221be6-99f2-473f-bd32-01c6a0e9ca3b",
        "isEnabled": True,
        "origin": "Application",
        "value": "Policy.ReadWrite.Authorization"
    },
    "fbf67eee-e074-4ef7-b965-ab5ce1c1f689": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the application to read the metadata of print jobs without a signed-in user.\u00a0Does not allow access to print job document content.",
        "displayName": "Read basic information for print jobs",
        "id": "fbf67eee-e074-4ef7-b965-ab5ce1c1f689",
        "isEnabled": True,
        "origin": "Application",
        "value": "PrintJob.ReadBasic.All"
    },
    "fd7ccf6b-3d28-418b-9701-cd10f5cd2fd4": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to anonymously join group calls and scheduled meetings in your organization, without a signed-in user. \u00a0The app will be joined as a guest to meetings in your organization.",
        "displayName": "Join group calls and meetings as a guest",
        "id": "fd7ccf6b-3d28-418b-9701-cd10f5cd2fd4",
        "isEnabled": True,
        "origin": "Application",
        "value": "Calls.JoinGroupCallAsGuest.All"
    },
    "fd9ce730-a250-40dc-bd44-8dc8d20f39ea": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows a Teams app to read, install, upgrade, and uninstall all tabs for any chat, without a signed-in user.",
        "displayName": "Allow the Teams app to manage all tabs for all chats",
        "id": "fd9ce730-a250-40dc-bd44-8dc8d20f39ea",
        "isEnabled": True,
        "origin": "Application",
        "value": "TeamsTab.ReadWriteForChat.All"
    },
    "fdc4c997-9942-4479-bfcb-75a36d1138df": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read policies for privileged role-based access control (RBAC) assignments of your company's directory, without a signed-in user.",
        "displayName": "Read all policies for privileged role assignments of your company's directory",
        "id": "fdc4c997-9942-4479-bfcb-75a36d1138df",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleManagementPolicy.Read.Directory"
    },
    "fee28b28-e1f3-4841-818e-2704dc62245f": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read and manage the eligible role-based access control (RBAC) assignments and schedules for your company's directory, without a signed-in user. This includes managing eligible directory role membership, and reading directory role templates, directory roles and eligible memberships.",
        "displayName": "Read, update, and delete all eligible role assignments and schedules for your company's directory",
        "id": "fee28b28-e1f3-4841-818e-2704dc62245f",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleEligibilitySchedule.ReadWrite.Directory"
    },
    "ff278e11-4a33-4d0c-83d2-d01dc58929a5": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read the eligible role-based access control (RBAC) assignments and schedules for your company's directory, without a signed-in user. This includes reading directory role templates, and directory roles.",
        "displayName": "Read all eligible role assignments and role schedules for your company's directory",
        "id": "ff278e11-4a33-4d0c-83d2-d01dc58929a5",
        "isEnabled": True,
        "origin": "Application",
        "value": "RoleEligibilitySchedule.Read.Directory"
    },
    "fff194f1-7dce-4428-8301-1badb5518201": {
        "allowedMemberTypes": [
            "Application"
        ],
        "description": "Allows the app to read trust framework key set properties without a signed-in user.",
        "displayName": "Read trust framework key sets",
        "id": "fff194f1-7dce-4428-8301-1badb5518201",
        "isEnabled": True,
        "origin": "Application",
        "value": "TrustFrameworkKeySet.Read.All"
    }
}