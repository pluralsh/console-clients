# Plural Console Python Client Example

Example usage of the Plural Console Python REST client.

## Setup

1. Install the client from the parent directory:

```bash
cd ../../python
pip install -e .
```

Or install directly from PyPI (once published):

```bash
pip install pluralsh-console-client
```

2. Set environment variables:

```bash
export CONSOLE_URL="https://console.plrl-dev-aws.onplural.sh"
export CONSOLE_TOKEN="your-api-token"
```

## Running the Example

```bash
python example.py
```

## Example Output

```
Current user: User(id='...', email='user@example.com', name='John Doe', ...)
  ID: ...
  Email: user@example.com
  Name: John Doe
```

## Usage Patterns

### Synchronous API Calls

```python
from plural_rest_api_client import AuthenticatedClient
from plural_rest_api_client.api.user import me

client = AuthenticatedClient(
    base_url="https://console.plrl-dev-aws.onplural.sh",
    token="your-api-token",
    prefix="Bearer"
)

user = me.sync(client=client)
print(user)
```

### Asynchronous API Calls

```python
import asyncio
from plural_rest_api_client import AuthenticatedClient
from plural_rest_api_client.api.user import me

async def get_user():
    client = AuthenticatedClient(
        base_url="https://console.plrl-dev-aws.onplural.sh",
        token="your-api-token",
        prefix="Bearer"
    )

    user = await me.asyncio(client=client)
    print(user)

asyncio.run(get_user())
```

## API Structure

The generated client follows this structure:

- `plural_rest_api_client.api.<resource>.<endpoint>` - API endpoint functions
- `plural_rest_api_client.models.<Model>` - Data models
- Each endpoint has `sync()` and `asyncio()` methods for sync/async calls
