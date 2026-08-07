# Easy Auth utilities

Helpers in [`azol.utils`](../reference/utils.md) work with App Service / Functions Easy Auth:

- `get_easy_auth_user_tokens` — call `/.auth/me` with an `X-ZUMO-AUTH` token
- `create_signed_easy_auth_token` — mint a signed Easy Auth JWT (AAD IdP) when you have the signing key
- `decrypt_easy_auth_token` — decrypt Easy Auth encrypted payloads with the hex key from site settings

These are low-level assessment utilities — validate against your authorization and ROE before use.
