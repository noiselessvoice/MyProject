import json
import os
import requests

def send_message(token, space_id, message):
    url = f"https://chat.googleapis.com/v1/spaces/{space_id}/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    payload = {
        "text": message
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code

def post_message_to_chat(request):
    request_json = request.get_json()
    if request_json and 'message' in request_json:
        message = request_json['message']
        
        # Set your Google Chat bot token and space ID as environment variables
        token = os.environ.get('CHAT_BOT_TOKEN')
        space_id = os.environ.get('CHAT_SPACE_ID')
        
        if token and space_id:
            status_code = send_message(token, space_id, message)
            return f'Message posted with status code: {status_code}', status_code
        else:
            return 'Error: Google Chat bot token or space ID not provided.', 500
    else:
        return 'Error: No message provided in the request.', 400
