import flask
import os 
import random
import json

from flask import render_template
from flask import session, redirect, url_for
from mlt_data import *
from flask_login import (LoginManager, UserMixin, login_required, login_user, logout_user,
                         current_user)
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized
    
app = flask.Flask(__name__)

SECRET_KEY='AIzaSyAuQo0MS-TgejKC75M9uGTeU0WXnyxeOww'
GOOGLE_LOGIN_CLIENT_ID="415070769795-0a1chfviiumsdsv7ov2fcaqdlotut530.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET='zT2-uqTe1wqdJGWUs7Y8LZvX'
GOOGLE_LOGIN_REDIRECT_URI='https://mlt-stats.herokuapp.com/oauth2callback'

app.config['SECRET_KEY'] = SECRET_KEY
goog_blueprint = make_google_blueprint(
    client_id= GOOGLE_LOGIN_CLIENT_ID,
    client_secret= GOOGLE_LOGIN_CLIENT_SECRET,
    reprompt_consent=True
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'google.login'

app.register_blueprint(goog_blueprint)

@app.route('/home')
def home():
    # data = MLT_Data("fellow_data.json")
    data = MLT_Data("test.json")
    fellow = data.get_fellow_data("janedoe@gmail.com")

    return render_template('index.html', fellow_data = fellow)
    
    
@app.route('/oauth2callback')
@oauth_authorized.connect_via(goog_blueprint)
def google_logged_in(blueprint, token):
    resp = blueprint.session.get('/oauth2/v2/userinfo')
    user_info = resp.json()
    print(user_info)
    user_id = str(user_info['id'])
    oauth = OAuth.query.filter_by(provider=blueprint.name,
                                  provider_user_id=user_id).first()
    if not oauth:
        oauth = OAuth(provider=blueprint.name,
                      provider_user_id=user_id,
                      token=token)
    else:
        oauth.token = token
        db.session.add(oauth)
        db.session.commit()
        login_user(oauth.user)
    if not oauth.user:
        user = User(email=user_info["email"],
                    name=user_info["name"])
        oauth.user = user
        db.session.add_all([user, oauth])
        db.session.commit()
        login_user(user)

    return False
    
    # return redirect(url_for('home'))
    
@app.route('/')
def main():
    google_data = None
    user_info_endpoint = '/oauth2/v2/userinfo'
    if current_user.is_authenticated and google.authorized:
        google_data = google.get(user_info_endpoint).json()
    return render_template('login.html', google_url = "/google", google_data = google_data)
    

    
@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html')

app.run(
    port = int(os.getenv('PORT')),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)