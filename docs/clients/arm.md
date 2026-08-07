# ArmClient

`ArmClient` calls Azure Resource Manager for subscriptions, resources, RBAC, PIM at Azure scopes, Logic Apps, Automation, App Service, and related surfaces.

## Construct a client

```python
from azol.credentials import User
from azol.clients import ArmClient

cred = User(username="user@contoso.com")
arm = ArmClient(tenant="contoso.onmicrosoft.com", cred=cred)
```

On construction, the client loads providers unless you pass `ignore_providers=True`.

## Fluent ARM calls

```python
tenants = (
    arm.call("/tenants")
    .api_version("2020-01-01")
    .get()
    .values()
)
```

## Common helpers

- `get_tenants`, `get_subscriptions`, `get_management_groups`
- `get_resources`, `get_resource`, `get_resource_groups`
- `get_rbac_role_assignments`, `get_own_rbac_role_assignments`
- App Service / Function and Automation helpers

See the [ArmClient API reference](../reference/clients/arm_client.md).
