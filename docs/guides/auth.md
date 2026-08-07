# Authentication

All azol HTTP clients inherit from [`OAuthHTTPClient`](../reference/clients/oauth_http_client.md) and take a **credential** plus a **tenant** (required for app credentials; often inferred for users).

## Credential types

| Class | Use when |
| --- | --- |
| [`User`](../reference/credentials.md) | Interactive, device code, refresh token, or ESTS cookie auth |
| [`ServicePrincipal`](../reference/credentials.md) | Client secret or certificate (app-only) |
| [`ApplicationObject`](../reference/credentials.md) | Application object credentials |
| [`AccessToken`](../reference/credentials.md) | You already have a raw bearer token |
| [`DevOpsAgentCredential`](../reference/credentials.md) | Azure DevOps agent RSA key material |
| [`ADOWorkloadFederationCredential`](../reference/credentials.md) | DevOps OIDC / workload identity federation |

## OAuth flows

Flow constants live on [`azol.constants.OAUTHFLOWS`](../reference/constants.md):

- `client_credentials` — service principals (default)
- `device_code` — user device code (User default)
- `authorization_code` — interactive browser flow
- `refresh_token` — reuse a stolen / cached refresh token
- `raw_token` — present an existing access token

Pass `oauth_flow=...` into the client constructor when you need to override the credential default.

## Resources

Clients request tokens for a resource id (see [`OAuthResourceIDs`](../reference/constants.md)): Graph, ARM, Key Vault, DevOps, and others.

## Secrets providers & caches

Pass `secrets_provider=` ([`KeyVaultProvider`](../reference/providers.md) / [`FileSecretProvider`](../reference/providers.md)) when credentials should load secrets from elsewhere. Token caching is enabled by default (`use_persistent_cache=True`); tokens are stored under `~/.azol`.
