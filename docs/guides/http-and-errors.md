# HTTP & errors

Clients share a fluent HTTP stack under [`azol.http`](../reference/http.md).

## Fluent calls

Most clients expose `.call(path)` (or Graph/ARM-specific builders) that return a chainable request:

```python
result = (
    client.call("/subscriptions")
    .api_version("2020-01-01")
    .get()
)
items = result.values()   # follow paging when present
body = result.json()      # single response body
```

Graph uses OData helpers (`select`, `expand`, `filter`, …). ARM uses `api_version` and ARM paging.

## Errors

Failed responses raise subclasses of `AzolHTTPError` from [`azol.http`](../reference/http.md), including:

- `AzolAuthError` (401)
- `AzolForbiddenError` (403)
- `AzolNotFoundError` (404)
- `AzolConflictError` (409)
- `AzolThrottledError` (429)
- `AzolClientError` / `AzolServerError` for other 4xx / 5xx
