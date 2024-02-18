import json
from google.cloud import bigquery

def process_json(request):
    # Check if request contains a JSON payload
    request_json = request.get_json(silent=True)
    if request_json:
        # Assuming request_json contains the JSON payload
        json_data = request_json
        
        # Extracting only the required fields (age, name, and email)
        filtered_data = {key: json_data[key] for key in ['age', 'name', 'email'] if key in json_data}
        
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
