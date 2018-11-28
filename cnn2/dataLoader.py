# Dataloader
# Loads pictures for use in traning and prediction
# in my neural network.

# TODO - Add routiene to resize the images for the neural network.

# Dependancies
import zipfile
import cv2
import os
import numpy as np
from glob import glob


# Define filepaths
train_data_path = os.path.join(os.path.dirname(__file__), "traning_data\\")

# Load a sequense of images and a sequense of labels.
# These values will corrispond to our label name.

# TODO - aquire cv2 to load these images into
# tensorflow

# This returns a 2D numpy array containing raning images and
# labels. 
# image = [np.array(img), label(i)]
def loadTraningData(label_names[], image_width, image_height):
    traning_data = [,]

    for name in label_names:
        # Create a destination file path.
        path = os.path.join(train_data_path, name + "\\")
        images = glob(path, "*.jpg")
        images += glob(path, "*.png")

        # load the images into the array.
        for image in images:
            image_texture = cv2.imread(image)
            loaded_texture = cv2.resize(image_texture, (image_width, image_height), interpolation=cv2.INTER_CUBIC)
            training_data.append(loaded_texture, name)
    
    
    return traning_data
    
