# EmailPuller.PY

EmailPuller.py
EmailPuller.py is a Python script that retrieves email addresses for a list of users by querying Microsoft Graph API using Azure AD application credentials. It supports lookup by either display name or user principal name (UPN).

Features
Authenticates with Microsoft Graph via Azure AD (client credentials flow).

Accepts user identifiers (display names or UPNs).

Returns the user's email address or UPN if not found in the mail attribute.

Provides simple and readable output for each lookup.

Prerequisites
Python 3.6+

An Azure AD app registration with:

Client ID

Client Secret

Tenant ID

API permissions for User.Read.All (application type) granted and admin consented.

Installation
Clone the repository or copy the script.

Install dependencies:

bash
Copy
Edit
pip install msal requests
Update the script with your Azure AD credentials:

python
Copy
Edit
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
TENANT_ID = 'your-tenant-id'
Usage
Modify the user_identifiers list with the display names or UPNs you wish to query:

python
Copy
Edit
user_identifiers = [
    'john.doe@yourdomain.com',
    'Jane Smith',
    'alex.jones@yourdomain.com'
]
Run the script:

bash
Copy
Edit
python EmailPuller.py
Example output:

graphql
Copy
Edit
john.doe@yourdomain.com -> john.doe@yourdomain.com
Jane Smith -> jane.smith@yourdomain.com
alex.jones@yourdomain.com -> alex.jones@yourdomain.com
Notes
If the mail attribute is empty, the script falls back to returning userPrincipalName.

If the user is not found, a "User not found" message is returned.
