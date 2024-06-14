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

    # get total songs
    # request data to spotify and store get response
    response = get(API_BASE_URL + 'me/tracks?limit=1', headers=headers)

    total = response.json()["total"]
    limit = 50
    offset = 0
    
    while (limit * offset < 100):
        # request data to spotify and store get response
        response = get(API_BASE_URL + f'me/tracks?limit=50&offset={limit * offset}', headers=headers)

        # parse json
        saved_tracks = response.json()

        # add saved songs to saved_songs table
        for song in saved_tracks["items"]:
            cursor.execute("INSERT INTO saved_songs (title) VALUES (?)", (song["track"]["name"],))

        # add artists to artists table
        
        unique_artists = [] # make a list to add unique artist 

        for track in saved_tracks["items"]:
            for artist in track["track"]["artists"]:
                if artist["name"] not in unique_artists:
                    unique_artists.append(artist["name"])
                    cursor.execute("INSERT INTO artists (name) VALUES (?)", (artist["name"],))

        conn.commit()
        offset += 1
    

    return saved_tracks

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
