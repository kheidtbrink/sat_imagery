import os

from google.cloud import storage
from termcolor import colored
import cv2


def storage_upload(rm=False):
    
    BUCKET_NAME= 'sat-imagery-621-best'
    MODEL_NAME = 'satellite_image_classifier'
    MODEL_VERSION = 'v1'
    
    client = storage.Client().bucket(BUCKET_NAME)

    local_model_name = 'model.joblib' #MODEL NOT YET COMPLETELY DONE
    storage_location = f"models/{MODEL_NAME}/{MODEL_VERSION}/{local_model_name}"
    blob = client.blob(storage_location)
    blob.upload_from_filename('model.joblib')
    print(colored(f"=> model.joblib uploaded to bucket {BUCKET_NAME} inside {storage_location}",
                  "green"))
    if rm:
        os.remove('model.joblib')