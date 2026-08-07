# Azure DevOps

azol includes two DevOps-oriented clients:

- [`AzureDevOpsClient`](../reference/clients/azure_devops_client.md) — org/project APIs (pipelines, service connections, etc.)
- [`AzureDevOpsAgentClient`](../reference/clients/devops_agent_client.md) — agent / session flows with [`DevOpsAgentCredential`](../reference/credentials.md)

For pipeline OIDC, use [`ADOWorkloadFederationCredential`](../reference/credentials.md) (requires the system access token and a service connection used in the same job — see that class docstring).

```python
from azol.credentials import ServicePrincipal
from azol.clients import AzureDevOpsClient

cred = ServicePrincipal(client_id="...", client_secret="...")
ado = AzureDevOpsClient(tenant="contoso.onmicrosoft.com", cred=cred)
```
