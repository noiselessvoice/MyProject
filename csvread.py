from google.cloud import storage, bigquery
import pandas as pd

# Initialize the Google Cloud Storage client
storage_client = storage.Client()

# Initialize the BigQuery client
bigquery_client = bigquery.Client()

def read_csv_from_gcs(bucket_name, file_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_string()
    df = pd.read_csv(pd.compat.StringIO(content.decode('utf-8')))
    return df

def load_df_to_bigquery(df, table_id):
    job = bigquery_client.load_table_from_dataframe(df, table_id)
    job.result()  # Wait for the job to complete.
    print(f"Loaded {job.output_rows} rows into {table_id}.")

# Example usage
bucket_name = 'your-bucket-name'
file_name = 'path/to/your/file.csv'
table_id = 'your-project.your_dataset.your_table'

# Read CSV from Cloud Storage
df = read_csv_from_gcs(bucket_name, file_name)

# Load DataFrame into BigQuery
load_df_to_bigquery(df, table_id)

