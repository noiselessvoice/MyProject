from google.cloud import bigquery
import pandas as pd

def upload_csv_to_bigquery(csv_file_path, project_id, dataset_id, table_id):
    """
    Uploads CSV data to a Google BigQuery table.

    Args:
        csv_file_path (str): Local path to the CSV file.
        project_id (str): Google Cloud project ID.
        dataset_id (str): BigQuery dataset ID.
        table_id (str): BigQuery table ID.
    """
    # Initialize the BigQuery client
    client = bigquery.Client(project=project_id)

    # Full table ID in the format `project.dataset.table`
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Configure the job settings
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,  # Append to table
        source_format=bigquery.SourceFormat.CSV,  # Specify the source format
        autodetect=True,  # Let BigQuery infer the schema
    )

    # Load the DataFrame into BigQuery
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)

    # Wait for the job to complete
    job.result()

    # Fetch and display table info
    table = client.get_table(table_ref)
    print(f"Uploaded {len(df)} rows to {table.project}.{table.dataset_id}.{table.table_id}")

# Example usage
csv_path = "your_data.csv"
project = "your-project-id"
dataset = "your-dataset-id"
table = "your-table-id"

upload_csv_to_bigquery(csv_path, project, dataset, table)
