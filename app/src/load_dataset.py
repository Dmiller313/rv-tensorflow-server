#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

DATADIR = "./data"
CATEGORIES = ["coffee","cardboard","bottle"]

training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) #path to data directory
        class_num = CATEGORIES.index(category) #assign classification int
        for img in os.listdir(path):
            joinPath = os.path.join(path,img)
            if(img != ".ipynb_checkpoints"):
                try:
                    print(joinPath)
                    img_array = cv2.imread(joinPath, cv2.IMREAD_GRAYSCALE) #create array, make all images grayscale
                    new_array = cv2.resize(img_array, (128,128))
                    #do not resize image LxW, all images are 512x512
                    training_data.append([new_array, class_num])
                except Exception as e:
                    pass #this is bad code

create_training_data()
        
        


# In[7]:


print(len(training_data)) #how many images do we have in the model?


# In[3]:


random.shuffle(training_data) #shuffle images so dataset does not skew


# In[8]:


X = [] #featureset
y = [] #labels

for features, label in training_data:
    #print(label)
    X.append(features)
    y.append(label)
    
X = np.array(X).reshape(-1, 128, 128, 1)
y = np.array(y)


# In[9]:


import pickle

pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()


# In[70]:


X = pickle.load(open("X.pickle","rb"))
y = pickle.load(open("y.pickle","rb"))


# In[ ]:




