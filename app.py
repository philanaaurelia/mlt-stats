import flask
import os 
import random
import requests
import json
from flask import render_template
from flask import request, redirect
from mlt_data import *

    
app = flask.Flask(__name__)

@app.route('/')
def main():
    # data = MLT_Data("fellow_data.json")
    data = MLT_Data("test.json")
    fellow = data.get_fellow_data("janedoe@gmail.com")

    return render_template('index.html', fellow_data = fellow)
    
    
@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('login.html')
    
@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html')
    
@app.route('/result', methods = ['POST', 'GET'])
def result():
    yo = request.form['call-schedule']
    print("The email address is '" + yo + "'")
    return main()
    
app.run(
    port = int(os.getenv('PORT')),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)