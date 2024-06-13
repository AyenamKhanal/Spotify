from dotenv import load_dotenv
import os
from urllib.parse import urlencode
from requests import post, get
from flask import Flask, render_template, redirect, request, jsonify, session
from datetime import datetime

from helpers import access_required, session_expiry

load_dotenv()
app = Flask(__name__)
app.secret_key = "phenom"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://localhost:5000/callback"
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API_BASE_URL = "https://api.spotify.com/v1/"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    scope = 'user-read-private user-read-email user-top-read user-library-read'

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

    return redirect('/saved-tracks')


def generate_headers():
    return  {'Authorization': f"Bearer {session['access_token']}"}


@app.route('/playlists')
@access_required
@session_expiry
def get_playlists():

    # generate headers
    headers = generate_headers()

    # request data to spotify and store get response
    response = get(API_BASE_URL + 'me/playlists', headers=headers)

    # parse json
    playlists = response.json()

    return  jsonify(playlists)


@app.route('/artists')
@access_required
@session_expiry
def get_artists():

    # generate headers
    headers = generate_headers()

    # request data to spotify and store get response
    response = get(API_BASE_URL + 'me/top/artists?limit=50&time_range=long_term', headers=headers)

    # parse json
    top_artists = response.json()

    for artist in top_artists["items"]:
        print(artist["name"])

    return top_artists


@app.route('/tracks')
@access_required
@session_expiry
def get_tracks():

    # generate headers
    headers = generate_headers()

    # request data to spotify and store get response
    response = get(API_BASE_URL + 'me/top/tracks?limit=50&time_range=long_term', headers=headers)

    # parse json
    top_tracks = response.json()

    for track in top_tracks["items"]:
        print(track["name"])

    return top_tracks

@app.route('/saved-tracks')
@access_required
@session_expiry
def get_saved_tracks():

    # generate headers
    headers = generate_headers()

    # request data to spotify and store get response
    response = get(API_BASE_URL + 'me/tracks?limit=50', headers=headers)

    # parse json
    saved_tracks = response.json()

    for track in saved_tracks["items"]:
        print(track["track"]["name"])

    return saved_tracks


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
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
