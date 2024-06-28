from extra.queries import topArtists, topTracks, userProfile, searchTracks, searchArtists, trackStats, trackByID, artistByID

def get_home_page_data(track_time_range, artist_time_range):

    # declare a dictionary to return data
    homepage_data= {}

    # get necessary instances
    top_tracks_instance = topTracks(track_time_range)
    top_artists_instance = topArtists(artist_time_range)

    # get artist name and pic
    homepage_data["top_artists"]= top_artists_instance.get_top_artists_info()

    # get top tracks info
    homepage_data["top_tracks"] = top_tracks_instance.get_top_tracks_info()

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

    # get track's data
    searched_songs_data = searched_songs_instance.get_tracks_info()

    return searched_songs_data


def get_artist_search_data(artist):

    # create necessary instance
    searched_artist_instance = searchArtists(artist)

    # get artist's data
    searched_artist_data = searched_artist_instance.get_artist_info()

    return searched_artist_data


def get_track_stats(trackid):

    # create necessary instance
    track_stats_instance = trackStats(trackid)

    # get track's stats
    track_stats = track_stats_instance.get_audio_features()

    return track_stats


def get_track_by_id(trackid):

    # create necessary instance
    track_details_instance = trackByID(trackid)

    # get track's stats
    track_details = track_details_instance.get_track_details()

    return track_details

def get_artist_by_id(artistid):

    # create necessary instance
    artist_details_instance = artistByID(artistid)

    # get artist's stats
    artist_details = artist_details_instance.get_artist_details()

    return artist_details 
