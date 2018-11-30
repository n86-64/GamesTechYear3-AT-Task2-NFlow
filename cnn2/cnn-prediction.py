# CNN prediction script.
# Writes out a prediction for an object. 
# Called within unity and writes out to stdout.


# Dependancies
import dataLoader as dl
import os
import tensorflow as tf
import sys

# Inputs - the model path and the image path.
model_path = sys.argv[1]
image_file_path = sys.argv[2]


def main():
    model = tf.keras.models.load_model(model_path)
    test_image = dl.loadPredictionImage(image_path=image_file_path, image_width=50, image_height=50)
    result = model.predict(test_image)
    print(result) # write the result to stdout.
    return

if __name__=="__main__":
    main()
