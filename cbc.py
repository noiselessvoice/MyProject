himport requests

# Replace these variables with your actual API credentials and URL
API_KEY = 'your_api_key'
ORG_KEY = 'your_org_key'
API_URL = 'https://api.your_cb_cloud.com/investigate/v2/orgs/{}/devices/_search'.format(ORG_KEY)

# Headers for the API request
headers = {
    'X-Auth-Token': API_KEY,
    'Content-Type': 'application/json'
}

# Example payload to search for devices (customize based on your needs)
payload = {
    "query": "hostname:*",
    "rows": 10
}

# Make the API request
response = requests.post(API_URL, headers=headers, json=payload)

# Check for successful response
if response.status_code == 200:
    data = response.json()
    print("Success:", data)
else:
    print("E
