import requests

def get_bearer_token(username, password):
    # Prisma Cloud authentication endpoint
    auth_endpoint = 'https://app.prismacloud.io/login'

    # Send authentication request
    response = requests.post(auth_endpoint, json={"username": username, "password": password})
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse access token from response
        access_token = response.json().get('access_token')
        return access_token
    else:
        print(f"Failed to authenticate. Status code: {response.status_code}")
        return None

# Example usage
username = 'your_username'
password = 'your_password'
bearer_token = get_bearer_token(username, password)

if bearer_token:
    print(f"Bearer Token: {bearer_token}")
else:
    print("Authentication failed.")
