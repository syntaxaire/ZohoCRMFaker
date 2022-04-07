"""Module for OAuth 2.0 authentication to Zoho CRM"""
from oauthlib.oauth2 import BackendApplicationClient

from config import config


client = BackendApplicationClient(config['Zoho CRM token'])
