from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# init app
app = Flask(__name__)

# Init cors
CORS(app)

# Encrypt
@app.route('/encrypt', methods=['GET'])
def encrypt():
    