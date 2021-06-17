import pandas as pd
import cv2
from sat_imagery.data import get_all_images
import numpy as np
from sklearn.base import TransformerMixin
from sklearn.base import BaseEstimator


class PreprocessingImages(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None):
        return self

    def transform(self, X, scale_percent=50):
        # content of standardizing + resizing data goes here

        image_array_shape = []
        for i in X:  ########### getting the shape of every images from the training set
            image_array_shape.append(i.shape)
        df_shape = pd.DataFrame(image_array_shape)
        x_min = df_shape[0].min()
        y_min = df_shape[1].min()
        reshape_image = []
        for image in X:  ######### reshaping to lowest height, width from the dataset
            reshape_image.append(image[:x_min, :y_min])

        ####Setting up and sizing the dimensions#####
        img_shape = reshape_image[0].shape
        scale_percent = scale_percent  # percent of original size
        width = int(img_shape[1] * scale_percent / 100)
        height = int(img_shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize each image in a list
        transformed_images = []
        for ind_i in reshape_image:
            transformed_images.append(
                cv2.resize(ind_i, dim, interpolation=cv2.INTER_AREA)
            )

        transformed_images = np.asarray(transformed_images)
        return transformed_images
