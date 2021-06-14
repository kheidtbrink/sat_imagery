from google import storage
from PIL import Image
import numpy as np
import pandas as pd
import os

BUCKET_TRAIN_PATH = 'raw_data/train_geojson_v3'

#Get the training images

def get_training():

    dirname = '/sat_imagery/raw_data/Satellite/three_band/'  #temp might be changed later (increase number of images)
    training_images = []   # list which will contain array of individual training images
    # iterate through the file directory
    for fname in os.listdir(dirname):
        im = Image.open(os.path.join(dirname, fname))
        imarray = np.array(im)
        training_images.append(imarray)
    return training_images

def get_target_training():
    
    file = 'sat_imagery/raw_data/Satellite/train_geojson_v3/'

    for name in os.listdir(file):
        files = os.walk(file)
        geojson_files = [f[0] for f in os.walk(file)]
    
    geojson_per_image = {}
    geojson_folders = os.listdir(geojson_files[0])
    for i in geojson_folders:
        fichiers = os.listdir(geojson_files[0]+ f"/{i}")
        geojson_per_image[i] = int(any('008' in s for s in fichiers)) #target water 008
        #geojson_per_image[i] = int(any('005' in s for s in fichiers)) #target vegetation 
    df_target = pd.DataFrame.from_dict(geojson_per_image, orient='index')
    y = df_target
    
    return y