Upload randomly generated information to Zoho for integration tests.

Example configuration: Create a fake user and subscription in Zoho Billing demo environment.

Usage: Create file `.env` and set the following environment variables:
```
ZOHO_CLIENT_ID=
ZOHO_CLIENT_SECRET=
ZOHO_REFRESH_TOKEN=
```

`ZOHO_ACCESS_TOKEN` will be added to `.env` automatically.

Simply click the run button in VSCode or press F5. The test subscription will be created in Billing.
