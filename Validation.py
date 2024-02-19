import json
from google.cloud import bigquery

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
                return 'JSON payload received and updated in BigQuery successfully.', 200
        except Exception as e:
            print('Error:', e)
            return 'Error: Failed to update BigQuery.', 500
    else:
        # Sending error response if no JSON payload found
        return 'Error: No JSON payload found in the request.', 400
