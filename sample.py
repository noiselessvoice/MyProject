import json

def process_json(request):
    # Check if request contains a JSON payload
    request_json = request.get_json(silent=True)
    if request_json:
        # Assuming request_json contains the JSON payload
        json_data = request_json
        
        # Print the received JSON data
        print('Received JSON data:', json_data)
        
        # Sending a response
        return 'JSON payload received and processed successfully.', 200
    else:
        # Sending error response if no JSON payload found
        return 'Error: No JSON payload found in the request.', 400
