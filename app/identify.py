#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
import tensorflow as tf

DATADIR = "./data/sample/"
CATEGORIES = ["coffee"]

def prepare (filepath):
    IMG_SIZE = 512
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def identifyObject():
    model = tf.keras.models.load_model("512_79_coffee.model")

    for sample in os.listdir(DATADIR):
        img = os.path.join(DATADIR,sample)
        print(img)
        prediction = model.predict([prepare(img)])
        print(prediction)
        print(CATEGORIES[int(prediction[0][0])])
    


# In[ ]:





# In[ ]:




