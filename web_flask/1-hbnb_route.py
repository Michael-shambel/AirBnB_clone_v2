#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
	return "Hello HBNB!"

@app.route('/hnbnb', strict_slashes=False)
def hbnb():
	return "HBNB"
