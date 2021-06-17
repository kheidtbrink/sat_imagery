import streamlit as st
import requests
import numpy as np
from PIL import Image, ImageOps
import cv2
import joblib
import pdb
from tensorflow.keras import Sequential, layers
from tensorflow.keras import optimizers
from tensorflow.keras.layers.experimental.preprocessing import Rescaling


#titles
st.title("Image Classification - Batch621 -  Brussel")
st.header("Sattelite image Classification")
st.text("Upload a sattelite Image for image classification")

####################################################################
#classification #####this piece of code could be used as an import####

def classification(img, model):
    #load the model
    model = joblib.load('model.joblib')
    #Create the array of the right shape  1672 * 1667
    data = np.ndarray(shape=(1, 1667, 1672, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (1672, 1667)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    #turn the image into a numpy array
    image_array = np.asarray(image)
    #nporamlize the image

    normalized_image_array = (image_array.astype(np.float32) / 130.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array
    #import pdb; pdb.set_trace()
    #run the prediction
    prediction = model.predict(data)
###################################################################


uploaded_file = st.file_uploader("Choose a sattelite image ...", type="tif")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Sat.', use_column_width=True)
    st.write("")
    st.write("Detecting...")
    label = classification(image, 'model.joblib')
    if label == 0:
        st.write("----")
    else:
        st.write("---")
