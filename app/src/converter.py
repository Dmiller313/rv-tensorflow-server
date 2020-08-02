import tensorflow as tf
import pathlib
import os

model = tf.keras.models.load_model("256_optimized.model")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with tf.io.gfile.GFile('model.tflite', 'wb') as f:
    f.write(tflite_model)

#manually change the .from_saved_model() method to convert different models
#this may need to be .from_keras_model() instead
#files = pathlib.Path('512_79_coffee_lite.model')
#files.write_bytes(tflite_model)

#tflite_model.save('512_coffee_lite.model')

#with tf.io.gfile.GFile('model.tflite', 'wb') as f:
#    f.write(tflite_model)

#Solid attempt here, gets some sort of output, not folder structure
#tflite_file = os.path.join('tflite', 'coffee_tflite_model.h5')
#converter = tf.lite.TFLiteConverter.from_saved_model('512_79_coffee.model')
#tflite_model = converter.convert()
#open(tflite_file, "wb").write(tflite_model)

#this code creates a WB file - not helpful
'''
tflite_file = os.path.join('tflite', 'coffee_tflite_model.h5')
model_keras = tf.keras.models.load_model('512_79_coffee.model')

converter = tf.lite.TFLiteConverter.from_keras_model(model_keras)
tflite_model = converter.convert()

open(tflite_file, "wb").write(tflite_model)
'''
