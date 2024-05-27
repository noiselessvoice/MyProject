from google.cloud import asset_v1

def list_assets_in_folder(folder_id):
    # Initialize the Asset Service client
    client = asset_v1.AssetServiceClient()

    # Construct the full folder name
    parent = f"folders/{folder_id}"

    # Create the request
    request = asset_v1.ListAssetsRequest(
        parent=parent,
        asset_types=[],
        content_type=asset_v1.ContentType.RESOURCE,
    )

    # Fetch and print the asset inventory
    response = client.list_assets(request=request)
    
    # Print the results
    for asset in response:
        print(f"Asset name: {asset.name}")
        print(f"Asset type: {asset.asset_type}")
        print(f"Resource: {asset.resource.data}")
        print("\n")

if __name__ == "__main__":
    # Replace 'your-folder-id' with your actual folder ID
    folder_id = 'your-folder-id'
    list_assets_in_folder(folder_id)
