# tf.Keras based tensorflow graph.
# Nathan Butt
# Script takes labels and images as input.
# Neural network is then compiled and outputted.
# Allows for some customisation.

# Dependancies
import sys
import dataLoader as dl
import tensorflow as tf
import numpy as np

# code to import labels.
label_names = sys.argv[1]

class_names = open(label_names).readlines()
class_names = [x.strip('\n') for x in class_names]
class_names_length = len(class_names)

def createOptimiser():
    return tf.keras.optimizers.Adam(lr=1e-4)

def createClassifier(image_width, image_height, channels, batch_c):
    input_shape = [image_width, image_height, channels]
    model_input = tf.keras.layers.Input(shape=input_shape, batch_size=batch_c)

    # Defines the elements of the model.
    network = tf.keras.layers.Conv2D(filters=32, kernel_size=5, strides=1, padding='same', activation='relu')(model_input)
    network = tf.keras.layers.MaxPool2D(pool_size=5, padding='same')(network)

    network = tf.keras.layers.Conv2D(filters=64, kernel_size=5, strides=1, padding='same', activation='relu')(network)
    network = tf.keras.layers.MaxPool2D(pool_size=5, padding='same')(network)

    network = tf.keras.layers.Dropout(0.25)(network)
    network = tf.keras.layers.Flatten()(network)
    
    model = tf.keras.Model(inputs=model_input, outputs=network)
    
    return model

def main():
    print("Tensorflow: " + tf.VERSION)
    train_data = dl.loadTraningData(label_name="test.txt")
    print(train_data)
    
   # cnn = createClassifier(image_width=50, image_height=50, channels=3, batch_c=5)
  #  optimiser = createOptimiser()

    
    return


if __name__=="__main__":
    main()
