from google.cloud import logging_v2

def list_log_names(project_id):
    # Initialize the client
    client = logging_v2.LoggingServiceV2Client()

    # Create the parent resource path
    parent = f"projects/{project_id}"

    # Initialize a list to hold log names
    log_names = []

    # Use the client to list log names
    for log_entry in client.list_logs(parent=parent):
        log_names.append(log_entry)

    return log_names

if __name__ == "__main__":
    project_id = "your-project-id"  # Replace with your GCP project ID
    log_names = list_log_names(project_id)
    
    # Print the log names
    print("Log names in project {}:".format(project_id))
    for log_name in log_names:
        print(log_name)
