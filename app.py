import flask
import os 
import random
import requests
import json
import twit
import geni
from flask import render_template
from flask import request, redirect
from mlt_data import *

    
app = flask.Flask(__name__)

@app.route('/')
def main():
    
    song = geni.get_song_data()
    tweet = twit.get_tweet() 
    # data = MLT_Data("fellow_data.json")
    data = MLT_Data("test.json")
    fellow = data.get_fellow_data("philanab@gmail.com")

    return render_template('index.html', song_data = song, twitter_data = tweet, fellow_data = fellow)
    
    
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