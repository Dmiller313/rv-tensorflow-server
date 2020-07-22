#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

DATADIR = "./data"
CATEGORIES = ["coffee"]

training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) #path to data directory
        class_num = CATEGORIES.index(category) #assign classification int
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE) #create array, make all images grayscale
                #plt.imshow(img_array, cmap="gray")
                #plt.show()
                #do not resize image LxW, all images are 512x512
                training_data.append([img_array, class_num])
            except Exception as e:
                pass #this is bad code

create_training_data()
        
        


# In[8]:


print(len(training_data)) #how many images do we have in the model?


# In[9]:


random.shuffle(training_data) #shuffle images so dataset does not skew


# In[10]:


X = [] #featureset
y = [] #labels

for features, label in training_data:
    X.append(features)
    y.append(label)
    
X = np.array(X).reshape(-1, 512, 512, 1)
y = np.array(y)


# In[11]:


import pickle

pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()


# In[12]:


X = pickle.load(open("X.pickle","rb"))
y = pickle.load(open("y.pickle","rb"))


# In[ ]:




