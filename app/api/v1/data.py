from azure.storage.blob import BlobClient
import json,logging
def fetch_restaurant_data():
    sas_url = "https://beerapistorage.blob.core.windows.net/beerapi-container/data.json?sp=r&st=2025-11-24T09:12:12Z&se=2025-11-24T17:27:12Z&spr=https&sv=2024-11-04&sr=b&sig=bXJ5sVrvsZIcMYjYBf2EvSZ%2F9%2FhLbf2IDurXZt3yqsg%3D"
    logging.info("Starting to download blob from SAS URL.")
    # Create a BlobClient directly from the SAS URL
    blob = BlobClient.from_blob_url(sas_url)

    # Download file bytes
    file_bytes = blob.download_blob().readall()
    logging.info("Blob downloaded successfully.")
    json_data = json.loads(file_bytes)
    
    return (json_data.get("restaurants"))
