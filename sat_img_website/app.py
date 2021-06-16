import streamlit as st
import requests
import numpy as np
from PIL import Image, ImageOps
import cv2
import joblib


#titles
st.title("Image Classification - Batch621 -  Brussel")
st.header("Sattelite image Classification")
st.text("Upload a sattelite Image for image classification")

####################################################################
#classification #####this piece of code could be used as an import####

def classification(img, model):
    #load the model
    model = joblib.load('#.pkl ou .joblib ?')

#Create the array of the right shape  1672 * 1667
data = np.ndarray(shape=(1, 1672, 1667, 3), dtype=np.float32)
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
#run the prediction
prediction = model.predict(data)
###################################################################


uploaded_file = st.file_uploader("Choose a sattelite image ...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Sat.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = classification(image, '###modelname .pkl .joblib')
    if label == 0:
        st.write("----")
    else:
        st.write("---")


