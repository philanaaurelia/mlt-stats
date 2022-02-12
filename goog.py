
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer import oauth_authorized


SECRET_KEY='AIzaSyAuQo0MS-TgejKC75M9uGTeU0WXnyxeOww'
GOOGLE_LOGIN_CLIENT_ID="415070769795-0a1chfviiumsdsv7ov2fcaqdlotut530.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET='zT2-uqTe1wqdJGWUs7Y8LZvX'


goog_blueprint = make_google_blueprint(
    client_id= GOOGLE_LOGIN_CLIENT_ID,
    client_secret= GOOGLE_LOGIN_CLIENT_SECRET,
    scope= ["openid","https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"]
)


# login_manager.login_view = 'google.login'

# app.register_blueprint(goog_blueprint)


    
# index home page
# @app.route('/')
# def index():
    # google_data = None
    # user_info_endpoint = '/oauth2/v2/userinfo'
    # if current_user.is_authenticated and google.authorized:
    #    google_data = google.get(user_info_endpoint).json()
    # return render_template('index.html', google_url = "/glogin")
    

        

# @oauth_authorized.connect_via(goog_blueprint)
# def logged_in(blueprint, token):
                
    # resp = google.get("/oauth2/v1/userinfo")
    
    # user_info = resp.json()
    # return redirect(url_for('home'))
    
#@app.route("/glogin")
#def glogin():
#    return redirect(url_for("google.login"))
    

