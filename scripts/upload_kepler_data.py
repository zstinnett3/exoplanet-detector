import os
import boto3
import requests
from pathlib import Path

# ---- Configuration ----
DATA_URL = "https://storage.googleapis.com/kepler_data/kepler_ffi_data.zip"  # example source
LOCAL_FILENAME = "kepler_data.zip"
S3_BUCKET = "exoplanet-detection-data"           # Replace with your actual bucket
S3_KEY = "datasets/kepler_data.zip"      # S3 path

# ---- Download data ----
def download_data():
    if not os.path.exists(LOCAL_FILENAME):
        print(f"Downloading {LOCAL_FILENAME}...")
        response = requests.get(DATA_URL, stream=True)
        with open(LOCAL_FILENAME, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Download complete.")
    else:
        print("File already downloaded.")

# ---- Upload to S3 ----
def upload_to_s3():
    s3 = boto3.client("s3")
    print(f"Uploading {LOCAL_FILENAME} to s3://{S3_BUCKET}/{S3_KEY}")
    s3.upload_file(LOCAL_FILENAME, S3_BUCKET, S3_KEY)
    print("Upload complete.")

# ---- Run Steps ----
if __name__ == "__main__":
    download_data()
    upload_to_s3()