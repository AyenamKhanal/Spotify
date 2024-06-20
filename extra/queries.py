from requests import get

from extra.helpers import generate_headers

API_BASE_URL = "https://api.spotify.com/v1/"




def top_tracks():

    track_name = []

    # generate headers
    headers = generate_headers()

    # request spotify for user's top tracks
    response = get(API_BASE_URL + 'me/top/tracks?time_range=short_term&limit=5', headers=headers)
    
    tracks = response.json()

    return tracks

def get_top_tracks(tracks):

    # parse track names from json 
    for track in tracks["items"]:
        track_name.append(track["name"])

    return tracks


def get_top_artists():

    artist_name = []

    # generate headers
    headers = generate_headers()

    # request spotify for user's top tracks
    response = get(API_BASE_URL + 'me/top/artists?time_range=short_term&limit=5', headers=headers)
    
    artists = response.json()

    for artist in artists["items"]:
        artist_name.append(artist["name"])

    return artists



def get_album_cover():

    album_covers = []

    # generate headers
    headers = generate_headers()

    # request spotify for user's top tracks
    response = get(API_BASE_URL + 'me/top/artists?time_range=short_term&limit=5', headers=headers)
    
    artists = response.json()

    for artist in artists["items"]:
        album_covers.append(artist["name"])

    return artists