import requests

def get_rql_config_query_result(bearer_token, rql_query):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }

    try:
        rql_endpoint = 'https://api.prismacloud.io/search'
        payload = {
            'search_type': 'config',
            'query': rql_query
        }
        response = requests.post(rql_endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving RQL config query result: {e}")
        return None

# Example usage
bearer_token = 'your_bearer_token'
rql_query = 'config where cloud.type = "aws" limit 10'
result = get_rql_config_query_result(bearer_token, rql_query)

if result:
    print("RQL Config Query Result:")
    print(result)
else:
    print("Failed to retrieve RQL config query result.")
