from google.cloud import storage, bigquery
from google.oauth2 import service_account
import pandas as pd

# Set up credentials (you can also use ADC - Application Default Credentials)
credentials = service_account.Credentials.from_service_account_file('path/to/your-service-account-file.json')

# Initialize Google Cloud Storage client
storage_client = storage.Client(credentials=credentials)

# Initialize BigQuery client
bigquery_client = bigquery.Client(credentials=credentials)

# Function to download the CSV file from Google Cloud Storage
def download_csv_from_gcs(bucket_name, source_blob_name, destination_file_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f'CSV file {source_blob_name} downloaded to {destination_file_name}.')

# Function to upload the CSV to BigQuery
def upload_csv_to_bigquery(dataset_id, table_id, source_file_name):
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True,
    )

    with open(source_file_name, 'rb') as source_file:
        job = bigquery_client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Waits for the job to complete
    print(f'CSV file {source_file_name} uploaded to {table_id} in BigQuery.')

# Define your variables
bucket_name = 'your-bucket-name'
source_blob_name = 'path/to/your-file.csv'
destination_file_name = 'local-file.csv'
dataset_id = 'your_dataset_id'
table_id = 'your_table_id'

# Download CSV from GCS
download_csv_from_gcs(bucket_name, source_blob_name, destination_file_name)

# Upload CSV to BigQuery
upload_csv_to_bigquery(dataset_id, table_id, destination_file_name)
