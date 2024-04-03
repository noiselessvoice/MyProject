import requests
import json

def generate_bearer_token(access_key, secret_key):
    try:
        auth_endpoint = 'https://api.prismacloud.io/login'
        payload = {
            'username': access_key,
            'password': secret_key
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(auth_endpoint, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        return response.json().get('token')
    except requests.exceptions.RequestException as e:
        print(f"Error generating bearer token: {e}")
        return None

# Example usage
access_key = 'your_access_key'
secret_key = 'your_secret_key'
bearer_token = generate_bearer_token(access_key, secret_key)

if bearer_token:
    print("Bearer Token:")
    print(bearer_token)
else:
    print("Failed to generate bearer token.")
