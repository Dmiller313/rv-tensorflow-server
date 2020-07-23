import os
import identify
import json
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
server = Flask(__name__)
port = int(os.environ.get("PORT", 8000))

model = tf.keras.models.load_model("512_79_coffee.model")
UPLOAD_FOLDER = 'UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

server.secret_key = 'ah5XAw.|$ZlPviFeFUeM'
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
server.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
     return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def identifyObject(img):
     prediction = model.predict([prepare(img)])
    jsonBuild = {
        "foundObject":CATEGORIES[int(prediction[0][0])]#,
        #"matchPercentage":calculateMatch(),
        #"otherInfo":"other"
    }
    return jsonBuild

@server.route("/")
def hello():
     return "HELLO WORLD"
    

@server.route("/upload", methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
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
            json = identifyObject(os.path.join(server.config['UPLOAD_FOLDER'], dt_string + '_' + filename)
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
