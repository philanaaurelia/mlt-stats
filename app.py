import flask
import os 
import random
import requests
import json
import tweepy
import twit
import geni
from flask import render_template

    
app = flask.Flask(__name__)

@app.route('/')
def main():
    song_data = geni.get_song_data()
    tweet = twit.get_tweet() 
    
    return render_template('index.html', song_data = song_data, tweet = tweet)
    
app.run(
    port = int(os.getenv('PORT')),
    host = os.getenv('IP','0.0.0.0'),
    # debug=True
)