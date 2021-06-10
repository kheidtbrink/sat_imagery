import streamlit as st
import requests
import numpy as np
from PIL import Image
import cv2


st.title('Image Classifier')
st.text("Provide Url of Img for image classification")


path = st.text_input('Enter Image URL to Classify...', 'http://google.be')
if path is not None:
    content = requests.get(path).content 