# Key Vault

`KeyVaultClient` targets a single vault hostname and works with any azol credential that can get a Key Vault token.

```python
from azol.credentials import ServicePrincipal
from azol.clients import KeyVaultClient

cred = ServicePrincipal(client_id="...", client_secret="...")
kv = KeyVaultClient("my-vault", tenant="contoso.onmicrosoft.com", cred=cred)

for secret in kv.get_secrets():
    print(secret)
```

Helpers include listing keys/secrets/certificates and reading a secret by name (optional version).

See the [KeyVaultClient API reference](../reference/clients/key_vault_client.md).
