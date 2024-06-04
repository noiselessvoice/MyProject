kfrom google.cloud import asset_v1

def list_compute_instances_at_folder(folder_id):
    # Initialize the client
    client = asset_v1.AssetServiceClient()

    # The folder resource for which the assets are to be listed
    folder_resource = f"folders/{folder_id}"

    # Set the content type to RESOURCE to get resource metadata
    content_type = asset_v1.ContentType.RESOURCE

    # Create the request
    request = asset_v1.ListAssetsRequest(
        parent=folder_resource,
        content_type=content_type,
        asset_types=["compute.googleapis.com/Instance"]
    )

    # Make the request and handle the response
    response = client.list_assets(request=request)

    for asset in response:
        print(asset)

if __name__ == "__main__":
    folder_id = "your-folder-id"
    list_compute_instances_at_folder(folder_id)
