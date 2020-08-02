import os
import tensorflow as tf
import cv2
import json
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
server = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

server.secret_key = 'ah5XAw.|$ZlPviFeFUeM'

#this file set up simply to allow for running Jupyter conversions within Docker

@server.route("/")
def hello():
     
     return "HELLO WORLD"

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=port)
