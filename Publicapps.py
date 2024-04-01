import requests

def pull_data_from_prisma(request):
    # Prisma endpoint URL
    prisma_url = "YOUR_PRISMA_ENDPOINT_URL"

    # RQL query to pull data
    rql_query = "YOUR_RQL_QUERY_HERE"

    # Headers for authentication if required
    headers = {
        "Authorization": "Bearer YOUR_AUTH_TOKEN",
        "Content-Type": "application/json"
    }

    # Sending request to Prisma
    response = requests.post(prisma_url, json={"query": rql_query}, headers=headers)

    # Checking if request was successful
    if response.status_code == 200:
        data = response.json()
        return {"status": "success", "data": data}
    else:
        return {"status": "error", "message": "Failed to retrieve data from Prisma."}
