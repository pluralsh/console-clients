import os
import sys

# Allow running without installing the package (e.g. from examples/python)
_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "python")
if _src not in sys.path:
    sys.path.insert(0, _src)

from plural_rest_api_client import AuthenticatedClient
from plural_rest_api_client.api.user import me


def main():
    base_url = os.getenv("CONSOLE_URL", "https://console.plrl-dev-aws.onplural.sh")
    token = os.getenv("CONSOLE_TOKEN", "")

    # Create authenticated client
    client = AuthenticatedClient(
        base_url=base_url,
        token=token,
        prefix="Bearer",  # Authorization header will be "Bearer <token>"
    )

    # Get current user information
    try:
        user = me.sync(client=client)
        if user:
            print("Current user:", user)
            print(f"  ID: {user.id}")
            print(f"  Email: {user.email}")
        else:
            print("No user data returned")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
