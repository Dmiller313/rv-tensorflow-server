import cv2
import os
import tensorflow as tf

DATADIR = "./data/"
CATEGORIES = ["coffee","plastic","cardboard"]

def prepare (filepath):
    IMG_SIZE = 128
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model("128_true_optimized.model")

MATCHES = [0,0,0]

for cat in CATEGORIES:
    dir_ = os.path.join(DATADIR,cat)
    print(dir_)
    count = 0
    for sample in os.listdir(dir_):
        if(sample != ".ipynb_checkpoints"):
            img = os.path.join(dir_,sample)
            #print(img)
            prediction = model.predict([prepare(img)])
            output = prediction[0]
            #print(img)
            print("================================")
            print(prediction)
            if(output[0] == 1 and cat == "coffee"):
                print(img)
                print(output)
                MATCHES[0] = MATCHES[0] + 1
            if(output[1] == 1 and cat == "plastic"):
                print(img)
                print(output)
                MATCHES[1] = MATCHES[1] + 1
            if(output[2] == 1 and cat == "cardboard"):
                print(img)
                print(output)
                MATCHES[2] = MATCHES[2] + 1
            print("================================")
    print(MATCHES)
