# Game generation CNN. For use in providing data to unity.
# Nathan Butt
# Student No - 16013327
# Initialy will use the mnist dataset.


# Dependancies.
import tensorflow as tf
import numpy as np

tf.logging.set_verbosity(tf.logging.INFO)

# Output labels (used for prediction)


# Generates the CNN used in this example.
# Provide - feature values, output labels and the traning mode
# return - model which can then be trained.

# Functions must be created this way as this is used to create the learning model.
def cnn_network_fn(features, labels, mode):
    print("Creating the neural network defintions.")

    # input to our model. Defines a tensor which is a set of input node values.
    input_layer = tf.reshape(features["x"], [-1, 28, 28, 1])

    # Convolutional layer 1 - use a 5x5 filter/kernel for training.
    # outputs to 32 nodes.
    layer_conv_1 = tf.layers.conv2d(inputs=input_layer, filters=32, kernel_size=[5, 5], padding="same", activation=tf.nn.relu)
    layer_pool_1 = tf.layers.max_pooling2d(inputs=layer_conv_1, pool_size=[2, 2], strides=2)

    layer_conv_2 = tf.layers.conv2d(inputs=layer_pool_1, filters=64, kernel_size=[5, 5], padding="same", activation=tf.nn.relu)
    layer_pool_2 = tf.layers.max_pooling2d(inputs=layer_conv_2, pool_size=[2, 2], strides=2)

    # flatten the input for second layer.
    layer_pool_1_flat = tf.reshape(layer_pool_2, [-1, 7 * 7 * 64])
    dense = tf.layers.dense(inputs=layer_pool_1_flat, units=1024, activation=tf.nn.relu)
    
    # Add dropout operation; 0.6 probability that element will be kept
    dropout = tf.layers.dropout(
    inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    
    # the network output layer.
    logits = tf.layers.dense(inputs=dropout, units=10)

    # Code from tensorflow
    # generates preditctions as well as calculates losses.

    predictions = {
          # Generate predictions (for PREDICT and EVAL mode)
          "classes": tf.argmax(input=logits, axis=1),
          # Add `softmax_tensor` to the graph. It is used for PREDICT and by the
          # `logging_hook`.
          "probabilities": tf.nn.softmax(logits, name="softmax_tensor")
      }
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

      # Calculate Loss (for both TRAIN and EVAL modes)
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

      # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

      # Add evaluation metrics (for EVAL mode)
    eval_metric_ops = {
          "accuracy": tf.metrics.accuracy(
              labels=labels, predictions=predictions["classes"])}
    return tf.estimator.EstimatorSpec(
          mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


# tensorflow notes - tf.app.run() looks for main(argv) entry point. Must define one.
def main(unused_argv):
    print("Hello world. How are you today.")
    mnist = tf.contrib.learn.datasets.load_dataset("mnist")

    # Input data and properties for training. 
    train_data = mnist.train.images
    train_labels = np.asarray(mnist.train.labels, dtype=np.int32)

    # Input data for testing of neural network.
    eval_data = mnist.test.images
    eval_labels = np.asarray(mnist.test.labels, dtype=np.int32)

    # Create an estimator which is the object that evaluates our neural networks.
    classifier = tf.estimator.Estimator(model_fn=cnn_network_fn, model_dir="/tmp/mnist_convnet_model")

    # Create handle for input data and then train the model.
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": eval_data},
        y=eval_labels,
        num_epochs=1,
        shuffle=False
        )
    classifier.train(input_fn=train_input_fn,
                     steps=20000)
    

if __name__ == "__main__":
    tf.app.run() # Defines entrypoint for a tensorflow app.

