from requests import get

from extra.helpers import generate_headers

API_BASE_URL = "https://api.spotify.com/v1/"


def get_top_tracks():

    # arrays:
    track_name = []
    artist_name = []

    # generate headers
    headers = generate_headers()

    # request spotify for user's top tracks
    response = get(API_BASE_URL + 'me/top/tracks?time_range=short_term', headers=headers)
    
    tracks = response.json()

    # parse track names from json 
    for track in tracks["items"]:
        track_name.append(track["name"])

    return track_name


def get_top_artists():

    # arrays:
    track_name = []
    artist_name = []

    # generate headers
    headers = generate_headers()

    # request spotify for user's top tracks
    response = get(API_BASE_URL + 'me/top/artists?time_range=short_term', headers=headers)
    
    artists = response.json()

    for artist in artists["items"]:
        artist_name.append(artist["name"])


    return artist_name




