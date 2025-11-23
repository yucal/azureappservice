from azure.storage.blob import BlobClient
import json
def fetch_restaurant_data():
    sas_url = "https://beerapistorage.blob.core.windows.net/beerapi-container/data.json?sp=r&st=2025-11-23T21:22:18Z&se=2025-11-24T05:37:18Z&spr=https&sv=2024-11-04&sr=b&sig=ccNl83fow3AeBOYhki1c1TtM85Esv%2FBAhjGrpbigN2k%3D"

    # Create a BlobClient directly from the SAS URL
    blob = BlobClient.from_blob_url(sas_url)

    # Download file bytes
    file_bytes = blob.download_blob().readall()

    json_data = json.loads(file_bytes)
    return (json_data.get("restaurants"))
