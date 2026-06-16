from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import json
import os

# Azurite connection string
connect_str = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

container_name = "datasets"
blob_name = "All_Diets.csv"

try:
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create container if it doesn't exist
    try:
        blob_service_client.create_container(container_name)
        print("Container created.")
    except:
        print("Container already exists or could not be created.")

    # Upload CSV to Azurite
    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open("All_Diets.csv", "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print("All_Diets.csv uploaded to Azurite Blob Storage.")

    # Download CSV from Azurite
    downloaded_data = blob_client.download_blob().readall()

    df = pd.read_csv(io.BytesIO(downloaded_data))

    # Calculate averages
    avg_macros = df.groupby("Diet_type")[["Protein(g)", "Carbs(g)", "Fat(g)"]].mean()

    # Create output folder
    os.makedirs("simulated_nosql", exist_ok=True)

    # Save results as JSON
    result = avg_macros.reset_index().to_dict(orient="records")

    with open("simulated_nosql/results.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Data processed successfully from Azurite Blob Storage.")
    print("Results saved to simulated_nosql/results.json")

except Exception as e:
    print("ERROR:")
    print(e)