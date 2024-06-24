from extra.queries import topArtists, topTracks, userProfile, searchTracks

def get_home_page_data(track_time_range, artist_time_range):

    # declare a dictionary to return data
    homepage_data= {}

    # get necessary instances
    top_tracks_instance = topTracks(track_time_range)
    top_artists_instance = topArtists(artist_time_range)

    # get artist name and pic
    homepage_data["artists"] = top_artists_instance.get_top_artists()
    homepage_data["artists_profile_pics"] = top_artists_instance.get_profile_pictures()

    # get track name and pic
    homepage_data["tracks"] = top_tracks_instance.get_top_tracks()
    homepage_data["covers"] = top_tracks_instance.get_album_cover()

    return homepage_data


def get_user_profile():
    
    # declare dictionary to store user profile data
    user_profile_data = {}
    
    # create a instance
    user_profile_instance = userProfile()

    # get user's name and pic
    user_profile_data["user_name"] = user_profile_instance.get_user_name()
    user_profile_data["user_profile_pic"] = user_profile_instance.get_user_profile_pic()

    return user_profile_data


def get_song_search_data(track):

    # create necessary instance
    searched_songs_instance = searchTracks(track)

    # get track's name
    searched_songs_data = searched_songs_instance.get_tracks_info()

    return searched_songs_data
