"""Module containing constants in azol"""
from dataclasses import dataclass
from pathlib import Path

ARMURL="https://management.azure.com"
GRAPHBETAURL="https://graph.microsoft.com/beta"
GRAPHV1URL="https://graph.microsoft.com/v1.0"
KEYVAULTURL="https://vault.azure.net"
KEYVAULTAPIVERSION="7.3"
IDENTITYPLATFORMURL="https://login.microsoftonline.com"
DEFAULTSCOPE=".default"

homeDirectory = Path.home()
AZOL_HOME = str(homeDirectory) + "/.azol"
PROVIDER_CACHE_DIR = AZOL_HOME + "/provider_cache"
PROVIDER_CACHE = AZOL_HOME + "/provider_cache/refresh"
AZOLSECRETPROVIDERFOLDER = AZOL_HOME + "/secrets"
TOKENCACHEDIR = AZOL_HOME + "/token_cache"

@dataclass(frozen=True)
class UserAgents:
    """
        A data class containing constant strings for known user agents
    """
    Iphone_Safari="Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Mobile/15E148 Safari/604."
    Iphone_Chrome="Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/360.1.737798518 Mobile/15E148 Safari/604."
    Android_Chrome="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.3"
    OSX_Safari="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.10 Safari/605.1.1"
    OSX_Chrome="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.3"
    Windows_Chrome="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3"
    Linux_Chrome="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3"
    Windows_Edge="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0."

@dataclass(frozen=True)
class OAuthResourceIDs:
    """
        A data class containing constant strings for OAuth flow types
    """
    Arm="https://management.azure.com"
    Graph="https://graph.microsoft.com"
    KeyVault="https://vault.azure.net"
    CosmosDB="https://cosmos.azure.com"
    AzureDataLake="https://datalake.azure.net"
    AzureSQL="https://database.windows.net"
    OneNote="https://onenote.com"
    AzureDevOps="https://app.vssps.visualstudio.com"
    StorageAccount="https://storage.azure.com"
    Sharepoint="https://microsoft.sharepoint.com"
    PowerBI="https://analysis.windows.net/powerbi/api"
    PowerAutomate="https://service.flow.microsoft.com"
    DynamicsCRM="https://admin.services.crm.dynamics.com"
    Intune="https://api.manage.microsoft.com"
    OfficeManagement="https://manage.office.com"
    DynamicsBusinessCentral="https://dynamics.microsoft.com/business-central/overview"
    Yammer="https://api.yammer.com"
    SkypeForBusiness="https://api.skypeforbusiness.com"
    AzureCommunicationServices="https://auth.msft.communication.azure.com"


@dataclass(frozen=True)
class OAUTHFLOWS:
    """
        A data class containing constant strings for OAuth flow types
    """
    CLIENT_CREDENTIALS="client_credentials"
    DEVICE_CODE="device_code"
    REFRESH_TOKEN="refresh_token"
    RAW_TOKEN="raw_token"
    AUTHORIZATION_CODE="authorization_code"

roleNameMap = {
    "ae79f266-94d4-4dab-b730-feca7e132178": "Catalog Owner",
    "44272f93-9762-48e8-af59-1b5351b1d6b3": "Catalog Reader",
    "7f480852-ebdc-47d4-87de-0d8498384a83": "Access Package Manager",
    "e2182095-804a-4656-ae11-64734e9b7ae5": "Access Package Assignment Manager",
    "62e90394-69f5-4237-9190-012177145e10": "Global Administrator",
    "10dae51f-b6af-4016-8d66-8c2a99b929b3": "Guest User",
    "2af84b1e-32c8-42b7-82bc-daa82404023b": "Restricted Guest User",
    "95e79109-95c0-4d8e-aee3-d01accf2d47b": "Guest Inviter",
    "fe930be7-5e62-47db-91af-98c3a49a38b1": "User Administrator",
    "729827e3-9c14-49f7-bb1b-9608f156bbb8": "Helpdesk Administrator",
    "f023fd81-a637-4b56-95fd-791ac0226033": "Service Support Administrator",
    "b0f54661-2d74-4c50-afa3-1ec803f12efe": "Billing Administrator",
    "a0b1b346-4d3e-4e8b-98f8-753987be4970": "User",
    "4ba39ca4-527c-499a-b93d-d9b492c50246": "Partner Tier1 Support",
    "e00e864a-17c5-4a4b-9c06-f5b95a8d5bd8": "Partner Tier2 Support",
    "88d8e3e3-8f55-4a1e-953a-9b9898b8876b": "Directory Readers",
    "9360feb5-f418-4baa-8175-e2a00bac4301": "Directory Writers",
    "29232cdf-9323-42fd-ade2-1d097af3e4de": "Exchange Administrator",
    "f28a1f50-f6e7-4571-818b-6a12f2af6b6c": "SharePoint Administrator",
    "75941009-915a-4869-abe7-691bff18279e": "Skype for Business Administrator",
    "d405c6df-0af8-4e3b-95e4-4d06e542189e": "Device Users",
    "9f06204d-73c1-4d4c-880a-6edb90606fd8": "Azure AD Joined Device Local Administrator",
    "9c094953-4995-41c8-84c8-3ebb9b32c93f": "Device Join",
    "c34f683f-4d5a-4403-affd-6615e00e3a7f": "Workplace Device Join",
    "17315797-102d-40b4-93e0-432062caca18": "Compliance Administrator",
    "d29b2b05-8046-44ba-8758-1e26182fcf32": "Directory Synchronization Accounts",
    "2b499bcd-da44-4968-8aec-78e1674fa64d": "Device Managers",
    "9b895d92-2cd3-44c7-9d02-a6ac2d5ea5c3": "Application Administrator",
    "cf1c38e5-3621-4004-a7cb-879624dced7c": "Application Developer",
    "5d6b6bb7-de71-4623-b4af-96380a352509": "Security Reader",
    "194ae4cb-b126-40b2-bd5b-6091b380977d": "Security Administrator",
    "e8611ab8-c189-46e8-94e1-60213ab1f814": "Privileged Role Administrator",
    "3a2c62db-5318-420d-8d74-23affee5d9d5": "Intune Administrator",
    "158c047a-c907-4556-b7ef-446551a6b5f7": "Cloud Application Administrator",
    "5c4f9dcd-47dc-4cf7-8c9a-9e4207cbfc91": "Customer LockBox Access Approver",
    "44367163-eba1-44c3-98af-f5787879f96a": "Dynamics 365 Administrator",
    "a9ea8996-122f-4c74-9520-8edcd192826c": "Fabric Administrator",
    "b1be1c3e-b65d-4f19-8427-f6fa0d97feb9": "Conditional Access Administrator",
    "4a5d8f65-41da-4de4-8968-e035b65339cf": "Reports Reader",
    "790c1fb9-7f7d-4f88-86a1-ef1f95c05c1b": "Message Center Reader",
    "7495fdc4-34c4-4d15-a289-98788ce399fd": "Azure Information Protection Administrator",
    "38a96431-2bdf-4b4c-8b6e-5d3d8abac1a4": "Desktop Analytics Administrator",
    "4d6ac14f-3453-41d0-bef9-a3e0c569773a": "License Administrator",
    "7698a772-787b-4ac8-901f-60d6b08affd2": "Cloud Device Administrator",
    "c4e39bd9-1100-46d3-8c65-fb160da0071f": "Authentication Administrator",
    "7be44c8a-adaf-4e2a-84d6-ab2649e08a13": "Privileged Authentication Administrator",
    "baf37b3a-610e-45da-9e62-d9d1e5e8914b": "Teams Communications Administrator",
    "f70938a0-fc10-4177-9e90-2178f8765737": "Teams Communications Support Engineer",
    "fcf91098-03e3-41a9-b5ba-6f0ec8188a12": "Teams Communications Support Specialist",
    "69091246-20e8-4a56-aa4d-066075b2a7a8": "Teams Administrator",
    "eb1f4a8d-243a-41f0-9fbd-c7cdf6c5ef7c": "Insights Administrator",
    "ac16e43d-7b2d-40e0-ac05-243ff356ab5b": "Message Center Privacy Reader",
    "6e591065-9bad-43ed-90f3-e9424366d2f0": "External ID User Flow Administrator",
    "0f971eea-41eb-4569-a71e-57bb8a3eff1e": "External ID User Flow Attribute Administrator",
    "aaf43236-0c0d-4d5f-883a-6955382ac081": "B2C IEF Keyset Administrator",
    "3edaf663-341e-4475-9f94-5c398ef6c070": "B2C IEF Policy Administrator",
    "be2f45a1-457d-42af-a067-6ec1fa63bc45": "External Identity Provider Administrator",
    "e6d1a23a-da11-4be4-9570-befc86d067a7": "Compliance Data Administrator",
    "5f2222b1-57c3-48ba-8ad5-d4759f1fde6f": "Security Operator",
    "74ef975b-6605-40af-a5d2-b9539d836353": "Kaizala Administrator",
    "f2ef992c-3afb-46b9-b7cf-a126ee74c451": "Global Reader",
    "0964bb5e-9bdb-4d7b-ac29-58e794862a40": "Search Administrator",
    "8835291a-918c-4fd7-a9ce-faa49f0cf7d9": "Search Editor",
    "966707d0-3269-4727-9be2-8c3a10f19b9d": "Password Administrator",
    "644ef478-e28f-4e28-b9dc-3fdde9aa0b1f": "Printer Administrator",
    "e8cef6f1-e4bd-4ea8-bc07-4b8d950f4477": "Printer Technician",
    "0526716b-113d-4c15-b2c8-68e3c22b9f80": "Authentication Policy Administrator",
    "fdd7a751-b60b-444a-984c-02652fe8fa1c": "Groups Administrator",
    "11648597-926c-4cf3-9c36-bcebb0ba8dcc": "Power Platform Administrator",
    "e3973bdf-4987-49ae-837a-ba8e231c7286": "Azure DevOps Administrator",
    "8ac3fc64-6eca-42ea-9e69-59f4c7b60eb2": "Hybrid Identity Administrator",
    "2b745bdf-0803-4d80-aa65-822c4493daac": "Office Apps Administrator",
    "d37c8bed-0711-4417-ba38-b4abe66ce4c2": "Network Administrator",
    "31e939ad-9672-4796-9c2e-873181342d2d": "Insights Business Leader",
    "3d762c5a-1b6c-493f-843e-55a3b42923d4": "Teams Devices Administrator",
    "c430b396-e693-46cc-96f3-db01bf8bb62a": "Attack Simulation Administrator",
    "9c6df0f2-1e7c-4dc3-b195-66dfbd24aa8f": "Attack Payload Author",
    "75934031-6c7e-415a-99d7-48dbd49e875e": "Usage Summary Reports Reader",
    "b5a8dcf3-09d5-43a9-a639-8e29ef291470": "Knowledge Administrator",
    "744ec460-397e-42ad-a462-8b3f9747a02c": "Knowledge Manager",
    "8329153b-31d0-4727-b945-745eb3bc5f31": "Domain Name Administrator",
    "8424c6f0-a189-499e-bbd0-26c1753c96d4": "Attribute Definition Administrator",
    "58a13ea3-c632-46ae-9ee0-9c0d43cd7f3d": "Attribute Assignment Administrator",
    "1d336d2c-4ae8-42ef-9711-b3604ce3fc2c": "Attribute Definition Reader",
    "ffd52fa5-98dc-465c-991d-fc073eb59f8f": "Attribute Assignment Reader",
    "31392ffb-586c-42d1-9346-e59415a2cc4e": "Exchange Recipient Administrator",
    "45d8d3c5-c802-45c6-b32a-1d70b5e1e86e": "Identity Governance Administrator",
    "892c5842-a9a6-463a-8041-72aa08ca3cf6": "Cloud App Security Administrator",
    "32696413-001a-46ae-978c-ce0f6b3620d2": "Windows Update Deployment Administrator",
    "11451d60-acb2-45eb-a7d6-43d0f0125c13": "Windows 365 Administrator",
    "3f1acade-1e04-4fbc-9b69-f0302cd84aef": "Edge Administrator",
    "810a2642-a034-447f-a5e8-41beaa378541": "Yammer Administrator",
    "25a516ed-2fa0-40ea-a2d0-12923a21473a": "Authentication Extensibility Administrator",
    "e300d9e7-4a2b-4295-9eff-f1c78b36cc98": "Virtual Visits Administrator",
    "25df335f-86eb-4119-b717-0ff02de207e9": "Insights Analyst",
    "1501b917-7653-4ff9-a4b5-203eaf33784f": "Microsoft Hardware Warranty Administrator",
    "281fe777-fb20-4fbb-b7a3-ccebce5b0d96": "Microsoft Hardware Warranty Specialist",
    "112ca1a2-15ad-4102-995e-45b0bc479a6a": "Tenant Creator",
    "59d46f88-662b-457b-bceb-5c3809e5908f": "Lifecycle Workflows Administrator",
    "92b086b3-e367-4ef2-b869-1de128fb986e": "Viva Goals Administrator",
    "27460883-1df1-4691-b032-3b79643e5e63": "User Experience Success Manager",
    "af78dc32-cf4d-46f9-ba4e-4428526346b5": "Permissions Management Administrator",
    "507f53e4-4e52-4077-abd3-d2e1558b6ea2": "Organizational Messages Writer",
    "ac434307-12b9-4fa1-a708-88bf58caabc1": "Global Secure Access Administrator",
    "87761b17-1ed2-4af3-9acd-92a150038160": "Viva Pulse Administrator",
    "dd13091a-6207-4fc0-82ba-3641e056ab95": "Extended Directory User Administrator",
    "5b784334-f94b-471a-a387-e7219fc49ca2": "Attribute Log Administrator",
    "9c99539d-8186-4804-835f-fd51ef9e2dcd": "Attribute Log Reader",
    "aa38014f-0993-46e9-9b45-30501a20909d": "Teams Telephony Administrator",
    "963797fb-eb3b-4cde-8ce3-5878b3f32a3f": "Dynamics 365 Business Central Administrator",
    "8c8b803f-96e1-4129-9349-20738d9f9652": "Microsoft 365 Migration Administrator",
    "1a7d78b6-429f-476b-b8eb-35fb715fffd4": "SharePoint Embedded Administrator",
    "92ed04bf-c94a-4b82-9729-b799a7a4c178": "Organizational Branding Administrator",
    "e48398e2-f4bb-4074-8f31-4586725e205b": "Organizational Messages Approver",
    "8311e382-0749-4cb8-b61a-304f252e45ec": "AcrPush",
    "312a565d-c81f-4fd8-895a-4e21e48d571c": "API Management Service Contributor",
    "7f951dda-4ed3-4680-a7ca-43fe172d538d": "AcrPull",
    "6cef56e8-d556-48e5-a04f-b8e64114680f": "AcrImageSigner",
    "c2f4ef07-c644-48eb-af81-4b1b4947fb11": "AcrDelete",
    "cdda3590-29a3-44f6-95f2-9f980659eb04": "AcrQuarantineReader",
    "c8d4ff99-41c3-41a8-9f60-21dfdad59608": "AcrQuarantineWriter",
    "e022efe7-f5ba-4159-bbe4-b44f577e9b61": "API Management Service Operator Role",
    "71522526-b88f-4d52-b57f-d31fc3546d0d": "API Management Service Reader Role",
    "ae349356-3a1b-4a5e-921d-050484c6347e": "Application Insights Component Contributor",
    "08954f03-6346-4c2e-81c0-ec3a5cfae23b": "Application Insights Snapshot Debugger",
    "fd1bd22b-8476-40bc-a0bc-69b95687b9f3": "Attestation Reader",
    "4fe576fe-1146-4730-92eb-48519fa6bf9f": "Automation Job Operator",
    "5fb5aef8-1081-4b8e-bb16-9d5d0385bab5": "Automation Runbook Operator",
    "d3881f73-407a-4167-8283-e981cbba0404": "Automation Operator",
    "4f8fab4f-1852-4a58-a46a-8eaf358af14a": "Avere Contributor",
    "c025889f-8102-4ebf-b32c-fc0c6f0c6bd9": "Avere Operator",
    "0ab0b1a8-8aac-4efd-b8c2-3ee1fb270be8": "Azure Kubernetes Service Cluster Admin Role",
    "4abbcc35-e782-43d8-92c5-2d3f1bd2253f": "Azure Kubernetes Service Cluster User Role",
    "423170ca-a8f6-4b0f-8487-9e4eb8f49bfa": "Azure Maps Data Reader",
    "6f12a6df-dd06-4f3e-bcb1-ce8be600526a": "Azure Stack Registration Owner",
    "5e467623-bb1f-42f4-a55d-6e525e11384b": "Backup Contributor",
    "fa23ad8b-c56e-40d8-ac0c-ce449e1d2c64": "Billing Reader",
    "a795c7a0-d4a2-40c1-ae25-d81f01202912": "Backup Reader",
    "31a002a1-acaf-453e-8a5b-297c9ca1ea24": "Blockchain Member Node Access (Preview)",
    "5e3c6656-6cfa-4708-81fe-0de47ac73342": "BizTalk Contributor",
    "426e0c7f-0c7e-4658-b36f-ff54d6c29b45": "CDN Endpoint Contributor",
    "ec156ff8-a8d1-4d15-830c-5b80698ca432": "CDN Profile Contributor",
    "8f96442b-4075-438f-813d-ad51ab4019af": "CDN Profile Reader",
    "b34d265f-36f7-4a0d-a4d4-e158ca92e90f": "Classic Network Contributor",
    "86e8f5dc-a6e9-4c67-9d15-de283e8eac25": "Classic Storage Account Contributor",
    "985d6b00-f706-48f5-a6fe-d0ca12fb668d": "Classic Storage Account Key Operator Service Role",
    "9106cda0-8a86-4e81-b686-29a22c54effe": "ClearDB MySQL DB Contributor",
    "d73bb868-a0df-4d4d-bd69-98a00b01fccb": "Classic Virtual Machine Contributor",
    "a97b65f3-24c7-4388-baec-2e87135dc908": "Cognitive Services User",
    "b59867f0-fa02-499b-be73-45a86b5b3e1c": "Cognitive Services Data Reader (Preview)",
    "25fbc0a9-bd7c-42a3-aa1a-3b75d497ee68": "Cognitive Services Contributor",
    "db7b14f2-5adf-42da-9f96-f2ee17bab5cb": "CosmosBackupOperator",
    "b24988ac-6180-42a0-ab88-20f7382dd24c": "Contributor",
    "fbdf93bf-df7d-467e-a4d2-9458aa1360c8": "Cosmos DB Account Reader Role",
    "434105ed-43f6-45c7-a02f-909b2ba83430": "Cost Management Contributor",
    "72fafb9e-0641-4937-9268-a91bfd8191a3": "Cost Management Reader",
    "add466c9-e687-43fc-8d98-dfcf8d720be5": "Data Box Contributor",
    "028f4ed7-e2a9-465e-a8f4-9c0ffdfdc027": "Data Box Reader",
    "673868aa-7521-48a0-acc6-0f60742d39f5": "Data Factory Contributor",
    "150f5e0c-0603-4f03-8c7f-cf70034c4e90": "Data Purger",
    "47b7735b-770e-4598-a7da-8b91488b4c88": "Data Lake Analytics Developer",
    "76283e04-6283-4c54-8f91-bcf1374a3c64": "DevTest Labs User",
    "5bd9cd88-fe45-4216-938b-f97437e15450": "DocumentDB Account Contributor",
    "befefa01-2a29-4197-83a8-272ff33ce314": "DNS Zone Contributor",
    "428e0ff0-5e57-4d9c-a221-2c70d0e0a443": "EventGrid EventSubscription Contributor",
    "2414bbcf-6497-4faf-8c65-045460748405": "EventGrid EventSubscription Reader",
    "b60367af-1334-4454-b71e-769d9a4f83d9": "Graph Owner",
    "8d8d5a11-05d3-4bda-a417-a08778121c7c": "HDInsight Domain Services Contributor",
    "03a6d094-3444-4b3d-88af-7477090a9e5e": "Intelligent Systems Account Contributor",
    "f25e0fa2-a7c8-4377-a976-54943a77a395": "Key Vault Contributor",
    "ee361c5d-f7b5-4119-b4b6-892157c8f64c": "Knowledge Consumer",
    "b97fb8bc-a8b2-4522-a38b-dd33c7e65ead": "Lab Creator",
    "73c42c96-874c-492b-b04d-ab87d138a893": "Log Analytics Reader",
    "92aaf0da-9dab-42b6-94a3-d43ce8d16293": "Log Analytics Contributor",
    "515c2055-d9d4-4321-b1b9-bd0c9a0f79fe": "Logic App Operator",
    "87a39d53-fc1b-424a-814c-f7e04687dc9e": "Logic App Contributor",
    "c7393b34-138c-406f-901b-d8cf2b17e6ae": "Managed Application Operator Role",
    "b9331d33-8a36-4f8c-b097-4f54124fdb44": "Managed Applications Reader",
    "f1a07417-d97a-45cb-824c-7a7467783830": "Managed Identity Operator",
    "e40ec5ca-96e0-45a2-b4ff-59039f2c2b59": "Managed Identity Contributor",
    "5d58bcaf-24a5-4b20-bdb6-eed9f69fbe4c": "Management Group Contributor",
    "ac63b705-f282-497d-ac71-919bf39d939d": "Management Group Reader",
    "43d0d8ad-25c7-4714-9337-8ba259a9fe05": "Monitoring Reader",
    "4d97b98b-1d4f-4787-a291-c67834d212e7": "Network Contributor",
    "5d28c62d-5b37-4476-8438-e587778df237": "New Relic APM Account Contributor",
    "8e3af657-a8ff-443c-a75c-2fe8c4bcb635": "Owner",
    "acdd72a7-3385-48ef-bd42-f606fba81ae7": "Reader",
    "e0f68234-74aa-48ed-b826-c38b57376e17": "Redis Cache Contributor",
    "c12c1c16-33a1-487b-954d-41c89c60f349": "Reader and Data Access",
    "36243c78-bf99-498c-9df9-86d9f8d28608": "Resource Policy Contributor",
    "188a0f2f-5c9e-469b-ae67-2aa5ce574b94": "Scheduler Job Collections Contributor",
    "7ca78c08-252a-4471-8644-bb5ff32d4ba0": "Search Service Contributor",
    "e3d13bf0-dd5a-482e-ba6b-9b8433878d10": "Security Manager (Legacy)",
    "39bc4728-0917-49c7-9d2c-d95423bc2eb4": "Security Reader",
    "8bbe83f1-e2a6-4df7-8cb4-4e04d4e5c827": "Spatial Anchors Account Contributor",
    "6670b86e-a3f7-4917-ac9b-5d6ab1be4567": "Site Recovery Contributor",
    "494ae006-db33-4328-bf46-533a6560a3ca": "Site Recovery Operator",
    "5d51204f-eb77-4b1c-b86a-2ec626c49413": "Spatial Anchors Account Reader",
    "dbaa88c4-0c30-4179-9fb3-46319faa6149": "Site Recovery Reader",
    "70bbe301-9835-447d-afdd-19eb3167307c": "Spatial Anchors Account Owner",
    "4939a1f6-9ae0-4e48-a1e0-f2cbe897382d": "SQL Managed Instance Contributor",
    "9b7fa17d-e63e-47b0-bb0a-15c516ac86ec": "SQL DB Contributor",
    "056cd41c-7e88-42e1-933e-88ba6a50c9c3": "SQL Security Manager",
    "17d1049b-9a84-46fb-8f53-869881c3d3ab": "Storage Account Contributor",
    "6d8ee4ec-f05a-4a1d-8b00-a9b17e38b437": "SQL Server Contributor",
    "81a9662b-bebf-436f-a333-f67b29880f12": "Storage Account Key Operator Service Role",
    "ba92f5b4-2d11-453d-a403-e96b0029c9fe": "Storage Blob Data Contributor",
    "b7e6dc6d-f1e8-4753-8033-0f276bb0955b": "Storage Blob Data Owner",
    "2a2b9908-6ea1-4ae2-8e65-a410df84e7d1": "Storage Blob Data Reader",
    "974c5e8b-45b9-4653-ba55-5f855dd0fb88": "Storage Queue Data Contributor",
    "8a0f0c08-91a1-4084-bc3d-661d67233fed": "Storage Queue Data Message Processor",
    "c6a89b2d-59bc-44d0-9896-0f6e12d7b80a": "Storage Queue Data Message Sender",
    "19e7f393-937e-4f77-808e-94535e297925": "Storage Queue Data Reader",
    "cfd33db0-3dd1-45e3-aa9d-cdbdf3b6f24e": "Support Request Contributor",
    "a4b10055-b0c7-44c2-b00f-c7b5b3550cf7": "Traffic Manager Contributor",
    "18d7d88d-d35e-4fb5-a5c3-7773c20a72d9": "User Access Administrator",
    "9980e02c-c2be-4d73-94e8-173b1dc7cf3c": "Virtual Machine Contributor",
    "2cc479cb-7b4d-49a8-b449-8c00fd0f0a4b": "Web Plan Contributor",
    "de139f84-1756-47ae-9be6-808fbbe84772": "Website Contributor",
    "090c5cfd-751d-490a-894a-3ce6f1109419": "Azure Service Bus Data Owner",
    "f526a384-b230-433a-b45c-95f59c4a2dec": "Azure Event Hubs Data Owner",
    "bbf86eb8-f7b4-4cce-96e4-18cddf81d86e": "Attestation Contributor",
    "61ed4efc-fab3-44fd-b111-e24485cc132a": "HDInsight Cluster Operator",
    "230815da-be43-4aae-9cb4-875f7bd000aa": "Cosmos DB Operator",
    "48b40c6e-82e0-4eb3-90d5-19e40f49b624": "Hybrid Server Resource Administrator",
    "5d1e5ee4-7c68-4a71-ac8b-0739630a3dfb": "Hybrid Server Onboarding",
    "a638d3c7-ab3a-418d-83e6-5f17a39d4fde": "Azure Event Hubs Data Receiver",
    "2b629674-e913-4c01-ae53-ef4638d8f975": "Azure Event Hubs Data Sender",
    "4f6d3b9b-027b-4f4c-9142-0e5a2a2247e0": "Azure Service Bus Data Receiver",
    "69a216fc-b8fb-44d8-bc22-1f3c2cd27a39": "Azure Service Bus Data Sender",
    "aba4ae5f-2193-4029-9191-0cb91df5e314": "Storage File Data SMB Share Reader",
    "0c867c2a-1d8c-454a-a3db-ab2ea1bdc8bb": "Storage File Data SMB Share Contributor",
    "b12aa53e-6015-4669-85d0-8515ebb3ae7f": "Private DNS Zone Contributor",
    "db58b8e5-c6ad-4a2a-8342-4190687cbf4a": "Storage Blob Delegator",
    "1d18fff3-a72a-46b5-b4a9-0b38a3cd7e63": "Desktop Virtualization User",
    "a7264617-510b-434b-a828-9731dc254ea7": "Storage File Data SMB Share Elevated Contributor",
    "41077137-e803-4205-871c-5a86e6a753b4": "Blueprint Contributor",
    "437d2ced-4a38-4302-8479-ed2bcb43d090": "Blueprint Operator",
    "ab8e14d6-4a74-4a29-9ba8-549422addade": "Microsoft Sentinel Contributor",
    "3e150937-b8fe-4cfb-8069-0eaf05ecd056": "Microsoft Sentinel Responder",
    "8d289c81-5878-46d4-8554-54e1e3d8b5cb": "Microsoft Sentinel Reader",
    "66bb4e9e-b016-4a94-8249-4c0511c2be84": "Policy Insights Data Writer (Preview)",
    "04165923-9d83-45d5-8227-78b77b0a687e": "SignalR AccessKey Reader",
    "8cf5e20a-e4b2-4e9d-b3a1-5ceb692c2761": "SignalR/Web PubSub Contributor",
    "b64e21ea-ac4e-4cdf-9dc9-5b892992bee7": "Azure Connected Machine Onboarding",
    "91c1777a-f3dc-4fae-b103-61d183457e46": "Managed Services Registration assignment Delete Role",
    "5ae67dd6-50cb-40e7-96ff-dc2bfa4b606b": "App Configuration Data Owner",
    "516239f1-63e1-4d78-a4de-a74fb236a071": "App Configuration Data Reader",
    "34e09817-6cbe-4d01-b1a2-e0eac5743d41": "Kubernetes Cluster - Azure Arc Onboarding",
    "7f646f1b-fa08-80eb-a22b-edd6ce5c915c": "Experimentation Contributor",
    "466ccd10-b268-4a11-b098-b4849f024126": "Cognitive Services QnA Maker Reader",
    "f4cc2bf9-21be-47a1-bdf1-5c5804381025": "Cognitive Services QnA Maker Editor",
    "7f646f1b-fa08-80eb-a33b-edd6ce5c915c": "Experimentation Administrator",
    "3df8b902-2a6f-47c7-8cc5-360e9b272a7e": "Remote Rendering Administrator",
    "d39065c4-c120-43c9-ab0a-63eed9795f0a": "Remote Rendering Client",
    "641177b8-a67a-45b9-a033-47bc880bb21e": "Managed Application Contributor Role",
    "612c2aa1-cb24-443b-ac28-3ab7272de6f5": "Security Assessment Contributor",
    "4a9ae827-6dc8-4573-8ac7-8239d42aa03f": "Tag Contributor",
    "c7aa55d3-1abb-444a-a5ca-5e51e485d6ec": "Integration Service Environment Developer",
    "a41e2c5b-bd99-4a07-88f4-9bf657a760b8": "Integration Service Environment Contributor",
    "ed7f3fbd-7b88-4dd4-9017-9adb7ce333f8": "Azure Kubernetes Service Contributor Role",
    "d57506d4-4c8d-48b1-8587-93c323f6a5a3": "Azure Digital Twins Data Reader",
    "bcd981a7-7f74-457b-83e1-cceb9e632ffe": "Azure Digital Twins Data Owner",
    "350f8d15-c687-4448-8ae1-157740a3936d": "Hierarchy Settings Administrator",
    "5a1fc7df-4bf1-4951-a576-89034ee01acd": "FHIR Data Contributor",
    "3db33094-8700-4567-8da5-1501d4e7e843": "FHIR Data Exporter",
    "4c8d0bbc-75d3-4935-991f-5f3c56d81508": "FHIR Data Reader",
    "3f88fce4-5892-4214-ae73-ba5294559913": "FHIR Data Writer",
    "49632ef5-d9ac-41f4-b8e7-bbe587fa74a1": "Experimentation Reader",
    "4dd61c23-6743-42fe-a388-d8bdd41cb745": "Object Understanding Account Owner",
    "8f5e0ce6-4f7b-4dcf-bddf-e6f48634a204": "Azure Maps Data Contributor",
    "c1ff6cc2-c111-46fe-8896-e0ef812ad9f3": "Cognitive Services Custom Vision Contributor",
    "5c4089e1-6d96-4d2f-b296-c1bc7137275f": "Cognitive Services Custom Vision Deployment",
    "88424f51-ebe7-446f-bc41-7fa16989e96c": "Cognitive Services Custom Vision Labeler",
    "93586559-c37d-4a6b-ba08-b9f0940c2d73": "Cognitive Services Custom Vision Reader",
    "0a5ae4ab-0d65-4eeb-be61-29fc9b54394b": "Cognitive Services Custom Vision Trainer",
    "00482a5a-887f-4fb3-b363-3b7fe8e74483": "Key Vault Administrator",
    "12338af0-0e69-4776-bea7-57ae8d297424": "Key Vault Crypto User",
    "b86a8fe4-44ce-4948-aee5-eccb2c155cd7": "Key Vault Secrets Officer",
    "4633458b-17de-408a-b874-0445c86b69e6": "Key Vault Secrets User",
    "a4417e6f-fecd-4de8-b567-7b0420556985": "Key Vault Certificates Officer",
    "21090545-7ca7-4776-b22c-e363652d74d2": "Key Vault Reader",
    "e147488a-f6f5-4113-8e2d-b22465e65bf6": "Key Vault Crypto Service Encryption User",
    "63f0a09d-1495-4db4-a681-037d84835eb4": "Azure Arc Kubernetes Viewer",
    "5b999177-9696-4545-85c7-50de3797e5a1": "Azure Arc Kubernetes Writer",
    "8393591c-06b9-48a2-a542-1bd6b377f6a2": "Azure Arc Kubernetes Cluster Admin",
    "dffb1e0c-446f-4dde-a09f-99eb5cc68b96": "Azure Arc Kubernetes Admin",
    "b1ff04bb-8a4e-4dc4-8eb5-8693973ce19b": "Azure Kubernetes Service RBAC Cluster Admin",
    "3498e952-d568-435e-9b2c-8d77e338d7f7": "Azure Kubernetes Service RBAC Admin",
    "7f6c6a51-bcf8-42ba-9220-52d62157d7db": "Azure Kubernetes Service RBAC Reader",
    "a7ffa36f-339b-4b5c-8bdf-e2c188b2c0eb": "Azure Kubernetes Service RBAC Writer",
    "82200a5b-e217-47a5-b665-6d8765ee745b": "Services Hub Operator",
    "d18777c0-1514-4662-8490-608db7d334b6": "Object Understanding Account Reader",
    "fd53cd77-2268-407a-8f46-7e7863d0f521": "SignalR REST API Owner",
    "daa9e50b-21df-454c-94a6-a8050adab352": "Collaborative Data Contributor",
    "e9dba6fb-3d52-4cf0-bce3-f06ce71b9e0f": "Device Update Reader",
    "02ca0879-e8e4-47a5-a61e-5c618b76e64a": "Device Update Administrator",
    "0378884a-3af5-44ab-8323-f5b22f9f3c98": "Device Update Content Administrator",
    "d1ee9a80-8b14-47f0-bdc2-f4a351625a7b": "Device Update Content Reader",
    "cb43c632-a144-4ec5-977c-e80c4affc34a": "Cognitive Services Metrics Advisor Administrator",
    "3b20f47b-3825-43cb-8114-4bd2201156a8": "Cognitive Services Metrics Advisor User",
    "2c56ea50-c6b3-40a6-83c0-9d98858bc7d2": "Schema Registry Reader (Preview)",
    "5dffeca3-4936-4216-b2bc-10343a5abb25": "Schema Registry Contributor (Preview)",
    "7ec7ccdc-f61e-41fe-9aaf-980df0a44eba": "AgFood Platform Service Reader",
    "8508508a-4469-4e45-963b-2518ee0bb728": "AgFood Platform Service Contributor",
    "f8da80de-1ff9-4747-ad80-a19b7f6079e3": "AgFood Platform Service Admin",
    "18500a29-7fe2-46b2-a342-b16a415e101d": "Managed HSM contributor",
    "0b555d9b-b4a7-4f43-b330-627f0e5be8f0": "Security Detonation Chamber Submitter",
    "ddde6b66-c0df-4114-a159-3618637b3035": "SignalR REST API Reader",
    "7e4f1700-ea5a-4f59-8f37-079cfe29dce3": "SignalR Service Owner",
    "f7b75c60-3036-4b75-91c3-6b41c27c1689": "Reservation Purchaser",
    "635dd51f-9968-44d3-b7fb-6d9a6bd613ae": "AzureML Metrics Writer (preview)",
    "e5e2a7ff-d759-4cd2-bb51-3152d37e2eb1": "Storage Account Backup Contributor",
    "6188b7c9-7d01-4f99-a59f-c88b630326c0": "Experimentation Metric Contributor",
    "9ef4ef9c-a049-46b0-82ab-dd8ac094c889": "Project Babylon Data Curator",
    "c8d896ba-346d-4f50-bc1d-7d1c84130446": "Project Babylon Data Reader",
    "05b7651b-dc44-475e-b74d-df3db49fae0f": "Project Babylon Data Source Administrator",
    "ca6382a4-1721-4bcf-a114-ff0c70227b6b": "Application Group Contributor",
    "49a72310-ab8d-41df-bbb0-79b649203868": "Desktop Virtualization Reader",
    "082f0a83-3be5-4ba1-904c-961cca79b387": "Desktop Virtualization Contributor",
    "21efdde3-836f-432b-bf3d-3e8e734d4b2b": "Desktop Virtualization Workspace Contributor",
    "ea4bfff8-7fb4-485a-aadd-d4129a0ffaa6": "Desktop Virtualization User Session Operator",
    "2ad6aaab-ead9-4eaa-8ac5-da422f562408": "Desktop Virtualization Session Host Operator",
    "ceadfde2-b300-400a-ab7b-6143895aa822": "Desktop Virtualization Host Pool Reader",
    "e307426c-f9b6-4e81-87de-d99efb3c32bc": "Desktop Virtualization Host Pool Contributor",
    "aebf23d0-b568-4e86-b8f9-fe83a2c6ab55": "Desktop Virtualization Application Group Reader",
    "86240b0e-9422-4c43-887b-b61143f32ba8": "Desktop Virtualization Application Group Contributor",
    "0fa44ee9-7a7d-466b-9bb2-2bf446b1204d": "Desktop Virtualization Workspace Reader",
    "3e5e47e6-65f7-47ef-90b5-e5dd4d455f24": "Disk Backup Reader",
    "b50d9833-a0cb-478e-945f-707fcc997c13": "Disk Restore Operator",
    "7efff54f-a5b4-42b5-a1c5-5411624893ce": "Disk Snapshot Contributor",
    "5548b2cf-c94c-4228-90ba-30851930a12f": "Microsoft.Kubernetes connected cluster role",
    "a37b566d-3efa-4beb-a2f2-698963fa42ce": "Security Detonation Chamber Submission Manager",
    "352470b3-6a9c-4686-b503-35deb827e500": "Security Detonation Chamber Publisher",
    "7a6f0e70-c033-4fb1-828c-08514e5f4102": "Collaborative Runtime Operator",
    "5432c526-bc82-444a-b7ba-57c5b0b5b34f": "CosmosRestoreOperator",
    "a1705bd2-3a8f-45a5-8683-466fcfd5cc24": "FHIR Data Converter",
    "0e5f05e5-9ab9-446b-b98d-1e2157c94125": "Quota Request Operator",
    "1e241071-0855-49ea-94dc-649edcd759de": "EventGrid Contributor",
    "28241645-39f8-410b-ad48-87863e2951d5": "Security Detonation Chamber Reader",
    "4a167cdf-cb95-4554-9203-2347fe489bd9": "Object Anchors Account Reader",
    "ca0835dd-bacc-42dd-8ed2-ed5e7230d15b": "Object Anchors Account Owner",
    "d17ce0a2-0697-43bc-aac5-9113337ab61c": "WorkloadBuilder Migration Agent Role",
    "b5537268-8956-4941-a8f0-646150406f0c": "Azure Spring Cloud Data Reader",
    "0e75ca1e-0464-4b4d-8b93-68208a576181": "Cognitive Services Speech Contributor",
    "9894cab4-e18a-44aa-828b-cb588cd6f2d7": "Cognitive Services Face Recognizer",
    "054126f8-9a2b-4f1c-a9ad-eca461f08466": "Media Services Account Administrator",
    "532bc159-b25e-42c0-969e-a1d439f60d77": "Media Services Live Events Administrator",
    "e4395492-1534-4db2-bedf-88c14621589c": "Media Services Media Operator",
    "c4bba371-dacd-4a26-b320-7250bca963ae": "Media Services Policy Administrator",
    "99dba123-b5fe-44d5-874c-ced7199a5804": "Media Services Streaming Endpoints Administrator",
    "1ec5b3c1-b17e-4e25-8312-2acb3c3c5abf": "Stream Analytics Query Tester",
    "a2138dac-4907-4679-a376-736901ed8ad8": "AnyBuild Builder",
    "b447c946-2db7-41ec-983d-d8bf3b1c77e3": "IoT Hub Data Reader",
    "494bdba2-168f-4f31-a0a1-191d2f7c028c": "IoT Hub Twin Contributor",
    "4ea46cd5-c1b2-4a8e-910b-273211f9ce47": "IoT Hub Registry Contributor",
    "4fc6c259-987e-4a07-842e-c321cc9d413f": "IoT Hub Data Contributor",
    "15e0f5a1-3450-4248-8e25-e2afe88a9e85": "Test Base Reader",
    "1407120a-92aa-4202-b7e9-c0e197c71c8f": "Search Index Data Reader",
    "8ebe5a00-799e-43f5-93ac-243d3dce84a7": "Search Index Data Contributor",
    "76199698-9eea-4c19-bc75-cec21354c6b6": "Storage Table Data Reader",
    "0a9a7e1f-b9d0-4cc4-a60d-0319b160aaa3": "Storage Table Data Contributor",
    "e89c7a3c-2f64-4fa1-a847-3e4c9ba4283a": "DICOM Data Reader",
    "58a3b984-7adf-4c20-983a-32417c86fbc8": "DICOM Data Owner",
    "d5a91429-5739-47e2-a06b-3470a27159e7": "EventGrid Data Sender",
    "60fc6e62-5479-42d4-8bf4-67625fcc2840": "Disk Pool Operator",
    "f6c7c914-8db3-469d-8ca1-694a8f32e121": "AzureML Data Scientist",
    "22926164-76b3-42b3-bc55-97df8dab3e41": "Grafana Admin",
    "e8113dce-c529-4d33-91fa-e9b972617508": "Azure Connected SQL Server Onboarding",
    "26baccc8-eea7-41f1-98f4-1762cc7f685d": "Azure Relay Sender",
    "2787bf04-f1f5-4bfe-8383-c8a24483ee38": "Azure Relay Owner",
    "26e0b698-aa6d-4085-9386-aadae190014d": "Azure Relay Listener",
    "60921a7e-fef1-4a43-9b16-a26c52ad4769": "Grafana Viewer",
    "a79a5197-3a5c-4973-a920-486035ffd60f": "Grafana Editor",
    "f353d9bd-d4a6-484e-a77a-8050b599b867": "Automation Contributor",
    "85cb6faf-e071-4c9b-8136-154b5a04f717": "Kubernetes Extension Contributor",
    "10745317-c249-44a1-a5ce-3a4353c0bbd8": "Device Provisioning Service Data Reader",
    "dfce44e4-17b7-4bd1-a6d1-04996ec95633": "Device Provisioning Service Data Contributor",
    "2837e146-70d7-4cfd-ad55-7efa6464f958": "Trusted Signing Certificate Profile Signer",
    "cff1b556-2399-4e7e-856d-a8f754be7b65": "Azure Spring Cloud Service Registry Reader",
    "f5880b48-c26d-48be-b172-7927bfa1c8f1": "Azure Spring Cloud Service Registry Contributor",
    "d04c6db6-4947-4782-9e91-30a88feb7be7": "Azure Spring Cloud Config Server Reader",
    "a06f5c24-21a7-4e1a-aa2b-f19eb6684f5b": "Azure Spring Cloud Config Server Contributor",
    "6ae96244-5829-4925-a7d3-5975537d91dd": "Azure VM Managed identities restore Contributor",
    "6be48352-4f82-47c9-ad5e-0acacefdb005": "Azure Maps Search and Render Data Reader",
    "dba33070-676a-4fb0-87fa-064dc56ff7fb": "Azure Maps Contributor",
    "b748a06d-6150-4f8a-aaa9-ce3940cd96cb": "Azure Arc VMware VM Contributor",
    "ce551c02-7c42-47e0-9deb-e3b6fc3a9a83": "Azure Arc VMware Private Cloud User",
    "ddc140ed-e463-4246-9145-7c664192013f": "Azure Arc VMware Administrator role ",
    "f72c8140-2111-481c-87ff-72b910f6e3f8": "Cognitive Services LUIS Owner",
    "7628b7b8-a8b2-4cdc-b46f-e9b35248918e": "Cognitive Services Language Reader",
    "f2310ca1-dc64-4889-bb49-c8e0fa3d47a8": "Cognitive Services Language Writer",
    "f07febfe-79bc-46b1-8b37-790e26e6e498": "Cognitive Services Language Owner",
    "18e81cdc-4e98-4e29-a639-e7d10c5a6226": "Cognitive Services LUIS Reader",
    "6322a993-d5c9-4bed-b113-e49bbea25b27": "Cognitive Services LUIS Writer",
    "a9a19cc5-31f4-447c-901f-56c0bb18fcaf": "PlayFab Reader",
    "749a398d-560b-491b-bb21-08924219302e": "Load Test Contributor",
    "45bb0b16-2f0c-4e78-afaa-a07599b003f6": "Load Test Owner",
    "0c8b84dc-067c-4039-9615-fa1a4b77c726": "PlayFab Contributor",
    "3ae3fb29-0000-4ccd-bf80-542e7b26e081": "Load Test Reader",
    "b2de6794-95db-4659-8781-7e080d3f2b9d": "Cognitive Services Immersive Reader User",
    "f69b8690-cc87-41d6-b77a-a4bc3c0a966f": "Lab Services Contributor",
    "2a5c394f-5eb7-4d4f-9c8e-e8eae39faebc": "Lab Services Reader",
    "ce40b423-cede-4313-a93f-9b28290b72e1": "Lab Assistant",
    "a36e6959-b6be-4b12-8e9f-ef4b474d304d": "Lab Operator",
    "5daaa2af-1fe8-407c-9122-bba179798270": "Lab Contributor",
    "fb1c8493-542b-48eb-b624-b4c8fea62acd": "Security Admin",
    "12cf5a90-567b-43ae-8102-96cf46c7d9b4": "Web PubSub Service Owner",
    "bfb1c7d2-fb1a-466b-b2ba-aee63b92deaf": "Web PubSub Service Reader",
    "420fcaa2-552c-430f-98ca-3264be4806c7": "SignalR App Server",
    "fb879df8-f326-4884-b1cf-06f3ad86be52": "Virtual Machine User Login",
    "1c0163c0-47e6-4577-8991-ea5c82e286e4": "Virtual Machine Administrator Login",
    "cd570a14-e51a-42ad-bac8-bafd67325302": "Azure Connected Machine Resource Administrator",
    "00c29273-979b-4161-815c-10b084fb9324": "Backup Operator",
    "e8ddcd69-c73f-4f9f-9844-4100522f16ad": "Workbook Contributor",
    "b279062a-9be3-42a0-92ae-8b3cf002ec4d": "Workbook Reader",
    "749f88d5-cbae-40b8-bcfc-e573ddc772fa": "Monitoring Contributor",
    "3913510d-42f4-4e42-8a64-420c390055eb": "Monitoring Metrics Publisher",
    "8a3c2885-9b38-4fd2-9d99-91af537c1347": "Purview role 1 (Deprecated)",
    "200bba9e-f0c8-430f-892b-6f0794863803": "Purview role 2 (Deprecated)",
    "ff100721-1b9d-43d8-af52-42b69c1272db": "Purview role 3 (Deprecated)",
    "b8b15564-4fa6-4a59-ab12-03e1d9594795": "Autonomous Development Platform Data Contributor (Preview)",
    "27f8b550-c507-4db9-86f2-f4b8e816d59d": "Autonomous Development Platform Data Owner (Preview)",
    "d63b75f7-47ea-4f27-92ac-e0d173aaf093": "Autonomous Development Platform Data Reader (Preview)",
    "14b46e9e-c2b7-41b4-b07b-48a6ebf60603": "Key Vault Crypto Officer",
    "49e2f5d2-7741-4835-8efa-19e1fe35e47f": "Device Update Deployments Reader",
    "e4237640-0e3d-4a46-8fda-70bc94856432": "Device Update Deployments Administrator",
    "67d33e57-3129-45e6-bb0b-7cc522f762fa": "Azure Arc VMware Private Clouds Onboarding",
    "4e9b8407-af2e-495b-ae54-bb60a55b1b5a": "Chamber Admin",
    "f4c81013-99ee-4d62-a7ee-b3f1f648599a": "Microsoft Sentinel Automation Contributor",
    "871e35f6-b5c1-49cc-a043-bde969a0f2cd": "CDN Endpoint Reader",
    "4447db05-44ed-4da3-ae60-6cbece780e32": "Chamber User",
    "f2dc8367-1007-4938-bd23-fe263f013447": "Cognitive Services Speech User",
    "a6333a3e-0164-44c3-b281-7a577aff287f": "Windows Admin Center Administrator Login",
    "18ed5180-3e48-46fd-8541-4ea054d57064": "Azure Kubernetes Service Policy Add-on Deployment",
    "088ab73d-1256-47ae-bea9-9de8e7131f31": "Guest Configuration Resource Contributor",
    "361898ef-9ed1-48c2-849c-a832951106bb": "Domain Services Reader",
    "eeaeda52-9324-47f6-8069-5d5bade478b2": "Domain Services Contributor",
    "0f2ebee7-ffd4-4fc0-b3b7-664099fdad5d": "DNS Resolver Contributor",
    "00493d72-78f6-4148-b6c5-d3ce8e4799dd": "Azure Arc Enabled Kubernetes Cluster User Role",
    "959f8984-c045-4866-89c7-12bf9737be2e": "Data Operator for Managed Disks",
    "6b77f0a0-0d89-41cc-acd1-579c22c17a67": "AgFood Platform Sensor Partner Contributor",
    "1ef6a3be-d0ac-425d-8c01-acb62866290b": "Compute Gallery Sharing Admin",
    "cd08ab90-6b14-449c-ad9a-8f8e549482c6": "Scheduled Patching Contributor",
    "45d50f46-0b78-4001-a660-4198cbe8cd05": "DevCenter Dev Box User",
    "331c37c6-af14-46d9-b9f4-e1909e1b95a0": "DevCenter Project Admin",
    "602da2ba-a5c2-41da-b01d-5360126ab525": "Virtual Machine Local User Login",
    "e582369a-e17b-42a5-b10c-874c387c530b": "Azure Arc ScVmm VM Contributor",
    "a92dfd61-77f9-4aec-a531-19858b406c87": "Azure Arc ScVmm Administrator role",
    "6aac74c4-6311-40d2-bbdd-7d01e7c6e3a9": "Azure Arc ScVmm Private Clouds Onboarding",
    "c0781e91-8102-4553-8951-97c6d4243cda": "Azure Arc ScVmm Private Cloud User",
    "7656b436-37d4-490a-a4ab-d39f838f0042": "HDInsight on AKS Cluster Pool Admin",
    "fd036e6b-1266-47a0-b0bb-a05d04831731": "HDInsight on AKS Cluster Admin",
    "4465e953-8ced-4406-a58e-0f6e3f3b530b": "FHIR Data Importer",
    "c031e6a8-4391-4de0-8d69-4706a7ed3729": "API Management Developer Portal Content Editor",
    "d24ecba3-c1f4-40fa-a7bb-4588a071e8fd": "VM Scanner Operator",
    "80dcbedb-47ef-405d-95bd-188a1b4ac406": "Elastic SAN Owner",
    "af6a70f8-3c9f-4105-acf1-d719e9fca4ca": "Elastic SAN Reader",
    "a959dbd1-f747-45e3-8ba6-dd80f235f97c": "Desktop Virtualization Virtual Machine Contributor",
    "40c5ff49-9181-41f8-ae61-143b0e78555e": "Desktop Virtualization Power On Off Contributor",
    "489581de-a3bd-480d-9518-53dea7416b33": "Desktop Virtualization Power On Contributor",
    "a8281131-f312-4f34-8d98-ae12be9f0d23": "Elastic SAN Volume Group Owner",
    "76cc9ee4-d5d3-4a45-a930-26add3d73475": "Access Review Operator Service Role",
    "4339b7cf-9826-4e41-b4ed-c7f4505dac08": "Trusted Signing Identity Verifier",
    "a2c4a527-7dc0-4ee3-897b-403ade70fafb": "Video Indexer Restricted Viewer",
    "b0d8363b-8ddd-447d-831f-62ca05bff136": "Monitoring Data Reader",
    "5af6afb3-c06c-4fa4-8848-71a8aee05683": "Azure Kubernetes Fleet Manager RBAC Writer",
    "434fb43a-c01c-447e-9f67-c3ad923cfaba": "Azure Kubernetes Fleet Manager RBAC Admin",
    "63bb64ad-9799-4770-b5c3-24ed299a07bf": "Azure Kubernetes Fleet Manager Contributor Role",
    "30b27cfc-9c84-438e-b0ce-70e35255df80": "Azure Kubernetes Fleet Manager RBAC Reader",
    "18ab4d3d-a1bf-4477-8ad9-8359bc988f69": "Azure Kubernetes Fleet Manager RBAC Cluster Admin",
    "ba79058c-0414-4a34-9e42-c3399d80cd5a": "Kubernetes Namespace User",
    "c6decf44-fd0a-444c-a844-d653c394e7ab": "Data Labeling - Labeler",
    "f58310d9-a9f6-439a-9e8d-f62e7b41a168": "Role Based Access Control Administrator",
    "1c9b6475-caf0-4164-b5a1-2142a7116f4b": "Template Spec Contributor",
    "392ae280-861d-42bd-9ea5-08ee6d83b80e": "Template Spec Reader",
    "51d6186e-6489-4900-b93f-92e23144cca5": "Microsoft Sentinel Playbook Operator",
    "18e40d4e-8d2e-438d-97e1-9528336e149c": "Deployment Environments User",
    "80558df3-64f9-4c0f-b32d-e5094b036b0b": "Azure Spring Apps Connect Role",
    "a99b0159-1064-4c22-a57b-c9b3caa1c054": "Azure Spring Apps Remote Debugging Role",
    "1823dd4f-9b8c-4ab6-ab4e-7397a3684615": "AzureML Registry User",
    "e503ece1-11d0-4e8e-8e2c-7a6c3bf38815": "AzureML Compute Operator",
    "aabbc5dd-1af0-458b-a942-81af88f9c138": "Azure Center for SAP solutions service role",
    "05352d14-a920-4328-a0de-4cbe7430e26b": "Azure Center for SAP solutions reader",
    "7b0c7e81-271f-4c71-90bf-e30bdfdbc2f7": "Azure Center for SAP solutions administrator",
    "fbc52c3f-28ad-4303-a892-8a056630b8f1": "AppGw for Containers Configuration Manager",
    "4ba50f17-9666-485c-a643-ff00808643f0": "FHIR SMART User",
    "a001fd3d-188f-4b5d-821b-7da978bf7442": "Cognitive Services OpenAI Contributor",
    "5e0bd9bd-7b93-4f28-af87-19fc36ad61bd": "Cognitive Services OpenAI User",
    "36e80216-a7e8-4f42-a7e1-f12c98cbaf8a": "Impact Reporter",
    "68ff5d27-c7f5-4fa9-a21c-785d0df7bd9e": "Impact Reader",
    "1afdec4b-e479-420e-99e7-f82237c7c5e6": "Azure Kubernetes Service Cluster Monitoring User",
    "ad2dd5fb-cd4b-4fd4-a9b6-4fed3630980b": "ContainerApp Reader",
    "f5819b54-e033-4d82-ac66-4fec3cbf3f4c": "Azure Connected Machine Resource Manager",
    "189207d4-bb67-4208-a635-b06afe8b2c57": "SqlDb Migration Role",
    "c4bc862a-3b64-4a35-a021-a380c159b042": "Bayer Ag Powered Services GDU Solution",
    "ef29765d-0d37-4119-a4f8-f9f9902c9588": "Bayer Ag Powered Services Imagery Solution",
    "0105a6b0-4bb9-43d2-982a-12806f9faddb": "Azure Center for SAP solutions Service role for management",
    "6d949e1d-41e2-46e3-8920-c6e4f31a8310": "Azure Center for SAP solutions Management role",
    "d5a2ae44-610b-4500-93be-660a0c5f5ca6": "Kubernetes Agentless Operator",
    "f0310ce6-e953-4cf8-b892-fb1c87eaf7f6": "Azure Usage Billing Data Sender",
    "1d335eef-eee1-47fe-a9e0-53214eba8872": "SqlMI Migration Role",
    "a9b99099-ead7-47db-8fcf-072597a61dfa": "Bayer Ag Powered Services CWUM Solution",
    "ae8036db-e102-405b-a1b9-bae082ea436d": "SqlVM Migration Role",
    "0ab34830-df19-4f8c-b84e-aa85b8afa6e8": "Azure Front Door Domain Contributor",
    "0db238c4-885e-4c4f-a933-aa2cef684fca": "Azure Front Door Secret Reader",
    "3f2eb865-5811-4578-b90a-6fc6fa0df8e5": "Azure Front Door Secret Contributor",
    "0f99d363-226e-4dca-9920-b807cf8e1a5f": "Azure Front Door Domain Reader",
    "bda0d508-adf1-4af0-9c28-88919fc3ae06": "Azure Stack HCI Administrator",
    "d18ad5f3-1baf-4119-b49b-d944edb1f9d0": "MySQL Backup And Export Operator",
    "a8835c7d-b5cb-47fa-b6f0-65ea10ce07a2": "LocalNGFirewallAdministrator role",
    "bfc3b73d-c6ff-45eb-9a5f-40298295bf20": "LocalRulestacksAdministrator role",
    "7392c568-9289-4bde-aaaa-b7131215889d": "Azure Extension for SQL Server Deployment",
    "d6470a16-71bd-43ab-86b3-6f3a73f4e787": "Azure Maps Data Read and Batch Role",
    "d59a3e9c-6d52-4a5a-aeed-6bf3cf0e31da": "API Management Service Workspace API Product Manager",
    "56328988-075d-4c6a-8766-d93edd6725b6": "API Management Workspace API Developer",
    "ef1c2c96-4a77-49e8-b9a4-6179fe1d2fd2": "API Management Workspace Reader",
    "73c2c328-d004-4c5e-938c-35c6f5679a1f": "API Management Workspace API Product Manager",
    "9565a273-41b9-4368-97d2-aeb0c976a9b3": "API Management Service Workspace API Developer",
    "0c34c906-8d99-4cb7-8bb7-33f5b0a1a799": "API Management Workspace Contributor",
    "b8eda974-7b85-4f76-af95-65846b26df6d": "Storage File Data Privileged Reader",
    "69566ab7-960f-475b-8e7c-b3118f30c6bd": "Storage File Data Privileged Contributor",
    "7eabc9a4-85f7-4f71-b8ab-75daaccc1033": "Windows 365 Network User",
    "3d55a8f6-4133-418d-8051-facdb1735758": "Windows365SubscriptionReader",
    "1f135831-5bbe-4924-9016-264044c00788": "Windows 365 Network Interface Contributor",
    "ffc6bbe0-e443-4c3b-bf54-26581bb2f78e": "App Compliance Automation Reader",
    "0f37683f-2463-46b6-9ce7-9b788b988ba2": "App Compliance Automation Administrator",
    "8b9dfcab-4b77-4632-a6df-94bd07820648": "Azure Sphere Contributor",
    "e9b8712a-cbcf-4ea7-b0f7-e71b803401e6": "SaaS Hub Contributor",
    "c8ae6279-5a0b-4cb2-b3f0-d4d62845742c": "Azure Sphere Reader",
    "6d994134-994b-4a59-9974-f479f0b227fb": "Azure Sphere Publisher",
    "ea01e6af-a1c1-4350-9563-ad00f8c72ec5": "Azure Machine Learning Workspace Connection Secrets Reader",
    "be1a1ac2-09d3-4261-9e57-a73a6e227f53": "Procurement Contributor",
    "7ac06ca7-21ca-47e3-a67b-cbd6e6223baf": "Cognitive Search Serverless Data Contributor (Deprecated)",
    "79b01272-bf9f-4f4c-9517-5506269cf524": "Cognitive Search Serverless Data Reader (Deprecated)",
    "5e28a61e-8040-49db-b175-bb5b88af6239": "Community Owner Role",
    "9c1607d1-791d-4c68-885d-c7b7aaff7c8a": "Firmware Analysis Admin",
    "8b54135c-b56d-4d72-a534-26097cfdc8d8": "Key Vault Data Access Administrator",
    "1e7ca9b1-60d1-4db8-a914-f2ca1ff27c40": "Defender for Storage Data Scanner",
    "df2711a6-406d-41cf-b366-b0250bff9ad1": "Compute Diagnostics Role",
    "fa6cecf6-5db3-4c43-8470-c540bcb4eafa": "Elastic SAN Network Admin",
    "bba48692-92b0-4667-a9ad-c31c7b334ac2": "Cognitive Services Usages Reader",
    "c088a766-074b-43ba-90d4-1fb21feae531": "PostgreSQL Flexible Server Long Term Retention Backup Role",
    "a02f7c31-354d-4106-865a-deedf37fa038": "Search Parameter Manager",
    "66f75aeb-eabe-4b70-9f1e-c350c4c9ad04": "Virtual Machine Data Access Administrator (preview)",
    "523776ba-4eb2-4600-a3c8-f2dc93da4bdb": "Logic Apps Standard Developer (Preview)",
    "ad710c24-b039-4e85-a019-deb4a06e8570": "Logic Apps Standard Contributor (Preview)",
    "b70c96e9-66fe-4c09-b6e7-c98e69c98555": "Logic Apps Standard Operator (Preview)",
    "4accf36b-2c05-432f-91c8-5c532dff4c73": "Logic Apps Standard Reader (Preview)",
    "7b3e853f-ad5d-4fb5-a7b8-56a3581c7037": "IPAM Pool User",
    "e9c9ed2b-2a99-4071-b2ff-5b113ebf73a1": "SpatialMapsAccounts Account Owner",
    "0b962ed2-6d56-471c-bd5f-3477d83a7ba4": "Azure Resource Notifications System Topics Subscriber",
    "90e8b822-3e73-47b5-868a-787dc80c008f": "Elastic SAN Volume Importer",
    "1c4770c0-34f7-4110-a1ea-a5855cc7a939": "Elastic SAN Snapshot Exporter",
    "49435da6-99fe-48a5-a235-fc668b9dc04a": "Community Contributor Role",
    "4b0f2fd7-60b4-4eca-896f-4435034f8bf5": "EventGrid TopicSpaces Subscriber",
    "a12b0b94-b317-4dcd-84a8-502ce99884c6": "EventGrid TopicSpaces Publisher",
    "d1a38570-4b05-4d70-b8e4-1100bcf76d12": "Data Boundary Tenant Administrator",
    "bb6577c4-ea0a-40b2-8962-ea18cb8ecd4e": "DeID Realtime Data User",
    "b73a14ee-91f5-41b7-bd81-920e12466be9": "DeID Batch Data Reader",
    "8a90fa6b-6997-4a07-8a95-30633a7c97b9": "DeID Batch Data Owner",
    "fa0d39e6-28e5-40cf-8521-1eb320653a4c": "Carbon Optimization Reader",
    "38863829-c2a4-4f8d-b1d2-2e325973ebc7": "Landing Zone Management Owner",
    "8fe6e843-6d9e-417b-9073-106b048f50bb": "Landing Zone Management Reader",
    "865ae368-6a45-4bd1-8fbf-0d5151f56fc1": "Azure Stack HCI Device Management Role",
    "4dae6930-7baf-46f5-909e-0383bc931c46": "Azure Customer Lockbox Approver for Subscription",
    "7b1f81f9-4196-4058-8aae-762e593270df": "Azure Resource Bridge Deployment Role",
    "4b3fe76c-f777-4d24-a2d7-b027b0f7b273": "Azure Stack HCI VM Reader",
    "64702f94-c441-49e6-a78b-ef80e0188fee": "Azure AI Developer",
    "874d1c73-6003-4e60-a13a-cb31ea190a85": "Azure Stack HCI VM Contributor",
    "eb960402-bf75-4cc3-8d68-35b34f960f72": "Deployment Environments Reader",
    "78cbd9e7-9798-4e2e-9b5a-547d9ebb31fb": "EventGrid Data Receiver",
    "1d8c3fe3-8864-474b-8749-01e3783e8157": "EventGrid Data Contributor",
    "8aac15f0-d885-4138-8afa-bfb5872f7d13": "Advisor Reviews Contributor",
    "c64499e0-74c3-47ad-921c-13865957895c": "Advisor Reviews Reader",
    "3afb7f49-54cb-416e-8c09-6dc049efa503": "Azure AI Inference Deployment Operator",
    "65a14201-8f6c-4c28-bec4-12619c5a9aaa": "Connected Cluster Managed Identity CheckAccess Reader",
    "a8d4b70f-0fb9-4f72-b267-b87b2f990aec": "AgFood Platform Dataset Admin",
    "0f641de8-0b88-4198-bdef-bd8b45ceba96": "Defender for Storage Scanner Operator",
    "662802e2-50f6-46b0-aed2-e834bacc6d12": "Azure Front Door Profile Reader",
    "86fede04-b259-4277-8c3e-e26b9865abd8": "Enclave Reader Role",
    "fc3f91a1-40bf-4439-8c46-45edbd83563a": "Azure Kubernetes Service Hybrid Cluster User Role",
    "b5092dac-c796-4349-8681-1a322a31c3f9": "Azure Kubernetes Service Hybrid Cluster Admin Role",
    "e7037d40-443a-4434-a3fb-8cd202011e1d": "Azure Kubernetes Service Hybrid Contributor Role",
    "3d5f3eff-eb94-473d-91e3-7aac74d6c0bb": "Enclave Owner Role",
    "19feefae-eacc-4106-81fd-ac34c0671f14": "Enclave Contributor Role",
    "e6aadb6b-e64f-41c0-9392-d2bba3bc3ebc": "Community Reader Role",
    "a316ed6d-1efe-48ac-ac08-f7995a9c26fb": "Storage Account Encryption Scope Contributor Role",
    "44f0a1a8-6fea-4b35-980a-8ff50c487c97": "Operator Nexus Key Vault Writer Service Role (Preview)",
    "08bbd89e-9f13-488c-ac41-acfcb10c90ab": "Key Vault Crypto Service Release User",
    "0cd9749a-3aaf-4ae5-8803-bd217705bf3b": "KubernetesRuntime Storage Class Contributor Role",
    "609c0c20-e0a0-4a71-b99f-e7e755ac493d": "Azure Programmable Connectivity Gateway User",
    "db79e9a7-68ee-4b58-9aeb-b90e7c24fcba": "Key Vault Certificate User",
    "52fd16bd-6ed5-46af-9c40-29cbd7952a29": "Azure Spring Apps Managed Components Log Reader Role",
    "6593e776-2a30-40f9-8a32-4fe28b77655d": "Azure Spring Apps Application Configuration Service Log Reader Role",     
    "4301dc2a-25a9-44b0-ae63-3636cf7f2bd2": "Azure Spring Apps Spring Cloud Gateway Log Reader Role",
    "207bcc4b-86a6-4487-9141-d6c1f4c238aa": "Azure Edge On-Site Deployment Engineer",
    "c7244dfb-f447-457d-b2ba-3999044d1706": "Azure API Center Data Reader",
    "dfb2f09d-25f8-4558-8986-497084006d7a": "Azure impact-insight reader",
    "8bb6f106-b146-4ee6-a3f9-b9c5a96e0ae5": "Defender Kubernetes Agent Operator",
    "a1f96423-95ce-4224-ab27-4e3dc72facd4": "Azure RedHat OpenShift Cloud Controller Manager Role",
    "5b7237c5-45e1-49d6-bc18-a1f62f400748": "Azure RedHat OpenShift Storage Operator Role",
    "be7a6435-15ae-4171-8f30-4a343eff9e8f": "Azure RedHat OpenShift Network Operator Role",
    "8b32b316-c2f5-4ddf-b05b-83dacd2d08b5": "Azure RedHat OpenShift Image Registry Operator Role",
    "0d7aedc0-15fd-4a67-a412-efad370c947e": "Azure RedHat OpenShift Azure Files Storage Operator Role",
    "4436bae4-7702-4c84-919b-c4069ff25ee2": "Azure RedHat OpenShift Service Operator",
    "0358943c-7e01-48ba-8889-02cc51d78637": "Azure RedHat OpenShift Machine API Operator Role",
    "0336e1d3-7a87-462b-b6db-342b63f7802c": "Azure RedHat OpenShift Cluster Ingress Operator Role",
    "5a382001-fe36-41ff-bba4-8bf06bd54da9": "Azure Sphere Owner",
    "e2217c0e-04bb-4724-9580-91cf9871bc01": "GroupQuota Request Operator",
    "d0f495dc-44ef-4140-aeb0-b89110e6a7c1": "GroupQuota Reader",
    "539283cd-c185-4a9a-9503-d35217a1db7b": "Bayer Ag Powered Services Smart Boundary Solution User Role",
    "8480c0f0-4509-4229-9339-7c10018cb8c4": "Defender CSPM Storage Scanner Operator",
    "6b534d80-e337-47c4-864f-140f5c7f593d": "Advisor Recommendations Contributor (Assessments and Reviews)",
    "c9c97b9c-105d-4bb5-a2a7-7d15666c2484": "GeoCatalog Administrator",
    "b7b8f583-43d0-40ae-b147-6b46f53661c1": "GeoCatalog Reader",
    "af854a69-80ce-4ff7-8447-f1118a2e0ca8": "Health Bot Editor",
    "eb5a76d5-50e7-4c33-a449-070e7c9c4cf2": "Health Bot Reader",
    "c20923c5-b089-47a5-bf67-fd89569c4ad9": "Azure Programmable Connectivity Gateway Dataplane User",
    "f1082fec-a70f-419f-9230-885d2550fb38": "Health Bot Admin",
    "b556d68e-0be0-4f35-a333-ad7ee1ce17ea": "Azure AI Enterprise Network Connection Approver",
    "08d4c71a-cc63-4ce4-a9c8-5dd251b4d619": "Azure Container Storage Operator",
    "95dd08a6-00bd-4661-84bf-f6726f83a4d0": "Azure Container Storage Contributor",
    "95de85bd-744d-4664-9dde-11430bc34793": "Azure Container Storage Owner",
    "5d3f1697-4507-4d08-bb4a-477695db5f82": "Azure Kubernetes Service Arc Contributor Role",
    "233ca253-b031-42ff-9fba-87ef12d6b55f": "Azure Kubernetes Service Arc Cluster User Role",
    "b29efa5f-7782-4dc3-9537-4d5bc70a5e9f": "Azure Kubernetes Service Arc Cluster Admin Role",
    "f54b6d04-23c6-443e-b462-9c16ab7b4a52": "Backup MUA Operator",
    "c2a970b4-16a7-4a51-8c84-8a8ea6ee0bb8": "Backup MUA Admin",
    "3d24a3a0-c154-4f6f-a5ed-adc8e01ddb74": "Savings plan Purchaser",
    "b6ee44de-fe58-4ddc-b5c2-ab174eb23f05": "CrossConnectionReader",
    "399c3b2b-64c2-4ff1-af34-571db925b068": "CrossConnectionManager",
    "5e93ba01-8f92-4c7a-b12a-801e3df23824": "Kubernetes Agent Operator",
    "dd24193f-ef65-44e5-8a7e-6fa6e03f7713": "Azure API Center Service Contributor",
    "6cba8790-29c5-48e5-bab1-c7541b01cb04": "Azure API Center Service Reader",
    "ede9aaa3-4627-494e-be13-4aa7c256148d": "Azure API Center Compliance Manager",
    "b5b192c1-773c-4543-bfb0-6c59254b74a9": "Bayer Ag Powered Services Historical Weather Data Solution User Role",    
    "e9ce8739-6fa2-4123-a0a2-0ef41a67806f": "Oracle.Database VmCluster Administrator Built-in Role",
    "4562aac9-b209-4bd7-a144-6d7f3bb516f4": "Oracle.Database Owner Built-in Role",
    "4caf51ec-f9f5-413f-8a94-b9f5fddba66b": "Oracle Subscriptions Manager Built-in Role",
    "f27b7598-bc64-41f7-8a44-855ff16326c2": "Azure Messaging Catalog Data Owner",
    "25211fc6-dc78-40b6-b205-e4ac934fd9fd": "Azure Spring Apps Application Configuration Service Config File Pattern Reader Role",
    "5d9c6a55-fc0e-4e21-ae6f-f7b095497342": "Azure Hybrid Database Administrator - Read Only Service Role",
    "c18f9900-27b8-47c7-a8f0-5b3b3d4c2bc2": "Microsoft Sentinel Business Applications Agent Operator",
    "0fb8eba5-a2bb-4abe-b1c1-49dfad359bb0": "Azure ContainerApps Session Creator",
    "ef318e2a-8334-4a05-9e4a-295a196c6a6e": "Azure Red Hat OpenShift Federated Credential Role",
    "39138f76-04e6-41f0-ba6b-c411b59081a9": "Bayer Ag Powered Services Crop Id Solution User Role",
    "b67fe603-310e-4889-b9ee-8257d09d353d": "Scheduled Events Contributor",
    "91422e52-bb88-4415-bb4a-90f5b71f6dcb": "Azure Spring Apps Job Execution Instance List Role",
    "b459aa1d-e3c8-436f-ae21-c0531140f43e": "Azure Spring Apps Job Log Reader Role"
}

appPermissionNameMap = {
    "60b235bc-7419-4bde-8dda-c6d389fde4bc": "Device.Read",
    "640bd519-35de-4a25-994f-ae29551cc6d2": "Analysis.All",
    "d533b86d-8f67-45f0-b8bb-c0cee8da0356": "Analysis.All",
    "e1e4ebc7-1bb4-4ccc-8394-895d471ba1a7": "user_impersonation",
    "c9265686-1717-4d25-a640-1f46263a162c": "BingCortana-Internal.ReadWrite",
    "d5b659cc-4375-466d-9c53-348d569b471a": "User.Read",
    "80692e1c-c3eb-439d-8ca4-ff20ad6cbb0e": "CompliancePolicy-Internal.ReadWrite",
    "5320cf34-4df3-4e6b-9727-fa69d3e2dd76": "UnifiedPolicy.User.Read",
    "58e8028a-07da-44f8-9dce-69f2052e9a0f": "vso.threads_full",
    "6c67f103-736c-44a0-9c09-6e72547c7d99": "vso.securefiles_write",
    "a07b91f9-72ea-4d16-a874-018f0350e3c1": "vso.securefiles_read",
    "2b7fbe3e-6b64-4f44-a125-fb407930daaf": "vso.securefiles_manage",
    "7c6f675c-fff5-4f8a-adf1-1a3d6f3fafdc": "vso.pipelineresources_use",
    "8deb8858-ff9b-4c4e-b702-5a6abbb28db0": "vso.pipelineresources_manage",
    "c994c1ad-fd6d-42ae-9af7-20d4820fe36c": "vso.connected_server",
    "ba2781d8-d6df-4b58-ac73-d80e7cdd25cd": "vso.auditstreams_manage",
    "47446fe8-9e9f-4bb2-bc8b-81a861caeddb": "vso.auditlog",
    "fcd8f1a4-ac62-487a-b198-13632f189646": "vso.analytics",
    "8f4f9d85-c065-4d6c-8535-99d2998c84bd": "vso.environment_manage",
    "09370e63-5e5c-4c44-b89a-6368427605d4": "vso.agentpools_manage",
    "ff83db68-cb4a-4cff-9bfe-285ed2bb9e45": "vso.agentpools",
    "0d85fdcb-8267-4af0-857e-7f76b110fbdc": "vso.build",
    "b64406bf-2a08-4182-b51e-f51dd0f6d5a3": "vso.build_execute",
    "b325850d-aa53-41ed-b77a-c5036b2f39fa": "vso.code",
    "028ffaf1-6f06-490a-979e-38011f92fb7c": "vso.code_write",
    "5f1d8cdf-acb3-47db-b79d-e0c6f18e262d": "vso.code_manage",
    "9aae797f-f2fc-47b9-bae7-1db49fdd874b": "vso.code_full",
    "7082e756-8e76-4ebc-a2b0-353809a642c2": "vso.code_status",
    "c3cbdc26-4b85-4be1-bfb4-af3a552fb28c": "vso.entitlements",
    "eafb48a2-84ed-4179-802a-5d6f1fe452f6": "vso.memberentitlementmanagement",
    "7f232b5a-2cf4-410c-833e-7fcb6175eb94": "vso.memberentitlementmanagement_write",
    "8fd343dd-9d94-4128-b3a3-f0ba1b869463": "vso.extension",
    "657d7b2a-c30e-48d1-8041-f563ec1c94fa": "vso.extension_manage",
    "9a68ae69-5073-4b4d-bb8a-d9f5acc6f008": "vso.extension.data",
    "c144cb3f-c759-4b9f-991d-37b7b8877072": "vso.extension.data_write",
    "75a97209-eb46-4571-9d6b-777ae5fcb245": "vso.graph",
    "e5125ad5-f716-4bc5-8688-14499b80567e": "vso.graph_manage",
    "8b01a8c5-f24c-4740-8104-d74337d52c0f": "vso.identity_manage",
    "98b7775c-bc8f-4a14-8ca3-d83bfff24d81": "vso.machinegroup_manage",
    "c2353c51-3f94-413b-b7b1-083b387258c0": "vso.gallery",
    "87cbee9a-42a4-4213-963a-189cb029f8fa": "vso.gallery_acquire",
    "ac7ed1fb-75be-4f8c-adf3-4d19a5cead08": "vso.gallery_publish",
    "05ac28f3-1561-4528-8579-c379a0f02805": "vso.gallery_manage",
    "e7fce5bb-fd6c-4f04-9a7d-bc4d67ea64fc": "vso.notification",
    "10e32108-6193-4cd9-b405-ab95c87509b0": "vso.notification_write",
    "90f74b44-f4ec-4f41-9003-cb9cb64cdd32": "vso.notification_manage",
    "0284cfbf-b7a6-4576-b9f4-cade73cfc16f": "vso.notification_diagnostics",
    "fcc79b02-ad6b-4ac7-af05-70cb9e349708": "vso.packaging",
    "fb6a8425-8933-4b7f-9c4a-154568e06e5c": "vso.packaging_write",
    "1c2a30a3-4b4c-42b1-bb10-6f24faf344d7": "vso.packaging_manage",
    "7b1a2725-1134-40f5-a891-d20bbb122919": "vso.project",
    "e8a8f033-da2f-4059-ba3e-63a8f69b8842": "vso.project_write",
    "0bf9fd64-9272-43aa-8459-00e29f78e146": "vso.project_manage",
    "a6abae6c-fe64-4795-aea0-ccf174ec25cf": "vso.release",
    "1decc0a5-a110-4bb7-86e5-0b0ecf40c010": "vso.release_execute",
    "36d3e2c4-2a6b-4dd0-aa72-058aaedf09d4": "vso.release_manage",
    "59ead6af-1488-485a-bd24-059f30ad33f2": "vso.security_manage",
    "503568bd-aea0-4478-a536-a8325f5f0830": "vso.serviceendpoint",
    "81928d24-d278-4dc9-baf9-6756e5ea62e2": "vso.serviceendpoint_query",
    "3e49c96c-b24e-493b-a225-497a7b3805ab": "vso.work_full",
    "dfc8977a-1f87-4e99-95cb-4bd25e4f546d": "vso.work_write",
    "3214d9aa-5551-4ef3-a866-22914177e2a4": "vso.work",
    "859fb1f9-e5ab-4e67-88f8-a971d3e4707a": "vso.tokenadministration",
    "ea83b09f-09d2-4ee5-bb93-d346c57debdb": "vso.tokens",
    "6f9f984c-a956-40b7-a6ac-4f7e3f091f96": "vso.serviceendpoint_manage",
    "c424c3d9-15df-4837-9fa3-b9ed83b3687a": "vso.symbols",
    "61b345ff-217b-4c81-9648-88991cf1c1ee": "vso.symbols_write",
    "6314624e-fd22-4945-a279-2bab145fe26e": "vso.symbols_manage",
    "8f5046df-6ee0-497b-b5b2-5e125f882eae": "vso.taskgroups_read",
    "8be3739c-dabb-4cf4-a05d-207a5220e4f0": "vso.taskgroups_write",
    "7a350bc8-d2d9-4842-9c59-a815a1923097": "vso.taskgroups_manage",
    "e9e366b1-b116-44b7-bd65-575d6bc13fc8": "vso.dashboards",
    "885358bd-5763-4432-a781-5f2c78eb29e2": "vso.dashboards_manage",
    "c0efe20b-0db1-4aec-9cb5-cdc097b2e773": "vso.test",
    "0a731f7b-93ec-4267-aa35-47b4b9fcdf08": "vso.test_write",
    "4ee63f9b-9e65-476c-a487-9fea1e00c7ef": "vso.profile",
    "cf053792-b7ad-46ba-aecb-a8e9b706587e": "vso.profile_write",
    "469808c3-0aad-4ce3-854e-0080dfc973d9": "vso.variablegroups_read",
    "c4679fff-04f1-4e29-88b4-4ae78bf4ee27": "vso.variablegroups_write",
    "e20dcb7e-deff-4025-805a-853e74ff44c1": "vso.variablegroups_manage",
    "7ad94a7f-9169-422b-a66b-1c74dea4c016": "vso.wiki",
    "b5ffdb18-5c2f-420d-a35a-8ffe20092235": "vso.wiki_write",
    "e1bca0e2-994e-4688-b5f6-665b49ee1787": "vso.identity",
    "ee69721e-6c3a-468f-a9ec-302d16a4c599": "user_impersonation",
    "ddbb8d0c-c86b-4ece-bcb7-0f031a9cf103": "CustomDetections.ReadWrite",
    "15f11de4-5113-4268-a2d1-0bad43d781f9": "AdvancedHunting.Read",
    "12c153a4-4204-4224-aa3c-4626e2f47c2b": "Incident.Read",
    "2af415cc-88cf-4146-a0c8-444c3a80d5db": "Incident.ReadWrite",
    "06b7d4cf-7757-4402-b310-dfc29621dc81": "Forms.Read",
    "2b46f208-3e71-4016-b165-71b4918b527b": "Forms.ReadWrite",
    "17a73123-533c-4f69-a37c-be22ec00e5fe": "Responses.ReadWrite",
    "67959cf5-ad1e-4b18-b9df-58fad1e7eb40": "Responses.Read.All",
    "c9c9a04d-3b66-4ca8-a00c-fca953e2afd3": "user_impersonation",
    "9e24c11e-3043-4e1f-bf19-c9560ef9a969": "Sways.ReadWrite",
    "c1b318ae-a684-4c27-ab24-81350fb6a401": "workspace.write",
    "f05e1490-846d-4ed2-abcf-869977a8a09f": "workspace.read",
    "902331d7-9647-4800-bf07-7965fac11f10": "user_impersonation",
    "d603c21a-d512-4b5a-b552-c233ebbeaf2e": "get_data_warehouse",
    "a0f3e90e-0c99-4c7d-bfaf-69531a09579c": "deploymenttask.read",
    "64b22404-2ac7-4ca5-a15d-607e62d2694b": "deploymenttask.readwrite",
    "50bf3dfa-9431-427d-823a-f146d9350034": "TBD",
    "05d808b8-d17a-47c9-ae7f-e20768cbad5d": "ComplianceManager.ReadWrite.All",
    "e808ab43-7555-447f-8b87-1d6a5c5038ef": "Documents.Read.All",
    "df0d2e21-1705-4006-b158-1114609fdfbd": "eDiscovery.Export.Download",
    "06d98eed-6e1d-47d1-af81-f69ca60a0e97": "Connector.Read",
    "fd7bf697-168c-45be-b7ba-e94b3529deff": "user_impersonation",
    "6f47731f-d307-453d-a5fb-72c9d98ab40d": "Region.ReadWrite",
    "09be18e9-0ff4-4f30-bb6b-5b92aade000c": "apps.read.all",
    "60b1c89f-1cb7-4c03-886c-60986531eccf": "Authorization.ReadWrite",
    "fe9a8b27-e305-4092-99e1-2cfe1d895f9d": "Read/Write",
    "33622fe9-9998-44a0-acd3-e5b2ec2bca45": "ServiceHealth.Read",
    "a1709332-8cf0-4afe-b4d8-2b7b4eb87a88": "ServiceHealth.Write",
    "825c9d21-ba03-4e97-8007-83f020ff8c0f": "Deprecated_ActivityReports.Read",
    "69784729-33e3-471d-b130-744ce05343e5": "Deprecated_ThreatIntelligence.Read",
    "b3b78c39-cb1d-4d17-820a-25d9196a800e": "ActivityReports.Read",
    "17f1c501-83cd-414c-9064-cd10f7aef836": "ThreatIntelligence.Read",
    "4807a72c-ad38-4250-94c9-4eabfe26cd55": "ActivityFeed.ReadDlp",
    "594c1fb6-4f81-4475-ae41-0c394909246c": "ActivityFeed.Read",
    "e2cea78f-e743-4d8f-a16a-75b629a038ae": "ServiceHealth.Read",
    "5184a2ce-115e-4318-9526-df3e39c2e839": "EndUser.Access",
    "27c61d54-eb42-4315-8793-6e5715a19746": "Flows.Write.Plans",
    "0b575251-2c95-46df-bc75-c8c43e6b7116": "Flows.Read.Plans",
    "e45c5562-459d-4d1b-8148-83eb1b6dcf83": "Flows.Read.All",
    "30b2d850-00c3-4802-b7ae-ece9af9de5c6": "Flows.Manage.All",
    "822a9cde-503a-472d-a530-d1dc9cd0d52b": "Activity.Read.All",
    "e9cbd5de-0031-493e-8fb1-60712d03cc8b": "Approvals.Read.All",
    "d05743e4-fb24-4dff-8a33-0f6c73c964bd": "Approvals.Manage.All",
    "44d8c55c-9ffc-4546-883e-9041b5bb0b01": "User",
    "e323f13a-1fcc-49cc-883f-c6da13ae0542": "MicrosoftTunnelGatewayEnrollment",
    "76e55082-bbde-4602-b506-bba9c6368668": "Account.ReadWrite.All",
    "0db7d603-2368-4c9a-8f47-adc9ac73e5e1": "Notification.ReadWrite.All",
    "15fdfc00-27d5-4f79-8a38-8efe91e3c1cc": "Device.Read.All",
    "c8750fbf-30e2-40ed-8519-e2876cbeccb9": "Account.Read.All",
    "66a874a2-b739-43fa-8e1a-176cd8290cf5": "Collection.Read.All",
    "d430b935-3087-4654-8d58-25faba0dabb5": "InventoryClass.Read.All",
    "b026af69-9eae-4bb3-9351-304d4987e170": "Boundary.Read.All",
    "47d9c114-7cc8-47c6-9e62-4c5955b05905": "SPHome",
    "0a8cab7d-5369-41c7-ae0f-dc63a8f0465a": "Application.ReadWrite",
    "e1eeeffa-b5a5-4b80-ae8f-ccb93d4b75eb": "PeopleSettings.Read.All",
    "5430838e-68e7-4b12-b353-06478ace39c3": "PeopleSettings.ReadWrite.All",
    "bbbcc29c-7bd7-48f0-8c8b-ef5f9865b626": "ReportingWebService.Read",
    "17f07f5d-fb80-4278-ba37-70ae04d476a3": "Organization.ReadWrite.All",
    "1d490c92-d2ca-4a30-b52e-6edf5f279f4d": "Organization.Read.All",
    "dab085de-3e14-432f-a47f-84b6457059c4": "Mail.ReadBasic",
    "505d82a7-24f3-4632-bffc-4d21625b31de": "Notes.Read",
    "1b69a6c3-108d-42d0-a3ec-fafcd610e80b": "Notes.ReadWrite",
    "3b5f3d61-589b-4a3c-a359-5dd4b5ee5bd5": "EWS.AccessAsUser.All",
    "eb665d05-7f76-4d1b-b176-1cfc814e668d": "User.Read.All",
    "9b005f11-86f0-45f7-8c27-4fff5d849916": "User.ReadBasic.All",
    "d36ad51d-15a2-458d-9b3a-16dbe4c51c30": "MailboxSettings.Read",
    "c21d8660-9de1-4404-85b6-59695921bd8d": "Calendars.Read.Shared",
    "4585ecca-5b47-432f-ac70-e1391e4951ed": "Calendars.ReadWrite.Shared",
    "16572339-6149-452b-b084-280b01354687": "Mail.Send.Shared",
    "b09ec548-3f99-4d0a-859c-c9b7ff53b7a9": "Mail.ReadWrite.Shared",
    "1d894596-c906-42b1-8422-9360440c1c0c": "Mail.Read.Shared",
    "c54cba4f-60fe-4332-b0de-b5990fd1999e": "Contacts.ReadWrite.Shared",
    "d6aa6fa9-3360-416a-b8db-021249d58e86": "Contacts.Read.Shared",
    "3d5e9942-27d3-4e96-80b1-696c7a3369c1": "Tasks.Read.Shared",
    "2915e980-bca5-4194-9a3f-71c4ccdbd77b": "Tasks.ReadWrite.Shared",
    "185758ba-798d-4b72-9e54-429a413a2510": "Mail.Read",
    "75767999-c7a8-481e-a6b4-19458e0b30a5": "Mail.ReadWrite",
    "5eb43c10-865a-4259-960a-83946678f8dd": "Mail.Send",
    "5b9be81f-2977-4d27-8faf-bb43af8fc705": "Calendars.Read",
    "765f423e-b55d-412e-97e3-13a800c3a537": "Calendars.ReadWrite",
    "181aac24-028a-486e-a649-b3742c74ec71": "Contacts.Read",
    "32253599-e142-4cf0-810d-4827eedd1cfa": "Contacts.ReadWrite",
    "b5c79e22-9bf2-42d7-b60d-1b95c11ebc66": "Group.Read.All",
    "27235839-268c-4d68-a668-351401ff623a": "Group.ReadWrite.All",
    "6223a6d3-53ef-4f8f-982a-895b39483c61": "User.Read",
    "f9408c03-bd3d-48c4-8bee-17a72d20bd9c": "User.ReadWrite",
    "6222dbab-a24c-4210-9d91-2f47cf565614": "User.ReadBasic.All",
    "9478ac54-3753-4543-b95a-4fad24978902": "People.Read",
    "a88daf86-d44d-4077-8258-54131dd44e5d": "People.ReadWrite",
    "ab4f2b77-0b06-4fc1-a9de-02113fc2ab7c": "Exchange.Manage",
    "8af8046f-5694-470f-91e4-d47ad05eda18": "Tasks.Read",
    "6b49b74d-642f-4417-a6b4-820576845707": "Tasks.ReadWrite",
    "2e83d72d-8895-4b66-9eea-abb43449ab8b": "MailboxSettings.ReadWrite",
    "44882612-f346-430a-b938-4f00ee1c77a7": "Contacts.ReadWrite.All",
    "d660a04c-7b62-4b4c-bea3-89226df00142": "Contacts.Read.All",
    "bbd1ca91-75e0-4814-ad94-9c5dbbae3415": "Calendars.ReadWrite.All",
    "da710fc9-1e83-407b-8c5c-09d225031769": "Calendars.Read.All",
    "e843bc88-e493-446d-a73c-0ded7ff1913f": "Mail.Send.All",
    "140e747e-90d3-4de0-8618-85a0cc7a1129": "Mail.ReadWrite.All",
    "ad13ac2e-ad46-4dc0-b7da-249c94395a6d": "Mail.Read.All",
    "266d2589-20b5-4f91-9a03-89247d1be8da": "EAS.AccessAsUser.All",
    "43ed0a33-2264-4716-b3bd-c5d8e248eebf": "Place.Read.All",
    "fb698133-92fa-453e-a9ed-688e10f2e5ac": "POP.AccessAsUser.All",
    "76faac2a-0f20-42f1-928a-50de5b9dbe52": "SMTP.Send",
    "195adc35-e27b-454b-a7ed-1ecdffa1c09f": "IMAP.AccessAsUser.All",
    "8cac6046-ce43-4348-855c-efd9d956b7bf": "OPX.MyDay",
    "405782ba-4062-4ea3-bd33-f7c731841e3b": "OPX.MyDay.Shared",
    "d056cee4-aed2-4aa4-b2a9-292fe18b06d2": "OPX.MyDay.All",
    "3c7192af-9629-4473-9276-d35e4e4b36c5": "DeviceManagementManagedApps.ReadWrite",
    "36393f92-d362-4c50-8880-82c92586a155": "OrgSettings-Planner.Read.All",
    "2e483df6-5d5c-44ee-88f3-e5238f38ebb6": "OrgSettings-Planner.ReadWrite.All",
    "0c93847b-70f8-4a59-b353-a04ef5d88f75": "Tasks.ReadWrite.Published",
    "8057a3f8-ac27-4195-984c-ee6efa721ef1": "Tasks.Read.Published",
    "817468d0-81dd-4cb5-94ac-07ca133fbbf6": "Purview.DelegatedAccess",
    "ba9c6a98-63fd-487c-b835-c1f895764e25": "webhook.readwrite.all",
    "086327cd-9afe-4777-8341-b136a1866bb3": "self_service_device_delete",
    "e79e5e22-ae68-4744-b17f-95a009916d6e": "InformationProtectionPolicy.Read",
    "bf59e00b-be0a-4c3d-bf14-ce55d7146a41": "InformationProtectionPolicy.Read.All",
    "fdf2c210-c550-4378-b72d-0d94197f7bd3": "Mail.Read",
    "749d9cae-ceda-4718-bd22-1ae6830cbee6": "Files.Read",
    "36073ebf-e0ad-4838-b99a-8f63f2b60db1": "People.Read",
    "2aec0168-f9e2-4ce1-bb0f-1145f35f5a64": "SubstrateSearch-Internal.ReadWrite",
    "537ceb4f-32cd-4b8e-bab3-8303e950ccf0": "QnA.Read.All",
    "9af00aa9-a362-40d2-bb42-7ef349af67d4": "organizationsettings.readwrite",
    "0eb56b90-a7b5-43b5-9402-8137a8083e90": "User",
    "934e7a4e-6b72-4c56-966c-0ab878a30c89": "operations.readwrite",
    "739f66f6-655e-48e4-b5bd-2bbeb6077954": "Purview.DataAccess.All",
    "384a8502-84c5-41d9-a875-7834b77c8005": "RbacAccessCheck.read",
    "6f44fc23-ea08-4666-8329-85597e11bdcd": "mtproleinfo.read",
    "6b300195-82d7-4a39-a7bc-0510371998cc": "alert.read",
    "bcc2bc0d-d08c-412a-b24d-f6f78d714bdc": "alert.write",
    "edfd2d1c-b4b5-4b83-b5e8-c38594e49c26": "RbacTenantStatus.Read",
    "4e26c42d-fab0-4daa-9ea6-d860a28aa7d0": "RbacTenantStatus.Write",
    "06ab0d31-7112-476e-a479-66394bec63d6": "MessageTrace.Read.All",
    "3e4e080e-55db-4fa9-8d68-0d9199d4c792": "QuarantinedMessage.Read.All",
    "cc02f7ae-3d9b-42c9-bc91-3424d92c5547": "AirAdminAction.tenant.read",
    "43f2aa58-36d7-421e-8628-fbe9b129bf76": "AirAdminAction.tenant.write",
    "27787a44-0423-4f0d-a417-1276c93397fb": "TenantLicenseStatus.Read.All",
    "b87cb2cc-0570-4e76-9606-3528d5fb44e7": "AtpStandardPolicy.Tenant.Read",
    "9945d5be-d9cb-45d0-b347-3f827c0d374d": "AtpStandardPolicy.Tenant.Write",
    "2da9421b-01d5-43ec-9c8e-b1bfa4a8b2bb": "LabelAnalyticsActivityData.Read.All",
    "78ce3f0f-a1ce-49c2-8cde-64b5c0896db4": "user_impersonation",
    "898f9f5d-bf7c-4bf5-97ed-39cda772c50a": "PushChannel.ReadWrite.All",
    "ed05fd6e-dbd5-4815-b368-18c07b9acc1e": "pidlsdktest.read",
    "59c7e161-b483-4c17-91db-1c8b632c90b1": "proposal.read",
    "e734da10-5e7c-48a0-a906-1a0d8b751264": "teams",
    "7779ae0d-4f2f-4872-814a-93f7abc91f97": "PowerBi.Read.All",
    "96e14e6f-576d-4ee9-ae5c-e9fe7445abac": "Topic.Read.All",
    "dddc7efc-d0ac-464b-86c6-376374a9aea9": "Calendar.ReadWrite",
    "92bacdd9-8c69-46f7-a004-387210ecd2eb": "Acronym.Read.All",
    "92f12b12-0573-4bc5-b115-41dd9c760233": "Bookmark.ReadWrite.Suggested",
    "9ee66b54-9cf0-41b8-87da-d62f8c21222b": "User.Read.All",
    "fe6d53fc-0936-42ba-8388-d39c6855c3f2": "Group.Read.All",
    "e017a1f7-f5a6-4dc5-a7b6-4342362e299b": "Bookmark.Read.All",
    "bfc6f88b-6314-451d-ac7c-501307ad192a": "QnA.Read.All",
    "ff60b1a1-5694-4b26-9c81-a5f4fabf51f5": "FloorPlan.Read.All",
    "b74d6cc7-732d-424d-9f47-b08e1404f765": "Building.Read.All",
    "79bb59ea-208c-4cff-881e-098caabe543a": "Files.Read.All",
    "917d67d7-f22b-4ff6-a49f-5e402819ba8a": "Sites.Read.All",
    "3c4d478b-f6a6-450d-a6d9-4c0e217aaa18": "Conversations.Read.All",
    "73c5d1d0-1ba7-4978-ad4c-32f0a8a1a9ed": "Calendar.Read.All",
    "c11daebe-235e-4429-ab4c-43569661ff2a": "NewsFeed.Read",
    "4b007936-25ce-4129-a310-7367d52b2036": "NewsFeed.ReadWrite",
    "e06fee6d-72ac-417d-bb34-d1b82b9f5346": "People.Read.All",
    "8040cfef-0635-4aa6-b099-9f40d6866bbb": "invoke",
    "857ba34d-369c-4a02-89ae-83e98336ec02": "UserPolicies.ReadWrite",
    "7e204991-dcdd-4986-9ff0-d058192184d7": "UserPolicies.Read",
    "44e84b5a-52a3-4b41-975c-6c960414004a": "Conversations.Initiate",
    "d0c8f2ea-8f80-4289-8e78-4bc821cde1bc": "Meetings.ReadWrite",
    "208afe8f-9dfa-4f72-a755-6b810d61f42f": "User.ReadWrite",
    "4d48dea7-b534-4bca-9d76-5f8a7a8edae8": "Conversations.Receive",
    "5bdeff8b-73d9-4b8a-9e9b-d44c6105f9b4": "Contacts.ReadWrite",
    "0cea5a30-f6f8-42b5-87a0-84cc26822e02": "User.Read.All",
    "82866913-39a9-4be7-8091-f4fa781088ae": "User.ReadWrite.All",
    "2cfdc887-d7b4-4798-9b33-3d98d6b95dd2": "MyFiles.Write",
    "dd2c8d78-58e1-46d7-82dd-34d411282686": "MyFiles.Read",
    "56680e0d-d2a3-4ae1-80d8-3c4f2100e3d0": "AllSites.FullControl",
    "b3f70a70-8a4b-4f95-9573-d71c496a53f4": "AllSites.Manage",
    "640ddd16-e5b7-4d71-9690-3f4022699ee7": "AllSites.Write",
    "4e0d77b0-96ba-4398-af14-3baa780278f4": "AllSites.Read",
    "1002502a-9a71-4426-8551-69ab83452fab": "Sites.Search.All",
    "59a198b5-0420-45a8-ae59-6da1cb640505": "TermStore.ReadWrite.All",
    "a468ea40-458c-4cc2-80c4-51781af71e41": "TermStore.Read.All",
    "e7e732bd-932b-45c4-8ce5-40d60a7daad9": "ProjectWebApp.FullControl",
    "2beb830c-70d1-4f5b-a983-79cbdb0c6c6a": "Project.Read",
    "d75a7b17-f04e-40d9-8e35-79b949bdb891": "Project.Write",
    "b8341dab-4143-49da-8eb9-3d8c073f9e77": "EnterpriseResource.Read",
    "2511a087-5795-4cae-9123-d5b7d6ec4844": "EnterpriseResource.Write",
    "c4258712-0efb-41f1-b6bc-be58e4e32f3f": "TaskStatus.Submit",
    "a4c14cd7-8bd6-4337-8e87-78623dfc023b": "ProjectWebAppReporting.Read",
    "59d925c6-b0e3-424b-96f0-779fff385048": "user_impersonation",
    "fc946a4f-bc4d-413b-a090-b2c86113ec4f": "LicenseManager.AccessAsUser",
    "e9aa7b67-ea0d-435b-ab36-592cd9b23d61": "discovery.read",
    "cb792285-1541-416c-a581-d8ede4ebc219": "settings.manage",
    "8e41f311-31d5-43aa-bb79-8fd4e14a8745": "settings.read",
    "f6e78c1a-b9c7-42d3-b067-220689a7a2e9": "discovery.manage",
    "83bc8d83-2679-44ef-b813-d5f556fc4474": "investigation.read",
    "a832eaa3-0cfc-4a2b-9af1-27c5b092dd40": "investigation.manage",
    "a8737248-d2c2-4a7c-9759-3dfaad5c2f19": "user_impersonation",
    "3105f1e2-2f5e-4dbc-b276-a29474e18597": "Connector.Read",
    "07c496ee-38d1-46df-b73d-45e1ff46d11e": "User.Read.All",
    "fb3f85f1-4cd2-4a54-a18f-3cb26ceb50a7": "user_impersonation",
    "34f7024b-1bed-402f-9664-f5316a1e1b4a": "UnifiedPolicy.User.Read",
    "5db81a03-0de0-432b-b31e-71d57c8d2e0b": "user_impersonation",
    "8e5870bb-8808-44dc-8e10-c509ed919ddd": "access_as_user",
    "7a638d43-6e2d-4bf0-bffd-477785a2c721": "Environment.Execute.All",
    "72e814f5-a6b9-4316-b2ca-d07f426c178c": "Environment.Reshare.All",
    "995d4201-6a2d-45c6-bad2-9f2aba89298d": "Environment.ReadWrite.All",
    "80a4f621-10a7-45e5-a961-79e9b81831d0": "Environment.Read.All",
    "346e63ff-7cb8-4d86-9f6b-c9212f86a719": "Connection.Reshare.All",
    "3be8fe94-2189-4d8b-89c6-dd35c5cea6ef": "Connection.ReadWrite.All",
    "9ff18859-b8d5-4a89-9912-448b84dfb097": "Connection.Read.All",
    "b43e1ada-25ee-416f-bd5c-512976ddc74b": "UserState.ReadWrite.All",
    "76e2ebd5-0dfb-4a5b-93c7-ed89e0362834": "Capacity.Read.All",
    "4eabc3d1-b762-40ff-9da5-0e18fdf11230": "Capacity.ReadWrite.All",
    "b2f1b2fa-f35c-407c-979c-a858a808ba85": "Workspace.Read.All",
    "445002fb-a6f2-4dc1-a81e-4254a111cd29": "Workspace.ReadWrite.All",
    "d2e42f6b-2baf-4ff4-83ef-51e66321516e": "Gateway.Read.All",
    "ddb3ca45-a192-477d-acb2-46bf9dc586de": "Gateway.ReadWrite.All",
    "d594897b-76e7-4b2b-984b-b4adff35e109": "Tenant.ReadWrite.All",
    "f3076109-ca66-412a-be10-d4ee1be95d47": "Content.Create",
    "322b68b2-0804-416e-86a5-d772c567b6e6": "Dataset.ReadWrite.All",
    "7f33e027-4039-419b-938e-2f8ca153e68e": "Dataset.Read.All",
    "2448370f-f988-42cd-909c-6528efd67c1a": "Dashboard.Read.All",
    "01944dba-21df-426f-bb8c-796488be96ad": "Tenant.Read.All",
    "8b01a991-5a5a-47f8-91a2-84d6bfd72c02": "App.Read.All",
    "27789c5b-aca8-4cb6-94b8-bcc8964dd8ad": "StorageAccount.ReadWrite.All",
    "e677843f-76d8-44d3-bcdb-ec40dea919e7": "StorageAccount.Read.All",
    "dbe6434c-63f0-42bb-be8e-122ec1bad4d2": "Pipeline.Read.All",
    "199f155b-cccd-4be4-bbe6-ca9a867b24b4": "Pipeline.ReadWrite.All",
    "652d7d02-6ff0-4cf7-9516-cf77d33a3ae4": "Pipeline.Deploy",
    "6098cd04-d625-4e1c-91d6-f7888f645256": "Datamart.ReadWrite.All",
    "7a27a256-301d-4359-b77b-c2b759d2e362": "Item.ReadWrite.All",
    "9e7c970c-1dc5-482d-b2a1-2a4fed211921": "SemanticModel.ReadWrite.All",
    "35735863-502b-4a11-8f65-b0bbe7ec8e95": "Warehouse.ReadWrite.All",
    "d2bc95fc-440e-4b0e-bafd-97182de7aef5": "Item.Read.All",
    "caf40b1a-f10e-4da1-86e4-5fda17eb2b07": "Item.Execute.All",
    "a405c0f7-5d2f-4e19-8db7-7323bae0b3c3": "PaginatedReport.ReadWrite.All",
    "bd305576-f504-4e9a-81d4-d16c7eb5334b": "Eventstream.ReadWrite.All",
    "726667b1-01a6-4be4-b04c-e95eae4023a8": "KQLDatabase.ReadWrite.All",
    "753e9303-2fd9-496e-aa7c-cf84a133f42a": "KQLDataConnection.ReadWrite.All",
    "dbc7f8f6-3822-41e6-aebd-5a79e2ddc72a": "SQLEndpoint.Read.All",
    "88ba374a-d581-4944-b7c7-1181754eba74": "KQLQueryset.ReadWrite.All",
    "e0c0aef0-3eab-49ca-9662-50cc7bd13bfb": "DataPipeline.ReadWrite.All",
    "91f75836-b68c-4fff-84db-4372412a2c82": "Datamart.Read.All",
    "d2090f0b-c876-45ea-b6fa-785e7ef84788": "SemanticModel.Read.All",
    "6f4dd5b6-1369-4aef-a71b-8a734a9e0a20": "Warehouse.Read.All",
    "565b3968-767c-4100-8771-a827146f38ce": "Lakehouse.Execute.All",
    "3e801746-e22a-4fcb-a3f5-315ace8e165a": "Notebook.Execute.All",
    "3492d2fc-251d-4a2b-8be4-97f06fd6d0d4": "SparkJobDefinition.Execute.All",
    "7e010a28-f5fa-4e63-b03d-2dc25cba9d2e": "DataPipeline.Execute.All",
    "5ce2a0b7-2512-440d-bf05-d5db590cc4c7": "Eventstream.Read.All",
    "24367f1a-a6d6-410d-b438-378ed19cb875": "KQLDatabase.Read.All",
    "59b5791b-482f-4b95-8498-fe078f6bd6fa": "KQLDataConnection.Read.All",
    "8826b95a-bc76-4025-97f1-8c89c3d5f210": "KQLQueryset.Read.All",
    "e93694df-fa72-4011-aad8-f3648588c762": "PaginatedReport.Read.All",
    "a61cf2d1-8b81-4518-b2bb-a24e0831c17a": "DataPipeline.Read.All",
    "b13a1be2-e407-47b5-8429-12f4ad4f9fcd": "Scorecard.ReadWrite.All",
    "a74298d9-12f6-45f5-808d-7907af21179c": "Scorecard.Read.All",
    "529939f7-18e3-4be4-ba92-b01894a4fadf": "Dataflow.Execute.All",
    "3101f5b2-b314-4bbd-a1f6-8a05f94f33ea": "MLExperiment.Execute.All",
    "6b03f425-0a8e-4c54-ba35-df73806f1396": "MLModel.Execute.All",
    "17cddc84-5ff7-4b6a-a017-632384c5e063": "Datamart.Execute.All",
    "110e2f5f-6226-4c3f-8d02-4b30b33e5fd1": "Eventstream.Execute.All",
    "21b4da43-510a-43ac-afd4-580e1e2c09c8": "KQLDatabase.Execute.All",
    "6872ffe8-d8d4-46f9-9a32-5537dad08dd2": "KQLDataConnection.Execute.All",
    "b84b0d8d-9870-4b2b-92d2-9bfa7f940db3": "KQLQueryset.Execute.All",
    "b0a64161-0e6a-4f7c-aa14-a1f9413136f3": "Report.Execute.All",
    "4aaafe5b-1b27-4403-88f2-e3ebbb8bccc5": "PaginatedReport.Execute.All",
    "dc75a12a-fef2-436d-8311-fed5b7e3a9d0": "Scorecard.Execute.All",
    "42b94671-298c-48a0-a55d-077e48186883": "SemanticModel.Execute.All",
    "aa70d616-e57e-4a5a-84cd-07de4250dd2e": "SQLEndpoint.Execute.All",
    "d17eaf78-91ce-4314-9101-868b933996fb": "Warehouse.Execute.All",
    "c67b16d3-b5b8-4c87-8ca0-a8e00c6d6ff3": "Dashboard.Reshare.All",
    "ad056abd-4839-4bb1-ba68-ffcf8194a869": "Dataflow.Reshare.All",
    "881e9f00-4e9c-4798-bc50-832fea2cdbe6": "Lakehouse.Reshare.All",
    "27296d33-1a83-44d6-9665-63f4902781f9": "MLExperiment.Reshare.All",
    "44abf802-73c1-42f4-a26f-915b4c27fa8f": "Datamart.Reshare.All",
    "ff4d87c4-a161-49a8-a886-fe14bf6a2203": "Eventstream.Reshare.All",
    "02e8d710-956c-4760-b996-2e83935c2cf5": "Item.Reshare.All",
    "83a35b59-6a34-40f4-ac4e-5bf5a6ff9a5d": "KQLDatabase.Reshare.All",
    "8191607d-cbe5-49c6-b480-1aae71f3dce6": "KQLDataConnection.Reshare.All",
    "b02aa3b5-6fb3-48b8-803a-57bdef45d20c": "Notebook.ReadWrite.All",
    "2cb667b2-c449-4f2d-a1ad-e0ffa27b5d75": "MLModel.ReadWrite.All",
    "5d9a285a-0847-4aa7-a9db-4991dedc2b53": "MLModel.Read.All",
    "e4f65fe4-b466-4254-89ea-2fcdc8d8ac49": "MLExperiment.ReadWrite.All",
    "179809f0-8b05-4f65-bdd0-920fb4945c33": "MLExperiment.Read.All",
    "ec20a3e3-8c0b-4d75-8d1b-a9ffdbbe2519": "SparkJobDefinition.ReadWrite.All",
    "beaf3087-05af-4060-a0a5-29779c902004": "SparkJobDefinition.Read.All",
    "eee83281-2212-467d-b9e3-2aadfb170f33": "Lakehouse.ReadWrite.All",
    "13060bfd-9305-4ec6-8388-8916580f4fa9": "Lakehouse.Read.All",
    "0a25ca24-b130-4a32-affd-29d640b63f14": "Notebook.Read.All",
    "f9759906-80a4-4f4a-b010-24b832bc6a30": "Dataflow.Read.All",
    "ddd37690-e119-40c5-a821-3746ea6125c4": "Dataflow.ReadWrite.All",
    "b271f05e-8329-4b97-baa4-91cf15b99cf1": "Dashboard.ReadWrite.All",
    "4ae1bf56-f562-4747-b7bc-2fa0874ed46f": "Report.Read.All",
    "7504609f-c495-4c64-8542-686125a5a36f": "Report.ReadWrite.All",
    "2d3aa07c-d364-4ce0-acbc-b7e151ee161d": "KQLQueryset.Reshare.All",
    "5a93e9d0-4312-4fad-bbb5-44c74a75083a": "MLModel.Reshare.All",
    "9ff20ed3-e70b-486e-9686-006be349a5d6": "Notebook.Reshare.All",
    "54f4913d-63d6-4256-a270-f16a6222e625": "Report.Reshare.All",
    "49dd4a50-f26f-4cc8-b895-227eb620861d": "SparkJobDefinition.Reshare.All",
    "b510092a-d399-45f3-b1d5-4e2d34c87997": "PaginatedReport.Reshare.All",
    "62816fca-afaa-44af-abd6-9e8f604d8dbb": "Scorecard.Reshare.All",
    "868c9b47-9e35-4c69-bac3-042213ef72a3": "SemanticModel.Reshare.All",
    "15a808d7-2065-4357-8b76-47f701df3575": "SQLEndpoint.Reshare.All",
    "d7629fc2-75c0-412f-9c11-052513f055ae": "Warehouse.Reshare.All",
    "9afd59c7-4e4d-4a5d-b2aa-2777debb5cd9": "DataPipeline.Reshare.All",
    "e5c15c39-f5e8-45b2-b858-edba09abc583": "SQLEndpoint.ReadWrite.All",
    "bcd38192-b0a2-4c40-bc0e-5728ec6ee69d": "Dashboard.Execute.All",
    "b23bb8c4-af74-49b0-91dd-79ffb83cddb9": "DevX.ReadWrite.All",
    "1ddcbaa9-c4cf-4684-9048-e04a12739a8c": "RetailDataManager.Read.All",
    "e87305de-874c-4fb9-a7c1-fff664dc5d6e": "RetailDataManager.ReadWrite.All",
    "5793b2af-bc3b-4f1d-bbb1-9a3e359dd8e1": "RetailDataManager.Execute.All",
    "d95f0afe-0ace-431b-9741-b29d7a02e19b": "RetailDataManager.Reshare.All",
    "cd1718e4-3e09-4381-a6e1-183e245f8613": "Eventhouse.Read.All",
    "b13393d0-9253-4ca8-be5a-be145f337ea3": "Eventhouse.ReadWrite.All",
    "0a5f551e-003b-482b-b5fb-7124a9510ba1": "Eventhouse.Execute.All",
    "1318ed2f-75ad-4748-b33a-d49044214bdb": "Eventhouse.Reshare.All",
    "a55d4405-a37a-4d41-ad6e-745665a3bbcb": "Workspace.GitCommit.All",
    "5809ab1d-9154-49e7-a105-d82760eac8cf": "Workspace.GitUpdate.All",
    "547211ef-7223-404f-8519-fee52fda6402": "OneLake.Read.All",
    "ada1b44b-4474-40ed-b32c-e3543dccec0e": "OneLake.ReadWrite.All",
    "ebfcd32b-babb-40f4-a14b-42706e83bd28": "AccessReview.Read.All",
    "e4aa47b9-9a69-4109-82ed-36ec70d85ff1": "AccessReview.ReadWrite.All",
    "5af8c3f5-baca-439a-97b0-ea58a435e269": "AccessReview.ReadWrite.Membership",
    "9084c10f-a2d6-4713-8732-348def50fe02": "Acronym.Read.All",
    "3361d15d-be43-4de6-b441-3c746d05163d": "AdministrativeUnit.Read.All",
    "7b8a2d34-6b3f-4542-a343-54651608ad81": "AdministrativeUnit.ReadWrite.All",
    "af2819c9-df71-4dd3-ade7-4d7c9dc653b7": "Agreement.Read.All",
    "ef4b5d93-3104-4664-9053-a5c49ab44218": "Agreement.ReadWrite.All",
    "0b7643bb-5336-476f-80b5-18fbfbc91806": "AgreementAcceptance.Read",
    "a66a5341-e66e-4897-9d52-c2df58c2bfb9": "AgreementAcceptance.Read.All",
    "e03cf23f-8056-446a-8994-7d93dfc8b50e": "Analytics.Read",
    "1b6ff35f-31df-4332-8571-d31ea5a4893f": "APIConnectors.Read.All",
    "c67b52c5-7c69-48b6-9d48-7b3af3ded914": "APIConnectors.ReadWrite.All",
    "88e58d74-d3df-44f3-ad47-e89edf4472e4": "AppCatalog.Read.All",
    "1ca167d5-1655-44a1-8adf-1414072e1ef9": "AppCatalog.ReadWrite.All",
    "3db89e36-7fa6-4012-b281-85f3d9d9fd2e": "AppCatalog.Submit",
    "af281d3a-030d-4122-886e-146fb30a0413": "AppCertTrustConfiguration.Read.All",
    "4bae2ed4-473e-4841-a493-9829cfd51d48": "AppCertTrustConfiguration.ReadWrite.All",
    "ffa91d43-2ad8-45cc-b592-09caddeb24bb": "Application-RemoteDesktopConfig.ReadWrite.All",
    "c79f8feb-a9db-4090-85f9-90d820caa0eb": "Application.Read.All",
    "bdfbf15f-ee85-4955-8675-146e8e5296b5": "Application.ReadWrite.All",
    "84bccea3-f856-4a8a-967b-dbe0a3d53a64": "AppRoleAssignment.ReadWrite.All",
    "104a7a4b-ca76-4677-b7e7-2f4bc482f381": "AttackSimulation.Read.All",
    "27608d7c-2c66-4cad-a657-951d575f5a60": "AttackSimulation.ReadWrite.All",
    "e4c9e354-4dc5-45b8-9e7c-e1393b0b1a20": "AuditLog.Read.All",
    "ba78b16f-1e01-41b6-89ca-73e0a32b304c": "AuditLogsQuery-CRM.Read.All",
    "ee3409fe-617f-43cf-bd1e-fc8b38049e69": "AuditLogsQuery-Endpoint.Read.All",
    "5ff2f415-e0f1-4d11-bfd0-6d87c0f667fd": "AuditLogsQuery-Entra.Read.All",
    "6c8c71d2-c7e1-45b0-ac6d-1d2724fba6ae": "AuditLogsQuery-Exchange.Read.All",
    "4a72c235-a50d-4870-b598-fd88fd1fa074": "AuditLogsQuery-OneDrive.Read.All",
    "30630b65-ed12-4a81-9130-e3a964109fae": "AuditLogsQuery-SharePoint.Read.All",
    "1d9e7ac3-0eca-442c-82f9-e92625af6e6d": "AuditLogsQuery.Read.All",
    "57b030f1-8c35-469c-b0d9-e4a077debe70": "AuthenticationContext.Read.All",
    "ba6d575a-1344-4516-b777-1404f5593057": "AuthenticationContext.ReadWrite.All",
    "2bf6d319-dfca-4c22-9879-f88dcfaee6be": "BillingConfiguration.ReadWrite.All",
    "b27a61ec-b99c-4d6a-b126-c4375d08ae30": "BitlockerKey.Read.All",
    "5a107bfc-4f00-4e1a-b67e-66451267bc68": "BitlockerKey.ReadBasic.All",
    "7f36b48e-542f-4d3b-9bcb-8406f0ab9fdb": "Bookings.Manage.All",
    "33b1df99-4b29-4548-9339-7a7b83eaeebc": "Bookings.Read.All",
    "948eb538-f19d-4ec5-9ccc-f059e1ea4c72": "Bookings.ReadWrite.All",
    "02a5a114-36a6-46ff-a102-954d89d9ab02": "BookingsAppointment.ReadWrite.All",
    "98b17b35-f3b1-4849-a85f-9f13733002f0": "Bookmark.Read.All",
    "fb9be2b7-a7fc-4182-aec1-eda4597c43d5": "BrowserSiteLists.Read.All",
    "83b34c85-95bf-497b-a04e-b58eca9d49d0": "BrowserSiteLists.ReadWrite.All",
    "d16480b2-e469-4118-846b-d3d177327bee": "BusinessScenarioConfig.Read.All",
    "c47e7b6e-d6f1-4be9-9ffd-1e00f3e32892": "BusinessScenarioConfig.Read.OwnedBy",
    "755e785b-b658-446f-bb22-5a46abd029ea": "BusinessScenarioConfig.ReadWrite.All",
    "b3b7fcff-b4d4-4230-bf6f-90bd91285395": "BusinessScenarioConfig.ReadWrite.OwnedBy",
    "25b265c4-5d34-4e44-952d-b567f6d3b96d": "BusinessScenarioData.Read.OwnedBy",
    "19932d57-2952-4c60-8634-3655c79fc527": "BusinessScenarioData.ReadWrite.OwnedBy",
    "465a38f9-76ea-45b9-9f34-9e8b0d4b0b42": "Calendars.Read",
    "2b9c4092-424d-4249-948d-b43879977640": "Calendars.Read.Shared",
    "662d75ba-a364-42ad-adee-f5f880ea4878": "Calendars.ReadBasic",
    "1ec239c2-d7c9-4623-a91a-a9775856bb36": "Calendars.ReadWrite",
    "12466101-c9b8-439a-8589-dd09ee67e8e9": "Calendars.ReadWrite.Shared",
    "43431c03-960e-400f-87c6-8f910321dca3": "CallEvents.Read",
    "101147cf-4178-4455-9d58-02b5c164e759": "Channel.Create",
    "cc83893a-e232-4723-b5af-bd0b01bcfe65": "Channel.Delete.All",
    "9d8982ae-4365-4f57-95e9-d6032a4c0b87": "Channel.ReadBasic.All",
    "2eadaff8-0bce-4198-a6b9-2cfc35a30075": "ChannelMember.Read.All",
    "0c3e411a-ce45-4cd1-8f30-f99a3efa7b11": "ChannelMember.ReadWrite.All",
    "2b61aa8a-6d36-4b2f-ac7b-f29867937c53": "ChannelMessage.Edit",
    "767156cb-16ae-4d10-8f8b-41b657c8c8c8": "ChannelMessage.Read.All",
    "5922d31f-46c8-4404-9eaf-2117e390a8a4": "ChannelMessage.ReadWrite",
    "ebf0f66e-9fb1-49e4-a278-222f76911cf4": "ChannelMessage.Send",
    "233e0cf1-dd62-48bc-b65b-b38fe87fcf8e": "ChannelSettings.Read.All",
    "d649fb7c-72b4-4eec-b2b4-b15acf79e378": "ChannelSettings.ReadWrite.All",
    "38826093-1258-4dea-98f0-00003be2b8d0": "Chat.Create",
    "bb64e6fc-6b6d-4752-aea0-dd922dbba588": "Chat.ManageDeletion.All",
    "f501c180-9344-439a-bca0-6cbf209fd270": "Chat.Read",
    "9547fcb5-d03f-419d-9948-5928bbf71b0f": "Chat.ReadBasic",
    "9ff7295e-131b-4d94-90e1-69fde507ac11": "Chat.ReadWrite",
    "7e9a077b-3711-42b9-b7cb-5fa5f3f7fea7": "Chat.ReadWrite.All",
    "c5a9e2b1-faf6-41d4-8875-d381aa549b24": "ChatMember.Read",
    "dea13482-7ea6-488f-8b98-eb5bbecf033d": "ChatMember.ReadWrite",
    "cdcdac3a-fd45-410d-83ef-554db620e5c7": "ChatMessage.Read",
    "116b7235-7cc6-461e-b163-8e55691d839e": "ChatMessage.Send",
    "ad46d60e-1027-4b75-af88-7c14ccf43a19": "CloudApp-Discovery.Read.All",
    "5252ec4e-fd40-4d92-8c68-89dd1d3c6110": "CloudPC.Read.All",
    "9d77138f-f0e2-47ba-ab33-cd246c8b79d1": "CloudPC.ReadWrite.All",
    "12ae2e92-14b5-47b2-babb-4e890bbedc0a": "Community.Read.All",
    "9e69467d-e0e2-402b-a926-3d796990197f": "Community.ReadWrite.All",
    "f2143d35-9b4b-480d-951c-d083e69eeb2c": "ConsentRequest.Create",
    "5942b2f6-5a7b-40af-aa37-4b6ea5447506": "ConsentRequest.Read",
    "f3bfad56-966e-4590-a536-82ecf548ac1e": "ConsentRequest.Read.All",
    "e694a3a1-7878-46d8-8c29-3d195f6589f4": "ConsentRequest.ReadApprove.All",
    "497d9dfa-3bd1-481a-baab-90895e54568c": "ConsentRequest.ReadWrite.All",
    "ff74d97f-43af-4b68-9f2a-b77ee6968c5d": "Contacts.Read",
    "242b9d9e-ed24-4d09-9a52-f43769beb9d4": "Contacts.Read.Shared",
    "d56682ec-c09e-4743-aaf4-1a3aac4caa21": "Contacts.ReadWrite",
    "afb6c84b-06be-49af-80bb-8f3f77004eab": "Contacts.ReadWrite.Shared",
    "81594d25-e88e-49cf-ac8c-fecbff49f994": "CrossTenantInformation.ReadBasic.All",
    "cb1ba48f-d22b-4325-a07f-74135a62ee41": "CrossTenantUserProfileSharing.Read",
    "759dcd16-3c90-463c-937e-abf89f991c18": "CrossTenantUserProfileSharing.Read.All",
    "eed0129d-dc60-4f30-8641-daf337a39ffd": "CrossTenantUserProfileSharing.ReadWrite",
    "64dfa325-cbf8-48e3-938d-51224a0cac01": "CrossTenantUserProfileSharing.ReadWrite.All",
    "b2052569-c98c-4f36-a5fb-43e5c111e6d0": "CustomAuthenticationExtension.Read.All",
    "8dfcf82f-15d0-43b3-bc78-a958a13a5792": "CustomAuthenticationExtension.ReadWrite.All",
    "b13ff42e-f321-4d7d-a462-141c46a1b832": "CustomDetection.Read.All",
    "c34088fb-0649-4714-af0b-bcbfec155897": "CustomDetection.ReadWrite.All",
    "b46ffa80-fe3d-4822-9a1a-c200932d54d0": "CustomSecAttributeAssignment.Read.All",
    "ca46335e-8453-47cd-a001-8459884efeae": "CustomSecAttributeAssignment.ReadWrite.All",
    "1fcdeaab-b519-44dd-bffc-ed1fd15a24e0": "CustomSecAttributeAuditLogs.Read.All",
    "ce026878-a0ff-4745-a728-d4fedd086c07": "CustomSecAttributeDefinition.Read.All",
    "8b0160d4-5743-482b-bb27-efc0a485ca4a": "CustomSecAttributeDefinition.ReadWrite.All",
    "de6ea87d-10bd-467c-8682-d525a0c61b89": "CustomTags.Read.All",
    "2f1bbe0a-f34b-4efb-9edb-8db8dcb50eca": "CustomTags.ReadWrite.All",
    "0c0064ea-477b-4130-82a5-4c2cc4ff68aa": "DelegatedAdminRelationship.Read.All",
    "885f682f-a990-4bad-a642-36736a74b0c7": "DelegatedAdminRelationship.ReadWrite.All",
    "a197cdc4-a8e8-4d49-9d35-4ca7c83887b4": "DelegatedPermissionGrant.Read.All",
    "41ce6ca6-6826-4807-84f1-1c82854f7ee5": "DelegatedPermissionGrant.ReadWrite.All",
    "bac3b9c2-b516-4ef4-bd3b-c2ef73d8d804": "Device.Command",
    "11d4cd79-5ba5-460f-803f-e22c8ab85ccd": "Device.Read",
    "951183d1-1a61-466f-a6d1-1fde911bfd95": "Device.Read.All",
    "280b3b69-0437-44b1-bc20-3b2fca1ee3e9": "DeviceLocalCredential.Read.All",
    "9917900e-410b-4d15-846e-42a357488545": "DeviceLocalCredential.ReadBasic.All",
    "4edf5f54-4666-44af-9de9-0144fb4b6e8c": "DeviceManagementApps.Read.All",
    "7b3f05d5-f68c-4b8d-8c59-a2ecd12f24af": "DeviceManagementApps.ReadWrite.All",
    "f1493658-876a-4c87-8fa7-edb559b3476a": "DeviceManagementConfiguration.Read.All",
    "0883f392-0a7a-443d-8c76-16a6d39c7b63": "DeviceManagementConfiguration.ReadWrite.All",
    "3404d2bf-2b13-457e-a330-c24615765193": "DeviceManagementManagedDevices.PrivilegedOperations.All",
    "314874da-47d6-4978-88dc-cf0d37f0bb82": "DeviceManagementManagedDevices.Read.All",
    "44642bfe-8385-4adc-8fc6-fe3cb2c375c3": "DeviceManagementManagedDevices.ReadWrite.All",
    "49f0cc30-024c-4dfd-ab3e-82e137ee5431": "DeviceManagementRBAC.Read.All",
    "0c5e8a55-87a6-4556-93ab-adc52c4d862d": "DeviceManagementRBAC.ReadWrite.All",
    "8696daa5-bce5-4b2e-83f9-51b6defc4e1e": "DeviceManagementServiceConfig.Read.All",
    "662ed50a-ac44-4eef-ad86-62eed9be2a29": "DeviceManagementServiceConfig.ReadWrite.All",
    "0e263e50-5827-48a4-b97c-d940288653c7": "Directory.AccessAsUser.All",
    "06da0dbc-49e2-44d2-8312-53f166ab848a": "Directory.Read.All",
    "c5366453-9fb0-48a5-a156-24f0c49a4b84": "Directory.ReadWrite.All",
    "cba5390f-ed6a-4b7f-b657-0efc2210ed20": "Directory.Write.Restricted",
    "34d3bd24-f6a6-468c-b67c-0c365c1d6410": "DirectoryRecommendations.Read.All",
    "f37235e8-90a0-4189-93e2-e55b53867ccd": "DirectoryRecommendations.ReadWrite.All",
    "2f9ee017-59c1-4f1d-9472-bd5529a7b311": "Domain.Read.All",
    "0b5d694c-a244-4bde-86e6-eb5cd07730fe": "Domain.ReadWrite.All",
    "ff91d191-45a0-43fd-b837-bd682c4a0b0f": "EAS.AccessAsUser.All",
    "99201db3-7652-4d5a-809a-bdb94f85fe3c": "eDiscovery.Read.All",
    "acb8f680-0834-4146-b69e-4ab1b39745ad": "eDiscovery.ReadWrite.All",
    "8523895c-6081-45bf-8a5d-f062a2f12c9f": "EduAdministration.Read",
    "63589852-04e3-46b4-bae9-15d5b1050748": "EduAdministration.ReadWrite",
    "091460c9-9c4a-49b2-81ef-1f3d852acce2": "EduAssignments.Read",
    "c0b0103b-c053-4b2e-9973-9f3a544ec9b8": "EduAssignments.ReadBasic",
    "2f233e90-164b-4501-8bce-31af2559a2d3": "EduAssignments.ReadWrite",
    "2ef770a1-622a-47c4-93ee-28d6adbed3a0": "EduAssignments.ReadWriteBasic",
    "484859e8-b9e2-4e92-b910-84db35dadd29": "EduCurricula.Read",
    "4793c53b-df34-44fd-8d26-d15c517732f5": "EduCurricula.ReadWrite",
    "a4389601-22d9-4096-ac18-36a927199112": "EduRoster.Read",
    "5d186531-d1bf-4f07-8cea-7c42119e1bd9": "EduRoster.ReadBasic",
    "359e19a6-e3fa-4d7f-bcab-d28ec592b51e": "EduRoster.ReadWrite",
    "64a6cdd6-aab1-4aaf-94b8-3cc8405e90d0": "email",
    "5449aa12-1393-4ea2-a7c7-d0e06c1a56b2": "EntitlementManagement.Read.All",
    "ae7a573d-81d7-432b-ad44-4ed5c9d89038": "EntitlementManagement.ReadWrite.All",
    "e9fdcbbb-8807-410f-b9ec-8d5468c7c2ac": "EntitlementMgmt-SubjectAccess.ReadWrite",
    "f7dd3bed-5eec-48da-bc73-1c0ef50bc9a1": "EventListener.Read.All",
    "d11625a6-fe21-4fc6-8d3d-063eba5525ad": "EventListener.ReadWrite.All",
    "9769c687-087d-48ac-9cb3-c37dde652038": "EWS.AccessAsUser.All",
    "a38267a5-26b6-4d76-9493-935b7599116b": "ExternalConnection.Read.All",
    "bbbbd9b3-3566-4931-ac37-2b2180d9e334": "ExternalConnection.ReadWrite.All",
    "4082ad95-c812-4f02-be92-780c4c4f1830": "ExternalConnection.ReadWrite.OwnedBy",
    "922f9392-b1b7-483c-a4be-0089be7704fb": "ExternalItem.Read.All",
    "b02c54f8-eb48-4c50-a9f0-a149e5a2012f": "ExternalItem.ReadWrite.All",
    "4367b9d7-cee7-4995-853c-a0bdfe95c1f9": "ExternalItem.ReadWrite.OwnedBy",
    "47167bec-55a7-4caf-9ecc-8d4566e3cfb1": "ExternalUserProfile.Read.All",
    "c6068dc7-a791-46a4-a811-b8228e6649ab": "ExternalUserProfile.ReadWrite.All",
    "3a1e4806-a744-4c70-80fc-223bf8582c46": "Family.Read",
    "10465720-29dd-4523-a11a-6a75c743c9d9": "Files.Read",
    "df85f4d6-205c-4ac5-a5ea-6bf408dba283": "Files.Read.All",
    "5447fe39-cb82-4c1a-b977-520e67e724eb": "Files.Read.Selected",
    "5c28f0bf-8a70-41f1-8ab2-9032436ddb65": "Files.ReadWrite",
    "863451e7-0667-486c-a5d6-d135439485f0": "Files.ReadWrite.All",
    "8019c312-3263-48e6-825e-2b833497195b": "Files.ReadWrite.AppFolder",
    "17dde5bd-8c17-420f-a486-969730c1b827": "Files.ReadWrite.Selected",
    "085ca537-6565-41c2-aca7-db852babc212": "FileStorageContainer.Selected",
    "f534bf13-55d4-45a9-8f3c-c92fe64d6131": "Financials.ReadWrite.All",
    "092211d9-ca1a-427b-813e-b79c7653fe71": "Goals-Export.Read.All",
    "2edeb9fd-4228-480c-a26d-2ed52011cf3d": "Goals-Export.ReadWrite.All",
    "5f8c59db-677d-491f-a6b8-5f174b11ec1d": "Group.Read.All",
    "4e46008b-f24c-477d-8fff-7bb4ec7aafe0": "Group.ReadWrite.All",
    "bc024368-1153-4739-b217-4326f2e966d0": "GroupMember.Read.All",
    "f81125ac-d3b7-4573-a3b2-7099cc39df9e": "GroupMember.ReadWrite.All",
    "43781733-b5a7-4d1b-98f4-e8edff23e1a9": "IdentityProvider.Read.All",
    "f13ce604-1677-429f-90bd-8a10b9f01325": "IdentityProvider.ReadWrite.All",
    "8f6a01e7-0391-4ee5-aa22-a3af122cef27": "IdentityRiskEvent.Read.All",
    "9e4862a5-b68f-479e-848a-4e07e25c9916": "IdentityRiskEvent.ReadWrite.All",
    "ea5c4ab0-5a73-4f35-8272-5d5337884e5d": "IdentityRiskyServicePrincipal.Read.All",
    "bb6f654c-d7fd-4ae3-85c3-fc380934f515": "IdentityRiskyServicePrincipal.ReadWrite.All",
    "d04bb851-cb7c-4146-97c7-ca3e71baf56c": "IdentityRiskyUser.Read.All",
    "e0a7cdbb-08b0-4697-8264-0069786e9674": "IdentityRiskyUser.ReadWrite.All",
    "2903d63d-4611-4d43-99ce-a33f3f52e343": "IdentityUserFlow.Read.All",
    "281892cc-4dbf-4e3a-b6cc-b21029bb4e82": "IdentityUserFlow.ReadWrite.All",
    "652390e4-393a-48de-9484-05f9b1212954": "IMAP.AccessAsUser.All",
    "d19c0de5-7ecb-4aba-b090-da35ebcd5425": "IndustryData-DataConnector.Read.All",
    "5ce933ac-3997-4280-aed0-cc072e5c062a": "IndustryData-DataConnector.ReadWrite.All",
    "fc47391d-ab2c-410f-9059-5600f7af660d": "IndustryData-DataConnector.Upload",
    "cb0774da-a605-42af-959c-32f438fb38f4": "IndustryData-InboundFlow.Read.All",
    "97044676-2cec-40ee-bd70-38df444c9e70": "IndustryData-InboundFlow.ReadWrite.All",
    "4741a003-8952-4be4-9217-33a0ac327122": "IndustryData-OutboundFlow.Read.All",
    "aeb68e0b-e562-4a1f-b6dd-3484ad0cbb4b": "IndustryData-OutboundFlow.ReadWrite.All",
    "a3f96ffe-cb84-40a8-ac85-582d7ef97c2a": "IndustryData-ReferenceDefinition.Read.All",
    "92685235-50c4-4702-b2c8-36043db6fa79": "IndustryData-Run.Read.All",
    "49b7016c-89ae-41e7-bd6f-b7170c5490bf": "IndustryData-SourceSystem.Read.All",
    "9599f005-05d6-4ea7-b1b1-4929768af5d0": "IndustryData-SourceSystem.ReadWrite.All",
    "c9d51f28-8ccd-42b2-a836-fd8fe9ebf2ae": "IndustryData-TimePeriod.Read.All",
    "b6d56528-3032-4f9d-830f-5a24a25e6661": "IndustryData-TimePeriod.ReadWrite.All",
    "60382b96-1f5e-46ea-a544-0407e489e588": "IndustryData.ReadBasic.All",
    "12f4bffb-b598-413c-984b-db99728f8b54": "InformationProtectionConfig.Read",
    "4ad84827-5578-4e18-ad7a-86530b12f884": "InformationProtectionPolicy.Read",
    "7d249730-51a3-4180-8ec1-214f144f1bff": "Insights-UserMetric.Read.All",
    "ac08cdae-e845-41db-adf9-5899a0ec9ef6": "LearningAssignedCourse.Read",
    "ea4c1fd9-6a9f-4432-8e5d-86e06cc0da77": "LearningContent.Read.All",
    "53cec1c4-a65f-4981-9dc1-ad75dbf1c077": "LearningContent.ReadWrite.All",
    "dd8ce36f-9245-45ea-a99e-8ac398c22861": "LearningProvider.Read",
    "40c2eb57-abaf-49f5-9331-e90fd01f7130": "LearningProvider.ReadWrite",
    "f6403ef7-4a96-47be-a190-69ba274c3f11": "LearningSelfInitiatedCourse.Read",
    "f55016cc-149c-447e-8f21-7cf3ec1d6350": "LicenseAssignment.ReadWrite.All",
    "9bcb9916-765a-42af-bf77-02282e26b01a": "LifecycleWorkflows.Read.All",
    "84b9d731-7db8-4454-8c90-fd9e95350179": "LifecycleWorkflows.ReadWrite.All",
    "570282fd-fa5c-430d-a7fd-fc8dc98a9dca": "Mail.Read",
    "7b9103a5-4610-446b-9670-80643382c1fa": "Mail.Read.Shared",
    "a4b8392a-d8d1-4954-a029-8e668a39a170": "Mail.ReadBasic",
    "b11fa0e7-fdb7-4dc9-b1f1-59facd463480": "Mail.ReadBasic.Shared",
    "024d486e-b451-40bb-833d-3e66d98c5c73": "Mail.ReadWrite",
    "5df07973-7d5d-46ed-9847-1271055cbd51": "Mail.ReadWrite.Shared",
    "e383f46e-2787-4529-855e-0e479a3ffac0": "Mail.Send",
    "a367ab51-6b49-43bf-a716-a1fb06d2a174": "Mail.Send.Shared",
    "87f447af-9fa4-4c32-9dfa-4a57a73d18ce": "MailboxSettings.Read",
    "818c620a-27a9-40bd-a6a5-d96f7d610b4b": "MailboxSettings.ReadWrite",
    "dc34164e-6c4a-41a0-be89-3ae2fbad7cd3": "ManagedTenants.Read.All",
    "b31fa710-c9b3-4d9e-8f5e-8036eecddab9": "ManagedTenants.ReadWrite.All",
    "f6a3db3e-f7e8-4ed2-a414-557c8c9830be": "Member.Read.Hidden",
    "526aa72a-5878-49fe-bf4e-357973af9b06": "MultiTenantOrganization.Read.All",
    "225db56b-15b2-4daa-acb3-0eec2bbe4849": "MultiTenantOrganization.ReadBasic.All",
    "77af1528-84f3-4023-8d90-d219cd433108": "MultiTenantOrganization.ReadWrite.All",
    "b0c61509-cfc3-42bd-9bd4-66d81785fee4": "NetworkAccess-Reports.Read.All",
    "2f7013e0-ab4e-447f-a5e1-5d419950692d": "NetworkAccess.Read.All",
    "ae2df9c5-f18d-4ec4-a51b-bdeb807f177b": "NetworkAccess.ReadWrite.All",
    "4051c7fc-b429-4804-8d80-8f1f8c24a6f7": "NetworkAccessBranch.Read.All",
    "b8a36cc2-b810-461a-baa4-a7281e50bd5c": "NetworkAccessBranch.ReadWrite.All",
    "ba22922b-752c-446f-89d7-a2d92398fceb": "NetworkAccessPolicy.Read.All",
    "b1fbad0f-ef6e-42ed-8676-bca7fa3e7291": "NetworkAccessPolicy.ReadWrite.All",
    "9d822255-d64d-4b7a-afdb-833b9a97ed02": "Notes.Create",
    "371361e4-b9e2-4a3f-8315-2a301a3b0a3d": "Notes.Read",
    "dfabfca6-ee36-4db2-8208-7a28381419b3": "Notes.Read.All",
    "615e26af-c38a-4150-ae3e-c3b0d4cb1d6a": "Notes.ReadWrite",
    "64ac0503-b4fa-45d9-b544-71a463f05da0": "Notes.ReadWrite.All",
    "ed68249d-017c-4df5-9113-e684c7f8760b": "Notes.ReadWrite.CreatedByApp",
    "89497502-6e42-46a2-8cb2-427fd3df970a": "Notifications.ReadWrite.CreatedByApp",
    "7427e0e9-2fba-42fe-b0c0-848c9e6a8182": "offline_access",
    "110e5abb-a10c-4b59-8b55-9b4daa4ef743": "OnlineMeetingArtifact.Read.All",
    "190c2bb6-1fdd-4fec-9aa2-7d571b5e1fe3": "OnlineMeetingRecording.Read.All",
    "9be106e1-f4e3-4df5-bdff-e4bc531cbe43": "OnlineMeetings.Read",
    "a65f2972-a4f8-4f5e-afd7-69ccb046d5dc": "OnlineMeetings.ReadWrite",
    "30b87d18-ebb1-45db-97f8-82ccb1f0190c": "OnlineMeetingTranscript.Read.All",
    "f6609722-4100-44eb-b747-e6ca0536989d": "OnPremDirectorySynchronization.Read.All",
    "c2d95988-7604-4ba1-aaed-38a5f82a51c7": "OnPremDirectorySynchronization.ReadWrite.All",
    "8c4d5184-71c2-4bf8-bb9d-bc3378c9ad42": "OnPremisesPublishingProfiles.ReadWrite.All",
    "37f7f235-527c-4136-accd-4a02d197296e": "openid",
    "4908d5b9-3fb2-4b1e-9336-1888b7937185": "Organization.Read.All",
    "46ca0847-7e6b-426e-9775-ea810a948356": "Organization.ReadWrite.All",
    "9082f138-6f02-4f3a-9f4d-5f3c2ce5c688": "OrganizationalBranding.Read.All",
    "15ce63de-b141-4c9a-a9a5-241bf27c6aaf": "OrganizationalBranding.ReadWrite.All",
    "08432d1b-5911-483c-86df-7980af5cdee0": "OrgContact.Read.All",
    "1e9b7a7e-4d64-44ff-acf5-2e9651c1519f": "OrgSettings-AppsAndServices.Read.All",
    "c167b0e7-47c0-48e8-9eee-9892f58018fa": "OrgSettings-AppsAndServices.ReadWrite.All",
    "9862d930-5aec-4a98-8d4f-7277a8db9bcb": "OrgSettings-DynamicsVoice.Read.All",
    "4cea26fb-6967-4234-82c4-c044414743f8": "OrgSettings-DynamicsVoice.ReadWrite.All",
    "210051a0-1ffc-435c-ae76-02d226d05752": "OrgSettings-Forms.Read.All",
    "346c19ff-3fb2-4e81-87a0-bac9e33990c1": "OrgSettings-Forms.ReadWrite.All",
    "8cbdb9f6-9c2e-451a-814d-ec606e5d0212": "OrgSettings-Microsoft365Install.Read.All",
    "1ff35e91-19eb-42d8-aa2d-cc9891127ae5": "OrgSettings-Microsoft365Install.ReadWrite.All",
    "7ff96f41-f022-45ba-acd8-ef3f03063d6b": "OrgSettings-Todo.Read.All",
    "087502c2-5263-433e-abe3-8f77231a0627": "OrgSettings-Todo.ReadWrite.All",
    "8804798e-5934-4e30-8ce3-ef88257cecd4": "PartnerBilling.Read.All",
    "d88fd3fb-53d3-4c1c-8c39-787fcac2ed7a": "PendingExternalUserProfile.Read.All",
    "93a1fb28-c908-4826-904e-0c74ad352b73": "PendingExternalUserProfile.ReadWrite.All",
    "ba47897c-39ec-4d83-8086-ee8256fa737d": "People.Read",
    "b89f9189-71a5-4e70-b041-9887f0bc7e4a": "People.Read.All",
    "ec762c5f-388b-4b16-8693-ac1efbc611bc": "PeopleSettings.Read.All",
    "e67e6727-c080-415e-b521-e3f35d5248e9": "PeopleSettings.ReadWrite.All",
    "cb8f45a0-5c2e-4ea1-b803-84b870a7d7ec": "Place.Read.All",
    "4c06a06a-098a-4063-868e-5dfee3827264": "Place.ReadWrite.All",
    "4c7f93d2-6b0b-4e05-91aa-87842f0a2142": "PlaceDevice.Read.All",
    "eafd6a71-e95a-4f8a-bb6e-fb84ab7fbd9e": "PlaceDevice.ReadWrite.All",
    "572fea84-0151-49b2-9301-11cb16974376": "Policy.Read.All",
    "633e0fce-8c58-4cfb-9495-12bbd5a24f7c": "Policy.Read.ConditionalAccess",
    "d146432f-b803-4ed4-8d42-ba74193a6ede": "Policy.Read.IdentityProtection",
    "414de6ea-2d92-462f-b120-6e2a809a6d01": "Policy.Read.PermissionGrant",
    "4f5bc9c8-ea54-4772-973a-9ca119cb0409": "Policy.ReadWrite.AccessReview",
    "b27add92-efb2-4f16-84f5-8108ba77985c": "Policy.ReadWrite.ApplicationConfiguration",
    "edb72de9-4252-4d03-a925-451deef99db7": "Policy.ReadWrite.AuthenticationFlows",
    "7e823077-d88e-468f-a337-e18f1f0e6c7c": "Policy.ReadWrite.AuthenticationMethod",
    "edd3c878-b384-41fd-95ad-e7407dd775be": "Policy.ReadWrite.Authorization",
    "ad902697-1014-4ef5-81ef-2b4301988e8c": "Policy.ReadWrite.ConditionalAccess",
    "4d135e65-66b8-41a8-9f8b-081452c91774": "Policy.ReadWrite.ConsentRequest",
    "014b43d0-6ed4-4fc6-84dc-4b6f7bae7d85": "Policy.ReadWrite.CrossTenantAccess",
    "40b534c3-9552-4550-901b-23879c90bcf9": "Policy.ReadWrite.DeviceConfiguration",
    "b5219784-1215-45b5-b3f1-88fe1081f9c0": "Policy.ReadWrite.ExternalIdentities",
    "92a38652-f13b-4875-bc77-6e1dbb63e1b2": "Policy.ReadWrite.FeatureRollout",
    "be1be369-4540-4ac9-8928-79de99f70d8f": "Policy.ReadWrite.FedTokenValidation",
    "7256e131-3efb-4323-9854-cf41c6021770": "Policy.ReadWrite.IdentityProtection",
    "a8ead177-1889-4546-9387-f25e658e2a79": "Policy.ReadWrite.MobilityManagement",
    "2672f8bb-fd5e-42e0-85e1-ec764dd2614e": "Policy.ReadWrite.PermissionGrant",
    "0b2a744c-2abf-4f1e-ad7e-17a087e2be99": "Policy.ReadWrite.SecurityDefaults",
    "cefba324-1a70-4a6e-9c1d-fd670b7ae392": "Policy.ReadWrite.TrustFramework",
    "d7b7f2d9-0f45-4ea1-9d42-e50810c06991": "POP.AccessAsUser.All",
    "76bc735e-aecd-4a1d-8b4c-2b915deabb79": "Presence.Read",
    "9c7a330d-35b3-4aa1-963d-cb2b9f927841": "Presence.Read.All",
    "8d3c54a7-cf58-4773-bf81-c0cd6ad522bb": "Presence.ReadWrite",
    "d69c2d6d-4f72-4f99-a6b9-663e32f8cf68": "PrintConnector.Read.All",
    "79ef9967-7d59-4213-9c64-4b10687637d8": "PrintConnector.ReadWrite.All",
    "90c30bed-6fd1-4279-bf39-714069619721": "Printer.Create",
    "93dae4bd-43a1-4a23-9a1a-92957e1d9121": "Printer.FullControl.All",
    "3a736c8a-018e-460a-b60c-863b2683e8bf": "Printer.Read.All",
    "89f66824-725f-4b8f-928e-e1c5258dc565": "Printer.ReadWrite.All",
    "ed11134d-2f3f-440d-a2e1-411efada2502": "PrinterShare.Read.All",
    "5fa075e9-b951-4165-947b-c63396ff0a37": "PrinterShare.ReadBasic.All",
    "06ceea37-85e2-40d7-bec3-91337a46038f": "PrinterShare.ReadWrite.All",
    "21f0d9c0-9f13-48b3-94e0-b6b231c7d320": "PrintJob.Create",
    "248f5528-65c0-4c88-8326-876c7236df5e": "PrintJob.Read",
    "afdd6933-a0d8-40f7-bd1a-b5d778e8624b": "PrintJob.Read.All",
    "6a71a747-280f-4670-9ca0-a9cbf882b274": "PrintJob.ReadBasic",
    "04ce8d60-72ce-4867-85cf-6d82f36922f3": "PrintJob.ReadBasic.All",
    "b81dd597-8abb-4b3f-a07a-820b0316ed04": "PrintJob.ReadWrite",
    "036b9544-e8c5-46ef-900a-0646cc42b271": "PrintJob.ReadWrite.All",
    "6f2d22f2-1cb6-412c-a17c-3336817eaa82": "PrintJob.ReadWriteBasic",
    "3a0db2f6-0d2a-4c19-971b-49109b19ad3d": "PrintJob.ReadWriteBasic.All",
    "490f32fd-d90f-4dd7-a601-ff6cdc1a3f6c": "PrintSettings.Read.All",
    "9ccc526a-c51c-4e5c-a1fd-74726ef50b8f": "PrintSettings.ReadWrite.All",
    "b3a539c9-59cb-4ad5-825a-041ddbdc2bdb": "PrivilegedAccess.Read.AzureAD",
    "d329c81c-20ad-4772-abf9-3f6fdb7e5988": "PrivilegedAccess.Read.AzureADGroup",
    "1d89d70c-dcac-4248-b214-903c457af83a": "PrivilegedAccess.Read.AzureResources",
    "3c3c74f5-cdaa-4a97-b7e0-4e788bfcfb37": "PrivilegedAccess.ReadWrite.AzureAD",
    "32531c59-1f32-461f-b8df-6f8a3b89f73b": "PrivilegedAccess.ReadWrite.AzureADGroup",
    "a84a9652-ffd3-496e-a991-22ba5529156a": "PrivilegedAccess.ReadWrite.AzureResources",
    "02a32cc4-7ab5-4b58-879a-0586e0f7c495": "PrivilegedAssignmentSchedule.Read.AzureADGroup",
    "06dbc45d-6708-4ef0-a797-f797ee68bf4b": "PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup",
    "8f44f93d-ecef-46ae-a9bf-338508d44d6b": "PrivilegedEligibilitySchedule.Read.AzureADGroup",
    "ba974594-d163-484e-ba39-c330d5897667": "PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup",
    "14dad69e-099b-42c9-810b-d002981feec1": "profile",
    "c492a2e1-2f8f-4caa-b076-99bbf6e40fe4": "ProgramControl.Read.All",
    "50fd364f-9d93-4ae1-b170-300e87cccf84": "ProgramControl.ReadWrite.All",
    "04a4b2a2-3f26-4fc8-87ee-9c46e68db175": "PublicKeyInfrastructure.Read.All",
    "3591b7f3-dba8-4bad-b667-7a64bd4f2b83": "PublicKeyInfrastructure.ReadWrite.All",
    "f73fa04f-b9a5-4df9-8843-993ce928925e": "QnA.Read.All",
    "07f995eb-fc67-4522-ad66-2b8ca8ea3efd": "RecordsManagement.Read.All",
    "f2833d75-a4e6-40ab-86d4-6dfe73c97605": "RecordsManagement.ReadWrite.All",
    "02e97553-ed7b-43d0-ab3c-f8bace0d040c": "Reports.Read.All",
    "84fac5f4-33a9-4100-aa38-a20c6d29e5e7": "ReportSettings.Read.All",
    "b955410e-7715-4a88-a940-dfd551018df3": "ReportSettings.ReadWrite.All",
    "f1d91a8f-88e7-4774-8401-b668d5bca0c5": "ResourceSpecificPermissionGrant.ReadForUser",
    "344a729c-0285-42c6-9014-f12b9b8d6129": "RoleAssignmentSchedule.Read.Directory",
    "8c026be3-8e26-4774-9372-8d5d6f21daff": "RoleAssignmentSchedule.ReadWrite.Directory",
    "eb0788c2-6d4e-4658-8c9e-c0fb8053f03d": "RoleEligibilitySchedule.Read.Directory",
    "62ade113-f8e0-4bf9-a6ba-5acb31db32fd": "RoleEligibilitySchedule.ReadWrite.Directory",
    "48fec646-b2ba-4019-8681-8eb31435aded": "RoleManagement.Read.All",
    "9619b88a-8a25-48a7-9571-d23be0337a79": "RoleManagement.Read.CloudPC",
    "741c54c3-0c1e-44a1-818b-3f97ab4e8c83": "RoleManagement.Read.Directory",
    "3bc15058-7858-4141-b24f-ae43b4e80b52": "RoleManagement.Read.Exchange",
    "501d06f8-07b8-4f18-b5c6-c191a4af7a82": "RoleManagement.ReadWrite.CloudPC",
    "d01b97e9-cbc0-49fe-810a-750afd5527a3": "RoleManagement.ReadWrite.Directory",
    "c1499fe0-52b1-4b22-bed2-7a244e0e879f": "RoleManagement.ReadWrite.Exchange",
    "cce71173-f76d-446e-97ff-efb2d82e11b1": "RoleManagementAlert.Read.Directory",
    "435644c6-a5b1-40bf-8f52-fe8e5b53e19c": "RoleManagementAlert.ReadWrite.Directory",
    "7e26fdff-9cb1-4e56-bede-211fe0e420e8": "RoleManagementPolicy.Read.AzureADGroup",
    "3de2cdbe-0ff5-47d5-bdee-7f45b4749ead": "RoleManagementPolicy.Read.Directory",
    "0da165c7-3f15-4236-b733-c0b0f6abe41d": "RoleManagementPolicy.ReadWrite.AzureADGroup",
    "1ff1be21-34eb-448c-9ac9-ce1f506b2a68": "RoleManagementPolicy.ReadWrite.Directory",
    "fccf6dd8-5706-49fa-811f-69e2e1b585d0": "Schedule.Read.All",
    "63f27281-c9d9-4f29-94dd-6942f7f1feb0": "Schedule.ReadWrite.All",
    "07919803-6073-4cd8-bc55-28077db0ee10": "SchedulePermissions.ReadWrite.All",
    "7d307522-aa38-4cd0-bd60-90c6f0ac50bd": "SearchConfiguration.Read.All",
    "b1a7d408-cab0-47d2-a2a5-a74a3733600d": "SearchConfiguration.ReadWrite.All",
    "1638cddf-07a4-4de2-8645-69c96cacad73": "SecurityActions.Read.All",
    "dc38509c-b87d-4da0-bd92-6bec988bac4a": "SecurityActions.ReadWrite.All",
    "bc257fb8-46b4-4b15-8713-01e91bfbe4ea": "SecurityAlert.Read.All",
    "471f2a7f-2a42-4d45-a2bf-594d0838070d": "SecurityAlert.ReadWrite.All",
    "53e6783e-b127-4a35-ab3a-6a52d80a9077": "SecurityAnalyzedMessage.Read.All",
    "48eb8c83-6e58-46e7-a6d3-8805822f5940": "SecurityAnalyzedMessage.ReadWrite.All",
    "64733abd-851e-478a-bffb-e47a14b18235": "SecurityEvents.Read.All",
    "6aedf524-7e1c-45a7-bd76-ded8cab8d0fc": "SecurityEvents.ReadWrite.All",
    "a0d0da43-a6df-4416-b63d-99c79991aae8": "SecurityIdentitiesHealth.Read.All",
    "53e51eec-2d9b-4990-97f3-c9aa5d5652c3": "SecurityIdentitiesHealth.ReadWrite.All",
    "b9abcc4f-94fc-4457-9141-d20ce80ec952": "SecurityIncident.Read.All",
    "128ca929-1a19-45e6-a3b8-435ec44a36ba": "SecurityIncident.ReadWrite.All",
    "1fe7aa48-9373-4a47-8df3-168335e0f4c9": "ServiceActivity-Exchange.Read.All",
    "d74c75b1-d5a9-479d-902d-92f8f99182c1": "ServiceActivity-Microsoft365Web.Read.All",
    "347e3c16-30f3-4ac7-9b52-fc3c053de9c9": "ServiceActivity-OneDrive.Read.All",
    "404d76f0-e10e-460a-92be-ef19600c54d1": "ServiceActivity-Teams.Read.All",
    "55896846-df78-47a7-aa94-8d3d4442ca7f": "ServiceHealth.Read.All",
    "eda39fa6-f8cf-4c3c-a909-432c683e4c9b": "ServiceMessage.Read.All",
    "636e1b0b-1cc2-4b1c-9aa9-4eeed9b9761b": "ServiceMessageViewpoint.Write",
    "9f9ce928-e038-4e3b-8faf-7b59049a8ddc": "ServicePrincipalEndpoint.Read.All",
    "7297d82c-9546-4aed-91df-3d4f0a9b3ff0": "ServicePrincipalEndpoint.ReadWrite.All",
    "2ef70e10-5bfd-4ede-a5f6-67720500b258": "SharePointTenantSettings.Read.All",
    "aa07f155-3612-49b8-a147-6c590df35536": "SharePointTenantSettings.ReadWrite.All",
    "50f66e47-eb56-45b7-aaa2-75057d9afe08": "ShortNotes.Read",
    "328438b7-4c01-4c07-a840-e625a749bb89": "ShortNotes.ReadWrite",
    "5a54b8b3-347c-476d-8f8e-42d5c7424d29": "Sites.FullControl.All",
    "65e50fdc-43b7-4915-933e-e8138f11f40a": "Sites.Manage.All",
    "205e70e5-aba6-4c52-a976-6d2d46c48043": "Sites.Read.All",
    "89fe6a52-be36-487e-b7d8-d061c450a026": "Sites.ReadWrite.All",
    "f89c84ef-20d0-4b54-87e9-02e856d66d53": "Sites.Selected",
    "258f6531-6087-4cc4-bb90-092c5fb3ed3f": "SMTP.Send",
    "9b4aa4b1-aaf3-41b7-b743-698b27e77ff6": "SpiffeTrustDomain.Read.All",
    "8ba47079-8c47-4bfe-b2ce-13f28ef37247": "SpiffeTrustDomain.ReadWrite.All",
    "9c3af74c-fd0f-4db4-b17a-71939e2a9d77": "SubjectRightsRequest.Read.All",
    "2b8fcc74-bce1-4ae3-a0e8-60c53739299d": "SubjectRightsRequest.ReadWrite.All",
    "5f88184c-80bb-4d52-9ff2-757288b2e9b7": "Subscription.Read.All",
    "7aa02aeb-824f-4fbe-a3f7-611f751f5b55": "Synchronization.Read.All",
    "7bb27fa3-ea8f-4d67-a916-87715b6188bd": "Synchronization.ReadWrite.All",
    "1a2e7420-4e92-4d2b-94cb-fb2952e9ddf7": "SynchronizationData-User.Upload",
    "f45671fb-e0fe-4b4b-be20-3d3ce43f1bcb": "Tasks.Read",
    "88d21fd4-8e5a-4c32-b5e2-4a1c95f34f72": "Tasks.Read.Shared",
    "2219042f-cab5-40cc-b0d2-16b1540b4c5f": "Tasks.ReadWrite",
    "c5ddf11b-c114-4886-8558-8a4e557cd52b": "Tasks.ReadWrite.Shared",
    "7825d5d6-6049-4ce7-bdf6-3b8d53f4bcd0": "Team.Create",
    "485be79e-c497-4b35-9400-0e3fa7f2a5d4": "Team.ReadBasic.All",
    "2497278c-d82d-46a2-b1ce-39d4cdde5570": "TeamMember.Read.All",
    "4a06efd2-f825-4e34-813e-82a57b03d1ee": "TeamMember.ReadWrite.All",
    "2104a4db-3a2f-4ea0-9dba-143d457dc666": "TeamMember.ReadWriteNonOwnerRole.All",
    "0e755559-83fb-4b44-91d0-4cc721b9323e": "TeamsActivity.Read",
    "7ab1d787-bae7-4d5d-8db6-37ea32df9186": "TeamsActivity.Send",
    "bf3fbf03-f35f-4e93-963e-47e4d874c37a": "TeamsAppInstallation.ReadForChat",
    "5248dcb1-f83b-4ec3-9f4d-a4428a961a72": "TeamsAppInstallation.ReadForTeam",
    "c395395c-ff9a-4dba-bc1f-8372ba9dca84": "TeamsAppInstallation.ReadForUser",
    "e1408a66-8f82-451b-a2f3-3c3e38f7413f": "TeamsAppInstallation.ReadWriteAndConsentForChat",
    "946349d5-2a9d-4535-abc0-7beeacaedd1d": "TeamsAppInstallation.ReadWriteAndConsentForTeam",
    "2da62c49-dfbd-40df-ba16-fef3529d391c": "TeamsAppInstallation.ReadWriteAndConsentForUser",
    "a0e0e18b-8fb2-458f-8130-da2d7cab9c75": "TeamsAppInstallation.ReadWriteAndConsentSelfForChat",
    "4a6bbf29-a0e1-4a4d-a7d1-cef17f772975": "TeamsAppInstallation.ReadWriteAndConsentSelfForTeam",
    "7a349935-c54d-44ab-ab66-1b460d315be7": "TeamsAppInstallation.ReadWriteAndConsentSelfForUser",
    "aa85bf13-d771-4d5d-a9e6-bca04ce44edf": "TeamsAppInstallation.ReadWriteForChat",
    "2e25a044-2580-450d-8859-42eeb6e996c0": "TeamsAppInstallation.ReadWriteForTeam",
    "093f8818-d05f-49b8-95bc-9d2a73e9a43c": "TeamsAppInstallation.ReadWriteForUser",
    "0ce33576-30e8-43b7-99e5-62f8569a4002": "TeamsAppInstallation.ReadWriteSelfForChat",
    "0f4595f7-64b1-4e13-81bc-11a249df07a9": "TeamsAppInstallation.ReadWriteSelfForTeam",
    "207e0cb1-3ce7-4922-b991-5a760c346ebc": "TeamsAppInstallation.ReadWriteSelfForUser",
    "48638b3c-ad68-4383-8ac4-e6880ee6ca57": "TeamSettings.Read.All",
    "39d65650-9d3e-4223-80db-a335590d027e": "TeamSettings.ReadWrite.All",
    "a9ff19c2-f369-4a95-9a25-ba9d460efc8e": "TeamsTab.Create",
    "59dacb05-e88d-4c13-a684-59f1afc8cc98": "TeamsTab.Read.All",
    "b98bfd41-87c6-45cc-b104-e2de4f0dafb9": "TeamsTab.ReadWrite.All",
    "ee928332-e9c2-4747-b4a0-f8c164b68de6": "TeamsTab.ReadWriteForChat",
    "c975dd04-a06e-4fbb-9704-62daad77bb49": "TeamsTab.ReadWriteForTeam",
    "c37c9b61-7762-4bff-a156-afc0005847a0": "TeamsTab.ReadWriteForUser",
    "0c219d04-3abf-47f7-912d-5cca239e90e6": "TeamsTab.ReadWriteSelfForChat",
    "f266662f-120a-4314-b26a-99b08617c7ef": "TeamsTab.ReadWriteSelfForTeam",
    "395dfec1-a0b9-465f-a783-8250a430cb8c": "TeamsTab.ReadWriteSelfForUser",
    "cd87405c-5792-4f15-92f7-debc0db6d1d6": "TeamTemplates.Read",
    "594f4bb6-c083-4cf9-8aa8-213823bdf351": "Teamwork.Read.All",
    "44e060c4-bbdc-4256-a0b9-dcc0396db368": "TeamworkAppSettings.Read.All",
    "87c556f0-2bd9-4eed-bd74-5dd8af6eaf7e": "TeamworkAppSettings.ReadWrite.All",
    "b659488b-9d28-4208-b2be-1c6652b3c970": "TeamworkDevice.Read.All",
    "ddd97ecb-5c31-43db-a235-0ee20e635c40": "TeamworkDevice.ReadWrite.All",
    "57587d0b-8399-45be-b207-8050cec54575": "TeamworkTag.Read",
    "539dabd7-b5b6-4117-b164-d60cd15a8671": "TeamworkTag.ReadWrite",
    "b4d26916-07e0-4daf-9096-9f6d9174aa96": "TeamworkUserInteraction.Read.All",
    "297f747b-0005-475b-8fef-c890f5152b38": "TermStore.Read.All",
    "6c37c71d-f50f-4bff-8fd3-8a41da390140": "TermStore.ReadWrite.All",
    "cac97e40-6730-457d-ad8d-4852fddab7ad": "ThreatAssessment.ReadWrite.All",
    "b152eca8-ea73-4a48-8c98-1a6742673d99": "ThreatHunting.Read.All",
    "9cc427b4-2004-41c5-aa22-757b755e9796": "ThreatIndicators.Read.All",
    "91e7d36d-022a-490f-a748-f8e011357b42": "ThreatIndicators.ReadWrite.OwnedBy",
    "f266d9c0-ccb9-4fb8-a228-01ac0d8d6627": "ThreatIntelligence.Read.All",
    "fd5353c6-26dd-449f-a565-c4e16b9fce78": "ThreatSubmission.Read",
    "7083913a-4966-44b6-9886-c5822a5fd910": "ThreatSubmission.Read.All",
    "68a3156e-46c9-443c-b85c-921397f082b5": "ThreatSubmission.ReadWrite",
    "8458e264-4eb9-4922-abe9-768d58f13c7f": "ThreatSubmission.ReadWrite.All",
    "059e5840-5353-4c68-b1da-666a033fc5e8": "ThreatSubmissionPolicy.ReadWrite.All",
    "79c4c76f-409a-4f98-884d-e2c09291ec26": "Topic.Read.All",
    "7ad34336-f5b1-44ce-8682-31d7dfcd9ab9": "TrustFrameworkKeySet.Read.All",
    "39244520-1e7d-4b4a-aee0-57c65826e427": "TrustFrameworkKeySet.ReadWrite.All",
    "73e75199-7c3e-41bb-9357-167164dbb415": "UnifiedGroupMember.Read.AsGuest",
    "550e695c-7511-40f4-ac79-e8fb9c82552d": "User-ConvertToInternal.ReadWrite.All",
    "ed8d2a04-0374-41f1-aefe-da8ac87ccc87": "User-LifeCycleInfo.Read.All",
    "7ee7473e-bd4b-4c9f-987c-bd58481f5fa2": "User-LifeCycleInfo.ReadWrite.All",
    "f92e74e7-2563-467f-9dd0-902688cb5863": "User.EnableDisableAccount.All",
    "405a51b5-8d8d-430b-9842-8be4b0e9f324": "User.Export.All",
    "63dd7cd9-b489-4adf-a28c-ac38b9a0f962": "User.Invite.All",
    "637d7bec-b31e-4deb-acc9-24275642a2c9": "User.ManageIdentities.All",
    "e1fe6dd8-ba31-4d61-89e7-88639da4683d": "User.Read",
    "a154be20-db9c-4678-8ab7-66f6cc099a59": "User.Read.All",
    "b340eb25-3456-403f-be2f-af7a0d370277": "User.ReadBasic.All",
    "b4e74841-8e56-480b-be8b-910348b18b4c": "User.ReadWrite",
    "204e0828-b5ca-4ad8-b9f3-f32a958e7cc4": "User.ReadWrite.All",
    "47607519-5fb1-47d9-99c7-da4b48f369b1": "UserActivity.ReadWrite.CreatedByApp",
    "1f6b61c5-2f65-4135-9c9f-31c0f8d32b52": "UserAuthenticationMethod.Read",
    "aec28ec7-4d02-4e8c-b864-50163aea77eb": "UserAuthenticationMethod.Read.All",
    "48971fc1-70d7-4245-af77-0beb29b53ee2": "UserAuthenticationMethod.ReadWrite",
    "b7887744-6746-4312-813d-72daeaee7e2d": "UserAuthenticationMethod.ReadWrite.All",
    "26e2f3e8-b2a1-47fc-9620-89bb5b042024": "UserNotification.ReadWrite.CreatedByApp",
    "834bcc1c-762f-41b0-bb91-1cdc323ee4bf": "UserTeamwork.Read",
    "367492fc-594d-4972-a9b5-0d58c622c91c": "UserTimelineActivity.Write.CreatedByApp",
    "27470298-d3b8-4b9c-aad4-6334312a3eac": "VirtualAppointment.Read",
    "2ccc2926-a528-4b17-b8bb-860eed29d64c": "VirtualAppointment.ReadWrite",
    "20d02fff-a0ef-49e7-a46e-019d4a6523b7": "VirtualAppointmentNotification.Send",
    "6b616635-ae58-433a-a918-8c45e4f304dc": "VirtualEvent.Read",
    "d38d189c-e29b-4344-8b3b-829bfa81380b": "VirtualEvent.ReadWrite",
    "11776c0c-6138-4db3-a668-ee621bea2555": "WindowsUpdates.ReadWrite.All",
    "f1ccd5a7-6383-466a-8db8-1a656f7d06fa": "WorkforceIntegration.Read.All",
    "08c4b377-0d23-4a8b-be2a-23c1c1d88545": "WorkforceIntegration.ReadWrite.All",
    "6b0a3177-0946-453c-95bf-1d7b1886f0e4": "User.Read",
    "5c367ba1-3a11-4284-92e9-19c836b05b1d": "user_impersonation",
    "0ec94f6b-7dfb-43d3-a076-648593587760": "LowFriction.ReadWrite",
    "62c3283a-e0b2-4608-85d5-013e99604063": "Users.Signup.Product",
    "dc13fe4e-f936-494b-8b88-09d4e9a5cde0": "Subscription.Add",
    "83e1ccc9-47d7-4632-8fbd-1a4392c87254": "Soar.SendEmail",
    "8a82ad6b-9201-4f8e-a324-b97e0fcd3e46": "License.Assign",
    "2d05a661-f651-4d57-a595-489c91eda336": "Member.Read.Hidden",
    "311a71cc-e848-46a1-bdf8-97ff7156d8e6": "User.Read",
    "cba73afc-7f69-4d86-8450-4978e04ecd1a": "User.ReadBasic.All",
    "c582532d-9d9e-43bd-a97c-2667a28ce295": "User.Read.All",
    "6234d376-f627-4f0f-90e0-dff25c5211a3": "Group.Read.All",
    "970d6fa6-214a-4a9b-8513-08fad511e2fd": "Group.ReadWrite.All",
    "78c8a3c8-a07e-4b9e-af1b-b5ccab50a175": "Directory.ReadWrite.All",
    "5778995a-e1bf-45b8-affa-663a9f3f4d04": "Directory.Read.All",
    "a42657d6-7f20-40e3-b6f0-cee03008a62a": "Directory.AccessAsUser.All",
    "80e5b1bf-3ad0-4365-943a-0ec983009b67": "Policy.Read.All",
    "96d4258f-9187-4e6c-b031-724e789b9323": "shredder.files.read",
    "ff7ac806-f9c8-40b6-b133-f3412d436c54": "User.Read.All",
    "6662245d-d5f3-42cb-b401-b08c2f424d5f": "ContentDomain.ReadWrite",
    "bbee328f-fe32-4251-a58c-9b16f9bf50c8": "ContentDomain.Read.All",
    "ed20b8a8-12e9-45f5-b3e5-69f25572d7be": "Graph.ReadWrite.All",
    "df563937-6d21-4fa5-8284-f8cd6ff567fe": "ResourceSpecificPermission.Read",
    "0cf5e046-95b4-47da-83d3-b9ca4fb97744": "ResourceSpecificPermission.ReadWrite",
    "59146b7c-ba55-445c-ad99-b0ae77e28992": "TeamsAppValidation.Submit",
    "c433c028-68c7-4c20-9f86-f974e820dcec": "TeamsAppValidation.Execute",
    "7d00ce87-dff2-46f7-8cec-977df77a9e33": "ApiSecretRegistration.ReadWrite",
    "0c981b21-0229-4b35-a0b9-82acfa228288": "Sites.Read.All",
    "7757dd34-1b17-4123-afba-9bdbeeb48d1a": "Directory.AccessAsUser.All",
    "5c9d6e0e-0f69-4535-848c-a8f9585a3dc6": "user_impersonation",
    "0e276de4-189b-47b3-8c80-ce726cfb7671": "MailboxSettings.Read",
    "d326a74b-6caa-4da2-95a3-e2a64a01e18c": "Team.ReadBasic.All",
    "e60370c1-e451-437e-aa6e-d76df38e5f15": "user_impersonation",
    "44351fcc-b88d-4077-982f-3367f5078db1": "CEH_service",
    "5063317c-fd8e-4efd-94b8-60a68284f8c4": "teams-internal.readwrite",
    "82d632fa-68b9-40ab-8c4f-f24986a057fa": "teams.readwrite",
    "fb90b455-d8cb-43db-85c7-4985d8072ed3": "teamtemplates.readwrite",
    "162b1576-a2b2-458d-b7b9-04481911b4ef": "channels.readwrite",
    "41094075-9dad-400e-a0bd-54e686782033": "user_impersonation",
    "68c6d621-ef73-4169-82d9-8a3e930a2087": "user_impersonation",
    "9125c627-3755-4ad3-8742-4d6b193c4fc2": "filteredhierarchy.read.all",
    "8762e452-5668-459a-b06a-b8f7c8469dd2": "channelmessage.read.all",
    "f06d0c46-34d8-4358-9782-36a2e777c812": "announcements.read.all",
    "f89ec176-467b-452a-a2eb-7144ac6aa9cc": "Device.Read",
"640bd519-35de-4a25-994f-ae29551cc6d2": "Analysis.All",
"c9265686-1717-4d25-a640-1f46263a162c": "BingCortana-Internal.ReadWrite",
"47d1397b-a828-452a-9b8d-2796c4e65f4e": "SemanticMachineContext.ReadWrite",
"7b307ce5-1a3c-4a39-861b-ee5bf8a58941": "User.Read.All",
"925d5331-83ad-4bb7-ac7c-a78de52131ef": "CompliancePolicy-Internal.ReadWrite",
"338446c9-b981-47d7-a96b-3e02921beace": "UnifiedPolicy.Tenant.Read",
"28d646b8-7efa-4ff7-9e39-dfb3a53b7fa6": "vso.loadtest_write",
"e000c422-1bec-45ec-9d30-083f21df9d04": "vso.loadtest",
"a7deff90-e2f5-4e4e-83a3-2c74e7002e28": "CustomDetections.ReadWrite.All",
"a9790345-4595-42e4-971a-ccdc79f19b7c": "Incident.Read.All",
"8d90f441-09cf-4fdc-ab45-e874fa3a28e8": "Incident.ReadWrite.All",
"7734e8e5-8dde-42fc-b5ae-6eafea078693": "AdvancedHunting.Read.All",
"b2734fa3-8dfe-40a9-bdab-1e1901202739": "Inventory.ReadWrite.All",
"e36263dd-a5a9-488a-9fb6-8efc97320e2b": "EnterpriseInsights.ReadWrite.All",
"4e4d02ed-7e38-4f9d-aa08-12b14a713f5e": "Forms.ReadWrite.All",
"5dadf886-6063-4169-a7a7-88a2a9f8f7cd": "Forms.Read.All",
"e23bd57d-bfd5-4906-867f-89fb5ed8cd43": "Application.Read.All",
"006e763d-a822-41fc-8df5-8d3d7fe20022": "Content.Writer",
"7347eb49-7a1a-43c5-8eac-a5cd1d1c7cf0": "Content.SuperUser",
"7f740376-647b-4ad7-9ff7-292af252707a": "Content.DelegatedReader",
"d13f921c-7f21-4c08-bade-db9d048bd0da": "Content.DelegatedWriter",
"83262d98-99cb-496d-8da9-e0ceed85d0ed": "AzureEventGridSecureWebhookSubscriber",
"5fb95dd2-a975-42c6-8c44-1fc62f94a6aa": "Sways.ReadWrite",
"48b480b5-d7d4-4d89-a415-ba49b989518d": "callevents.write",
"39d724e8-6a34-4930-9a36-364082c35716": "scep_challenge_provider",
"907d16c7-7591-49a4-b523-6fd42e5f2c7e": "pfx_cert_provider",
"7828b294-fdcc-4ed6-a45a-854364afb21d": "send_data_usage",
"a5438881-186a-48f0-bc41-a93ae8a195fe": "update_device_health",
"7ec88bad-30c7-4928-a005-4455362cfd98": "get_device_compliance",
"7b3c62c0-bbe4-4ceb-971b-ecc50a191b3e": "update_device_attributes",
"3d9dc976-32fb-45a8-90bd-c9f8a850d098": "get_data_warehouse",
"3857e233-c379-404e-85e9-bdbf3a62b28f": "manage_partner_compliance_policy",
"a0f3e90e-0c99-4c7d-bfaf-69531a09579c": "deploymenttask.read",
"64b22404-2ac7-4ca5-a15d-607e62d2694b": "deploymenttask.readwrite",
"1994c32e-87b9-46f9-a8b8-7daf25cd5a95": "CustomerManagement.ReadWrite.MMD",
"6dc96d9f-75cd-4c03-a450-6bf81a89ad9e": "CustomerManagement.ReadWrite.CPMC",
"50bf3dfa-9431-427d-823a-f146d9350034": "TBD",
"fd7bf697-168c-45be-b7ba-e94b3529deff": "user_impersonation",
"0d9ce864-39e5-424f-8556-b68ce5dac482": "Region.Read.All",
"3ed42bc3-d6ed-4cf4-9531-d521e361223e": "Region.ReadWrite.All",
"91d6f071-cbcb-48b9-baba-557f0f1f46bc": "User.Read.All",
"4f217d7c-5ea7-4dde-a269-9025b80f2cd5": "AdminAppCatalog.Read.All",
"661e6b85-3355-45f4-80eb-cdad62416918": "Read/Write",
"33622fe9-9998-44a0-acd3-e5b2ec2bca45": "ServiceHealth.Read",
"a1709332-8cf0-4afe-b4d8-2b7b4eb87a88": "ServiceHealth.Write",
"825c9d21-ba03-4e97-8007-83f020ff8c0f": "Deprecated_ActivityReports.Read",
"69784729-33e3-471d-b130-744ce05343e5": "Deprecated_ThreatIntelligence.Read",
"b3b78c39-cb1d-4d17-820a-25d9196a800e": "ActivityReports.Read",
"17f1c501-83cd-414c-9064-cd10f7aef836": "ThreatIntelligence.Read",
"4807a72c-ad38-4250-94c9-4eabfe26cd55": "ActivityFeed.ReadDlp",
"594c1fb6-4f81-4475-ae41-0c394909246c": "ActivityFeed.Read",
"e2cea78f-e743-4d8f-a16a-75b629a038ae": "ServiceHealth.Read",
"c107831b-9c28-4609-b219-a7b3fc5cc190": "CloudPC.PartnerReadWrite.All",
"5184a2ce-115e-4318-9526-df3e39c2e839": "EndUser.Access",
"a7a0e953-7ed2-423c-849f-9d78b5e44612": "CmCollectionData.write",
"1ce9e34f-35e8-4af8-b172-09e4dd00453d": "CmCollectionData.read",
"76e55082-bbde-4602-b506-bba9c6368668": "Account.ReadWrite.All",
"4b03fb80-ef9e-4391-86c9-152c41bf0693": "Device.ReadWrite.All",
"20bd8bbf-3063-4a8f-ae4f-f2f5e5bda666": "Notification.Read.All",
"0db7d603-2368-4c9a-8f47-adc9ac73e5e1": "Notification.ReadWrite.All",
"15fdfc00-27d5-4f79-8a38-8efe91e3c1cc": "Device.Read.All",
"c8750fbf-30e2-40ed-8519-e2876cbeccb9": "Account.Read.All",
"66a874a2-b739-43fa-8e1a-176cd8290cf5": "Collection.Read.All",
"d430b935-3087-4654-8d58-25faba0dabb5": "InventoryClass.Read.All",
"b026af69-9eae-4bb3-9351-304d4987e170": "Boundary.Read.All",
"98ed40ef-611a-4479-bd35-eaa7863e946a": "PeopleSettings.ReadWrite.All",
"789ef6b5-4ecc-4f61-b6b3-66ef3109173c": "PeopleSettings.Read.All",
"7146a1f0-8703-45b3-9eae-527a64c00995": "SMTP.SendAsApp",
"b4d5a5c7-c085-487f-b922-ef0d6ebde6b1": "ReportingWebService.Read.All",
"c976971c-a54d-4835-a240-2479e3dac74a": "Organization.ReadWrite.All",
"cb842b43-da6e-4506-86fe-bb12199c656d": "POP.AccessAsApp",
"5e5addcd-3e8d-4e90-baf5-964efab2b20a": "IMAP.AccessAsApp",
"15f260d6-f874-4366-8672-6b3658c5a09b": "Organization.Read.All",
"f7264778-fba9-422d-8e9e-2675a2c4b513": "Mailbox.Migration",
"bf24470f-10c1-436d-8d53-7b997eb473be": "User.Read.All",
"77e65b5a-ceae-48b3-9490-50a86a038a48": "User.ReadBasic.All",
"d45fa9f8-36e5-4cd2-b601-b063c7cf9ac2": "MailboxSettings.Read",
"dc890d15-9560-4a4c-9b7f-a736ec74ec40": "full_access_as_app",
"b633e1c5-b582-4048-a93e-9f11b44c7e96": "Mail.Send",
"798ee544-9d2d-430c-a058-570e29e34338": "Calendars.Read",
"089fe4d0-434a-44c5-8827-41ba8a0b17f5": "Contacts.Read",
"810c84a8-4a9e-49e6-bf7d-12d183f40d01": "Mail.Read",
"e2a3a72e-5f79-4c64-b1b1-878b674786c9": "Mail.ReadWrite",
"6918b873-d17a-4dc1-b314-35f528134491": "Contacts.ReadWrite",
"f9156939-25cd-4ba8-abfe-7fabcf003749": "MailboxSettings.ReadWrite",
"c1b0de0a-1de9-455d-919f-eca451053141": "Tasks.Read",
"2c6a42ca-0d4d-49ad-bc0e-21222c449a65": "Tasks.ReadWrite",
"ef54d2bf-783f-4e0f-bca1-3210c0444d99": "Calendars.ReadWrite.All",
"2dfdc6dc-2fa7-4a2c-a922-dbd4f85d17be": "Calendars.Read.All",
"4830e04b-48ac-4de5-bbd9-8aceb58e506b": "Place.Read.All",
"dc50a0fb-09a3-484d-be87-e023b12c6440": "Exchange.ManageAsApp",
"fc2a0408-0ddc-4173-80b9-15a933a5ff57": "OrgSettings-Planner.Read.All",
"68067c9d-a1be-4603-b095-3eaf54a42510": "OrgSettings-Planner.ReadWrite.All",
"fdc2d224-c588-43f8-b0c0-8abf2b7abda7": "Task.Publish.Update",
"0f6934a9-4e8f-4059-b2f4-a4a59d2c5407": "Task.Publish.Delete",
"e83a13aa-744d-44ee-9a42-d6f5137d9d0a": "Task.Publish.Create",
"8d48872e-7710-4001-bfd0-7dac15c28f69": "Purview.ApplicationAccess",
"ab725b17-4fd4-46ee-a0bf-102895a209e3": "BingCortana-Internal.ReadWrite",
"dfa45ec9-c9fd-4944-93c8-d07af06cfa40": "InformationProtectionPolicy.Read.All",
"59c665e3-d1e1-4490-be50-435812e9a9c5": "organizationsettings.readwrite",
"934e7a4e-6b72-4c56-966c-0ab878a30c89": "operations.readwrite",
"06ab0d31-7112-476e-a479-66394bec63d6": "MessageTrace.Read.All",
"3e4e080e-55db-4fa9-8d68-0d9199d4c792": "QuarantinedMessage.Read.All",
"cc02f7ae-3d9b-42c9-bc91-3424d92c5547": "AirAdminAction.tenant.read",
"43f2aa58-36d7-421e-8628-fbe9b129bf76": "AirAdminAction.tenant.write",
"27787a44-0423-4f0d-a417-1276c93397fb": "TenantLicenseStatus.Read.All",
"092afc53-fa1b-44c3-9fdf-46fcd25a5d99": "Relocation.ReadWrite.All",
"926c05c5-5941-491b-973a-509c2a4a2542": "AzureActivityData.Read.All",
"a585dd3a-70b6-4ff4-a1b9-093b4214e7e4": "OcrBillingConfiguration-Internal.Write.All",
"9760b448-d4d4-478b-bebc-0ebe62c935c9": "AuditProvisioningData.Tenant.Read",
"67a4e76f-5125-4b64-bcd6-b42a60d47dbe": "Purview.DataAccess.All",
"43e3dfa5-222e-4a48-8253-d36086c5558c": "Alert.Read.All",
"5f124282-d2c3-47dd-87ff-106ba9aa079b": "MtpMailboxRuleAction.tenant.write",
"ca69fdfa-5ba6-4c33-9eac-013653c2c3af": "MtpMailboxRuleAction.tenant.read",
"182f95e9-8c6f-4c32-8de2-e1abc1fe6ea4": "DataInsightsSubscription.tenant.write",
"bfeb98e9-5067-42b0-a7df-9022b927a10e": "DataInsightsSubscription.tenant.read",
"59c90462-e42e-4698-8a51-196ebd407166": "compliancestatus.tenant.read",
"39de55cd-e81d-4d2a-880d-3872c4fb992d": "RecipientBatch.tenant.write",
"0eabd45c-e771-460d-a601-2d534e78a1be": "DataInsightsUsersData.tenant.read",
"e0ff780c-d4f4-4ef4-b0ad-b19863ca72a2": "UsersAggregateByAttackSimulation.tenant.read",
"81eac90b-5b5b-422f-8d2a-9bc2055c5453": "Recipient.tenant.read",
"7b67f132-5c43-45cb-8cc3-e78fd80d0776": "Recipient.tenant.write",
"06c43929-37aa-4707-ae05-68d6d967953e": "AttackSimulationData.tenant.read",
"38b568f3-92e4-4c17-92b7-a49c28904247": "TiRemediation.ReadWrite.All",
"5c6799ba-41c0-49cc-9f2d-7486a52d52a0": "TiRemediation.Read.All",
"dac43cb8-9b13-43b1-bc17-e7eb8fe26717": "RemediationEmailResult.ReadWrite.All",
"cae0e51f-af85-4f35-870d-9f024147648d": "RemediationEmailResult.Read.All",
"ba4ca83c-e834-4e66-bfe1-df738f63b557": "activitydata.tenant.read",
"57fee0bb-e97d-4e5c-a663-2b0c7ce0db37": "InsiderRiskData.Read.All",
"f9d2daf6-8028-48d1-b4c1-b963f7ae7a73": "AggConsumptionBillingReport.Read.All",
"15188c9e-7879-4e83-9d63-c728da8feb0d": "DynamicRiskPreventionTag.Tenant.Write",
"f63db487-96bf-49af-8a79-faa86287aee6": "DynamicRiskPreventionTag.Tenant.Read",
"944c8d5a-fdcd-4aac-af4d-3366942700d5": "ThreatSubmission.ReadWrite.All",
"e0ba9b2a-a247-4d95-bca6-43211b61057f": "CustomTag.Tenant.Read",
"92b5621e-0e43-46c9-b830-bc26b325a150": "CustomTag.Tenant.Write",
"85e837d7-9e4b-4bb2-9535-08bb51aa974a": "MessageTraceDetail.tenant.read",
"03f3ead7-60e6-4522-847b-8a67bb9c50df": "OneCyberRelocationData.tenant.write",
"9b31c028-bb6a-4d1a-8295-4514d184c061": "OneCyberRelocationData.tenant.read",
"86e9643d-f798-40d2-98bb-293a7daaa2d7": "MtpAction.tenant.read",
"e6e79fef-f4ee-4f93-aec3-3f0001087066": "MtpAction.tenant.write",
"723c28f9-60b9-4cd4-8b04-6d344a3c4d84": "alert.tenant.write",
"d91202fb-0f5f-4245-8148-dfe12af913e6": "alert.tenant.read",
"74450f94-a5b1-4243-a991-9a688375883f": "mtpstatus.tenant.read",
"51aa070e-cc8b-45a9-8530-3fc96b0aa701": "messageeventsummary.tenant.read",
"24c052b7-e297-4369-b344-e4b62baa3fca": "reducedrecipient.read.all",
"abe60d99-0a67-4250-afc0-290614d84b41": "RoleGroupMember.tenant.write",
"6c68db0a-4608-48d3-b0bf-4d0917b88bef": "PolicyStatusSummary-Internal.Write.All",
"898f9f5d-bf7c-4bf5-97ed-39cda772c50a": "PushChannel.ReadWrite.All",
"226ed26c-f1f6-46f4-8892-54c1d9569817": "Transitions.ReadWrite",
"189125ec-ea35-4135-b00a-e51472464beb": "Meetings.ScheduleOnDemand",
"05a4e3e8-cfa6-4934-bb91-b6fc4ce6f340": "Conversations.AudioVideo",
"30a91c70-863f-4a08-b01c-6c1d78685414": "Conversations.PSTN",
"f7a521bb-ae17-42df-8096-97ebcc8b4edb": "Conversations.Chat",
"e821ef97-a9f6-4c9e-bb6a-29fa0d8f6101": "Meetings.JoinManage",
"b783bde8-ffc2-4f0c-96ce-6e2900b7aa4e": "Anonymous",
"20d37865-089c-4dee-8c41-6967602d4ac8": "Sites.Selected",
"df021288-bdef-4463-88db-98f22de89214": "User.Read.All",
"741f803b-c850-494e-b5df-cde7c675a1ca": "User.ReadWrite.All",
"c8e3537c-ec53-43b9-bed3-b2bd3617ae97": "TermStore.ReadWrite.All",
"2a8d57a5-4090-4a41-bf1c-3c621d2ccad3": "TermStore.Read.All",
"9bff6588-13f2-4c48-bbf2-ddab62256b36": "Sites.Manage.All",
"678536fe-1083-478a-9c59-b99265e6b0d3": "Sites.FullControl.All",
"d13f72ca-a275-4b96-b789-48ebcc4da984": "Sites.Read.All",
"fbcd29d2-fcca-4405-aded-518d457caae4": "Sites.ReadWrite.All",
"9a7146cc-f57d-4b51-83a1-4e2a1b31b749": "LicensedProduct.Read.All",
"a06291f3-06ca-4506-a783-d9c9d8af7e84": "AllotmentSource.Read.All",
"cbbf6a32-6dcd-4f22-9be7-ffb128119fae": "LicenseManager.Fulfillment",
"e9aa7b67-ea0d-435b-ab36-592cd9b23d61": "discovery.read",
"cb792285-1541-416c-a581-d8ede4ebc219": "settings.manage",
"8e41f311-31d5-43aa-bb79-8fd4e14a8745": "settings.read",
"f6e78c1a-b9c7-42d3-b067-220689a7a2e9": "discovery.manage",
"83bc8d83-2679-44ef-b813-d5f556fc4474": "investigation.read",
"a832eaa3-0cfc-4a2b-9af1-27c5b092dd40": "investigation.manage",
"7ed1102e-6cd7-4ad1-86d4-7d54c6550141": "ResourceAccessFlag.Write",
"edaa88f0-574c-4dd3-a8a3-8aaed557cfc7": "api.invoke",
"8b2071cd-015a-4025-8052-1c0dba2d3f64": "UnifiedPolicy.Tenant.Read",
"42f58b5b-a80d-4260-a1a5-c9a412f6e0d4": "Notification.Send.All",
"654b31ae-d941-4e22-8798-7add8fdf049f": "Tenant.Read.All",
"28379fa9-8596-4fd9-869e-cb60a93b5d84": "Tenant.ReadWrite.All",
"d07a8cc0-3d51-4b77-b3b0-32704d1f69fa": "AccessReview.Read.All",
"ef5f7d5c-338f-44b0-86c3-351f46c8bb5f": "AccessReview.ReadWrite.All",
"18228521-a591-40f1-b215-5fad4488c117": "AccessReview.ReadWrite.Membership",
"8c0aed2c-0c61-433d-b63c-6370ddc73248": "Acronym.Read.All",
"134fd756-38ce-4afd-ba33-e9623dbe66c2": "AdministrativeUnit.Read.All",
"5eb59dd3-1da2-4329-8733-9dabdc435916": "AdministrativeUnit.ReadWrite.All",
"2f3e6f8c-093b-4c57-a58b-ba5ce494a169": "Agreement.Read.All",
"c9090d00-6101-42f0-a729-c41074260d47": "Agreement.ReadWrite.All",
"d8e4ec18-f6c0-4620-8122-c8b1f2bf400e": "AgreementAcceptance.Read.All",
"b86848a7-d5b1-41eb-a9b4-54a4e6306e97": "APIConnectors.Read.All",
"1dfe531a-24a6-4f1b-80f4-7a0dc5a0a171": "APIConnectors.ReadWrite.All",
"e12dae10-5a57-4817-b79d-dfbec5348930": "AppCatalog.Read.All",
"dc149144-f292-421e-b185-5953f2e98d7f": "AppCatalog.ReadWrite.All",
"3be0012a-cc4e-426b-895b-f9c836bf6381": "Application-RemoteDesktopConfig.ReadWrite.All",
"9a5d68dd-52b0-4cc2-bd40-abcf44ac3a30": "Application.Read.All",
"1bfefb4e-e0b5-418b-a88f-73c46d2cc8e9": "Application.ReadWrite.All",
"18a4783c-866b-4cc7-a460-3d5e5662c884": "Application.ReadWrite.OwnedBy",
"06b708a9-e830-4db3-a914-8e69da51d44f": "AppRoleAssignment.ReadWrite.All",
"93283d0a-6322-4fa8-966b-8c121624760d": "AttackSimulation.Read.All",
"e125258e-8c8a-42a8-8f55-ab502afa52f3": "AttackSimulation.ReadWrite.All",
"b0afded3-3588-46d8-8b3d-9842eff778da": "AuditLog.Read.All",
"20e6f8e4-ffac-4cf7-82f7-70ddb7564318": "AuditLogsQuery-CRM.Read.All",
"0bc85aed-7b0b-437a-bac8-3b29a1b84c99": "AuditLogsQuery-Endpoint.Read.All",
"7276d950-48fc-4269-8348-f22f2bb296d0": "AuditLogsQuery-Entra.Read.All",
"6b0d2622-d34e-4470-935b-b96550e5ca8d": "AuditLogsQuery-Exchange.Read.All",
"8a169a81-841c-45fd-ad43-96aede8801a0": "AuditLogsQuery-OneDrive.Read.All",
"91c64a47-a524-4fce-9bf3-3d569a344ecf": "AuditLogsQuery-SharePoint.Read.All",
"5e1e9171-754d-478c-812c-f1755a9a4c2d": "AuditLogsQuery.Read.All",
"381f742f-e1f8-4309-b4ab-e3d91ae4c5c1": "AuthenticationContext.Read.All",
"a88eef72-fed0-4bf7-a2a9-f19df33f8b83": "AuthenticationContext.ReadWrite.All",
"9e8be751-7eee-4c09-bcfd-d64f6b087fd8": "BillingConfiguration.ReadWrite.All",
"6e98f277-b046-4193-a4f2-6bf6a78cd491": "Bookings.Read.All",
"9769393e-5a9f-4302-9e3d-7e018ecb64a7": "BookingsAppointment.ReadWrite.All",
"be95e614-8ef3-49eb-8464-1c9503433b86": "Bookmark.Read.All",
"c5ee1f21-fc7f-4937-9af0-c91648ff9597": "BrowserSiteLists.Read.All",
"8349ca94-3061-44d5-9bfb-33774ea5e4f9": "BrowserSiteLists.ReadWrite.All",
"acc0fc4d-2cd6-4194-8700-1768d8423d86": "BusinessScenarioConfig.Read.OwnedBy",
"bbea195a-4c47-4a4f-bff2-cba399e11698": "BusinessScenarioConfig.ReadWrite.OwnedBy",
"6c0257fd-cffe-415b-8239-2d0d70fdaa9c": "BusinessScenarioData.Read.OwnedBy",
"f2d21f22-5d80-499e-91cc-0a8a4ce16f54": "BusinessScenarioData.ReadWrite.OwnedBy",
"798ee544-9d2d-430c-a058-570e29e34338": "Calendars.Read",
"8ba4a692-bc31-4128-9094-475872af8a53": "Calendars.ReadBasic.All",
"ef54d2bf-783f-4e0f-bca1-3210c0444d99": "Calendars.ReadWrite",
"1abb026f-7572-49f6-9ddd-ad61cbba181e": "CallEvents.Read.All",
"a2611786-80b3-417e-adaa-707d4261a5f0": "CallRecord-PstnCalls.Read.All",
"45bbb07e-7321-4fd7-a8f6-3ff27e6a81c8": "CallRecords.Read.All",
"a7a681dc-756e-4909-b988-f160edc6655f": "Calls.AccessMedia.All",
"284383ee-7f6e-4e40-a2a8-e85dcb029101": "Calls.Initiate.All",
"4c277553-8a09-487b-8023-29ee378d8324": "Calls.InitiateGroupCall.All",
"f6b49018-60ab-4f81-83bd-22caeabfed2d": "Calls.JoinGroupCall.All",
"fd7ccf6b-3d28-418b-9701-cd10f5cd2fd4": "Calls.JoinGroupCallAsGuest.All",
"f3a65bd4-b703-46df-8f7e-0174fea562aa": "Channel.Create",
"6a118a39-1227-45d4-af0c-ea7b40d210bc": "Channel.Delete.All",
"59a6b24b-4225-4393-8165-ebaec5f55d7a": "Channel.ReadBasic.All",
"3b55498e-47ec-484f-8136-9013221c06a9": "ChannelMember.Read.All",
"35930dcf-aceb-4bd1-b99a-8ffed403c974": "ChannelMember.ReadWrite.All",
"7b2449af-6ccd-4f4d-9f78-e550c193f0d1": "ChannelMessage.Read.All",
"4d02b0cc-d90b-441f-8d82-4fb55c34d6bb": "ChannelMessage.UpdatePolicyViolation.All",
"c97b873f-f59f-49aa-8a0e-52b32d762124": "ChannelSettings.Read.All",
"243cded2-bd16-4fd6-a953-ff8177894c3d": "ChannelSettings.ReadWrite.All",
"d9c48af6-9ad9-47ad-82c3-63757137b9af": "Chat.Create",
"9c7abde0-eacd-4319-bf9e-35994b1a1717": "Chat.ManageDeletion.All",
"6b7d71aa-70aa-4810-a8d9-5d9fb2830017": "Chat.Read.All",
"1c1b4c8e-3cc7-4c58-8470-9b92c9d5848b": "Chat.Read.WhereInstalled",
"b2e060da-3baf-4687-9611-f4ebc0f0cbde": "Chat.ReadBasic.All",
"818ba5bd-5b3e-4fe0-bbe6-aa4686669073": "Chat.ReadBasic.WhereInstalled",
"294ce7c9-31ba-490a-ad7d-97a7d075e4ed": "Chat.ReadWrite.All",
"ad73ce80-f3cd-40ce-b325-df12c33df713": "Chat.ReadWrite.WhereInstalled",
"7e847308-e030-4183-9899-5235d7270f58": "Chat.UpdatePolicyViolation.All",
"a3410be2-8e48-4f32-8454-c29a7465209d": "ChatMember.Read.All",
"93e7c9e4-54c5-4a41-b796-f2a5adaacda7": "ChatMember.Read.WhereInstalled",
"57257249-34ce-4810-a8a2-a03adf0c5693": "ChatMember.ReadWrite.All",
"e32c2cd9-0124-4e44-88fc-772cd98afbdb": "ChatMember.ReadWrite.WhereInstalled",
"b9bb2381-47a4-46cd-aafb-00cb12f68504": "ChatMessage.Read.All",
"64a59178-dad3-4673-89db-84fdcd622fec": "CloudApp-Discovery.Read.All",
"a9e09520-8ed4-4cde-838e-4fdea192c227": "CloudPC.Read.All",
"3b4349e1-8cf5-45a3-95b7-69d1751d3e6a": "CloudPC.ReadWrite.All",
"407f0cce-3212-441f-9f55-3bc91342cf86": "Community.Read.All",
"35d59e32-eab5-4553-9345-abb62b4c703c": "Community.ReadWrite.All",
"1260ad83-98fb-4785-abbb-d6cc1806fd41": "ConsentRequest.Read.All",
"9f1b81a7-0223-4428-bfa4-0bcb5535f27d": "ConsentRequest.ReadWrite.All",
"089fe4d0-434a-44c5-8827-41ba8a0b17f5": "Contacts.Read",
"6918b873-d17a-4dc1-b314-35f528134491": "Contacts.ReadWrite",
"cac88765-0581-4025-9725-5ebc13f729ee": "CrossTenantInformation.ReadBasic.All",
"8b919d44-6192-4f3d-8a3b-f86f8069ae3c": "CrossTenantUserProfileSharing.Read.All",
"306785c5-c09b-4ba0-a4ee-023f3da165cb": "CrossTenantUserProfileSharing.ReadWrite.All",
"88bb2658-5d9e-454f-aacd-a3933e079526": "CustomAuthenticationExtension.Read.All",
"c2667967-7050-4e7e-b059-4cbbb3811d03": "CustomAuthenticationExtension.ReadWrite.All",
"214e810f-fda8-4fd7-a475-29461495eb00": "CustomAuthenticationExtension.Receive.Payload",
"673a007a-9e0f-4c97-b066-3c0164486909": "CustomDetection.Read.All",
"e0fd9c8d-a12e-4cc9-9827-20c8c3cd6fb8": "CustomDetection.ReadWrite.All",
"3b37c5a4-1226-493d-bec3-5d6c6b866f3f": "CustomSecAttributeAssignment.Read.All",
"de89b5e4-5b8f-48eb-8925-29c2b33bd8bd": "CustomSecAttributeAssignment.ReadWrite.All",
"2a4f026d-e829-4e84-bdbf-d981a2703059": "CustomSecAttributeAuditLogs.Read.All",
"b185aa14-d8d2-42c1-a685-0f5596613624": "CustomSecAttributeDefinition.Read.All",
"12338004-21f4-4896-bf5e-b75dfaf1016d": "CustomSecAttributeDefinition.ReadWrite.All",
"ab8a5872-7c88-47a6-8141-7becce939190": "CustomTags.Read.All",
"2f503208-e509-4e39-974c-8cc16e5785c9": "CustomTags.ReadWrite.All",
"f6e9e124-4586-492f-adc0-c6f96e4823fd": "DelegatedAdminRelationship.Read.All",
"cc13eba4-8cd8-44c6-b4d4-f93237adce58": "DelegatedAdminRelationship.ReadWrite.All",
"81b4724a-58aa-41c1-8a55-84ef97466587": "DelegatedPermissionGrant.Read.All",
"8e8e4742-1d95-4f68-9d56-6ee75648c72a": "DelegatedPermissionGrant.ReadWrite.All",
"7438b122-aefc-4978-80ed-43db9fcc7715": "Device.Read.All",
"1138cb37-bd11-4084-a2b7-9f71582aeddb": "Device.ReadWrite.All",
"884b599e-4d48-43a5-ba94-15c414d00588": "DeviceLocalCredential.Read.All",
"db51be59-e728-414b-b800-e0f010df1a79": "DeviceLocalCredential.ReadBasic.All",
"7a6ee1e7-141e-4cec-ae74-d9db155731ff": "DeviceManagementApps.Read.All",
"78145de6-330d-4800-a6ce-494ff2d33d07": "DeviceManagementApps.ReadWrite.All",
"dc377aa6-52d8-4e23-b271-2a7ae04cedf3": "DeviceManagementConfiguration.Read.All",
"9241abd9-d0e6-425a-bd4f-47ba86e767a4": "DeviceManagementConfiguration.ReadWrite.All",
"5b07b0dd-2377-4e44-a38d-703f09a0dc3c": "DeviceManagementManagedDevices.PrivilegedOperations.All",
"2f51be20-0bb4-4fed-bf7b-db946066c75e": "DeviceManagementManagedDevices.Read.All",
"243333ab-4d21-40cb-a475-36241daa0842": "DeviceManagementManagedDevices.ReadWrite.All",
"58ca0d9a-1575-47e1-a3cb-007ef2e4583b": "DeviceManagementRBAC.Read.All",
"e330c4f0-4170-414e-a55a-2f022ec2b57b": "DeviceManagementRBAC.ReadWrite.All",
"06a5fe6d-c49d-46a7-b082-56b1b14103c7": "DeviceManagementServiceConfig.Read.All",
"5ac13192-7ace-4fcf-b828-1a26f28068ee": "DeviceManagementServiceConfig.ReadWrite.All",
"7ab1d382-f21e-4acd-a863-ba3e13f7da61": "Directory.Read.All",
"19dbc75e-c2e2-444c-a770-ec69d8559fc7": "Directory.ReadWrite.All",
"f20584af-9290-4153-9280-ff8bb2c0ea7f": "Directory.Write.Restricted",
"ae73097b-cb2a-4447-b064-5d80f6093921": "DirectoryRecommendations.Read.All",
"0e9eea12-4f01-45f6-9b8d-3ea4c8144158": "DirectoryRecommendations.ReadWrite.All",
"dbb9058a-0e50-45d7-ae91-66909b5d4664": "Domain.Read.All",
"7e05723c-0bb0-42da-be95-ae9f08a6e53c": "Domain.ReadWrite.All",
"50180013-6191-4d1e-a373-e590ff4e66af": "eDiscovery.Read.All",
"b2620db1-3bf7-4c5b-9cb9-576d29eac736": "eDiscovery.ReadWrite.All",
"7c9db06a-ec2d-4e7b-a592-5a1e30992566": "EduAdministration.Read.All",
"9bc431c3-b8bc-4a8d-a219-40f10f92eff6": "EduAdministration.ReadWrite.All",
"4c37e1b6-35a1-43bf-926a-6f30f2cdf585": "EduAssignments.Read.All",
"6e0a958b-b7fc-4348-b7c4-a6ab9fd3dd0e": "EduAssignments.ReadBasic.All",
"0d22204b-6cad-4dd0-8362-3e3f2ae699d9": "EduAssignments.ReadWrite.All",
"f431cc63-a2de-48c4-8054-a34bc093af84": "EduAssignments.ReadWriteBasic.All",
"6cdb464c-3a03-40f8-900b-4cb7ea1da9c0": "EduCurricula.Read.All",
"6a0c2318-d59d-4c7d-bf2e-5f3902dc2593": "EduCurricula.ReadWrite.All",
"ad248c30-1919-40c8-b3d2-304481894e88": "EduReports-Reading.Read.All",
"040330d7-be7e-4130-b349-a6eb3a56e2f8": "EduReports-Reading.ReadAnonymous.All",
"c5debf73-bdc8-473d-bf07-f4074ad05f71": "EduReports-Reflect.Read.All",
"f5d05dba-7ef0-46fc-b62c-a7282555f428": "EduReports-Reflect.ReadAnonymous.All",
"e0ac9e1b-cb65-4fc5-87c5-1a8bc181f648": "EduRoster.Read.All",
"0d412a8c-a06c-439f-b3ec-8abcf54d2f96": "EduRoster.ReadBasic.All",
"d1808e82-ce13-47af-ae0d-f9b254e6d58a": "EduRoster.ReadWrite.All",
"c74fd47d-ed3c-45c3-9a9e-b8676de685d2": "EntitlementManagement.Read.All",
"9acd699f-1e81-4958-b001-93b1d2506e19": "EntitlementManagement.ReadWrite.All",
"b7f6385c-6ce6-4639-a480-e23c42ed9784": "EventListener.Read.All",
"0edf5e9e-4ce8-468a-8432-d08631d18c43": "EventListener.ReadWrite.All",
"1914711b-a1cb-4793-b019-c2ce0ed21b8c": "ExternalConnection.Read.All",
"34c37bc0-2b40-4d5e-85e1-2365cd256d79": "ExternalConnection.ReadWrite.All",
"f431331c-49a6-499f-be1c-62af19c34a9d": "ExternalConnection.ReadWrite.OwnedBy",
"7a7cffad-37d2-4f48-afa4-c6ab129adcc2": "ExternalItem.Read.All",
"38c3d6ee-69ee-422f-b954-e17819665354": "ExternalItem.ReadWrite.All",
"8116ae0f-55c2-452d-9944-d18420f5b2c8": "ExternalItem.ReadWrite.OwnedBy",
"1987d7a0-d602-4262-ab90-cfdd43b37545": "ExternalUserProfile.Read.All",
"761327c9-d819-4c08-9a5f-874cd2826608": "ExternalUserProfile.ReadWrite.All",
"01d4889c-1287-42c6-ac1f-5d1e02578ef6": "Files.Read.All",
"75359482-378d-4052-8f01-80520e7db3cd": "Files.ReadWrite.All",
"b47b160b-1054-4efd-9ca0-e2f614696086": "Files.ReadWrite.AppFolder",
"40dc41bc-0f7e-42ff-89bd-d9516947e474": "FileStorageContainer.Selected",
"bf7b1a76-6e77-406b-b258-bf5c7720e98f": "Group.Create",
"5b567255-7703-4780-807c-7be8301ae99b": "Group.Read.All",
"62a82d76-70ea-41e2-9197-370581804d09": "Group.ReadWrite.All",
"98830695-27a2-44f7-8c18-0c3ebc9698f6": "GroupMember.Read.All",
"dbaae8cf-10b5-4b86-a4a1-f871c94c6695": "GroupMember.ReadWrite.All",
"e321f0bb-e7f7-481e-bb28-e3b0b32d4bd0": "IdentityProvider.Read.All",
"90db2b9a-d928-4d33-a4dd-8442ae3d41e4": "IdentityProvider.ReadWrite.All",
"6e472fd1-ad78-48da-a0f0-97ab2c6b769e": "IdentityRiskEvent.Read.All",
"db06fb33-1953-4b7b-a2ac-f1e2c854f7ae": "IdentityRiskEvent.ReadWrite.All",
"607c7344-0eed-41e5-823a-9695ebe1b7b0": "IdentityRiskyServicePrincipal.Read.All",
"cb8d6980-6bcb-4507-afec-ed6de3a2d798": "IdentityRiskyServicePrincipal.ReadWrite.All",
"dc5007c0-2d7d-4c42-879c-2dab87571379": "IdentityRiskyUser.Read.All",
"656f6061-f9fe-4807-9708-6a2e0934df76": "IdentityRiskyUser.ReadWrite.All",
"1b0c317f-dd31-4305-9932-259a8b6e8099": "IdentityUserFlow.Read.All",
"65319a09-a2be-469d-8782-f6b07debf789": "IdentityUserFlow.ReadWrite.All",
"7ab52c2f-a2ee-4d98-9ebc-725e3934aae2": "IndustryData-DataConnector.Read.All",
"eda0971c-482e-4345-b28f-69c309cb8a34": "IndustryData-DataConnector.ReadWrite.All",
"9334c44b-a7c6-4350-8036-6bf8e02b4c1f": "IndustryData-DataConnector.Upload",
"305f6ba2-049a-4b1b-88bb-fe7e08758a00": "IndustryData-InboundFlow.Read.All",
"e688c61f-d4c6-4d64-a197-3bcf6ba1d6ad": "IndustryData-InboundFlow.ReadWrite.All",
"61d0354c-5d88-483c-b974-a37ec3395a2c": "IndustryData-OutboundFlow.Read.All",
"24a65b4a-e501-47e2-8849-d679517887f0": "IndustryData-OutboundFlow.ReadWrite.All",
"6ee891c3-74a4-4148-8463-0c834375dfaf": "IndustryData-ReferenceDefinition.Read.All",
"f6f5d10b-3024-4d1d-b674-aae4df4a1a73": "IndustryData-Run.Read.All",
"bc167a60-39fe-4865-8b44-78400fc6ed03": "IndustryData-SourceSystem.Read.All",
"7d866958-e06e-4dd6-91c6-a086b3f5cfeb": "IndustryData-SourceSystem.ReadWrite.All",
"7c55c952-b095-4c23-a522-022bce4cc1e3": "IndustryData-TimePeriod.Read.All",
"7afa7744-a782-4a32-b8c2-e3db637e8de7": "IndustryData-TimePeriod.ReadWrite.All",
"4f5ac95f-62fd-472c-b60f-125d24ca0bc5": "IndustryData.ReadBasic.All",
"14f49b9f-4bf2-4d24-b80e-b27ec58409bd": "InformationProtectionConfig.Read.All",
"cbe6c7e4-09aa-4b8d-b3c3-2dbb59af4b54": "InformationProtectionContent.Sign.All",
"287bd98c-e865-4e8c-bade-1a85523195b9": "InformationProtectionContent.Write.All",
"19da66cb-0fb0-4390-b071-ebc76a349482": "InformationProtectionPolicy.Read.All",
"34cbd96c-d824-4755-90d3-1008ef47efc1": "Insights-UserMetric.Read.All",
"535e6066-2894-49ef-ab33-e2c6d064bb81": "LearningAssignedCourse.Read.All",
"236c1cbd-1187-427f-b0f5-b1852454973b": "LearningAssignedCourse.ReadWrite.All",
"8740813e-d8aa-4204-860e-2a0f8f84dbc8": "LearningContent.Read.All",
"444d6fcb-b738-41e5-b103-ac4f2a2628a3": "LearningContent.ReadWrite.All",
"467524fc-ed22-4356-a910-af61191e3503": "LearningSelfInitiatedCourse.Read.All",
"7654ed61-8965-4025-846a-0856ec02b5b0": "LearningSelfInitiatedCourse.ReadWrite.All",
"5facf0c1-8979-4e95-abcf-ff3d079771c0": "LicenseAssignment.ReadWrite.All",
"7c67316a-232a-4b84-be22-cea2c0906404": "LifecycleWorkflows.Read.All",
"5c505cf4-8424-4b8e-aa14-ee06e3bb23e3": "LifecycleWorkflows.ReadWrite.All",
"810c84a8-4a9e-49e6-bf7d-12d183f40d01": "Mail.Read",
"6be147d2-ea4f-4b5a-a3fa-3eab6f3c140a": "Mail.ReadBasic",
"693c5e45-0940-467d-9b8a-1022fb9d42ef": "Mail.ReadBasic.All",
"e2a3a72e-5f79-4c64-b1b1-878b674786c9": "Mail.ReadWrite",
"b633e1c5-b582-4048-a93e-9f11b44c7e96": "Mail.Send",
"40f97065-369a-49f4-947c-6a255697ae91": "MailboxSettings.Read",
"6931bccd-447a-43d1-b442-00a195474933": "MailboxSettings.ReadWrite",
"658aa5d8-239f-45c4-aa12-864f4fc7e490": "Member.Read.Hidden",
"4f994bc0-31bb-44bb-b480-7a7c1be8c02e": "MultiTenantOrganization.Read.All",
"f9c2b2a7-3895-4b2e-80f6-c924b456e50b": "MultiTenantOrganization.ReadBasic.All",
"920def01-ca61-4d2d-b3df-105b46046a70": "MultiTenantOrganization.ReadWrite.All",
"40049381-3cc1-42af-94ec-5ce755db4b0d": "NetworkAccess-Reports.Read.All",
"e30060de-caa5-4331-99d3-6ac6c966a9a4": "NetworkAccess.Read.All",
"b10642fc-a6cf-4c46-87f9-e1f96c2a18aa": "NetworkAccess.ReadWrite.All",
"39ae4a24-1ef0-49e8-9d63-2a66f5c39edd": "NetworkAccessBranch.Read.All",
"8137102d-ec16-4191-aaf8-7aeda8026183": "NetworkAccessBranch.ReadWrite.All",
"8a3d36bf-cb46-4bcc-bec9-8d92829dab84": "NetworkAccessPolicy.Read.All",
"f0c341be-8348-4989-8e43-660324294538": "NetworkAccessPolicy.ReadWrite.All",
"3aeca27b-ee3a-4c2b-8ded-80376e2134a4": "Notes.Read.All",
"0c458cef-11f3-48c2-a568-c66751c238c0": "Notes.ReadWrite.All",
"df01ed3b-eb61-4eca-9965-6b3d789751b2": "OnlineMeetingArtifact.Read.All",
"a4a08342-c95d-476b-b943-97e100569c8d": "OnlineMeetingRecording.Read.All",
"c1684f21-1984-47fa-9d61-2dc8c296bb70": "OnlineMeetings.Read.All",
"b8bb2037-6e08-44ac-a4ea-4674e010e2a4": "OnlineMeetings.ReadWrite.All",
"a4a80d8d-d283-4bd8-8504-555ec3870630": "OnlineMeetingTranscript.Read.All",
"bb70e231-92dc-4729-aff5-697b3f04be95": "OnPremDirectorySynchronization.Read.All",
"c22a92cc-79bf-4bb1-8b6c-e0a05d3d80ce": "OnPremDirectorySynchronization.ReadWrite.All",
"0b57845e-aa49-4e6f-8109-ce654fffa618": "OnPremisesPublishingProfiles.ReadWrite.All",
"498476ce-e0fe-48b0-b801-37ba7e2685c6": "Organization.Read.All",
"292d869f-3427-49a8-9dab-8c70152b74e9": "Organization.ReadWrite.All",
"eb76ac34-0d62-4454-b97c-185e4250dc20": "OrganizationalBranding.Read.All",
"d2ebfbc1-a5f8-424b-83a6-56ab5927a73c": "OrganizationalBranding.ReadWrite.All",
"e1a88a34-94c4-4418-be12-c87b00e26bea": "OrgContact.Read.All",
"56c84fa9-ea1f-4a15-90f2-90ef41ece2c9": "OrgSettings-AppsAndServices.Read.All",
"4a8e4191-c1c8-45f8-b801-f9a1a5ee6ad3": "OrgSettings-AppsAndServices.ReadWrite.All",
"c18ae2dc-d9f3-4495-a93f-18980a0e159f": "OrgSettings-DynamicsVoice.Read.All",
"c3f1cc32-8bbd-4ab6-bd33-f270e0d9e041": "OrgSettings-DynamicsVoice.ReadWrite.All",
"434d7c66-07c6-4b1f-ab21-417cf2cdaaca": "OrgSettings-Forms.Read.All",
"2cb92fee-97a3-4034-8702-24a6f5d0d1e9": "OrgSettings-Forms.ReadWrite.All",
"6cdf1fb1-b46f-424f-9493-07247caa22e2": "OrgSettings-Microsoft365Install.Read.All",
"83f7232f-763c-47b2-a097-e35d2cbe1da5": "OrgSettings-Microsoft365Install.ReadWrite.All",
"e4d9cd09-d858-4363-9410-abb96737f0cf": "OrgSettings-Todo.Read.All",
"5febc9da-e0d0-4576-bd13-ae70b2179a39": "OrgSettings-Todo.ReadWrite.All",
"7c3e1994-38ff-4412-a99b-9369f6bb7706": "PartnerBilling.Read.All",
"bdfb26d9-bb36-49be-9b4c-b8cbf4b05808": "PendingExternalUserProfile.Read.All",
"8363c2b8-6ff7-420b-9966-c5884c2d48bc": "PendingExternalUserProfile.ReadWrite.All",
"b528084d-ad10-4598-8b93-929746b4d7d6": "People.Read.All",
"ef02f2e7-e22d-4c77-8614-8f765683b86e": "PeopleSettings.Read.All",
"b6890674-9dd5-4e42-bb15-5af07f541ae1": "PeopleSettings.ReadWrite.All",
"913b9306-0ce1-42b8-9137-6a7df690a760": "Place.Read.All",
"8b724a84-ceac-4fd9-897e-e31ba8f2d7a3": "PlaceDevice.Read.All",
"2d510721-5c4e-43cd-bfdb-ac0f8819fb92": "PlaceDevice.ReadWrite.All",
"27fc435f-44e2-4b30-bf3c-e0ce74aed618": "PlaceDeviceTelemetry.ReadWrite.All",
"246dd0d5-5bd0-4def-940b-0421030a5b68": "Policy.Read.All",
"37730810-e9ba-4e46-b07e-8ca78d182097": "Policy.Read.ConditionalAccess",
"b21b72f6-4e6a-4533-9112-47eea9f97b28": "Policy.Read.IdentityProtection",
"9e640839-a198-48fb-8b9a-013fd6f6cbcd": "Policy.Read.PermissionGrant",
"77c863fd-06c0-47ce-a7eb-49773e89d319": "Policy.ReadWrite.AccessReview",
"be74164b-cff1-491c-8741-e671cb536e13": "Policy.ReadWrite.ApplicationConfiguration",
"25f85f3c-f66c-4205-8cd5-de92dd7f0cec": "Policy.ReadWrite.AuthenticationFlows",
"29c18626-4985-4dcd-85c0-193eef327366": "Policy.ReadWrite.AuthenticationMethod",
"fb221be6-99f2-473f-bd32-01c6a0e9ca3b": "Policy.ReadWrite.Authorization",
"01c0a623-fc9b-48e9-b794-0756f8e8f067": "Policy.ReadWrite.ConditionalAccess",
"999f8c63-0a38-4f1b-91fd-ed1947bdd1a9": "Policy.ReadWrite.ConsentRequest",
"338163d7-f101-4c92-94ba-ca46fe52447c": "Policy.ReadWrite.CrossTenantAccess",
"03cc4f92-788e-4ede-b93f-199424d144a5": "Policy.ReadWrite.ExternalIdentities",
"2044e4f1-e56c-435b-925c-44cd8f6ba89a": "Policy.ReadWrite.FeatureRollout",
"90bbca0b-227c-4cdc-8083-1c6cfb95bac6": "Policy.ReadWrite.FedTokenValidation",
"2dcf8603-09eb-4078-b1ec-d30a1a76b873": "Policy.ReadWrite.IdentityProtection",
"a402ca1c-2696-4531-972d-6e5ee4aa11ea": "Policy.ReadWrite.PermissionGrant",
"1c6e93a6-28e2-4cbb-9f64-1a46a821124d": "Policy.ReadWrite.SecurityDefaults",
"79a677f7-b79d-40d0-a36a-3e6f8688dd7a": "Policy.ReadWrite.TrustFramework",
"a70e0c2d-e793-494c-94c4-118fa0a67f42": "Presence.Read.All",
"83cded22-8297-4ff6-a7fa-e97e9545a259": "Presence.ReadWrite.All",
"9709bb33-4549-49d4-8ed9-a8f65e45bb0f": "Printer.Read.All",
"f5b3f73d-6247-44df-a74c-866173fddab0": "Printer.ReadWrite.All",
"58a52f47-9e36-4b17-9ebe-ce4ef7f3e6c8": "PrintJob.Manage.All",
"ac6f956c-edea-44e4-bd06-64b1b4b9aec9": "PrintJob.Read.All",
"fbf67eee-e074-4ef7-b965-ab5ce1c1f689": "PrintJob.ReadBasic.All",
"5114b07b-2898-4de7-a541-53b0004e2e13": "PrintJob.ReadWrite.All",
"57878358-37f4-4d3a-8c20-4816e0d457b1": "PrintJob.ReadWriteBasic.All",
"b5991872-94cf-4652-9765-29535087c6d8": "PrintSettings.Read.All",
"456b71a7-0ee0-4588-9842-c123fcc8f664": "PrintTaskDefinition.ReadWrite.All",
"4cdc2547-9148-4295-8d11-be0db1391d6b": "PrivilegedAccess.Read.AzureAD",
"01e37dc9-c035-40bd-b438-b2879c4870a6": "PrivilegedAccess.Read.AzureADGroup",
"5df6fe86-1be0-44eb-b916-7bd443a71236": "PrivilegedAccess.Read.AzureResources",
"854d9ab1-6657-4ec8-be45-823027bcd009": "PrivilegedAccess.ReadWrite.AzureAD",
"2f6817f8-7b12-4f0f-bc18-eeaf60705a9e": "PrivilegedAccess.ReadWrite.AzureADGroup",
"6f9d5abc-2db6-400b-a267-7de22a40fb87": "PrivilegedAccess.ReadWrite.AzureResources",
"cd4161cb-f098-48f8-a884-1eda9a42434c": "PrivilegedAssignmentSchedule.Read.AzureADGroup",
"41202f2c-f7ab-45be-b001-85c9728b9d69": "PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup",
"edb419d6-7edc-42a3-9345-509bfdf5d87c": "PrivilegedEligibilitySchedule.Read.AzureADGroup",
"618b6020-bca8-4de6-99f6-ef445fa4d857": "PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup",
"eedb7fdd-7539-4345-a38b-4839e4a84cbd": "ProgramControl.Read.All",
"60a901ed-09f7-4aa5-a16e-7dd3d6f9de36": "ProgramControl.ReadWrite.All",
"214fda0c-514a-4650-b037-b562b1a66124": "PublicKeyInfrastructure.Read.All",
"a2b63618-5350-462d-b1b3-ba6eb3684e26": "PublicKeyInfrastructure.ReadWrite.All",
"ee49e170-1dd1-4030-b44c-61ad6e98f743": "QnA.Read.All",
"ac3a2b8e-03a3-4da9-9ce0-cbe28bf1accd": "RecordsManagement.Read.All",
"eb158f57-df43-4751-8b21-b8932adb3d34": "RecordsManagement.ReadWrite.All",
"230c1aed-a721-4c5d-9cb4-a90514e508ef": "Reports.Read.All",
"ee353f83-55ef-4b78-82da-555bfa2b4b95": "ReportSettings.Read.All",
"2a60023f-3219-47ad-baa4-40e17cd02a1d": "ReportSettings.ReadWrite.All",
"acfca4d5-f49f-40ed-9648-84068b474c73": "ResourceSpecificPermissionGrant.ReadForUser.All",
"d5fe8ce8-684c-4c83-a52c-46e882ce4be1": "RoleAssignmentSchedule.Read.Directory",
"dd199f4a-f148-40a4-a2ec-f0069cc799ec": "RoleAssignmentSchedule.ReadWrite.Directory",
"ff278e11-4a33-4d0c-83d2-d01dc58929a5": "RoleEligibilitySchedule.Read.Directory",
"fee28b28-e1f3-4841-818e-2704dc62245f": "RoleEligibilitySchedule.ReadWrite.Directory",
"c7fbd983-d9aa-4fa7-84b8-17382c103bc4": "RoleManagement.Read.All",
"031a549a-bb80-49b6-8032-2068448c6a3c": "RoleManagement.Read.CloudPC",
"483bed4a-2ad3-4361-a73b-c83ccdbdc53c": "RoleManagement.Read.Directory",
"c769435f-f061-4d0b-8ff1-3d39870e5f85": "RoleManagement.Read.Exchange",
"274d0592-d1b6-44bd-af1d-26d259bcb43a": "RoleManagement.ReadWrite.CloudPC",
"9e3f62cf-ca93-4989-b6ce-bf83c28f9fe8": "RoleManagement.ReadWrite.Directory",
"025d3225-3f02-4882-b4c0-cd5b541a4e80": "RoleManagement.ReadWrite.Exchange",
"ef31918f-2d50-4755-8943-b8638c0a077e": "RoleManagementAlert.Read.Directory",
"11059518-d6a6-4851-98ed-509268489c4a": "RoleManagementAlert.ReadWrite.Directory",
"69e67828-780e-47fd-b28c-7b27d14864e6": "RoleManagementPolicy.Read.AzureADGroup",
"fdc4c997-9942-4479-bfcb-75a36d1138df": "RoleManagementPolicy.Read.Directory",
"b38dcc4d-a239-4ed6-aa84-6c65b284f97c": "RoleManagementPolicy.ReadWrite.AzureADGroup",
"31e08e0a-d3f7-4ca2-ac39-7343fb83e8ad": "RoleManagementPolicy.ReadWrite.Directory",
"0b21c159-dbf4-4dbb-a6f6-490e412c716e": "Schedule-WorkingTime.ReadWrite.All",
"7b2ebf90-d836-437f-b90d-7b62722c4456": "Schedule.Read.All",
"b7760610-0545-4e8a-9ec3-cce9e63db01c": "Schedule.ReadWrite.All",
"7239b71d-b402-4150-b13d-78ecfe8df441": "SchedulePermissions.ReadWrite.All",
"ada977a5-b8b1-493b-9a91-66c206d76ecf": "SearchConfiguration.Read.All",
"0e778b85-fefa-466d-9eec-750569d92122": "SearchConfiguration.ReadWrite.All",
"5e0edab9-c148-49d0-b423-ac253e121825": "SecurityActions.Read.All",
"f2bf083f-0179-402a-bedb-b2784de8a49b": "SecurityActions.ReadWrite.All",
"472e4a4d-bb4a-4026-98d1-0b0d74cb74a5": "SecurityAlert.Read.All",
"ed4fca05-be46-441f-9803-1873825f8fdb": "SecurityAlert.ReadWrite.All",
"b48f7ac2-044d-4281-b02f-75db744d6f5f": "SecurityAnalyzedMessage.Read.All",
"04c55753-2244-4c25-87fc-704ab82a4f69": "SecurityAnalyzedMessage.ReadWrite.All",
"bf394140-e372-4bf9-a898-299cfc7564e5": "SecurityEvents.Read.All",
"d903a879-88e0-4c09-b0c9-82f6a1333f84": "SecurityEvents.ReadWrite.All",
"f8dcd971-5d83-4e1e-aa95-ef44611ad351": "SecurityIdentitiesHealth.Read.All",
"ab03ddd5-7ae4-4f2e-8af8-86654f7e0a27": "SecurityIdentitiesHealth.ReadWrite.All",
"45cc0394-e837-488b-a098-1918f48d186c": "SecurityIncident.Read.All",
"34bf0e97-1971-4929-b999-9e2442d941d7": "SecurityIncident.ReadWrite.All",
"2b655018-450a-4845-81e7-d603b1ebffdb": "ServiceActivity-Exchange.Read.All",
"c766cb16-acc4-4663-ba09-6eedef5876c5": "ServiceActivity-Microsoft365Web.Read.All",
"57b4f899-b8c5-47c7-bdd3-c410c55602b7": "ServiceActivity-OneDrive.Read.All",
"4dfee10b-fa4a-41b5-b34d-ccf54cc0c394": "ServiceActivity-Teams.Read.All",
"79c261e0-fe76-4144-aad5-bdc68fbe4037": "ServiceHealth.Read.All",
"1b620472-6534-4fe6-9df2-4680e8aa28ec": "ServiceMessage.Read.All",
"5256681e-b7f6-40c0-8447-2d9db68797a0": "ServicePrincipalEndpoint.Read.All",
"89c8469c-83ad-45f7-8ff2-6e3d4285709e": "ServicePrincipalEndpoint.ReadWrite.All",
"83d4163d-a2d8-4d3b-9695-4ae3ca98f888": "SharePointTenantSettings.Read.All",
"19b94e34-907c-4f43-bde9-38b1909ed408": "SharePointTenantSettings.ReadWrite.All",
"0c7d31ec-31ca-4f58-b6ec-9950b6b0de69": "ShortNotes.Read.All",
"842c284c-763d-4a97-838d-79787d129bab": "ShortNotes.ReadWrite.All",
"a82116e5-55eb-4c41-a434-62fe8a61c773": "Sites.FullControl.All",
"0c0bf378-bf22-4481-8f81-9e89a9b4960a": "Sites.Manage.All",
"332a536c-c7ef-4017-ab91-336970924f0d": "Sites.Read.All",
"9492366f-7969-46a4-8d15-ed1a20078fff": "Sites.ReadWrite.All",
"883ea226-0bf2-4a8f-9f9d-92c9162a727d": "Sites.Selected",
"dcdfc277-41fd-4d68-ad0c-c3057235bd8e": "SpiffeTrustDomain.Read.All",
"17b78cfd-eeff-447d-8bab-2795af00055a": "SpiffeTrustDomain.ReadWrite.All",
"ee1460f0-368b-4153-870a-4e1ca7e72c42": "SubjectRightsRequest.Read.All",
"8387eaa4-1a3c-41f5-b261-f888138e6041": "SubjectRightsRequest.ReadWrite.All",
"5ba43d2f-fa88-4db2-bd1c-a67c5f0fb1ce": "Synchronization.Read.All",
"9b50c33d-700f-43b1-b2eb-87e89b703581": "Synchronization.ReadWrite.All",
"db31e92a-b9ea-4d87-bf6a-75a37a9ca35a": "SynchronizationData-User.Upload",
"f10e1f91-74ed-437f-a6fd-d6ae88e26c1f": "Tasks.Read.All",
"44e666d1-d276-445b-a5fc-8815eeb81d55": "Tasks.ReadWrite.All",
"23fc2474-f741-46ce-8465-674744c5c361": "Team.Create",
"2280dda6-0bfd-44ee-a2f4-cb867cfc4c1e": "Team.ReadBasic.All",
"660b7406-55f1-41ca-a0ed-0b035e182f3e": "TeamMember.Read.All",
"0121dc95-1b9f-4aed-8bac-58c5ac466691": "TeamMember.ReadWrite.All",
"4437522e-9a86-4a41-a7da-e380edd4a97d": "TeamMember.ReadWriteNonOwnerRole.All",
"70dec828-f620-4914-aa83-a29117306807": "TeamsActivity.Read.All",
"a267235f-af13-44dc-8385-c1dc93023186": "TeamsActivity.Send",
"cc7e7635-2586-41d6-adaa-a8d3bcad5ee5": "TeamsAppInstallation.ReadForChat.All",
"1f615aea-6bf9-4b05-84bd-46388e138537": "TeamsAppInstallation.ReadForTeam.All",
"9ce09611-f4f7-4abd-a629-a05450422a97": "TeamsAppInstallation.ReadForUser.All",
"6e74eff9-4a21-45d6-bc03-3a20f61f8281": "TeamsAppInstallation.ReadWriteAndConsentForChat.All",
"b0c13be0-8e20-4bc5-8c55-963c23a39ce9": "TeamsAppInstallation.ReadWriteAndConsentForTeam.All",
"32ca478f-f89e-41d0-aaf8-101deb7da510": "TeamsAppInstallation.ReadWriteAndConsentForUser.All",
"ba1ba90b-2d8f-487e-9f16-80728d85bb5c": "TeamsAppInstallation.ReadWriteAndConsentSelfForChat.All",
"1e4be56c-312e-42b8-a2c9-009600d732c0": "TeamsAppInstallation.ReadWriteAndConsentSelfForTeam.All",
"a87076cf-6abd-4e56-8559-4dbdf41bef96": "TeamsAppInstallation.ReadWriteAndConsentSelfForUser.All",
"9e19bae1-2623-4c4f-ab6e-2664615ff9a0": "TeamsAppInstallation.ReadWriteForChat.All",
"5dad17ba-f6cc-4954-a5a2-a0dcc95154f0": "TeamsAppInstallation.ReadWriteForTeam.All",
"74ef0291-ca83-4d02-8c7e-d2391e6a444f": "TeamsAppInstallation.ReadWriteForUser.All",
"73a45059-f39c-4baf-9182-4954ac0e55cf": "TeamsAppInstallation.ReadWriteSelfForChat.All",
"9f67436c-5415-4e7f-8ac1-3014a7132630": "TeamsAppInstallation.ReadWriteSelfForTeam.All",
"908de74d-f8b2-4d6b-a9ed-2a17b3b78179": "TeamsAppInstallation.ReadWriteSelfForUser.All",
"242607bd-1d2c-432c-82eb-bdb27baa23ab": "TeamSettings.Read.All",
"bdd80a03-d9bc-451d-b7c4-ce7c63fe3c8f": "TeamSettings.ReadWrite.All",
"49981c42-fd7b-4530-be03-e77b21aed25e": "TeamsTab.Create",
"46890524-499a-4bb2-ad64-1476b4f3e1cf": "TeamsTab.Read.All",
"a96d855f-016b-47d7-b51c-1218a98d791c": "TeamsTab.ReadWrite.All",
"fd9ce730-a250-40dc-bd44-8dc8d20f39ea": "TeamsTab.ReadWriteForChat.All",
"6163d4f4-fbf8-43da-a7b4-060fe85ed148": "TeamsTab.ReadWriteForTeam.All",
"425b4b59-d5af-45c8-832f-bb0b7402348a": "TeamsTab.ReadWriteForUser.All",
"9f62e4a2-a2d6-4350-b28b-d244728c4f86": "TeamsTab.ReadWriteSelfForChat.All",
"91c32b81-0ef0-453f-a5c7-4ce2e562f449": "TeamsTab.ReadWriteSelfForTeam.All",
"3c42dec6-49e8-4a0a-b469-36cff0d9da93": "TeamsTab.ReadWriteSelfForUser.All",
"6323133e-1f6e-46d4-9372-ac33a0870636": "TeamTemplates.Read.All",
"dfb0dd15-61de-45b2-be36-d6a69fba3c79": "Teamwork.Migrate.All",
"75bcfbce-a647-4fba-ad51-b63d73b210f4": "Teamwork.Read.All",
"475ebe88-f071-4bd7-af2b-642952bd4986": "TeamworkAppSettings.Read.All",
"ab5b445e-8f10-45f4-9c79-dd3f8062cc4e": "TeamworkAppSettings.ReadWrite.All",
"0591bafd-7c1c-4c30-a2a5-2b9aacb1dfe8": "TeamworkDevice.Read.All",
"79c02f5b-bd4f-4713-bc2c-a8a4a66e127b": "TeamworkDevice.ReadWrite.All",
"b74fd6c4-4bde-488e-9695-eeb100e4907f": "TeamworkTag.Read.All",
"a3371ca5-911d-46d6-901c-42c8c7a937d8": "TeamworkTag.ReadWrite.All",
"ea047cc2-df29-4f3e-83a3-205de61501ca": "TermStore.Read.All",
"f12eb8d6-28e3-46e6-b2c0-b7e4dc69fc95": "TermStore.ReadWrite.All",
"f8f035bb-2cce-47fb-8bf5-7baf3ecbee48": "ThreatAssessment.Read.All",
"dd98c7f5-2d42-42d3-a0e4-633161547251": "ThreatHunting.Read.All",
"197ee4e9-b993-4066-898f-d6aecc55125b": "ThreatIndicators.Read.All",
"21792b6c-c986-4ffc-85de-df9da54b52fa": "ThreatIndicators.ReadWrite.OwnedBy",
"e0b77adb-e790-44a3-b0a0-257d06303687": "ThreatIntelligence.Read.All",
"86632667-cd15-4845-ad89-48a88e8412e1": "ThreatSubmission.Read.All",
"d72bdbf4-a59b-405c-8b04-5995895819ac": "ThreatSubmission.ReadWrite.All",
"926a6798-b100-4a20-a22f-a4918f13951d": "ThreatSubmissionPolicy.ReadWrite.All",
"fff194f1-7dce-4428-8301-1badb5518201": "TrustFrameworkKeySet.Read.All",
"4a771c9a-1cf2-4609-b88e-3d3e02d539cd": "TrustFrameworkKeySet.ReadWrite.All",
"9d952b72-f741-4b40-9185-8c53076c2339": "User-ConvertToInternal.ReadWrite.All",
"8556a004-db57-4d7a-8b82-97a13428e96f": "User-LifeCycleInfo.Read.All",
"925f1248-0f97-47b9-8ec8-538c54e01325": "User-LifeCycleInfo.ReadWrite.All",
"3011c876-62b7-4ada-afa2-506cbbecc68c": "User.EnableDisableAccount.All",
"405a51b5-8d8d-430b-9842-8be4b0e9f324": "User.Export.All",
"09850681-111b-4a89-9bed-3f2cae46d706": "User.Invite.All",
"c529cfca-c91b-489c-af2b-d92990b66ce6": "User.ManageIdentities.All",
"df021288-bdef-4463-88db-98f22de89214": "User.Read.All",
"97235f07-e226-4f63-ace3-39588e11d3a1": "User.ReadBasic.All",
"741f803b-c850-494e-b5df-cde7c675a1ca": "User.ReadWrite.All",
"38d9df27-64da-44fd-b7c5-a6fbac20248f": "UserAuthenticationMethod.Read.All",
"50483e42-d915-4231-9639-7fdb7fd190e5": "UserAuthenticationMethod.ReadWrite.All",
"4e774092-a092-48d1-90bd-baad67c7eb47": "UserNotification.ReadWrite.CreatedByApp",
"de023814-96df-4f53-9376-1e2891ef5a18": "UserShiftPreferences.Read.All",
"d1eec298-80f3-49b0-9efb-d90e224798ac": "UserShiftPreferences.ReadWrite.All",
"fbcd7ef1-df0d-4e05-bb28-93424a89c6df": "UserTeamwork.Read.All",
"d4f67ec2-59b5-4bdc-b4af-d78f6f9c1954": "VirtualAppointment.Read.All",
"bf46a256-f47d-448f-ab78-f226fff08d40": "VirtualAppointment.ReadWrite.All",
"97e45b36-1250-48e4-bd70-2df6dab7e94a": "VirtualAppointmentNotification.Send",
"1dccb351-c4e4-4e09-a8d1-7a9ecbf027cc": "VirtualEvent.Read.All",
"23211fc1-f9d1-4e8e-8e9e-08a5d0a109bb": "VirtualEventRegistration-Anon.ReadWrite.All",
"7dd1be58-6e76-4401-bf8d-31d1e8180d5b": "WindowsUpdates.ReadWrite.All",
"202bf709-e8e6-478e-bcfd-5d63c50b68e3": "WorkforceIntegration.ReadWrite.All",
"570282fd-fa5c-430d-a7fd-fc8dc98a9daf": "User.Delete.AADSyncApp",
"570282fd-fa5c-430d-a7fd-fc8dc98a9adc": "Tenant.Delete.AADSyncApp",
"570282fd-fa5c-430d-a7fd-fc8dc98a9fda": "Team.Delete.AADSyncApp",
"8339ddc4-fc04-4ad0-b7d5-b7d83667da93": "ModernPostPurchaseProvisioning.Execute",
"fca3dabc-fd9a-4d63-bc1f-196bfa2df787": "Tenant.Create",
"3afa6a7d-9b1a-42eb-948e-1650a849e176": "Application.Read.All",
"1cda74f2-2616-4834-b122-5cb1b07f8a59": "Application.ReadWrite.All",
"824c81eb-e3f8-4ee6-8f6d-de7f50d565b7": "Application.ReadWrite.OwnedBy",
"9728c0c4-a06b-4e0e-8d1b-3d694e8ec207": "Member.Read.Hidden",
"1138cb37-bd11-4084-a2b7-9f71582aeddb": "Device.ReadWrite.All",
"78c8a3c8-a07e-4b9e-af1b-b5ccab50a175": "Directory.ReadWrite.All",
"abefe9df-d5a9-41c6-a60b-27b38eac3efb": "Domain.ReadWrite.All",
"5778995a-e1bf-45b8-affa-663a9f3f4d04": "Directory.Read.All",
"6c2d1b1d-a490-4178-ba6b-7efceda9129b": "Policy.Read.All",
"83447e6a-d68b-4373-bd75-efab237f20ba": "ContentDomainItem.ReadWrite.OwnedBy",
"175d9ac0-118e-4725-b5a1-be1e16948cf6": "ContentDomainItem.ReadWrite.All",
"6662245d-d5f3-42cb-b401-b08c2f424d5f": "ContentDomain.ReadWrite",
"bbee328f-fe32-4251-a58c-9b16f9bf50c8": "ContentDomain.Read.All",
"c79b0778-99a8-4d45-9063-3f160ec2776d": "EopPolicySync.AccessAsApp",
"8f819283-077c-4c68-aa24-0ad706da26e0": "ThreatSubmission.ReadWrite.All",
"ed20b8a8-12e9-45f5-b3e5-69f25572d7be": "Graph.ReadWrite.All",
"226fe4b3-a51b-403f-887c-b4f10a79c5aa": "ResourceSpecificPermission.Read.All",
"610a1fb0-5de2-4e6c-923b-b01b49ae9c54": "ResourceSpecificPermission.ReadWrite.All",
"dc4b90ad-de81-4835-8e77-ce5b1a60cbcb": "TenantLifeCycleEvent.Publish",
"af8f2fa3-fc06-41b1-aed5-e2645bfe886f": "ApiSecretRegistration.ReadUnredacted.All",
"f9d2a51f-70e2-41af-b617-3fceaa33ae55": "Communications.Get",
"15391dcf-e272-4693-b514-06792e967d66": "application_access",
"2becb389-af30-4221-8e0a-3384b5a0c656": "application_access_custom_sba_appliance",
"5063317c-fd8e-4efd-94b8-60a68284f8c4": "teams-internal.readwrite",
"82d632fa-68b9-40ab-8c4f-f24986a057fa": "teams.readwrite",
"fb90b455-d8cb-43db-85c7-4985d8072ed3": "teamtemplates.readwrite",
"162b1576-a2b2-458d-b7b9-04481911b4ef": "channels.readwrite",
"68c6d621-ef73-4169-82d9-8a3e930a2087": "user_impersonation",
"9125c627-3755-4ad3-8742-4d6b193c4fc2": "filteredhierarchy.read.all",
"8762e452-5668-459a-b06a-b8f7c8469dd2": "channelmessage.read.all",
"6ca54517-8a0c-421a-b622-4616966bdd75": "teamworktag.readwrite.all",
"182611cf-791c-4a5a-ad8a-73a350a8acfd": "teamsettings.readwrite.all",
"95c0908c-6f05-4ffd-894c-ca317e39b023": "tagmembers.read.all",
"5309cf8f-3921-43c0-9ca9-0f4805e77c6c": "channel.read.all",
"4c3d78f3-c4de-458d-9394-22e459393232": "chat.read.all",
"855fb32a-d020-4bb6-a6de-b4973e6fb72d": "scheduledtags.readwrite.all",
"739a5d4d-78ee-4ce9-b798-286b9e8aefc4": "groupsmetadata.read.all",
"811e23df-61a9-44db-9987-e37355ae33b1": "nodeaccess.read.all"
}

@dataclass(frozen=True)
class EntitlementManagementRoles:
    """
        A data class containing the guids of Entitlement Management roles

        token from here:
    """
    CatalogOwner="ae79f266-94d4-4dab-b730-feca7e132178",
    CatalogReader="44272f93-9762-48e8-af59-1b5351b1d6b3",
    AccessPackageManager="7f480852-ebdc-47d4-87de-0d8498384a83",
    AccessPackageAssignmentManager="e2182095-804a-4656-ae11-64734e9b7ae5"

@dataclass(frozen=True)
class FOCIClients:
    """
        A data class containing client IDs for FOCI Clients

        Taken from here: https://github.com/secureworks/family-of-client-ids-research/blob/main/known-foci-clients.csv
    """
    AzurePortal="c44b4083-3bb0-49c1-b47d-974e53cbdf3c"
    Office365Management="00b41c95-dab0-4487-9791-b9d2c32c80f2"
    MicrosoftAzurePowershell="1950a258-227b-4e31-a9cf-717495945fc2"
    MicrosoftAzureCLI="04b07795-8ddb-461a-bbee-02f9e1bf7b46"
    MicrosoftTeams="1fec8e78-bce4-4aaf-ab1b-5451cc387264"
    WindowsSearch="26a7ee05-5602-4d76-a7ba-eae8b7b67941"
    OutlookMobile="27922004-5251-4030-b22d-91ecd9a37ea4"
    MicrosoftAuthenticatorApp="4813382a-8fa7-425e-ab75-3b753aab3abb"
    OneDriveSyncEngine="ab9b8c07-8f02-4f72-87fa-80105867a763"
    MicrosoftOffice="d3590ed6-52b3-4102-aeff-aad2292ab01c"
    VisualStudio="872cd9fa-d31f-45e0-9eab-6e460a02d1f1"
    OneDriveiOSApp="af124e86-4e96-495a-b70a-90f90ab96707"
    MicrosoftBingSearchForMicrosoftEdge="2d7f3606-b07d-41d1-b9d2-0d0c9296a6e8"
    MicrosoftStreamMobileNative="844cca35-0656-46ce-b636-13f48b0eecbd"
    MicrosoftTeamsDeviceAdminAgent="87749df4-7ccf-48f8-aa87-704bad0e0e16"
    MicrosoftBingSearch="cf36b471-5b44-428c-9ce7-313bf84528de"
    OfficeUWPPWA="0ec893e0-5785-4de6-99da-4ed124e5296c"
    MicrosoftToDoClient="22098786-6e16-43cc-a27d-191a01a1e3b5"
    PowerApps="4e291c71-d680-4d0e-9640-0a3358e31177"
    MicrosoftWhiteboardClient="57336123-6e14-4acc-8dcf-287b6088aa28"
    MicrosoftFlow="57fcbcfa-7cee-4eb1-8b25-12d2030b4ee0"
    MicrosoftPlanner="66375f6b-983f-4c2c-9701-d680650f588f"
    MicrosoftIntuneCompanyPortal="9ba1a5c7-f17a-4de9-a1f1-6178c8d51223"
    AccountsControlUI="a40d7d7d-59aa-447e-a655-679a4107e548"
    YammeriPhone="a569458c-7f2b-45cb-bab9-b7dee514d112"
    OneDrive="b26aadf8-566f-4478-926f-589f601d9c74"
    MicrosoftPowerBI="c0d2a505-13b8-4ae0-aa9e-cddd5eab0b12"
    SharePoint="d326c1ce-6cc6-4de2-bebc-4591e5e13ef0"
    MicrosoftEdge="e9c51622-460d-4d3d-952d-966a5b1da34c"
    MicrosoftTunnel="eb539595-3fe1-474e-9c1d-feb3625d1be5"
    MicrosoftEdge2="ecd6b820-32c2-49b6-98a6-444530e5a77a"
    SharePointAndroid="f05ff7c9-f75a-4acd-a3b5-f4b6a870245d"
    MicrosoftEdge3="f44b1140-bc5e-48c6-8dc0-5cf5a53c0e34"
    M365ComplianceDriveClient="be1918be-3fe3-4be9-b32b-b542fc27f02e"
    MicrosoftDefenderPlatform="cab96880-db5b-4e15-90a7-f3f1d62ffe39"
    MicrosoftEdgeEnterpriseNewTabPage="d7b530a4-7680-4c23-a8bf-c52c121d2e87"
    MicrosoftDefenderForMobile="dd47d17a-3194-4d86-bfd5-c6ae6f5651e3"
    OutlookLite="e9b154d0-7658-433b-bb25-6b8e0a8a7c59"

known_client_redirect_uris={
    "c44b4083-3bb0-49c1-b47d-974e53cbdf3c": "https://portal.azure.com/signin/index/",
    "1fec8e78-bce4-4aaf-ab1b-5451cc387264":"https://login.microsoftonline.com/common/oauth2/nativeclient",
    "1950a258-227b-4e31-a9cf-717495945fc2": "http://localhost:8400",
    "04b07795-8ddb-461a-bbee-02f9e1bf7b46": "http://localhost:21282"
}

@dataclass(frozen=True)
class GraphAPIPermissions:
    """
        All Entra RBAC Role names mapped to their ids in a frozen data class
    """

@dataclass(frozen=True)
class EntraRolesDefinitionIds:
    """
        All Entra RBAC Role names mapped to their ids in a frozen data class
    """

@dataclass(frozen=True)
class RBACRoleDefinitionIds:
    """
        All Azure RBAC Role names mapped to their ids in a frozen data class
    """
    AcrPush="8311e382-0749-4cb8-b61a-304f252e45ec"
    API_Management_Service_Contributor="312a565d-c81f-4fd8-895a-4e21e48d571c"
    AcrPull="7f951dda-4ed3-4680-a7ca-43fe172d538d"
    AcrImageSigner="6cef56e8-d556-48e5-a04f-b8e64114680f"
    AcrDelete="c2f4ef07-c644-48eb-af81-4b1b4947fb11"
    AcrQuarantineReader="cdda3590-29a3-44f6-95f2-9f980659eb04"
    AcrQuarantineWriter="c8d4ff99-41c3-41a8-9f60-21dfdad59608"
    API_Management_Service_Operator_Role="e022efe7-f5ba-4159-bbe4-b44f577e9b61"
    API_Management_Service_Reader_Role="71522526-b88f-4d52-b57f-d31fc3546d0d"
    Application_Insights_Component_Contributor="ae349356-3a1b-4a5e-921d-050484c6347e"
    Application_Insights_Snapshot_Debugger="08954f03-6346-4c2e-81c0-ec3a5cfae23b"
    Attestation_Reader="fd1bd22b-8476-40bc-a0bc-69b95687b9f3"
    Automation_Job_Operator="4fe576fe-1146-4730-92eb-48519fa6bf9f"
    Automation_Runbook_Operator="5fb5aef8-1081-4b8e-bb16-9d5d0385bab5"
    Automation_Operator="d3881f73-407a-4167-8283-e981cbba0404"
    Avere_Contributor="4f8fab4f-1852-4a58-a46a-8eaf358af14a"
    Avere_Operator="c025889f-8102-4ebf-b32c-fc0c6f0c6bd9"
    Azure_Kubernetes_Service_Cluster_Admin_Role="0ab0b1a8-8aac-4efd-b8c2-3ee1fb270be8"
    Azure_Kubernetes_Service_Cluster_User_Role="4abbcc35-e782-43d8-92c5-2d3f1bd2253f"
    Azure_Maps_Data_Reader="423170ca-a8f6-4b0f-8487-9e4eb8f49bfa"
    Azure_Stack_Registration_Owner="6f12a6df-dd06-4f3e-bcb1-ce8be600526a"
    Backup_Contributor="5e467623-bb1f-42f4-a55d-6e525e11384b"
    Billing_Reader="fa23ad8b-c56e-40d8-ac0c-ce449e1d2c64"
    Backup_Reader="a795c7a0-d4a2-40c1-ae25-d81f01202912"
    Blockchain_Member_Node_Access="31a002a1-acaf-453e-8a5b-297c9ca1ea24"
    BizTalk_Contributor="5e3c6656-6cfa-4708-81fe-0de47ac73342"
    CDN_Endpoint_Contributor="426e0c7f-0c7e-4658-b36f-ff54d6c29b45"
    CDN_Profile_Contributor="ec156ff8-a8d1-4d15-830c-5b80698ca432"
    CDN_Profile_Reader="8f96442b-4075-438f-813d-ad51ab4019af"
    Classic_Network_Contributor="b34d265f-36f7-4a0d-a4d4-e158ca92e90f"
    Classic_Storage_Account_Contributor="86e8f5dc-a6e9-4c67-9d15-de283e8eac25"
    Classic_Storage_Account_Key_Operator_Service_Role="985d6b00-f706-48f5-a6fe-d0ca12fb668d"
    ClearDB_MySQL_DB_Contributor="9106cda0-8a86-4e81-b686-29a22c54effe"
    Classic_Virtual_Machine_Contributor="d73bb868-a0df-4d4d-bd69-98a00b01fccb"
    Cognitive_Services_User="a97b65f3-24c7-4388-baec-2e87135dc908"
    Cognitive_Services_Data_Reader="b59867f0-fa02-499b-be73-45a86b5b3e1c"
    Cognitive_Services_Contributor="25fbc0a9-bd7c-42a3-aa1a-3b75d497ee68"
    CosmosBackupOperator="db7b14f2-5adf-42da-9f96-f2ee17bab5cb"
    Contributor="b24988ac-6180-42a0-ab88-20f7382dd24c"
    Cosmos_DB_Account_Reader_Role="fbdf93bf-df7d-467e-a4d2-9458aa1360c8"
    Cost_Management_Contributor="434105ed-43f6-45c7-a02f-909b2ba83430"
    Cost_Management_Reader="72fafb9e-0641-4937-9268-a91bfd8191a3"
    Data_Box_Contributor="add466c9-e687-43fc-8d98-dfcf8d720be5"
    Data_Box_Reader="028f4ed7-e2a9-465e-a8f4-9c0ffdfdc027"
    Data_Factory_Contributor="673868aa-7521-48a0-acc6-0f60742d39f5"
    Data_Purger="150f5e0c-0603-4f03-8c7f-cf70034c4e90"
    Data_Lake_Analytics_Developer="47b7735b-770e-4598-a7da-8b91488b4c88"
    DevTest_Labs_User="76283e04-6283-4c54-8f91-bcf1374a3c64"
    DocumentDB_Account_Contributor="5bd9cd88-fe45-4216-938b-f97437e15450"
    DNS_Zone_Contributor="befefa01-2a29-4197-83a8-272ff33ce314"
    EventGrid_EventSubscription_Contributor="428e0ff0-5e57-4d9c-a221-2c70d0e0a443"
    EventGrid_EventSubscription_Reader="2414bbcf-6497-4faf-8c65-045460748405"
    Graph_Owner="b60367af-1334-4454-b71e-769d9a4f83d9"
    HDInsight_Domain_Services_Contributor="8d8d5a11-05d3-4bda-a417-a08778121c7c"
    Intelligent_Systems_Account_Contributor="03a6d094-3444-4b3d-88af-7477090a9e5e"
    Key_Vault_Contributor="f25e0fa2-a7c8-4377-a976-54943a77a395"
    Knowledge_Consumer="ee361c5d-f7b5-4119-b4b6-892157c8f64c"
    Lab_Creator="b97fb8bc-a8b2-4522-a38b-dd33c7e65ead"
    Log_Analytics_Reader="73c42c96-874c-492b-b04d-ab87d138a893"
    Log_Analytics_Contributor="92aaf0da-9dab-42b6-94a3-d43ce8d16293"
    Logic_App_Operator="515c2055-d9d4-4321-b1b9-bd0c9a0f79fe"
    Logic_App_Contributor="87a39d53-fc1b-424a-814c-f7e04687dc9e"
    Managed_Application_Operator_Role="c7393b34-138c-406f-901b-d8cf2b17e6ae"
    Managed_Applications_Reader="b9331d33-8a36-4f8c-b097-4f54124fdb44"
    Managed_Identity_Operator="f1a07417-d97a-45cb-824c-7a7467783830"
    Managed_Identity_Contributor="e40ec5ca-96e0-45a2-b4ff-59039f2c2b59"
    Management_Group_Contributor="5d58bcaf-24a5-4b20-bdb6-eed9f69fbe4c"
    Management_Group_Reader="ac63b705-f282-497d-ac71-919bf39d939d"
    Monitoring_Reader="43d0d8ad-25c7-4714-9337-8ba259a9fe05"
    Network_Contributor="4d97b98b-1d4f-4787-a291-c67834d212e7"
    New_Relic_APM_Account_Contributor="5d28c62d-5b37-4476-8438-e587778df237"
    Owner="8e3af657-a8ff-443c-a75c-2fe8c4bcb635"
    Reader="acdd72a7-3385-48ef-bd42-f606fba81ae7"
    Redis_Cache_Contributor="e0f68234-74aa-48ed-b826-c38b57376e17"
    Reader_and_Data_Access="c12c1c16-33a1-487b-954d-41c89c60f349"
    Resource_Policy_Contributor="36243c78-bf99-498c-9df9-86d9f8d28608"
    Scheduler_Job_Collections_Contributor="188a0f2f-5c9e-469b-ae67-2aa5ce574b94"
    Search_Service_Contributor="7ca78c08-252a-4471-8644-bb5ff32d4ba0"
    Security_Manager="e3d13bf0-dd5a-482e-ba6b-9b8433878d10"
    Security_Reader="39bc4728-0917-49c7-9d2c-d95423bc2eb4"
    Spatial_Anchors_Account_Contributor="8bbe83f1-e2a6-4df7-8cb4-4e04d4e5c827"
    Site_Recovery_Contributor="6670b86e-a3f7-4917-ac9b-5d6ab1be4567"
    Site_Recovery_Operator="494ae006-db33-4328-bf46-533a6560a3ca"
    Spatial_Anchors_Account_Reader="5d51204f-eb77-4b1c-b86a-2ec626c49413"
    Site_Recovery_Reader="dbaa88c4-0c30-4179-9fb3-46319faa6149"
    Spatial_Anchors_Account_Owner="70bbe301-9835-447d-afdd-19eb3167307c"
    SQL_Managed_Instance_Contributor="4939a1f6-9ae0-4e48-a1e0-f2cbe897382d"
    SQL_DB_Contributor="9b7fa17d-e63e-47b0-bb0a-15c516ac86ec"
    SQL_Security_Manager="056cd41c-7e88-42e1-933e-88ba6a50c9c3"
    Storage_Account_Contributor="17d1049b-9a84-46fb-8f53-869881c3d3ab"
    SQL_Server_Contributor="6d8ee4ec-f05a-4a1d-8b00-a9b17e38b437"
    Storage_Account_Key_Operator_Service_Role="81a9662b-bebf-436f-a333-f67b29880f12"
    Storage_Blob_Data_Contributor="ba92f5b4-2d11-453d-a403-e96b0029c9fe"
    Storage_Blob_Data_Owner="b7e6dc6d-f1e8-4753-8033-0f276bb0955b"
    Storage_Blob_Data_Reader="2a2b9908-6ea1-4ae2-8e65-a410df84e7d1"
    Storage_Queue_Data_Contributor="974c5e8b-45b9-4653-ba55-5f855dd0fb88"
    Storage_Queue_Data_Message_Processor="8a0f0c08-91a1-4084-bc3d-661d67233fed"
    Storage_Queue_Data_Message_Sender="c6a89b2d-59bc-44d0-9896-0f6e12d7b80a"
    Storage_Queue_Data_Reader="19e7f393-937e-4f77-808e-94535e297925"
    Support_Request_Contributor="cfd33db0-3dd1-45e3-aa9d-cdbdf3b6f24e"
    Traffic_Manager_Contributor="a4b10055-b0c7-44c2-b00f-c7b5b3550cf7"
    User_Access_Administrator="18d7d88d-d35e-4fb5-a5c3-7773c20a72d9"
    Virtual_Machine_Contributor="9980e02c-c2be-4d73-94e8-173b1dc7cf3c"
    Web_Plan_Contributor="2cc479cb-7b4d-49a8-b449-8c00fd0f0a4b"
    Website_Contributor="de139f84-1756-47ae-9be6-808fbbe84772"
    Azure_Service_Bus_Data_Owner="090c5cfd-751d-490a-894a-3ce6f1109419"
    Azure_Event_Hubs_Data_Owner="f526a384-b230-433a-b45c-95f59c4a2dec"
    Attestation_Contributor="bbf86eb8-f7b4-4cce-96e4-18cddf81d86e"
    HDInsight_Cluster_Operator="61ed4efc-fab3-44fd-b111-e24485cc132a"
    Cosmos_DB_Operator="230815da-be43-4aae-9cb4-875f7bd000aa"
    Hybrid_Server_Resource_Administrator="48b40c6e-82e0-4eb3-90d5-19e40f49b624"
    Hybrid_Server_Onboarding="5d1e5ee4-7c68-4a71-ac8b-0739630a3dfb"
    Azure_Event_Hubs_Data_Receiver="a638d3c7-ab3a-418d-83e6-5f17a39d4fde"
    Azure_Event_Hubs_Data_Sender="2b629674-e913-4c01-ae53-ef4638d8f975"
    Azure_Service_Bus_Data_Receiver="4f6d3b9b-027b-4f4c-9142-0e5a2a2247e0"
    Azure_Service_Bus_Data_Sender="69a216fc-b8fb-44d8-bc22-1f3c2cd27a39"
    Storage_File_Data_SMB_Share_Reader="aba4ae5f-2193-4029-9191-0cb91df5e314"
    Storage_File_Data_SMB_Share_Contributor="0c867c2a-1d8c-454a-a3db-ab2ea1bdc8bb"
    Private_DNS_Zone_Contributor="b12aa53e-6015-4669-85d0-8515ebb3ae7f"
    Storage_Blob_Delegator="db58b8e5-c6ad-4a2a-8342-4190687cbf4a"
    Desktop_Virtualization_User="1d18fff3-a72a-46b5-b4a9-0b38a3cd7e63"
    Storage_File_Data_SMB_Share_Elevated_Contributor="a7264617-510b-434b-a828-9731dc254ea7"
    Blueprint_Contributor="41077137-e803-4205-871c-5a86e6a753b4"
    Blueprint_Operator="437d2ced-4a38-4302-8479-ed2bcb43d090"
    Microsoft_Sentinel_Contributor="ab8e14d6-4a74-4a29-9ba8-549422addade"
    Microsoft_Sentinel_Responder="3e150937-b8fe-4cfb-8069-0eaf05ecd056"
    Microsoft_Sentinel_Reader="8d289c81-5878-46d4-8554-54e1e3d8b5cb"
    Policy_Insights_Data_Writer="66bb4e9e-b016-4a94-8249-4c0511c2be84"
    SignalR_AccessKey_Reader="04165923-9d83-45d5-8227-78b77b0a687e"
    Web_PubSub_Contributor="8cf5e20a-e4b2-4e9d-b3a1-5ceb692c2761"
    Azure_Connected_Machine_Onboarding="b64e21ea-ac4e-4cdf-9dc9-5b892992bee7"
    Managed_Services_Registration_assignment_Delete_Role="91c1777a-f3dc-4fae-b103-61d183457e46"
    App_Configuration_Data_Owner="5ae67dd6-50cb-40e7-96ff-dc2bfa4b606b"
    App_Configuration_Data_Reader="516239f1-63e1-4d78-a4de-a74fb236a071"
    Kubernetes_Cluster_Azure_Arc_Onboarding="34e09817-6cbe-4d01-b1a2-e0eac5743d41"
    Experimentation_Contributor="7f646f1b-fa08-80eb-a22b-edd6ce5c915c"
    Cognitive_Services_QnA_Maker_Reader="466ccd10-b268-4a11-b098-b4849f024126"
    Cognitive_Services_QnA_Maker_Editor="f4cc2bf9-21be-47a1-bdf1-5c5804381025"
    Experimentation_Administrator="7f646f1b-fa08-80eb-a33b-edd6ce5c915c"
    Remote_Rendering_Administrator="3df8b902-2a6f-47c7-8cc5-360e9b272a7e"
    Remote_Rendering_Client="d39065c4-c120-43c9-ab0a-63eed9795f0a"
    Managed_Application_Contributor_Role="641177b8-a67a-45b9-a033-47bc880bb21e"
    Security_Assessment_Contributor="612c2aa1-cb24-443b-ac28-3ab7272de6f5"
    Tag_Contributor="4a9ae827-6dc8-4573-8ac7-8239d42aa03f"
    Integration_Service_Environment_Developer="c7aa55d3-1abb-444a-a5ca-5e51e485d6ec"
    Integration_Service_Environment_Contributor="a41e2c5b-bd99-4a07-88f4-9bf657a760b8"
    Azure_Kubernetes_Service_Contributor_Role="ed7f3fbd-7b88-4dd4-9017-9adb7ce333f8"
    Azure_Digital_Twins_Data_Reader="d57506d4-4c8d-48b1-8587-93c323f6a5a3"
    Azure_Digital_Twins_Data_Owner="bcd981a7-7f74-457b-83e1-cceb9e632ffe"
    Hierarchy_Settings_Administrator="350f8d15-c687-4448-8ae1-157740a3936d"
    FHIR_Data_Contributor="5a1fc7df-4bf1-4951-a576-89034ee01acd"
    FHIR_Data_Exporter="3db33094-8700-4567-8da5-1501d4e7e843"
    FHIR_Data_Reader="4c8d0bbc-75d3-4935-991f-5f3c56d81508"
    FHIR_Data_Writer="3f88fce4-5892-4214-ae73-ba5294559913"
    Experimentation_Reader="49632ef5-d9ac-41f4-b8e7-bbe587fa74a1"
    Object_Understanding_Account_Owner="4dd61c23-6743-42fe-a388-d8bdd41cb745"
    Azure_Maps_Data_Contributor="8f5e0ce6-4f7b-4dcf-bddf-e6f48634a204"
    Cognitive_Services_Custom_Vision_Contributor="c1ff6cc2-c111-46fe-8896-e0ef812ad9f3"
    Cognitive_Services_Custom_Vision_Deployment="5c4089e1-6d96-4d2f-b296-c1bc7137275f"
    Cognitive_Services_Custom_Vision_Labeler="88424f51-ebe7-446f-bc41-7fa16989e96c"
    Cognitive_Services_Custom_Vision_Reader="93586559-c37d-4a6b-ba08-b9f0940c2d73"
    Cognitive_Services_Custom_Vision_Trainer="0a5ae4ab-0d65-4eeb-be61-29fc9b54394b"
    Key_Vault_Administrator="00482a5a-887f-4fb3-b363-3b7fe8e74483"
    Key_Vault_Crypto_User="12338af0-0e69-4776-bea7-57ae8d297424"
    Key_Vault_Secrets_Officer="b86a8fe4-44ce-4948-aee5-eccb2c155cd7"
    Key_Vault_Secrets_User="4633458b-17de-408a-b874-0445c86b69e6"
    Key_Vault_Certificates_Officer="a4417e6f-fecd-4de8-b567-7b0420556985"
    Key_Vault_Reader="21090545-7ca7-4776-b22c-e363652d74d2"
    Key_Vault_Crypto_Service_Encryption_User="e147488a-f6f5-4113-8e2d-b22465e65bf6"
    Azure_Arc_Kubernetes_Viewer="63f0a09d-1495-4db4-a681-037d84835eb4"
    Azure_Arc_Kubernetes_Writer="5b999177-9696-4545-85c7-50de3797e5a1"
    Azure_Arc_Kubernetes_Cluster_Admin="8393591c-06b9-48a2-a542-1bd6b377f6a2"
    Azure_Arc_Kubernetes_Admin="dffb1e0c-446f-4dde-a09f-99eb5cc68b96"
    Azure_Kubernetes_Service_RBAC_Cluster_Admin="b1ff04bb-8a4e-4dc4-8eb5-8693973ce19b"
    Azure_Kubernetes_Service_RBAC_Admin="3498e952-d568-435e-9b2c-8d77e338d7f7"
    Azure_Kubernetes_Service_RBAC_Reader="7f6c6a51-bcf8-42ba-9220-52d62157d7db"
    Azure_Kubernetes_Service_RBAC_Writer="a7ffa36f-339b-4b5c-8bdf-e2c188b2c0eb"
    Services_Hub_Operator="82200a5b-e217-47a5-b665-6d8765ee745b"
    Object_Understanding_Account_Reader="d18777c0-1514-4662-8490-608db7d334b6"
    SignalR_REST_API_Owner="fd53cd77-2268-407a-8f46-7e7863d0f521"
    Collaborative_Data_Contributor="daa9e50b-21df-454c-94a6-a8050adab352"
    Device_Update_Reader="e9dba6fb-3d52-4cf0-bce3-f06ce71b9e0f"
    Device_Update_Administrator="02ca0879-e8e4-47a5-a61e-5c618b76e64a"
    Device_Update_Content_Administrator="0378884a-3af5-44ab-8323-f5b22f9f3c98"
    Device_Update_Content_Reader="d1ee9a80-8b14-47f0-bdc2-f4a351625a7b"
    Cognitive_Services_Metrics_Advisor_Administrator="cb43c632-a144-4ec5-977c-e80c4affc34a"
    Cognitive_Services_Metrics_Advisor_User="3b20f47b-3825-43cb-8114-4bd2201156a8"
    Schema_Registry_Reader="2c56ea50-c6b3-40a6-83c0-9d98858bc7d2"
    Schema_Registry_Contributor="5dffeca3-4936-4216-b2bc-10343a5abb25"
    AgFood_Platform_Service_Reader="7ec7ccdc-f61e-41fe-9aaf-980df0a44eba"
    AgFood_Platform_Service_Contributor="8508508a-4469-4e45-963b-2518ee0bb728"
    AgFood_Platform_Service_Admin="f8da80de-1ff9-4747-ad80-a19b7f6079e3"
    Managed_HSM_contributor="18500a29-7fe2-46b2-a342-b16a415e101d"
    Security_Detonation_Chamber_Submitter="0b555d9b-b4a7-4f43-b330-627f0e5be8f0"
    SignalR_REST_API_Reader="ddde6b66-c0df-4114-a159-3618637b3035"
    SignalR_Service_Owner="7e4f1700-ea5a-4f59-8f37-079cfe29dce3"
    Reservation_Purchaser="f7b75c60-3036-4b75-91c3-6b41c27c1689"
    AzureML_Metrics_Writer="635dd51f-9968-44d3-b7fb-6d9a6bd613ae"
    Storage_Account_Backup_Contributor="e5e2a7ff-d759-4cd2-bb51-3152d37e2eb1"
    Experimentation_Metric_Contributor="6188b7c9-7d01-4f99-a59f-c88b630326c0"
    Project_Babylon_Data_Curator="9ef4ef9c-a049-46b0-82ab-dd8ac094c889"
    Project_Babylon_Data_Reader="c8d896ba-346d-4f50-bc1d-7d1c84130446"
    Project_Babylon_Data_Source_Administrator="05b7651b-dc44-475e-b74d-df3db49fae0f"
    Application_Group_Contributor="ca6382a4-1721-4bcf-a114-ff0c70227b6b"
    Desktop_Virtualization_Reader="49a72310-ab8d-41df-bbb0-79b649203868"
    Desktop_Virtualization_Contributor="082f0a83-3be5-4ba1-904c-961cca79b387"
    Desktop_Virtualization_Workspace_Contributor="21efdde3-836f-432b-bf3d-3e8e734d4b2b"
    Desktop_Virtualization_User_Session_Operator="ea4bfff8-7fb4-485a-aadd-d4129a0ffaa6"
    Desktop_Virtualization_Session_Host_Operator="2ad6aaab-ead9-4eaa-8ac5-da422f562408"
    Desktop_Virtualization_Host_Pool_Reader="ceadfde2-b300-400a-ab7b-6143895aa822"
    Desktop_Virtualization_Host_Pool_Contributor="e307426c-f9b6-4e81-87de-d99efb3c32bc"
    Desktop_Virtualization_Application_Group_Reader="aebf23d0-b568-4e86-b8f9-fe83a2c6ab55"
    Desktop_Virtualization_Application_Group_Contributor="86240b0e-9422-4c43-887b-b61143f32ba8"
    Desktop_Virtualization_Workspace_Reader="0fa44ee9-7a7d-466b-9bb2-2bf446b1204d"
    Disk_Backup_Reader="3e5e47e6-65f7-47ef-90b5-e5dd4d455f24"
    Disk_Restore_Operator="b50d9833-a0cb-478e-945f-707fcc997c13"
    Disk_Snapshot_Contributor="7efff54f-a5b4-42b5-a1c5-5411624893ce"
    Kubernetes_connected_cluster_role="5548b2cf-c94c-4228-90ba-30851930a12f"
    Security_Detonation_Chamber_Submission_Manager="a37b566d-3efa-4beb-a2f2-698963fa42ce"
    Security_Detonation_Chamber_Publisher="352470b3-6a9c-4686-b503-35deb827e500"
    Collaborative_Runtime_Operator="7a6f0e70-c033-4fb1-828c-08514e5f4102"
    CosmosRestoreOperator="5432c526-bc82-444a-b7ba-57c5b0b5b34f"
    FHIR_Data_Converter="a1705bd2-3a8f-45a5-8683-466fcfd5cc24"
    Quota_Request_Operator="0e5f05e5-9ab9-446b-b98d-1e2157c94125"
    EventGrid_Contributor="1e241071-0855-49ea-94dc-649edcd759de"
    Security_Detonation_Chamber_Reader="28241645-39f8-410b-ad48-87863e2951d5"
    Object_Anchors_Account_Reader="4a167cdf-cb95-4554-9203-2347fe489bd9"
    Object_Anchors_Account_Owner="ca0835dd-bacc-42dd-8ed2-ed5e7230d15b"
    WorkloadBuilder_Migration_Agent_Role="d17ce0a2-0697-43bc-aac5-9113337ab61c"
    Azure_Spring_Cloud_Data_Reader="b5537268-8956-4941-a8f0-646150406f0c"
    Cognitive_Services_Speech_Contributor="0e75ca1e-0464-4b4d-8b93-68208a576181"
    Cognitive_Services_Face_Recognizer="9894cab4-e18a-44aa-828b-cb588cd6f2d7"
    Media_Services_Account_Administrator="054126f8-9a2b-4f1c-a9ad-eca461f08466"
    Media_Services_Live_Events_Administrator="532bc159-b25e-42c0-969e-a1d439f60d77"
    Media_Services_Media_Operator="e4395492-1534-4db2-bedf-88c14621589c"
    Media_Services_Policy_Administrator="c4bba371-dacd-4a26-b320-7250bca963ae"
    Media_Services_Streaming_Endpoints_Administrator="99dba123-b5fe-44d5-874c-ced7199a5804"
    Stream_Analytics_Query_Tester="1ec5b3c1-b17e-4e25-8312-2acb3c3c5abf"
    AnyBuild_Builder="a2138dac-4907-4679-a376-736901ed8ad8"
    IoT_Hub_Data_Reader="b447c946-2db7-41ec-983d-d8bf3b1c77e3"
    IoT_Hub_Twin_Contributor="494bdba2-168f-4f31-a0a1-191d2f7c028c"
    IoT_Hub_Registry_Contributor="4ea46cd5-c1b2-4a8e-910b-273211f9ce47"
    IoT_Hub_Data_Contributor="4fc6c259-987e-4a07-842e-c321cc9d413f"
    Test_Base_Reader="15e0f5a1-3450-4248-8e25-e2afe88a9e85"
    Search_Index_Data_Reader="1407120a-92aa-4202-b7e9-c0e197c71c8f"
    Search_Index_Data_Contributor="8ebe5a00-799e-43f5-93ac-243d3dce84a7"
    Storage_Table_Data_Reader="76199698-9eea-4c19-bc75-cec21354c6b6"
    Storage_Table_Data_Contributor="0a9a7e1f-b9d0-4cc4-a60d-0319b160aaa3"
    DICOM_Data_Reader="e89c7a3c-2f64-4fa1-a847-3e4c9ba4283a"
    DICOM_Data_Owner="58a3b984-7adf-4c20-983a-32417c86fbc8"
    EventGrid_Data_Sender="d5a91429-5739-47e2-a06b-3470a27159e7"
    Disk_Pool_Operator="60fc6e62-5479-42d4-8bf4-67625fcc2840"
    AzureML_Data_Scientist="f6c7c914-8db3-469d-8ca1-694a8f32e121"
    Grafana_Admin="22926164-76b3-42b3-bc55-97df8dab3e41"
    Azure_Connected_SQL_Server_Onboarding="e8113dce-c529-4d33-91fa-e9b972617508"
    Azure_Relay_Sender="26baccc8-eea7-41f1-98f4-1762cc7f685d"
    Azure_Relay_Owner="2787bf04-f1f5-4bfe-8383-c8a24483ee38"
    Azure_Relay_Listener="26e0b698-aa6d-4085-9386-aadae190014d"
    Grafana_Viewer="60921a7e-fef1-4a43-9b16-a26c52ad4769"
    Grafana_Editor="a79a5197-3a5c-4973-a920-486035ffd60f"
    Automation_Contributor="f353d9bd-d4a6-484e-a77a-8050b599b867"
    Kubernetes_Extension_Contributor="85cb6faf-e071-4c9b-8136-154b5a04f717"
    Device_Provisioning_Service_Data_Reader="10745317-c249-44a1-a5ce-3a4353c0bbd8"
    Device_Provisioning_Service_Data_Contributor="dfce44e4-17b7-4bd1-a6d1-04996ec95633"
    Code_Signing_Certificate_Profile_Signer="2837e146-70d7-4cfd-ad55-7efa6464f958"
    Azure_Spring_Cloud_Service_Registry_Reader="cff1b556-2399-4e7e-856d-a8f754be7b65"
    Azure_Spring_Cloud_Service_Registry_Contributor="f5880b48-c26d-48be-b172-7927bfa1c8f1"
    Azure_Spring_Cloud_Config_Server_Reader="d04c6db6-4947-4782-9e91-30a88feb7be7"
    Azure_Spring_Cloud_Config_Server_Contributor="a06f5c24-21a7-4e1a-aa2b-f19eb6684f5b"
    Azure_VM_Managed_identities_restore_Contributor="6ae96244-5829-4925-a7d3-5975537d91dd"
    Azure_Maps_Search_and_Render_Data_Reader="6be48352-4f82-47c9-ad5e-0acacefdb005"
    Azure_Maps_Contributor="dba33070-676a-4fb0-87fa-064dc56ff7fb"
    Azure_Arc_VMware_VM_Contributor="b748a06d-6150-4f8a-aaa9-ce3940cd96cb"
    Azure_Arc_VMware_Private_Cloud_User="ce551c02-7c42-47e0-9deb-e3b6fc3a9a83"
    Azure_Arc_VMware_Administrator_role_="ddc140ed-e463-4246-9145-7c664192013f"
    Cognitive_Services_LUIS_Owner="f72c8140-2111-481c-87ff-72b910f6e3f8"
    Cognitive_Services_Language_Reader="7628b7b8-a8b2-4cdc-b46f-e9b35248918e"
    Cognitive_Services_Language_Writer="f2310ca1-dc64-4889-bb49-c8e0fa3d47a8"
    Cognitive_Services_Language_Owner="f07febfe-79bc-46b1-8b37-790e26e6e498"
    Cognitive_Services_LUIS_Reader="18e81cdc-4e98-4e29-a639-e7d10c5a6226"
    Cognitive_Services_LUIS_Writer="6322a993-d5c9-4bed-b113-e49bbea25b27"
    PlayFab_Reader="a9a19cc5-31f4-447c-901f-56c0bb18fcaf"
    Load_Test_Contributor="749a398d-560b-491b-bb21-08924219302e"
    Load_Test_Owner="45bb0b16-2f0c-4e78-afaa-a07599b003f6"
    PlayFab_Contributor="0c8b84dc-067c-4039-9615-fa1a4b77c726"
    Load_Test_Reader="3ae3fb29-0000-4ccd-bf80-542e7b26e081"
    Cognitive_Services_Immersive_Reader_User="b2de6794-95db-4659-8781-7e080d3f2b9d"
    Lab_Services_Contributor="f69b8690-cc87-41d6-b77a-a4bc3c0a966f"
    Lab_Services_Reader="2a5c394f-5eb7-4d4f-9c8e-e8eae39faebc"
    Lab_Assistant="ce40b423-cede-4313-a93f-9b28290b72e1"
    Lab_Operator="a36e6959-b6be-4b12-8e9f-ef4b474d304d"
    Lab_Contributor="5daaa2af-1fe8-407c-9122-bba179798270"
    Security_Admin="fb1c8493-542b-48eb-b624-b4c8fea62acd"
    Web_PubSub_Service_Owner="12cf5a90-567b-43ae-8102-96cf46c7d9b4"
    Web_PubSub_Service_Reader="bfb1c7d2-fb1a-466b-b2ba-aee63b92deaf"
    SignalR_App_Server="420fcaa2-552c-430f-98ca-3264be4806c7"
    Virtual_Machine_User_Login="fb879df8-f326-4884-b1cf-06f3ad86be52"
    Virtual_Machine_Administrator_Login="1c0163c0-47e6-4577-8991-ea5c82e286e4"
    Azure_Connected_Machine_Resource_Administrator="cd570a14-e51a-42ad-bac8-bafd67325302"
    Backup_Operator="00c29273-979b-4161-815c-10b084fb9324"
    Workbook_Contributor="e8ddcd69-c73f-4f9f-9844-4100522f16ad"
    Workbook_Reader="b279062a-9be3-42a0-92ae-8b3cf002ec4d"
    Monitoring_Contributor="749f88d5-cbae-40b8-bcfc-e573ddc772fa"
    Monitoring_Metrics_Publisher="3913510d-42f4-4e42-8a64-420c390055eb"
    Purview_role_1="8a3c2885-9b38-4fd2-9d99-91af537c1347"
    Purview_role_2="200bba9e-f0c8-430f-892b-6f0794863803"
    Purview_role_3="ff100721-1b9d-43d8-af52-42b69c1272db"
    Autonomous_Development_Platform_Data_Contributor="b8b15564-4fa6-4a59-ab12-03e1d9594795"
    Autonomous_Development_Platform_Data_Owner="27f8b550-c507-4db9-86f2-f4b8e816d59d"
    Autonomous_Development_Platform_Data_Reader="d63b75f7-47ea-4f27-92ac-e0d173aaf093"
    Key_Vault_Crypto_Officer="14b46e9e-c2b7-41b4-b07b-48a6ebf60603"
    Device_Update_Deployments_Reader="49e2f5d2-7741-4835-8efa-19e1fe35e47f"
    Device_Update_Deployments_Administrator="e4237640-0e3d-4a46-8fda-70bc94856432"
    Azure_Arc_VMware_Private_Clouds_Onboarding="67d33e57-3129-45e6-bb0b-7cc522f762fa"
    Chamber_Admin="4e9b8407-af2e-495b-ae54-bb60a55b1b5a"
    Microsoft_Sentinel_Automation_Contributor="f4c81013-99ee-4d62-a7ee-b3f1f648599a"
    CDN_Endpoint_Reader="871e35f6-b5c1-49cc-a043-bde969a0f2cd"
    Chamber_User="4447db05-44ed-4da3-ae60-6cbece780e32"
    Cognitive_Services_Speech_User="f2dc8367-1007-4938-bd23-fe263f013447"
    Windows_Admin_Center_Administrator_Login="a6333a3e-0164-44c3-b281-7a577aff287f"
    Azure_Kubernetes_Service_Policy_Add_On_Deployment="18ed5180-3e48-46fd-8541-4ea054d57064"
    Guest_Configuration_Resource_Contributor="088ab73d-1256-47ae-bea9-9de8e7131f31"
    Domain_Services_Reader="361898ef-9ed1-48c2-849c-a832951106bb"
    Domain_Services_Contributor="eeaeda52-9324-47f6-8069-5d5bade478b2"
    DNS_Resolver_Contributor="0f2ebee7-ffd4-4fc0-b3b7-664099fdad5d"
    Azure_Arc_Enabled_Kubernetes_Cluster_User_Role="00493d72-78f6-4148-b6c5-d3ce8e4799dd"
    Data_Operator_for_Managed_Disks="959f8984-c045-4866-89c7-12bf9737be2e"
    AgFood_Platform_Sensor_Partner_Contributor="6b77f0a0-0d89-41cc-acd1-579c22c17a67"
    Compute_Gallery_Sharing_Admin="1ef6a3be-d0ac-425d-8c01-acb62866290b"
    Scheduled_Patching_Contributor="cd08ab90-6b14-449c-ad9a-8f8e549482c6"
    DevCenter_Dev_Box_User="45d50f46-0b78-4001-a660-4198cbe8cd05"
    DevCenter_Project_Admin="331c37c6-af14-46d9-b9f4-e1909e1b95a0"
    Virtual_Machine_Local_User_Login="602da2ba-a5c2-41da-b01d-5360126ab525"
    Azure_Arc_ScVmm_VM_Contributor="e582369a-e17b-42a5-b10c-874c387c530b"
    Azure_Arc_ScVmm_Administrator_role="a92dfd61-77f9-4aec-a531-19858b406c87"
    Azure_Arc_ScVmm_Private_Clouds_Onboarding="6aac74c4-6311-40d2-bbdd-7d01e7c6e3a9"
    Azure_Arc_ScVmm_Private_Cloud_User="c0781e91-8102-4553-8951-97c6d4243cda"
    HDInsight_on_AKS_Cluster_Pool_Admin="7656b436-37d4-490a-a4ab-d39f838f0042"
    HDInsight_on_AKS_Cluster_Admin="fd036e6b-1266-47a0-b0bb-a05d04831731"
    FHIR_Data_Importer="4465e953-8ced-4406-a58e-0f6e3f3b530b"
    API_Management_Developer_Portal_Content_Editor="c031e6a8-4391-4de0-8d69-4706a7ed3729"
    VM_Scanner_Operator="d24ecba3-c1f4-40fa-a7bb-4588a071e8fd"
    Elastic_SAN_Owner="80dcbedb-47ef-405d-95bd-188a1b4ac406"
    Elastic_SAN_Reader="af6a70f8-3c9f-4105-acf1-d719e9fca4ca"
    Desktop_Virtualization_Virtual_Machine_Contributor="a959dbd1-f747-45e3-8ba6-dd80f235f97c"
    Desktop_Virtualization_Power_On_Off_Contributor="40c5ff49-9181-41f8-ae61-143b0e78555e"
    Desktop_Virtualization_Power_On_Contributor="489581de-a3bd-480d-9518-53dea7416b33"
    Elastic_SAN_Volume_Group_Owner="a8281131-f312-4f34-8d98-ae12be9f0d23"
    Access_Review_Operator_Service_Role="76cc9ee4-d5d3-4a45-a930-26add3d73475"
    Code_Signing_Identity_Verifier="4339b7cf-9826-4e41-b4ed-c7f4505dac08"
    Video_Indexer_Restricted_Viewer="a2c4a527-7dc0-4ee3-897b-403ade70fafb"
    Monitoring_Data_Reader="b0d8363b-8ddd-447d-831f-62ca05bff136"
    Azure_Kubernetes_Fleet_Manager_RBAC_Writer="5af6afb3-c06c-4fa4-8848-71a8aee05683"
    Azure_Kubernetes_Fleet_Manager_RBAC_Admin="434fb43a-c01c-447e-9f67-c3ad923cfaba"
    Azure_Kubernetes_Fleet_Manager_Contributor_Role="63bb64ad-9799-4770-b5c3-24ed299a07bf"
    Azure_Kubernetes_Fleet_Manager_RBAC_Reader="30b27cfc-9c84-438e-b0ce-70e35255df80"
    Azure_Kubernetes_Fleet_Manager_RBAC_Cluster_Admin="18ab4d3d-a1bf-4477-8ad9-8359bc988f69"
    Kubernetes_Namespace_User="ba79058c-0414-4a34-9e42-c3399d80cd5a"
    Data_Labeling_Labeler="c6decf44-fd0a-444c-a844-d653c394e7ab"
    Role_Based_Access_Control_Administrator="f58310d9-a9f6-439a-9e8d-f62e7b41a168"
    Template_Spec_Contributor="1c9b6475-caf0-4164-b5a1-2142a7116f4b"
    Template_Spec_Reader="392ae280-861d-42bd-9ea5-08ee6d83b80e"
    Microsoft_Sentinel_Playbook_Operator="51d6186e-6489-4900-b93f-92e23144cca5"
    Deployment_Environments_User="18e40d4e-8d2e-438d-97e1-9528336e149c"
    Azure_Spring_Apps_Connect_Role="80558df3-64f9-4c0f-b32d-e5094b036b0b"
    Azure_Spring_Apps_Remote_Debugging_Role="a99b0159-1064-4c22-a57b-c9b3caa1c054"
    AzureML_Registry_User="1823dd4f-9b8c-4ab6-ab4e-7397a3684615"
    AzureML_Compute_Operator="e503ece1-11d0-4e8e-8e2c-7a6c3bf38815"
    Azure_Center_for_SAP_solutions_service_role="aabbc5dd-1af0-458b-a942-81af88f9c138"
    Azure_Center_for_SAP_solutions_reader="05352d14-a920-4328-a0de-4cbe7430e26b"
    Azure_Center_for_SAP_solutions_administrator="7b0c7e81-271f-4c71-90bf-e30bdfdbc2f7"
    AppGw_for_Containers_Configuration_Manager="fbc52c3f-28ad-4303-a892-8a056630b8f1"
    FHIR_SMART_User="4ba50f17-9666-485c-a643-ff00808643f0"
    Cognitive_Services_OpenAI_Contributor="a001fd3d-188f-4b5d-821b-7da978bf7442"
    Cognitive_Services_OpenAI_User="5e0bd9bd-7b93-4f28-af87-19fc36ad61bd"
    Impact_Reporter="36e80216-a7e8-4f42-a7e1-f12c98cbaf8a"
    Impact_Reader="68ff5d27-c7f5-4fa9-a21c-785d0df7bd9e"
    Azure_Kubernetes_Service_Cluster_Monitoring_User="1afdec4b-e479-420e-99e7-f82237c7c5e6"
    ContainerApp_Reader="ad2dd5fb-cd4b-4fd4-a9b6-4fed3630980b"
    Azure_Connected_Machine_Resource_Manager="f5819b54-e033-4d82-ac66-4fec3cbf3f4c"
    SqlDb_Migration_Role="189207d4-bb67-4208-a635-b06afe8b2c57"
    Bayer_Ag_Powered_Services_GDU_Solution="c4bc862a-3b64-4a35-a021-a380c159b042"
    Bayer_Ag_Powered_Services_Imagery_Solution="ef29765d-0d37-4119-a4f8-f9f9902c9588"
    Azure_Center_for_SAP_solutions_Service_role_for_management="0105a6b0-4bb9-43d2-982a-12806f9faddb"
    Azure_Center_for_SAP_solutions_Management_role="6d949e1d-41e2-46e3-8920-c6e4f31a8310"
    Kubernetes_Agentless_Operator="d5a2ae44-610b-4500-93be-660a0c5f5ca6"
    Azure_Usage_Billing_Data_Sender="f0310ce6-e953-4cf8-b892-fb1c87eaf7f6"
    SqlMI_Migration_Role="1d335eef-eee1-47fe-a9e0-53214eba8872"
    Bayer_Ag_Powered_Services_CWUM_Solution="a9b99099-ead7-47db-8fcf-072597a61dfa"
    SqlVM_Migration_Role="ae8036db-e102-405b-a1b9-bae082ea436d"
    Azure_Front_Door_Domain_Contributor="0ab34830-df19-4f8c-b84e-aa85b8afa6e8"
    Azure_Front_Door_Secret_Reader="0db238c4-885e-4c4f-a933-aa2cef684fca"
    Azure_Front_Door_Secret_Contributor="3f2eb865-5811-4578-b90a-6fc6fa0df8e5"
    Azure_Front_Door_Domain_Reader="0f99d363-226e-4dca-9920-b807cf8e1a5f"
    Azure_Stack_HCI_Administrator="bda0d508-adf1-4af0-9c28-88919fc3ae06"
    MySQL_Backup_And_Export_Operator="d18ad5f3-1baf-4119-b49b-d944edb1f9d0"
    LocalNGFirewallAdministrator_role="a8835c7d-b5cb-47fa-b6f0-65ea10ce07a2"
    LocalRulestacksAdministrator_role="bfc3b73d-c6ff-45eb-9a5f-40298295bf20"
    Azure_Extension_for_SQL_Server_Deployment="7392c568-9289-4bde-aaaa-b7131215889d"
    Azure_Maps_Data_Read_and_Batch_Role="d6470a16-71bd-43ab-86b3-6f3a73f4e787"
    API_Management_Service_Workspace_API_Product_Manager="d59a3e9c-6d52-4a5a-aeed-6bf3cf0e31da"
    API_Management_Workspace_API_Developer="56328988-075d-4c6a-8766-d93edd6725b6"
    API_Management_Workspace_Reader="ef1c2c96-4a77-49e8-b9a4-6179fe1d2fd2"
    API_Management_Workspace_API_Product_Manager="73c2c328-d004-4c5e-938c-35c6f5679a1f"
    API_Management_Service_Workspace_API_Developer="9565a273-41b9-4368-97d2-aeb0c976a9b3"
    API_Management_Workspace_Contributor="0c34c906-8d99-4cb7-8bb7-33f5b0a1a799"
    Storage_File_Data_Privileged_Reader="b8eda974-7b85-4f76-af95-65846b26df6d"
    Storage_File_Data_Privileged_Contributor="69566ab7-960f-475b-8e7c-b3118f30c6bd"
    Windows_365_Network_User="7eabc9a4-85f7-4f71-b8ab-75daaccc1033"
    Windows365SubscriptionReader="3d55a8f6-4133-418d-8051-facdb1735758"
    Windows_365_Network_Interface_Contributor="1f135831-5bbe-4924-9016-264044c00788"
    App_Compliance_Automation_Reader="ffc6bbe0-e443-4c3b-bf54-26581bb2f78e"
    App_Compliance_Automation_Administrator="0f37683f-2463-46b6-9ce7-9b788b988ba2"
    Azure_Sphere_Contributor="8b9dfcab-4b77-4632-a6df-94bd07820648"
    SaaS_Hub_Contributor="e9b8712a-cbcf-4ea7-b0f7-e71b803401e6"
    Azure_Sphere_Reader="c8ae6279-5a0b-4cb2-b3f0-d4d62845742c"
    Azure_Sphere_Publisher="6d994134-994b-4a59-9974-f479f0b227fb"
    Azure_Machine_Learning_Workspace_Connection_Secrets_Reader="ea01e6af-a1c1-4350-9563-ad00f8c72ec5"
    Procurement_Contributor="be1a1ac2-09d3-4261-9e57-a73a6e227f53"
    Cognitive_Search_Serverless_Data_Contributor="7ac06ca7-21ca-47e3-a67b-cbd6e6223baf"
    Cognitive_Search_Serverless_Data_Reader="79b01272-bf9f-4f4c-9517-5506269cf524"
    Community_Owner_Role="5e28a61e-8040-49db-b175-bb5b88af6239"
    Firmware_Analysis_Admin="9c1607d1-791d-4c68-885d-c7b7aaff7c8a"
    Key_Vault_Data_Access_Administrator="8b54135c-b56d-4d72-a534-26097cfdc8d8"
    Defender_for_Storage_Data_Scanner="1e7ca9b1-60d1-4db8-a914-f2ca1ff27c40"
    Compute_Diagnostics_Role="df2711a6-406d-41cf-b366-b0250bff9ad1"
    Elastic_SAN_Network_Admin="fa6cecf6-5db3-4c43-8470-c540bcb4eafa"
    Cognitive_Services_Usages_Reader="bba48692-92b0-4667-a9ad-c31c7b334ac2"
    PostgreSQL_Flexible_Server_Long_Term_Retention_Backup_Role="c088a766-074b-43ba-90d4-1fb21feae531"
    Search_Parameter_Manager="a02f7c31-354d-4106-865a-deedf37fa038"
    Virtual_Machine_Data_Access_Administrator="66f75aeb-eabe-4b70-9f1e-c350c4c9ad04"
    Logic_Apps_Standard_Developer="523776ba-4eb2-4600-a3c8-f2dc93da4bdb"
    Logic_Apps_Standard_Contributor="ad710c24-b039-4e85-a019-deb4a06e8570"
    Logic_Apps_Standard_Operator="b70c96e9-66fe-4c09-b6e7-c98e69c98555"
    Logic_Apps_Standard_Reader="4accf36b-2c05-432f-91c8-5c532dff4c73"
    IPAM_Pool_Contributor="7b3e853f-ad5d-4fb5-a7b8-56a3581c7037"
    SpatialMapsAccounts_Account_Owner="e9c9ed2b-2a99-4071-b2ff-5b113ebf73a1"
    Azure_Resource_Notifications_System_Topics_Subscriber="0b962ed2-6d56-471c-bd5f-3477d83a7ba4"
    Elastic_SAN_Volume_Importer="90e8b822-3e73-47b5-868a-787dc80c008f"
    Elastic_SAN_Snapshot_Exporter="1c4770c0-34f7-4110-a1ea-a5855cc7a939"
    Community_Contributor_Role="49435da6-99fe-48a5-a235-fc668b9dc04a"
    EventGrid_TopicSpaces_Subscriber="4b0f2fd7-60b4-4eca-896f-4435034f8bf5"
    EventGrid_TopicSpaces_Publisher="a12b0b94-b317-4dcd-84a8-502ce99884c6"
    Data_Boundary_Tenant_Administrator="d1a38570-4b05-4d70-b8e4-1100bcf76d12"
    DeID_Realtime_Data_User="bb6577c4-ea0a-40b2-8962-ea18cb8ecd4e"
    DeID_Batch_Data_Reader="b73a14ee-91f5-41b7-bd81-920e12466be9"
    DeID_Batch_Data_Owner="8a90fa6b-6997-4a07-8a95-30633a7c97b9"
    Carbon_Optimization_Reader="fa0d39e6-28e5-40cf-8521-1eb320653a4c"
    Landing_Zone_Management_Owner="38863829-c2a4-4f8d-b1d2-2e325973ebc7"
    Landing_Zone_Management_Reader="8fe6e843-6d9e-417b-9073-106b048f50bb"
    Azure_Stack_HCI_Device_Management_Role="865ae368-6a45-4bd1-8fbf-0d5151f56fc1"
    Azure_Customer_Lockbox_Approver_for_Subscription="4dae6930-7baf-46f5-909e-0383bc931c46"
    Azure_Resource_Bridge_Deployment_Role="7b1f81f9-4196-4058-8aae-762e593270df"
    Azure_Stack_HCI_VM_Reader="4b3fe76c-f777-4d24-a2d7-b027b0f7b273"
    Azure_AI_Developer="64702f94-c441-49e6-a78b-ef80e0188fee"
    Azure_Stack_HCI_VM_Contributor="874d1c73-6003-4e60-a13a-cb31ea190a85"
    Deployment_Environments_Reader="eb960402-bf75-4cc3-8d68-35b34f960f72"
    EventGrid_Data_Receiver="78cbd9e7-9798-4e2e-9b5a-547d9ebb31fb"
    EventGrid_Data_Contributor="1d8c3fe3-8864-474b-8749-01e3783e8157"
    Advisor_Reviews_Contributor="8aac15f0-d885-4138-8afa-bfb5872f7d13"
    Advisor_Reviews_Reader="c64499e0-74c3-47ad-921c-13865957895c"
    Azure_AI_Inference_Deployment_Operator="3afb7f49-54cb-416e-8c09-6dc049efa503"
    Connected_Cluster_Managed_Identity_CheckAccess_Reader="65a14201-8f6c-4c28-bec4-12619c5a9aaa"
    AgFood_Platform_Dataset_Admin="a8d4b70f-0fb9-4f72-b267-b87b2f990aec"
    Azure_Front_Door_Profile_Reader="662802e2-50f6-46b0-aed2-e834bacc6d12"
    Enclave_Reader_Role="86fede04-b259-4277-8c3e-e26b9865abd8"
    Azure_Kubernetes_Service_Hybrid_Cluster_User_Role="fc3f91a1-40bf-4439-8c46-45edbd83563a"
    Azure_Kubernetes_Service_Hybrid_Cluster_Admin_Role="b5092dac-c796-4349-8681-1a322a31c3f9"
    Azure_Kubernetes_Service_Hybrid_Contributor_Role="e7037d40-443a-4434-a3fb-8cd202011e1d"
    Enclave_Owner_Role="3d5f3eff-eb94-473d-91e3-7aac74d6c0bb"
    Enclave_Contributor_Role="19feefae-eacc-4106-81fd-ac34c0671f14"
    Community_Reader_Role="e6aadb6b-e64f-41c0-9392-d2bba3bc3ebc"
    Storage_Account_Encryption_Scope_Contributor_Role="a316ed6d-1efe-48ac-ac08-f7995a9c26fb"
    Operator_Nexus_Key_Vault_Writer_Service_Role="44f0a1a8-6fea-4b35-980a-8ff50c487c97"
    Key_Vault_Crypto_Service_Release_User="08bbd89e-9f13-488c-ac41-acfcb10c90ab"
    KubernetesRuntime_Storage_Class_Contributor_Role="0cd9749a-3aaf-4ae5-8803-bd217705bf3b"
    Azure_Programmable_Connectivity_Gateway_User="609c0c20-e0a0-4a71-b99f-e7e755ac493d"
    Key_Vault_Certificate_User="db79e9a7-68ee-4b58-9aeb-b90e7c24fcba"
    Azure_Spring_Apps_Managed_Components_Log_Reader_Role="52fd16bd-6ed5-46af-9c40-29cbd7952a29"
    Azure_Spring_Apps_Application_Configuration_Service_Log_Reader_Role="6593e776-2a30-40f9-8a32-4fe28b77655d"
    Azure_Spring_Apps_Spring_Cloud_Gateway_Log_Reader_Role="4301dc2a-25a9-44b0-ae63-3636cf7f2bd2"
    Azure_Edge_On_Site_Deployment_Engineer="207bcc4b-86a6-4487-9141-d6c1f4c238aa"
    Azure_API_Center_Data_Reader="c7244dfb-f447-457d-b2ba-3999044d1706"
    Azure_impact_insight_reader="dfb2f09d-25f8-4558-8986-497084006d7a"
    Defender_Kubernetes_Agent_Operator="8bb6f106-b146-4ee6-a3f9-b9c5a96e0ae5"
    Azure_RedHat_OpenShift_Cloud_Controller_Manager_Role="a1f96423-95ce-4224-ab27-4e3dc72facd4"
    Azure_RedHat_OpenShift_Storage_Operator_Role="5b7237c5-45e1-49d6-bc18-a1f62f400748"
    Azure_RedHat_OpenShift_Network_Operator_Role="be7a6435-15ae-4171-8f30-4a343eff9e8f"
    Azure_RedHat_OpenShift_Image_Registry_Operator_Role="8b32b316-c2f5-4ddf-b05b-83dacd2d08b5"
    Azure_RedHat_OpenShift_Azure_Files_Storage_Operator_Role="0d7aedc0-15fd-4a67-a412-efad370c947e"
    Azure_RedHat_OpenShift_Service_Operator="4436bae4-7702-4c84-919b-c4069ff25ee2"
    Azure_RedHat_OpenShift_Machine_API_Operator_Role="0358943c-7e01-48ba-8889-02cc51d78637"
    Azure_RedHat_OpenShift_Cluster_Ingress_Operator_Role="0336e1d3-7a87-462b-b6db-342b63f7802c"
    Azure_Sphere_Owner="5a382001-fe36-41ff-bba4-8bf06bd54da9"
