import tensorflow as tf
import pathlib
import os

#manually change the .from_saved_model() method to convert different models
#this may need to be .from_keras_model() instead
converter = tf.lite.TFLiteConverter.from_saved_model('512_79_coffee.model')
tflite_model = converter.convert()
#files = pathlib.Path('512_79_coffee_lite.model')
#files.write_bytes(tflite_model)

with tf.io.gfile.GFile('model.tflite', 'wb') as f:
    f.write(tflite_model)
