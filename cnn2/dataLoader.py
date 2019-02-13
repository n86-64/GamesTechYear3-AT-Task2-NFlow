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
train_data_path = os.path.join(os.path.dirname(__file__), "training_data\\")
test_data_path = os.path.join(os.path.dirname(__file__), "testing_data\\")

# Load a sequense of images and a sequense of labels.
# These values will corrispond to our label name.

# TODO - aquire cv2 to load these images into
# tensorflow

# This returns a 2D numpy array containing raning images and
# labels. 
# image = [np.array(img), label(i)]
def loadTraningData(label_names, image_width, image_height):
    label_id = 0
    training_data = []
    training_labels = []

    for name in label_names:
        # Create a destination file path.
        path = os.path.join(train_data_path, name + "\\")
        images = glob(os.path.join(path, "*.jpg"))
        images = glob(os.path.join(path, "*.jpeg"))
        images = glob(os.path.join(path, "*.JPG"))
        images = glob(os.path.join(path, "*.JPEG"))
        images += glob(os.path.join(path, "*.png"))
        images += glob(os.path.join(path, "*.PNG"))

        # load the images into the array.
        for image in images:
            image_texture = cv2.imread(image)
            loaded_texture = cv2.resize(image_texture, (image_width, image_height), interpolation=cv2.INTER_CUBIC)
            training_data.append(loaded_texture)
            training_labels.append(label_id)

        label_id += 1

    training_data   = np.array(training_data)
    training_labels = np.array(training_labels)
    
    return training_data, training_labels

# Load a set of data to test the network we have created. 
def loadTestingData(label_names, image_width, image_height):
    label_id = 0
    training_data = []
    training_labels = []

    for name in label_names:
        # Create a destination file path.
        path = os.path.join(test_data_path, name + "\\")
        images = glob(os.path.join(path, "*.jpg"))
        images = glob(os.path.join(path, "*.jpeg"))
        images = glob(os.path.join(path, "*.JPG"))
        images = glob(os.path.join(path, "*.JPEG"))
        images += glob(os.path.join(path, "*.png"))
        images += glob(os.path.join(path, "*.PNG"))

        # load the images into the array.
        for image in images:
            image_texture = cv2.imread(image)
            loaded_texture = cv2.resize(image_texture, (image_width, image_height), interpolation=cv2.INTER_CUBIC)
            training_data.append(loaded_texture)
            training_labels.append(label_id)

        label_id += 1

    training_data   = np.array(training_data)
    training_labels = np.array(training_labels)
    
    return training_data, training_labels


# Loads an image for use in prediction.
def loadPredictionImage(image_path, image_width, image_height):

    data = []
    
    # Here we set the root path for the images.
    image = cv2.imread(image_path)
    image_texture = cv2.resize(image, (image_width, image_height), interpolation=cv2.INTER_CUBIC)
    
    data = np.array(image_texture)

    data.resize(1, image_width, image_height, 3)
    
    # returns the image.
    return data
    
