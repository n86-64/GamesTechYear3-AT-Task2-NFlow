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
# Todo - add routiene to customise batch size.
label_names = sys.argv[1]

class_names = open(label_names).readlines()
class_names = [x.strip('\n') for x in class_names]
class_names_length = len(class_names)

def createOptimiser():
    return tf.keras.optimizers.Adam(lr=1e-4)

def createClassifier(image_width, image_height, channels, batch_c):
    input_shape = (image_width, image_height, channels)
    model_input = tf.keras.layers.Input(shape=input_shape, batch_size=batch_c)

    # Defines the elements of the model.
    network = tf.keras.layers.Conv2D(filters=32, kernel_size=5, strides=1, padding='same', activation='relu')(model_input)
    network = tf.keras.layers.MaxPool2D(pool_size=5, padding='same')(network)

    network = tf.keras.layers.Conv2D(filters=64, kernel_size=5, strides=1, padding='same', activation='relu')(network)
    network = tf.keras.layers.MaxPool2D(pool_size=2, padding='same')(network)

    network = tf.keras.layers.Dropout(0.25)(network)
    network = tf.keras.layers.Flatten()(network)
    
    network = tf.keras.layers.Dense(128, activation='relu')(network)
    network = tf.keras.layers.Dropout(0.5)(network)

    network = tf.keras.layers.Dense(class_names_length, activation='softmax')(network)
    
    model = tf.keras.Model(inputs=model_input, outputs=network)

   # model.Summery()
    return model

def main():
    # print(class_names)
    print("Tensorflow: " + tf.VERSION)
    training_data, training_labels = dl.loadTraningData(label_names=class_names, image_width=50, image_height=50)

    # create the neural netowrking model and optimiser.
    cnn = createClassifier(image_width=50, image_height=50, channels=3, batch_c=5)
    optimiser = createOptimiser()

    #print(training_data.shape)
    training_labels_categories = tf.keras.utils.to_categorical(training_labels, class_names_length)
    
    # Compile the model and train.
    cnn.compile(optimiser, loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
    cnn.fit(training_data, training_labels, epochs=5)
    
    
    return


if __name__=="__main__":
    main()
