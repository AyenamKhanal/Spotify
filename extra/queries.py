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


    def get_top_tracks_info(self):

        # declare list to store track info 
        self.track_info = []

        # parse track names from json 
        for track in self.tracks["items"]:
            self.track_info.append({"name": track["name"], "artists": track["artists"], "cover": track["album"]["images"][0]["url"], "id": track["id"]})

        return self.track_info
    

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


    def get_top_artists_info(self):

        # declare list to store artist's info
        self.artist_info = []

        for artist in self.artists["items"]:
            self.artist_info.append({"name": artist["name"], "image": artist["images"][0]["url"], "id": artist["id"]})
            #self.artist_info.append({"name": artist["name"], "id": artist["id"]})


        return self.artist_info



class searchTracks():

    def __init__(self, track):

        # generate headers
        headers = generate_headers()

        # request spotify for user's top tracks
        response = get(API_BASE_URL + f'search?query={track}&type=track&limit=5', headers=headers)
    
        # store tracks json meta data into tracks
        self.searched_tracks = response.json()


    def get_tracks_info(self):

        # declare list to store tracks info 
        self.tracks_info = []

        # parse track names from json 
        for track in self.searched_tracks["tracks"]["items"]:
            self.tracks_info.append({"name": track["name"], "artists": track["artists"], "image": track["album"]["images"][0]["url"], "id": track["id"]})

        return self.tracks_info



class searchArtists():

    def __init__(self, artist):

        # generate headers
        headers = generate_headers()

        # request spotify for user's top tracks
        response = get(API_BASE_URL + f'search?query={artist}&type=artist&limit=5', headers=headers)
    
        # store tracks json meta data into tracks
        self.searched_artist = response.json()


    def get_artist_info(self):

        # declare list to store tracks info 
        self.artist_info = []

        # parse track names from json 
        for artist in self.searched_artist["artists"]["items"]:
            # try and except because some results don't have images, in those cases ignore and "continue" onto the next result 
            try: 
                self.artist_info.append({"name": artist["name"], "image": artist["images"][0]["url"], "id": artist["id"]})
            except IndexError:
                continue

        return self.artist_info


class trackStats():

    def __init__(self, trackid):

        # generate headers
        headers = generate_headers()

        # request spotify for user's top tracks
        response = get(API_BASE_URL + f'audio-features/{trackid}', headers=headers)
    
        # store tracks json meta data into tracks
        self.track_stats = response.json()


    def get_audio_features(self):

        # the JSON is already in the necessary format so no need to parse it

        # return the JSON itself
        return self.track_stats
    

class trackByID():

    def __init__(self, trackid):

        # generate headers
        headers = generate_headers()

        # request spotify for user's top tracks
        response = get(API_BASE_URL + f'tracks/{trackid}', headers=headers)
    
        # store tracks json meta data into tracks
        self.track_details = response.json()


    def get_track_details(self):

        # the JSON is already in the necessary format so no need to parse it

        # return the JSON itself
        return self.track_details
        
        
class artistByID():

    def __init__(self, artistid):

        # generate headers
        headers = generate_headers()

        # request spotify for user's top tracks
        response = get(API_BASE_URL + f'artists/{artistid}', headers=headers)
    
        # store artist json meta data into artists-details
        self.artist_details = response.json()


    def get_artist_details(self):

        # the JSON is already in the necessary format so no need to parse it

        # return the JSON itself
        return self.artist_details
    

class likedSongs():

    def __init__(self):

        # generate headers
        self.headers = generate_headers()

        # request spotify for user's top tracks
        response = get(API_BASE_URL + 'me/tracks?limit=20', headers=self.headers)
    
        # store artist json meta data into artists-details
        self.liked_songs_info = response.json()


    def get_liked_songs_details(self):

        self.liked_songs = []
        count = 0 

        while count < self.liked_songs_info["total"]:
            for song in self.liked_songs_info["items"]:

                try:
                    image_url = song["track"]["album"]["images"][0]["url"]
                except IndexError:
                    image_url = None

                self.liked_songs.append({"name": song["track"]["name"], "artists": song["track"]["artists"], "id": song["track"]["id"], "image": image_url})
                count += 1
            
            # request spotify for user's next page top tracks
            if self.liked_songs_info["next"]:
                response = get(self.liked_songs_info["next"], headers=self.headers)
           
    
            # store artist json meta data into artists-details
            self.liked_songs_info = response.json()
        

        return self.liked_songs

        

