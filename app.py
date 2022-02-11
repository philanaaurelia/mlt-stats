import flask
import os 
import random
import json
from flask_googlelogin import GoogleLogin
from flask import render_template
from flask import session, redirect, url_for
from mlt_data import *
from flask_login import (UserMixin, login_required, login_user, logout_user,
                         current_user)
    
app = flask.Flask(__name__)
app.config.update(
    SECRET_KEY='AIzaSyAuQo0MS-TgejKC75M9uGTeU0WXnyxeOww',
    GOOGLE_LOGIN_CLIENT_ID="415070769795-0a1chfviiumsdsv7ov2fcaqdlotut530.apps.googleusercontent.com",
    GOOGLE_LOGIN_CLIENT_SECRET='zT2-uqTe1wqdJGWUs7Y8LZvX',
    GOOGLE_LOGIN_REDIRECT_URI='https://mlt-stats.herokuapp.com/oauth2callback')
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
    user = User.filter_by(google_id=userinfo['id']).first()
    if user:
        user.name = userinfo['name']
        user.avatar = userinfo['picture']
    else:
        user = User(google_id=userinfo['id'],
                    name=userinfo['name'],
                    avatar=userinfo['picture'])
    db.session.add(user)
    db.session.flush()
    login_user(user)
    return redirect(url_for('form'))
    
    
@app.route('/')
def main():
    return render_template('login.html', google_url = googlelogin.login_url(approval_prompt='force'))
    

    
@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html')

app.run(
    port = int(os.getenv('PORT')),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)