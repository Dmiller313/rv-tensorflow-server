#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import os
import tensorflow as tf

#TEMP
import numpy as np
#TEMP

DATADIR = "./data/sample/"
CATEGORIES = ["coffee","bottle","cardboard"]

def prepare (filepath):
    IMG_SIZE = 128
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model("128_true_optimized.model")

for sample in os.listdir(DATADIR):
    if(sample != ".ipynb_checkpoints"):
        img = os.path.join(DATADIR,sample)
        #print(img)
        prediction = model.predict([prepare(img)])
        argmax = np.argmax(prediction, axis=1)
        #print(argmax)
        output = CATEGORIES[int(max(prediction))]
        print(output)
        print(int(max(prediction)))
        print(prediction)
        flat = prediction.flatten()
        #print(flat[0])


# In[ ]:





# In[ ]:




