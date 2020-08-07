import os
import tensorflow as tf
import cv2
import json
import gc
import numpy as np
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
server = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

#model = tf.keras.models.load_model("256_optimized.model")
model = tf.keras.models.load_model("128_true_optimized.model")

UPLOAD_FOLDER = 'UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

server.secret_key = 'ah5XAw.|$ZlPviFeFUeM'
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
server.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

DATADIR = "./data/sample/"
CATEGORIES = ["coffee","bottle","cardboard"]

def allowed_file(filename):
     return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare (filepath):
    IMG_SIZE = 128
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def identifyObject(sample):

     jsonBuild = {
          "foundObject":"none"
     }

     prediction = model.predict([prepare(sample)])
     output = prediction[0]

     if(output[0] == 1):
          result = CATEGORIES[0]
          jsonBuild = {
               "foundObject":result
          }
          gc.collect()
          os.remove(sample)
          print(jsonBuild)
          return jsonBuild
     elif(output[1] == 1):
          result = CATEGORIES[1]
          jsonBuild = {
               "foundObject":result
          }
          gc.collect()
          os.remove(sample)
          print(jsonBuild)
          return jsonBuild
     elif(output[2] == 1):
          result = CATEGORIES[2]
          jsonBuild = {
               "foundObject":result
          }
          gc.collect()
          os.remove(sample)
          print(jsonBuild)
          return jsonBuild
     else:
          return jsonBuild



@server.route("/")
def hello():
     return "HELLO WORLD"
    

@server.route("/upload", methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            if 'image' not in request.form:
                flash('No file part')
                return redirect(request.url)
            file = request.form['image']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                dt_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                flash('Processing image')
                filename = secure_filename(file.filename)
                file.save(os.path.join(server.config['UPLOAD_FOLDER'], dt_string + '_' + filename))
                #json = identify.identifyObject(os.path.join(server.config['UPLOAD_FOLDER'], dt_string + '_' + filename))
                json = identifyObject(os.path.join(server.config['UPLOAD_FOLDER'], dt_string + '_' + filename))
                #return redirect(url_for('upload_file', filename=filename))
                return jsonify(json)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            dt_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            flash('Processing image')
            filename = secure_filename(file.filename)
            file.save(os.path.join(server.config['UPLOAD_FOLDER'], dt_string + '_' + filename))
            #json = identify.identifyObject(os.path.join(server.config['UPLOAD_FOLDER'], dt_string + '_' + filename))
            json = identifyObject(os.path.join(server.config['UPLOAD_FOLDER'], dt_string + '_' + filename))
            #return redirect(url_for('upload_file', filename=filename))
            return jsonify(json)
        else:
             return '''<!doctype html><title>Image upload</title><h1>Invalid usage</h1>'''
    elif request.method == 'GET':
        return '''<!doctype html><title>Not POST</title><h1>Not POST</h1>'''
    else:
        return '''<!doctype html><title>Image upload</title><h1>Invalid usage</h1>'''

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=port)
