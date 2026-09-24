import os
from datetime import datetime, timezone


def check_shopee_chat():
    """Shopee chat patrol entry point.

    Connect this function to an official/authorized Shopee chat API or
    your existing authenticated integration. Do not hard-code credentials.
    """
    token = os.getenv("SHOPEE_AUTH_TOKEN")

    print(f"[{datetime.now(timezone.utc).isoformat()}] Shopee chat patrol started")

    if not token:
        print("SHOPEE_AUTH_TOKEN is not configured.")
        print("Patrol scheduler is working, but chat retrieval is not enabled yet.")
        return

    # TODO: Replace with the authorized Shopee chat retrieval implementation.
    print("Authentication secret detected.")
    print("TODO: fetch unread/pending Shopee chat conversations here.")


if __name__ == "__main__":
    check_shopee_chat()
