# Example derived from https://github.com/bankarpranit26/deep-learning/blob/master/learnings/TFServing_Local_LinearModel.ipynb

# Helper libraries
import numpy as np
import os

# TensorFlow
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
import tensorflow.keras.backend
from tensorflow import keras

def keras_test():
    print(tf.__version__)

    X = np.arange(-10.0, 10.0, 1e-2)
    np.random.shuffle(X)
    y = 2 * X + 1

    train_end = int(0.6 * len(X))
    test_start = int(0.8 * len(X))
    X_train, y_train = X[:train_end], y[:train_end]
    X_test, y_test = X[test_start:], y[test_start:]
    X_val, y_val = X[train_end:test_start], y[train_end:test_start]

    keras.backend.clear_session()
    #clear_session()
    linear_model = keras.models.Sequential([
                                           keras.layers.Dense(units=1, input_shape=[1], name='Single')
                                           ])
    linear_model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.mean_squared_error)
    linear_model.summary()


    linear_model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20)

    linear_model.evaluate(X_test, y_test, verbose=0)

    round(linear_model.predict([7.443]).tolist()[0][0], 4)

