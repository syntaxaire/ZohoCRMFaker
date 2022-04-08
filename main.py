"""Entry point to ZohoCRMFaker"""
import requests

from authentication import get_access_token
from config import config
from fakers import FakeCustomer


URL = 'https://www.zohoapis.com/crm/v2/Contacts/upsert'


def main():
    """Load fake data into the CRM."""
    access_token = get_access_token(config['Refresh token'])
    fake = FakeCustomer()
    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}
    data = {
        'data': [
            {'Last_Name': fake.last_name,
             'Email': fake.email,
             'Company': 'None',
             'Phone': fake.phone,
             'Address': fake.address,
             'Lead_Status': 'Contacted',
             }
        ]
    }
    response = requests.post(url=URL, headers=headers, json=data)
    reply = response.json()
    print(reply)


if __name__ == '__main__':
    main()
