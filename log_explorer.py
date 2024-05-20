import os
from google.cloud import logging_v2

# Set up your Google Cloud project ID
project_id = 'your-project-id'

# Initialize the logging client
client = logging_v2.Client(project=project_id)

# Define the log name (this should match the name of the log you want to read)
log_name = 'projects/{}/logs/{}'.format(project_id, 'your-log-id')

# Create a filter to specify the log entries you want to read
# For example, to filter logs from the last 24 hours:
import datetime
now = datetime.datetime.utcnow()
yesterday = now - datetime.timedelta(days=1)
filter_str = f'logName="{log_name}" AND timestamp>="{yesterday.isoformat()}Z"'

# Get the logger
logger = client.logger(log_name)

# Use the logging client to query log entries
entries = client.list_entries(
    filter_=filter_str,
    order_by=logging_v2.DESCENDING,
    page_size=10
)

# Print log entries
for entry in entries:
    print(f"Timestamp: {entry.timestamp}, Payload: {entry.payload}")

