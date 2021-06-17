from PIL import Image
import numpy as np
import pandas as pd
import os
import pdb

BUCKET_TRAIN_PATH = "raw_data/train_geojson_v3"

# Get the training images


def get_all_images(n=10):

    dirname = "sat_imagery/raw_data/Satellite/three_band/"
    training_images = []  # list which will contain array of individual training images

    ##### iterate through the file directory ######

    i = 0
    for image in os.listdir(dirname):
        if n == i:
            break
        im = Image.open(os.path.join(dirname, image))
        imarray = np.array(im)
        training_images.append(imarray)
        i += 1

    return training_images


def get_target_training():
    file = "sat_imagery/raw_data/target_database.csv"

    df_target = pd.read_csv(file)
    df_target = df_target.set_index("ImageID")
    df_target = df_target.dropna(axis=1)
    df_target = df_target.head(10)
    y = np.asarray(df_target).astype(np.float)

    return y


if "__main__" == __name__:
    y = get_target_training()
