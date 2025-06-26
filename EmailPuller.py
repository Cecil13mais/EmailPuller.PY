import requests
from msal import ConfidentialClientApplication

# Azure AD app credentials
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
TENANT_ID = 'your-tenant-id'

# List of users (display names or UPNs)
user_identifiers = [
    'john.doe@yourdomain.com',
    'Jane Smith',
    'alex.jones@yourdomain.com'
]

# Authentication with MS Graph
def get_access_token():
    authority = f'https://login.microsoftonline.com/{TENANT_ID}'
    app = ConfidentialClientApplication(
        CLIENT_ID,
        authority=authority,
        client_credential=CLIENT_SECRET
    )

    token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    return token['access_token']

# Search for users and get emails
def get_user_email(access_token, identifier):
    url = f"https://graph.microsoft.com/v1.0/users?$filter=startswith(displayName,'{identifier}') or userPrincipalName eq '{identifier}'"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        users = response.json().get('value', [])
        if users:
            return users[0].get('mail') or users[0].get('userPrincipalName')
        else:
            return f"User not found: {identifier}"
    else:
        return f"Error: {response.status_code} - {response.text}"

# Main
def main():
    token = get_access_token()
    for user in user_identifiers:
        email = get_user_email(token, user)
        print(f"{user} -> {email}")

if __name__ == "__main__":
    main()
