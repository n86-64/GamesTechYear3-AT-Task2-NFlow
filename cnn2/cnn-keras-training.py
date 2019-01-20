# tf.Keras based tensorflow graph.
# Nathan Butt
# Script takes labels and images as input.
# Neural network is then compiled and outputted.
# Allows for some customisation.

# Dependancies
import os
import sys
import dataLoader as dl
import tensorflow as tf
import numpy as np

# Import Arguements for the network.
label_names = sys.argv[1]
epochs = int(sys.argv[2])

buffer_size = 100

class_names = open(label_names).readlines()
class_names = [x.strip('\n') for x in class_names]
class_names_length = len(class_names)

def createOptimiser():
    return tf.keras.optimizers.Adam(lr=0.01)

def createClassifier(image_width, image_height, channels, batch_c):
    input_shape = (image_width, image_height, channels)
    model_input = tf.keras.layers.Input(shape=input_shape)

    # Defines the elements of the model.
    network = tf.keras.layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same', activation='relu')(model_input)
    network = tf.keras.layers.MaxPool2D(pool_size=3, padding='same')(network)

    network = tf.keras.layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same', activation='relu')(network)
    network = tf.keras.layers.MaxPool2D(pool_size=3, padding='same')(network)

    network = tf.keras.layers.Conv2D(filters=64, kernel_size=3, strides=1, padding='same', activation='relu')(network)
    network = tf.keras.layers.MaxPool2D(pool_size=3, padding='same')(network)

    network = tf.keras.layers.Dropout(0.25)(network)
    network = tf.keras.layers.Flatten()(network)
    
    network = tf.keras.layers.Dense(128, activation='relu')(network)
    network = tf.keras.layers.Dropout(0.5)(network)

    network = tf.keras.layers.Flatten()(network)
    network = tf.keras.layers.Dense(class_names_length, activation='sigmoid')(network)
    
    model = tf.keras.Model(inputs=model_input, outputs=network)

   # model.Summery()
    return model

def main():
    print(class_names_length)
    print("Tensorflow: " + tf.VERSION)

    training_data, training_labels = dl.loadTraningData(label_names=class_names, image_width=buffer_size, image_height=buffer_size)
    testing_data, testing_labels = dl.loadTestingData(label_names=class_names, image_width=buffer_size, image_height=buffer_size)

    # TODO - Do we need this.
    #seed = np.arange(training_data.shape[0])
    #np.random.shuffle(seed)
    #training_data = training_data[seed]
    #training_labels = training_labels[seed]

    # create the neural netowrking model and optimiser.
    cnn = createClassifier(image_width=buffer_size, image_height=buffer_size, channels=3, batch_c=5)
    optimiser = createOptimiser()
    
    # Compile the model and train.
    cnn.compile(optimiser, loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
    #cnn.fit(training_data, training_labels, batch_size=20, epochs=epochs, validation_data=(testing_data, testing_labels))
    cnn.fit(training_data, training_labels, batch_size=32, epochs=epochs, validation_split=0.2)

    result = cnn.save("cnn-game.hd5") # Saves the resulting neural network.

 #   model = tf.keras.models.load_model("cnn-game.hd5")

  #  test_image = dl.loadPredictionImage(image_path=os.path.join(os.path.dirname(__file__), "test.png"), image_width=50, image_height=50)
   # result = model.predict(test_image)

   # print(result)

    return


if __name__=="__main__":
    main()
