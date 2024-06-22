from dotenv import load_dotenv
import os
from urllib.parse import urlencode
from requests import post, get
from flask import Flask, render_template, redirect, request, jsonify, session
from datetime import datetime

from extra.helpers2 import get_home_page_data

app = Flask(__name__, template_folder='templates')
app.secret_key = "phenom"
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:5000/callback"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API_BASE_URL = "https://api.spotify.com/v1/"

@app.route('/')
def index():
    return render_template("welcome.html")

@app.route('/login')
def login():
    scope = 'user-top-read user-library-read user-read-private user-read-email'

    params = {
        'client_id' : CLIENT_ID,
        'response_type' : 'code',
        'redirect_uri' : REDIRECT_URI,
        'scope' : scope, 
        'show dialog': True
    }

    auth_url = f"{AUTH_URL}?{urlencode(params)}"

    return redirect(auth_url)

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error" : request.args['error']})
    
    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

        response = post(TOKEN_URL, data=req_body)
        token_info = response.json()

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

    return render_template('successful.html')


@app.route("/refresh-token")
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        response = post(TOKEN_URL, data=req_body)
        
        new_token_info = response.json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in'] 

        return redirect('/playlists')
    
@app.route("/home", methods=["GET", "POST"])
def home():

    if request.args.get("track-time"):
        track_time_range = request.args.get("track-time")
    else:
        track_time_range = "short_term"
    

    if request.args.get("artist-time"):
        artist_time_range = request.args.get("artist-time")
    else:
        artist_time_range = "short_term"
    #return render_template("test.html", response=[track_time_range, artist_time_range])


    homepage_data = get_home_page_data(track_time_range, artist_time_range)

    return render_template("home.html",
                            tracks=homepage_data["tracks"],
                            artists=homepage_data["artists"],
                            covers=homepage_data["covers"], 
                            artists_profile_pics=homepage_data["artists_profile_pics"], 
                            user_name=homepage_data["user_name"], 
                            user_profile_pic=homepage_data["user_profile_pic"],
                            track_time_range=track_time_range,
                            artist_time_range=artist_time_range
                            )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)