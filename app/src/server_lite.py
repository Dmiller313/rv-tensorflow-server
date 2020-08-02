import os
import tensorflow as tf
import cv2
import json
import numpy as np
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
server = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

#model = tf.keras.models.load_model("256_optimized.model")

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
    IMG_SIZE = 512
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def identifyObject(sample):
     interpreter = tf.lite.Interpreter(model_path="model.tflite")
     interpreter.allocate_tensors()

     input_details = interpreter.get_input_details()
     output_details = interpreter.get_output_details()

     input_shape = input_details[0]['shape']
     input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
     interpreter.set_tensor(input_details[0]['index'], input_data)

     interpreter.invoke()

     output_data = interpreter.get_tensor(output_details[0]['index'])
     print(output_data.flatten)
     jsonBuild = {
         "output":output_data.flatten
         #"foundObject":CATEGORIES[int(max(prediction))]#,
         #"matchPercentage":calculateMatch(),
         #"otherInfo":"other"
     }
     os.remove(img) #specifically, path to the image
     print(jsonBuild)
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
