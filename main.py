from requests import post, get
import sqlite3
from flask import render_template, redirect

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
    
    while (limit * offset < total):
        # request data to spotify and store get response
        response = get(API_BASE_URL + f'me/tracks?limit=50&offset={limit * offset}', headers=headers)

        # parse json
        saved_tracks = response.json()
        
        unique_artists = [] # make a list to add unique artist 

        for track in saved_tracks["items"]:
            # add saved songs to saved_songs table
            cursor.execute("INSERT INTO saved_songs (title) VALUES (?)", (track["track"]["name"],))

            # select song_id
            cursor.execute("SELECT song_id FROM saved_songs WHERE title=?", (track["track"]["name"],))
            s_id = cursor.fetchone()[0]

            # add artists to artists table
            for artist in track["track"]["artists"]:
                if artist["name"] not in unique_artists:
                    unique_artists.append(artist["name"])
                    cursor.execute("INSERT INTO artists (name) VALUES (?)", (artist["name"],))

                # add to song_artists table

                cursor.execute("SELECT artist_id FROM artists WHERE name=?", (artist["name"],)) # select artist_id
                a_id = cursor.fetchone()[0]

                cursor.execute("INSERT INTO song_artists (song_id, artist_id) VALUES(?,?)", (s_id, a_id))


        conn.commit()
        offset += 1
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return saved_tracks


@app.route('/thank-you')
@access_required
@session_expiry
def homepage():
    return "Thank You"

@app.route('/artist-count')
@access_required
@session_expiry
def artist_count():

    # connect to the database
    conn = sqlite3.connect('spotify.db')
    cursor = conn.cursor()

    countTable = {} # dict to store the table info

    # query to get the count of each artist
    cursor.execute("SELECT artist_id, COUNT(*) FROM song_artists GROUP BY artist_id")

    for row in cursor.fetchall():
        artist_id, count = row
        countTable[artist_id] = count

    return redirect('/thank-you')

    #return render_template('artistcount.html', countTable=countTable)


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
