# CNN-Prediction.py
# Loads the trained neural network model and outputs information
# Output in the form of stdout


# Dependancies.
import tensorflow as tf
import dataLoader
import sys


# Pass through two arguements via the command line. 
model_name = sys.argv[1]
image_to_test = sysy.argv[2]

def main():
    # Load the compiled model
    model = tf.keras.load_model(model_name)
    image = loadPredictionImage(image_to_test)

    # Predict the image result.
    prediction_int = model.predict([image])
    print(prediction_int)

    return



if __name__=="__main__":
    main()
