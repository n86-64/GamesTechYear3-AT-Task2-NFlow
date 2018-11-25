# CNN.py
# A CNN for performing classification of images.
# Reworked to allow for importing of test data.

# Dependancies
import tensorflow as tf
import numpy as np
import sys

label_names = sys.argv[1]

# Classification categories (Retrieve the probabilities of each.)
# Used to create the tensor we will be using.
# Load the labels in from a file.
class_names = open(label_names).readlines()
class_names = [x.strip('\n') for x in class_names]
class_names_length = len(class_names)

traning_filepath = "training_data"

# Represents the tensorflow session.
handle = tf.Session()

# global values
bias = 0.05

# Create a set of random weight values.
def createWeights(shape):
    return tf.Variable(tf.truncated_normal(shape, stddev=0.05))

# Creates a bias value which is added to the objects.
def createBias(size):
    return tf.Variable(tf.constant(bias, shape=[size]))

# Create a convolutional layer
def createConv2DLayer(input, inputChannelCount, filterSize, filterCount):

    # Defines the weights for the filters and 
    weights = createWeights(shape=[filterSize, filterSize, inputChannelCount, filterCount])
    bias = createBias(filterCount)

    layer = tf.nn.conv2D(input=input, filter=weights, strides=[1, 1, 1, 1], padding='SAME')
    layer += bias

    layer = tf.nn.max_pool(value=layer, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
    return layer

# Create a fully connected layer.
def createConnectedLayer(input, numInputs, numOutputs):

    weights = createWeights(shape=[numInputs, numOutputs])
    bias = createBias(num_outputs)

    layer = tf.nn.relu_layer(input)
    
    return layer

def main():
    # TODO - Load the test data in form an image loading library.
    # TODO - Add some code to define the network.

    

    print("Hello world")

if __name__=="__main__":
    main()
