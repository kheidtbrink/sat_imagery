import pandas as pd
import numpy as np
import tifffile as tif
import matplotlib.pyplot as plt
import os, gc, glob
from sat_imagery.data import get_training
from PIL import Image
from tensorflow.keras import layers
from tensorflow.keras import Sequential
import cv2
from google import storage
import joblib
from sklearn.pipeline import Pipeline


#GCP Storage
########STORAGE_LOCATION = 'models/simpletaxifare/model.joblib'
BUCKET_NAME = 'wagon-data-621-wang'

#Image reshaping & Image resizing

def reshaping():
    data = get_training()
    array_shape = []
    for i in data:
        array_shape.append(i.shape)
    df_shape = pd.DataFrame(array_shape)
    
    x_min = df_shape[0].min()
    y_min = df_shape[1].min()
    
    reshape_image = []
    for image in final:
        reshape_image.append(image[:x_min,:y_min])
        
    return reshape_image

#Image resizing

def resize_images(scale_percent, path):
    
    scale_percent = scale_percent # percent of original size
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized_image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized_image.shape)
    return resized_image

def save_model(reg):
    """method that saves the model into a .joblib file and uploads it on Google Storage /models folder
    HINTS : use joblib library and google-cloud-storage"""
    # saving the trained model to disk is mandatory to then beeing able to upload it to storage
    # Implement here
    joblib.dump(reg, 'model.joblib')
    print("saved model.joblib locally")

    # Implement here
    upload_model_to_gcp()
    print(f"uploaded model.joblib to gcp cloud storage under \n => {STORAGE_LOCATION}")

def initialize_model(): 
    pass

def model_pipeline():
    pipeline = Pipeline([
        'preprocessing': preprocessor(),
        'model':model.joblib
    ])
    return pipeline

def upload_model_to_gcp():

    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob(STORAGE_LOCATION)

    blob.upload_from_filename('model.joblib')
    
    
if '__main__' == '__name__':
    upload_model_to_gcp()