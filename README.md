# Azure Offensive Library

A python-based pentesting library for Azure and Entra ID

## Installation

Install the library using Python3 pip:

```pip install azol```

## Basic Usage

Log in as a user and get all subscriptions:

```
from azol.credentials import User
from azol.clients import ArmClient

cred = User(username="user@domain.com")
arm_client = ArmClient(tenant="tenant.com", cred=cred)

subscriptions=arm_client.get_subscriptions()

for sub_id in subscriptions:
  print(sub_id)
```

Log in as a Service Principal and get all groups, with owners

```
from pprint import pprint
from azol.credentials import ServicePrincipal
from azol.clients import GraphClient

cred = ServicePrincipal(client_id="00000000-0000-0000-0000-000000000000", client_secret="your secret" )

graph_client = GraphClient(tenant="tenant.com", cred=cred)

groups=graph_client.get_all_groups_and_owners()

for group in groups:
  pprint(group)

```

Log in as a user to their default tenant, but use an interactive signin. Get all tenants the user belongs to.

```
from azol import *

cred=User("user@domain.com")
arm_client=ArmClient(cred=cred, oauth_flow="authorization_code")

tenants=arm_client.get_tenants()

for tenant in tenants:
  print(tenant["defaultDomain"])

```