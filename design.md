# Library design

## Main Components

The main components within azol include:
- HTTP OAuth clients
- Credential objects
- Token Service
- Token Cache objects
- Secrets Providers

### HTTP Client objects

All clients objects can be imported from azol.clients

Client objects provide an interface for interacting with APIs that accept tokens created by the Microsoft identity Platform. Each client object provides methods for interacting with specific REST APIs.

A client has a 1:1 relationship with a credential object. The credential object is read-only, so the client object simply uses the credential object to define how to authenticate to Entra ID.

### Credential objects

Credential objects are simply containers for authentication data, such as secrets, client ids and usernames. These objects may be applications, service principals, users, or raw tokens. The logic for authentication is not found in the credential object, all credential objects should be read-only.

### Token Service

The OAuth HTTP client objects contain a TokenService object, which is a service responsible for managing OAuth interactions with the Microsoft Identity Platform. The credential object is passed into this token service, so the client object simply calls "fetch_token" on the token service when it needs a new token.

The TokenService implements all of the OAuth logic within azol.

### Token Cache objects

When the token service gets a new token, it stores the access token, refresh token, and id token in a cache for future use. This allows logins to persist across sessions in azol - for example, if a user logs in, the persistent cache may be used to store that user's token locally on the filesystem. That cache may either be a persistent cache, where the token is stored locally, or an in-memory cache, where the token never touches the filesystem.

### Secret Providers

In some cases, operational security may be important for users of azol. For example, maybe storing a sensitive secret on the local filesystem of an azol user is not desired, and users may want to avoid referencing secrets directly in azol scripts.

For this reason, a secret provider has been implemented as an optional way to reference sensitive secrets, such as client_secrets for applications and service principals. If a secret provider is used when instantiating a client object, secrets can be referenced in code using a "secret reference". In practice, this code looks like the following:

    provider = KeyVaultProvider( username="username@user.com", key_vault_name="keyVaultName", tenant_id="providerTenantId" )
    sp = ServicePrincipal( client_id="graphSpClientId", client_secret="secret:secretReferenceName" )
    graphClient = GraphClient( tenant=secretTenantId, cred=sp, secrets_provider=provider )

This code tells the Graph Client to use the Key Vault Provider to de-reference secrets from the credential object. the secret reference characters "secret:" tell the provider that "secretReferenceName" can be resolved by the provider.

The KeyVaultProvider will resolve secrets using an Azure key vault "keyVaultName" in tenant "providerTenantId", where the user "username@user.com" has access to read secrets. These secrets will then never be stored on the local filesystem.