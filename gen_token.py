"""Utility script to create an access and refresh token from a grant token,
for the OAuth2 implementation used by Zoho CRM, for the ZohoCRMFaker app.

The grant token is generated using an online form at:
https://api-console.zoho.com/
"""
import requests

from config import config


ACCOUNTS_URL = 'https://accounts.zoho.com'  # US site


def gen_token(grant_token) -> dict:
    """Use grant token supplied to create an access and refresh token."""
    url = f'{ACCOUNTS_URL}/oauth/v2/token'
    data = {'grant_type': 'authorization_code',
            'client_id': config['Client ID'],
            'client_secret': config['Client Secret'],
            'code': grant}
    response = requests.post(url, data=data)
    return response.json()


if __name__ == '__main__':
    grant = input('Please enter grant token: ')
    reply = gen_token(grant)
    print(reply)
