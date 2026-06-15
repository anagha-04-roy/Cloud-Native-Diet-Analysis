from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import json
import os

connect_str = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFeqCnrC4qF7mA==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

container_name = "datasets"
blob_name = "All_Diets.csv"

def process_nutritional_data():
    os.makedirs("simulated_nosql", exist_ok=True)

    try:
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client(container_name)

        try:
            container_client.create_container()
            print("Container created: datasets")
        except Exception:
            print("Container already exists or could not be created.")

        blob_client = container_client.get_blob_client(blob_name)

        with open(blob_name, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print("All_Diets.csv uploaded to Azurite Blob Storage.")

        stream = blob_client.download_blob().readall()
        df = pd.read_csv(io.BytesIO(stream))

        df.fillna(df.mean(numeric_only=True), inplace=True)

        avg_macros = (
            df.groupby("Diet_type")[["Protein(g)", "Carbs(g)", "Fat(g)"]]
            .mean()
            .reset_index()
        )

        result = avg_macros.to_dict(orient="records")

        with open("simulated_nosql/results.json", "w") as f:
            json.dump(result, f, indent=4)

        print("Data processed successfully from Azurite Blob Storage.")
        print("Results saved to simulated_nosql/results.json")

    except Exception as e:
        print("Error:", e)

process_nutritional_data() 
