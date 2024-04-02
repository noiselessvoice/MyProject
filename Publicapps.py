import requests
from flask import jsonify

def main(request):
    url = "https://api.prismacloud.io/search/api/v1/config"

    payload = {
      "skipSearchCreation": True,
      "limit": 0,
      "withResourceJson": True,
      "timeRange": {
        "type": "relative",
        "value": {
          "unit": "minute",
          "amount": 0
        }
      },
      "skipResult": True,
      "sort": [
        {
          "field": "ID",
          "direction": "asc"
        }
      ],
      "query": "string",
      "nextPageToken": "string"
    }

    headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'Accept': 'application/json; charset=UTF-8',
      'x-redlock-auth': '<API_KEY_VALUE>'
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return f"Error: {response.status_code} - {response.text}", response.status_code
