# GraphClient

`GraphClient` calls Microsoft Graph for users, groups, apps, directory objects, and related Entra ID surfaces.

## Construct a client

```python
from azol.credentials import ServicePrincipal
from azol.clients import GraphClient

cred = ServicePrincipal(
    client_id="00000000-0000-0000-0000-000000000000",
    client_secret="your secret",
)
graph = GraphClient(tenant="contoso.onmicrosoft.com", cred=cred)
```

## Fluent Graph calls

```python
users = (
    graph.call("/users")
    .select("id,displayName,userPrincipalName")
    .get()
    .values()
)
```

## Common helpers

- Directory and identity enumeration helpers on `GraphClient`
- OData query builders for `$select`, `$filter`, `$expand`, and paging

See the [GraphClient API reference](../reference/clients/graph_client.md).
