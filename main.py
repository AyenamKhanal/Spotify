from requests import post, get
import sqlite3

from utils.helpers import access_required, session_expiry, generate_headers
from utils.oauth import API_BASE_URL, app


@app.route('/saved-tracks')
@access_required
@session_expiry
def get_saved_tracks():

    # connect to the database
    conn = sqlite3.connect('spotify.db')
    cursor = conn.cursor()

    # generate headers
    headers = generate_headers()

    # request data to spotify and store get response
    response = get(API_BASE_URL + 'me/tracks?limit=50', headers=headers)

    # parse json
    saved_tracks = response.json()

    # get total songs
    total = saved_tracks["total"]
    limit = 50
    offset = 1
    
    while 

    for song in saved_tracks["items"]:
        cursor.execute("INSERT INTO saved_songs (name) VALUES (?)", (song["track"]["name"],))

    conn.commit()
    return saved_tracks

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
