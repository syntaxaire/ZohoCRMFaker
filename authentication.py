"""Module for OAuth 2.0 authentication to Zoho CRM"""
import requests

from config import config


ACCOUNTS_URL = 'https://accounts.zoho.com'  # US site


def get_access_token(refresh_token: str) -> str:
    """Use our stored refresh token to generate an access token.
    This lasts an hour according to:
    https://www.zoho.com/crm/developer/docs/api/v2/refresh.html
    """
    url = f'{ACCOUNTS_URL}/oauth/v2/token'
    params = {'refresh_token': refresh_token,
              'client_id': config['Client ID'],
              'client_secret': config['Client Secret'],
              'grant_type': 'refresh_token',
              }
    response = requests.post(url, params=params)
    reply = response.json()
    if 'access_token' not in reply:
        raise Exception(reply)
    return reply['access_token']
