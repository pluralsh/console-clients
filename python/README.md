# plural-rest-api-client

Python REST client for the Plural Console API. Generated from the OpenAPI spec using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

## Installation

```bash
pip install pluralsh-console-client
```

## Usage

```python
from plural_rest_api_client import AuthenticatedClient
from plural_rest_api_client.api.user import me

# Configure the API client
client = AuthenticatedClient(
    base_url="https://your-console.example.com",
    token="YOUR_TOKEN",
    prefix="Bearer"
)

# Call API methods
user = me.sync(client=client)
# or async
user = await me.asyncio(client=client)
```

All API operations and types are available through the `plural_rest_api_client` package.

## Regenerating the client

When `openapi.json` in the repo root changes, regenerate the client:

```bash
cd python
make generate
```

## Requirements

- Python 3.8+
