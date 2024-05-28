from google.cloud import asset_v1
from google.protobuf.json_format import MessageToDict

def list_project_assets(project_id):
    client = asset_v1.AssetServiceClient()

    # Project resource format
    project_resource = f"projects/{project_id}"

    # Create a request
    request = asset_v1.ListAssetsRequest(
        parent=project_resource,
        asset_types=[],
        content_type=asset_v1.ContentType.RESOURCE,
    )

    # List assets
    response = client.list_assets(request=request)

    assets = []
    for asset in response:
        # Convert the resource data to a dictionary
        resource_data = MessageToDict(asset.resource.data)

        asset_details = {
            'name': asset.name,
            'asset_type': asset.asset_type,
            'created': resource_data.get('createTime'),
            'status': resource_data.get('state', 'Unknown')  # Example for status, adjust based on your resource schema
        }
        assets.append(asset_details)
    
    return assets

if __name__ == "__main__":
    project_id = "your-project-id"  # Replace with your project ID
    assets = list_project_assets(project_id)
    
    for asset in assets:
        print(f"Asset Name: {asset['name']}")
        print(f"Asset Type: {asset['asset_type']}")
        print(f"Created: {asset['created']}")
        print(f"Status: {asset['status']}")
        print("\n")
