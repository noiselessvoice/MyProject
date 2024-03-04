import os
import json
from google.cloud import bigquery
import requests

# Define your key and token
key = "YOUR_GCHAT_KEY"
token = "YOUR_GCHAT_TOKEN"

def post_message_to_chat(space_id, message):
    url = f"https://chat.googleapis.com/v1/spaces/{space_id}/messages?key={key}&token={token}"
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    payload = {
        "text": message
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code

def process_json(request):
    # Check if request contains a JSON payload
    request_json = request.get_json(silent=True)
    if request_json:
        # Assuming request_json contains the JSON payload
        json_data = request_json
        
        # Define required fields
        required_fields = ['name', 'age', 'email']
        
        # Check if all required fields are present
        if not all(field in json_data for field in required_fields):
            return 'Error: Missing required fields.', 400

        # Validate data types and constraints for specific fields
        try:
            name = str(json_data['name'])
            age = int(json_data['age'])
            if age < 0:
                return 'Error: Age must be a non-negative integer.', 400

            email = str(json_data['email'])
            # You can add additional validation for the 'email' field if needed

        except (ValueError, KeyError) as e:
            return f'Error: Invalid data - {str(e)}', 400

        # Extracting only the required fields
        filtered_data = {'name': name, 'age': age, 'email': email}

        # Print the received JSON data
        print('Received JSON data:', filtered_data)
        
        # Insert filtered JSON data into BigQuery
        try:
            client = bigquery.Client()
            dataset_id = 'sample_dataset'
            table_id = 'sample_table'
            table_ref = client.dataset(dataset_id).table(table_id)
            table = client.get_table(table_ref)
            
            rows_to_insert = [filtered_data]
            errors = client.insert_rows(table, rows_to_insert)
            
            if errors:
                print('Error inserting rows:', errors)
                return 'Error: Failed to update BigQuery.', 500
            else:
                # Post message to Google Chat
                space_id = "YOUR_GCHAT_SPACE_ID"
                message = f"New record added: {json.dumps(filtered_data)}"
                status_code = post_message_to_chat(space_id, message)
                
                if status_code == 200:
                    return 'JSON payload received and updated in BigQuery. Message posted to Google Chat.', 200
                else:
                    return 'Error: Failed to post message to Google Chat.', 500
        except Exception as e:
            print('Error:', e)
            return 'Error: Failed to update BigQuery.', 500
    else:
        # Sending error response if no JSON payload found
        return 'Error: No JSON payload found in the request.', 400
