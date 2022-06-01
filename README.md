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
armClient = ArmClient(tenant="tenant.com", cred=cred)

subscriptions=armClient.get_subscriptions()

for sid in subscriptions:
  print(sid)
```

Log in as a Service Principal and get all groups, with owners

```
from pprint import pprint
from azol.credentials import ServicePrincipal
from azol.clients import GraphClient

cred = ServicePrincipal(client_id="00000000-0000-0000-0000-000000000000", client_secret="your secret" )

GraphClient = GraphClient(tenant="tenant.com", cred=cred)

groups=GraphClient.get_all_groups_and_owners()

for group in groups:
  pprint(group)

```