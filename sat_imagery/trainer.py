import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sat_imagery.data import get_all_images, get_target_training
from PIL import Image
from sat_imagery.preprocessing import PreprocessingImages
import cv2
from google.cloud import storage
import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sat_imagery.architecture import initialize_model
import pdb
from sklearn.preprocessing import FunctionTransformer
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
import pickle

BUCKET_NAME = "sat-imagery-621-best"

#def save_model(reg):
    #joblib.dump(reg, "model.joblib")

class Trainer:

    # GCP Storage
    STORAGE_LOCATION = "models/sat_imagery/model.joblib"

    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.pipeline = None

    def set_pipeline(self):
        #### model pipeline ####
        preprocessed = PreprocessingImages().transform(X=self.X)
        self.pipeline = Pipeline(
            steps=[
                ("preprocessing", PreprocessingImages()),
                ("model", initialize_model(preprocessed)),
            ]
        )
        return self.pipeline

    def fit(self, X, y):
        ###### run the pipeline ######
        
        self.set_pipeline()
        self.pipeline.fit(X, y)

    def save_model(self,reg):

        joblib.dump(reg, "model.joblib")


if "__main__" == __name__:
    pdb.set_trace()
    X = get_all_images()
    y = get_target_training()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    trainer = Trainer(X=X, y=y)
    trainer.set_pipeline()
    train = trainer.fit()
    trainer.save_model(train)
