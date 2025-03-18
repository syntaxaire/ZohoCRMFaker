"""Entry point to ZohoCRMFaker"""

import asyncio
import os
from pprint import pprint

from dotenv import load_dotenv, set_key
import httpx
from faker import Faker
from loguru import logger

ENV_FILE = ".env"
load_dotenv(ENV_FILE, verbose=True)
fake = Faker()


access_token = (
    os.getenv("ZOHO_ACCESS_TOKEN"),
)  # will be written back to .env, thus the state


async def ensure_access_token():
    """Ensure that the access token is valid."""
    global access_token

    # make a request to check
    if not access_token:
        pass
    else:
        # check existing
        result = httpx.get(
            "https://www.zohoapis.com/billing/v1/subscriptions",
            headers={"Authorization": f"Zoho-oauthtoken {access_token}"},
        )
        if result.status_code == 200:
            # it's good
            logger.info("Access token is valid")
            return

    # it's missing, bad or expired; refresh it
    params = {
        "client_id": os.getenv("ZOHO_CLIENT_ID"),
        "client_secret": os.getenv("ZOHO_CLIENT_SECRET"),
        "refresh_token": os.getenv("ZOHO_REFRESH_TOKEN"),
        "grant_type": "refresh_token",
    }
    result = httpx.post("https://accounts.zoho.com/oauth/v2/token", data=params)
    match result.json():
        case {"access_token": access_token}:
            logger.success("Access token refreshed")
            # write state to env file to avoid hitting token refresh rate limit across multiple executions
            set_key(ENV_FILE, "ZOHO_ACCESS_TOKEN", access_token)
        case _:
            logger.error("Failed to refresh access token")
            logger.error(result.json())


async def make_fake_billing_sub():
    """Make fake Billing subscription for tests."""
    headers = {"Authorization": f"Zoho-oauthtoken {access_token}"}
    name = fake.name()
    first_name = name.split()[0]
    last_name = name.split()[1]
    email = first_name.lower() + last_name.lower() + "@example.com"

    data = {
        "customer": {
            "display_name": fake.company(),
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "billing_address": {"state": fake.state(), "country": fake.country()},
        },
        "plan": {"plan_code": "FREE"},
    }
    response = httpx.post(
        url="https://www.zohoapis.com/billing/v1/subscriptions",
        headers=headers,
        json=data,
        timeout=30.0,
    )
    reply = response.json()
    pprint(reply["subscription"]["contactpersons"])


async def main():
    await ensure_access_token()
    await make_fake_billing_sub()


if __name__ == "__main__":
    asyncio.run(main())
