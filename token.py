import requests

def generate_jwt_token(api_key, api_secret):
    try:
        auth_endpoint = 'https://api.prismacloud.io/login'
        payload = {
            'username': api_key,
            'password': api_secret
        }
        response = requests.post(auth_endpoint, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        return response.json().get('token')
    except requests.exceptions.RequestException as e:
        print(f"Error generating JWT token: {e}")
        return None

# Example usage
api_key = 'your_api_key'
api_secret = 'your_api_secret'
jwt_token = generate_jwt_token(api_key, api_secret)

if jwt_token:
    print("JWT Token:")
    print(jwt_token)
else:
    print("Failed to generate JWT token.")
