from google.cloud import bigquery

def read_rows(project_id, dataset_id, table_id, start_row, end_row):
    client = bigquery.Client(project=project_id)
    
    # Calculate the number of rows to fetch
    limit = end_row - start_row + 1
    offset = start_row - 1
    
    query = f"""
        SELECT *
        FROM `{project_id}.{dataset_id}.{table_id}`
        LIMIT {limit}
        OFFSET {offset}
    """
    
    query_job = client.query(query)  # Make an API request.
    
    results = query_job.result()  # Wait for the job to complete.
    
    rows = []
    for row in results:
        rows.append(dict(row))
    
    return rows

if __name__ == "__main__":
    project_id = 'your_project_id'  # Replace with your project ID
    dataset_id = 'your_dataset_id'  # Replace with your dataset ID
    table_id = 'your_table_id'      # Replace with your table ID
    start_row = 100  # Start reading from this row
    end_row = 300    # Read until this row

    rows = read_rows(project_id, dataset_id, table_id, start_row, end_row)
    
    for row in rows:
        print(row)
