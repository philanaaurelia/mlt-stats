import flask
import os 
import random
import json
from flask import session, redirect, url_for, request, render_template
from mlt_data import *
from flask_login import (LoginManager, UserMixin, login_required, login_user, logout_user,
                         current_user)
from flask_dance.contrib.slack import make_slack_blueprint, slack
from flask_dance.consumer import oauth_authorized
import mlt_gdata

# loginfellows


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
SLACK_LOGIN_CLIENT_ID="971843552369.3095825635154"
SLACK_LOGIN_CLIENT_SECRET = "82c0f6f100d19d43c971b8fd70db5e9a"

slck_blueprint = make_slack_blueprint(
    client_id= SLACK_LOGIN_CLIENT_ID,
    client_secret= SLACK_LOGIN_CLIENT_SECRET,
    scope= ["openid,email,profile"]
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'slack.login'


app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(slck_blueprint)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
    
# index home page
@app.route('/')
def index():
    mlt_gdata.init();
    return render_template('index.html', slack_url = "/slogin")
   
# profile home page
@app.route('/sample_home')
def sample_home(): 
    data = MLT_Data("test.json")
    print("sample_home")
    member = data.get_member_data("janedoe@gmail.com")
    
    return render_template('home.html', fellow_data = member)

# profile home page
@app.route('/home')
def home():
    if session.get('session_id') and session['session_id']:
        # data = MLT_Data("fellow_data.json")
        data = MLT_Data("test.json")
        if session.get('email') and session['email']:
            member = data.get_member_data(session['email'])
        else:
            return "User NOT FOUND"
        
        if member.role == "coach":
            # fellows = data.get_fellows_data(member.email)
            fellows = data.get_fellows_data("all") # dummy variable for testing
            fellow_names = mlt_gdata.get_fellow_names()
            return render_template("overview.html", coach_data = member, fellows = fellows, fnames = fellow_names)
        else: 
            return render_template('home.html', fellow_data = member)
    else:
        return redirect(url_for('index'))
        
        
@oauth_authorized.connect_via(slck_blueprint)
def logged_in(blueprint, token):
    print(token)
    if not token:
        flash("Failed to log in with {}".format(blueprint.name), 'danger')
        return redirect(url_for('index'))
                
    session["session_id"] = os.urandom(16)
    
    resp = slack.get("openid.connect.userInfo")
    user_info = resp.json()
    session["email"] = user_info['email']
    print(user_info['email'])
    # print(user_info)
    return redirect(url_for('home'))

    
@app.route("/slogin")
def slogin():
    return redirect(url_for("slack.login"))



''' *************
Coach Funcs
*************** '''
@app.route('/preview', methods = ['POST', 'GET'])
def preview():
    
    # get URL parameters 
    chosen_fellow = request.args.get("preview_fellow")
    fellow_dta = mlt_gdata.get_fellow_data(chosen_fellow)

    return render_template('home.html', fellow_data = fellow_dta)


@app.route('/record', methods = ['POST', 'GET'])
def record():
    if session.get('session_id') and session['session_id']:
        if session.get('email') and session['email']: # update this to look for coach
            data = MLT_Data("test.json")
            # fellows = data.get_fellows_data(member.email)
            fellows = data.get_fellows_data("all") # dummy variable for testing
            return render_template("form.html", fellows = fellows)
    
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