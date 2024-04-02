import subprocess

def execute_curl_command(curl_command):
    try:
        result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error executing curl command: {result.stderr}")
            return None
    except Exception as e:
        print(f"Error executing curl command: {e}")
        return None

# Example usage
curl_command = 'curl -X GET "https://api.example.com/resource" -H "Authorization: Bearer your_token"'
response = execute_curl_command(curl_command)

if response:
    print("Curl Response:")
    print(response)
else:
    print("Failed to execute curl command.")
