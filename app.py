import flask
import os 
import random
import json
from flask import session, redirect, url_for, request, render_template
from mlt_data import *
from flask_login import (LoginManager, UserMixin, login_required, login_user, logout_user,
                         current_user)
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized


class ReverseProxied(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = environ.get('HTTP_X_FORWARDED_PROTO')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app = flask.Flask(__name__)
# needed to make sure https is sent to google
app.wsgi_app = ReverseProxied(app.wsgi_app)


SECRET_KEY='AIzaSyAuQo0MS-TgejKC75M9uGTeU0WXnyxeOww'
GOOGLE_LOGIN_CLIENT_ID="415070769795-0a1chfviiumsdsv7ov2fcaqdlotut530.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET='zT2-uqTe1wqdJGWUs7Y8LZvX'
GOOGLE_LOGIN_REDIRECT_URI='https://mlt-stats.herokuapp.com/oauth2callback'

app.config['SECRET_KEY'] = SECRET_KEY
goog_blueprint = make_google_blueprint(
    client_id= GOOGLE_LOGIN_CLIENT_ID,
    client_secret= GOOGLE_LOGIN_CLIENT_SECRET,
    scope= ["openid","https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"]
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'google.login'

app.register_blueprint(goog_blueprint)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
    
# index home page
@app.route('/')
def index():
    google_data = None
    user_info_endpoint = '/oauth2/v2/userinfo'
    if current_user.is_authenticated and google.authorized:
        google_data = google.get(user_info_endpoint).json()
    return render_template('index.html', google_url = "/login")
    

# profile home page
@app.route('/home')
def home():
    if session.get('session_id') and session['session_id']:
        # if 'google_id' in request.args:
        # parameter 'varname' is specified
        # google_id = request.args.get('google_id')
            # parameter 'varname' is NOT specified
        # data = MLT_Data("fellow_data.json")
        data = MLT_Data("test.json")
        fellow = data.get_fellow_data("janedoe@gmail.com")

        return render_template('home.html', fellow_data = fellow)
    else:
        return redirect(url_for('index'))
        
    
@app.route('/oauth2callback')
@oauth_authorized.connect_via(goog_blueprint)
def google_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with {}".format(blueprint.name), 'danger')
        return redirect(url_for('index'))
                
    session["session_id"] = os.urandom(16);
    resp = blueprint.session.get('/oauth2/v2/userinfo')
    # https://oauth2.googleapis.com/tokeninfo?id_token=XYZ123
    # resp = google.get("/oauth2/v1/userinfo")
    # token_url="https://accounts.google.com/o/oauth2/token",
    user_info = resp.json()
    print(user_info)
    return redirect(url_for('home'))
    
@app.route("/login")
def login():
    return redirect(url_for("google.login"))

    
@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html')
    
@app.route('/signout')
def signout():
    session.pop('session_id')
    return redirect(url_for("index"))

app.run(
    port = int(os.getenv('PORT')),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)