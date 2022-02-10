import flask
import os 
import random
import requests
import json
from flask_googlelogin import GoogleLogin
from flask import render_template
from flask import request, redirect, url_for
from mlt_data import *
from flask_login import (UserMixin, login_required, login_user, logout_user,
                         current_user)
    
app = flask.Flask(__name__)
app.config.update(
    SECRET_KEY='AIzaSyAuQo0MS-TgejKC75M9uGTeU0WXnyxeOww',
    GOOGLE_LOGIN_CLIENT_ID="415070769795-0a1chfviiumsdsv7ov2fcaqdlotut530.apps.googleusercontent.com",
    GOOGLE_LOGIN_CLIENT_SECRET='zT2-uqTe1wqdJGWUs7Y8LZvX',
    GOOGLE_LOGIN_REDIRECT_URI='https://a102ae043f294e90bb07ce6f68d9186f.vfs.cloud9.us-east-2.amazonaws.com/oauth2callback')
googlelogin = GoogleLogin(app)

@app.route('/home')
@login_required
def home():
    # data = MLT_Data("fellow_data.json")
    data = MLT_Data("test.json")
    fellow = data.get_fellow_data("janedoe@gmail.com")

    return render_template('index.html', fellow_data = fellow)
    
    
@app.route('/oauth2callback')
@googlelogin.oauth2callback
def callback(token, userinfo, **params):
    user = users[userinfo['id']] = User(userinfo)
    login_user(user)
    session['token'] = json.dumps(token)
    session['extra'] = params.get('extra')
    return redirect(params.get('next', url_for('/')))
    
    
@app.route('/', methods = ['POST', 'GET'])
def main():
    return render_template('login.html', google_url = googlelogin.login_url(params=dict(section='notifications', next=url_for('.callback'))))
    

    
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