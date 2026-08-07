# Quickstart

## List Azure subscriptions (ARM)

```python
from azol.credentials import User
from azol.clients import ArmClient

cred = User(username="user@domain.com")
arm = ArmClient(tenant="contoso.onmicrosoft.com", cred=cred)

for sub_id in arm.get_subscriptions():
    print(sub_id)
```

## Enumerate groups (Graph)

```python
from pprint import pprint
from azol.credentials import ServicePrincipal
from azol.clients import GraphClient

cred = ServicePrincipal(client_id="...", client_secret="...")
graph = GraphClient(tenant="contoso.onmicrosoft.com", cred=cred)

for group in graph.get_all_groups_and_owners():
    pprint(group)
```

## Interactive user sign-in

```python
from azol import User, ArmClient

cred = User("user@domain.com")
arm = ArmClient(cred=cred, oauth_flow="authorization_code")

for tenant in arm.get_tenants():
    print(tenant["defaultDomain"])
```

See [Authentication](auth.md) for credential types and OAuth flows.
