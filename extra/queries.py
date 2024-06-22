from requests import get

from extra.helpers import generate_headers

API_BASE_URL = "https://api.spotify.com/v1/"


class userProfile():

    def __init__(self):

        # generate headers
        headers = generate_headers()

        # request spotify for user profile
        response = get(API_BASE_URL + 'me', headers=headers)
    
        # store tracks json meta data into tracks
        self.profile = response.json()

    
    def get_user_name(self):

        # get name from JSON
        self.name = self.profile["display_name"]

        return self.name

    def get_user_profile_pic(self):

        # get profile pic url from JSON
        self.profile_pic = self.profile["images"][0]["url"]

        return self.profile_pic

class topTracks():

    def __init__(self, time_range):

        # initialize time_range
        self.time_range = time_range

        # generate headers
        headers = generate_headers()

        # request spotify for user's top tracks
        response = get(API_BASE_URL + f'me/top/tracks?time_range={self.time_range}&limit=5', headers=headers)
    
        # store tracks json meta data into tracks
        self.tracks = response.json()


    def get_top_tracks(self):

        # declare list to store track name 
        self.track_name = []

        # parse track names from json 
        for track in self.tracks["items"]:
            self.track_name.append(track["name"])

        return self.track_name
    

    def get_album_cover(self):

        # declare list to store album covers
        self.album_covers = []

        for track in self.tracks["items"]:
            self.album_covers.append(track["album"]["images"][0]["url"])

        return self.album_covers



class topArtists():

    def __init__(self, time_range):

        # initialize time_range
        self.time_range = time_range

        # generate headers
        headers = generate_headers()

        # request spotify for user's top tracks
        response = get(API_BASE_URL + f'me/top/artists?time_range={self.time_range}&limit=5', headers=headers)
    
        # store tracks json meta data into tracks
        self.artists = response.json()    


    def get_top_artists(self):

        # declare list to store artist's name
        self.artist_name = []

        for artist in self.artists["items"]:
            self.artist_name.append(artist["name"])

        return self.artist_name
    
    def get_profile_pictures(self):

        # declare list to store album covers
        self.profile_pictures = []

        for track in self.artists["items"]:
            self.profile_pictures.append(track["images"][0]["url"])

        return self.profile_pictures



