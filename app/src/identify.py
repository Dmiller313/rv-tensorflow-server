#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
import tensorflow as tf
from flask import jsonify

DATADIR = "./data/sample/"
CATEGORIES = ["coffee"] #will be added based on models in folder

def prepare (filepath):
    IMG_SIZE = 512
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def identifyObject(img):
    model = tf.keras.models.load_model("512_79_coffee.model")
    prediction = model.predict([prepare(img)])
    jsonBuild = {
        "foundObject":CATEGORIES[int(prediction[0][0])]#,
        #"matchPercentage":calculateMatch(),
        #"otherInfo":"other"
    }
    
    
    #for sample in os.listdir(DATADIR):
        #img = os.path.join(DATADIR,sample)
        #print(img)
        #output = output + "<p>" + img + "</p>"
        
        #print(prediction)
        #output = output + "<p>" + prediction + "</p>"
        #print(CATEGORIES[int(prediction[0][0])])
        #output = "{\"percentageMatch\": percentage, id: id,  objectName: object}"
        #SELECT * FROM instructions where item like '%coffee%'
        #output = output + "<p>" + CATEGORIES[int(prediction[0][0])] + "</p>"
    return jsonBuild
    


# In[ ]:





# In[ ]:




