# Project Title: Statstify

# Video Demo:  
https://www.youtube.com/watch?v=xiUjepA6zVE


# Description:

## Summary of the project:
This project, named "Statstify," utilizes the Spotify API to provide users with personalized music statistics.

Users can log in to Statstify using their Spotify account. Upon successful login, they can view their top 5 tracks and artists, categorized by different time ranges: short term (1 month), medium term (6 months), and long term (1 year). Additionally, users can access detailed information about these tracks and artists.

Statstify also offers a search functionality, allowing users to look up individual tracks and artists by clicking the "Song Stats" and "Artist Stats" links to view detailed statistics.

I have implemented OAuth to authorize users and obtain the access token required for making API calls.


## File details:

### 1. extra:
This directory mostly has helper files
    
#### helpers.py:
This file contains some helper functions.

It has access_required function to check if the user has access to view the pages other than the login page. 
It also has session_expiry function that checks if the access token has been expired. 

It also has apology function that renders "apology.html" template when there is some error while loading a page.

It has other simple funtions to convert the integers returned by spotify into their specific value. 

#### helpers2.py:
It has some functions that return data extracted from the JSON provided by spotify api by creating instances of specific classes.

#### queries.py
This file contains api calls.

I have made multiple classes to make a special type of API call.

userProile() requests for username and user profile picture

topTracks() requests for user's top tracks

topArtists()requests for user's top artists

searchTracks() requests for search results for tracks that the user makes the query for.

searchArtists() requests for search results for artists that the user makes the query for.

trackStats() requests for audio features of tracks

trackByID() requests for track details by providing the track's ID.

artistByID() requests for artist details by providing the artist's ID.

### static
This directory has static css and js files.

#### script.js
This file has a small amount of code. It makes sure that the value is auto submitted after the user makes changes to the time-period in the homepage.

#### style.css
This file contains all the styling for my website.

### templates
This directory contains all the html templates for my websites.

#### apology.html:
This has apology message

#### artist-stats-details.html:
This displays the stats for each artist

#### song-stats-details.html:
This displays the stats for each track

#### artist-stats.html
This provides the search bar to look up artists.

#### artists-list.html
This displays all the artists that are the result of the query from the user.

#### home.html
This is the homepage of my website. This contains all the information about the user's top tracks and artists. It also has navigation bar to go to other pages.

#### layout1.html
This is the basic layout that I have used in almost all of my web pages.

#### song-stats.html
This provides the search bar to look up tracks.

#### songs-list.html
This displays all the trakcs that are the result of the query from the user.

#### successful.html
This displays that the autorization has been successful

#### test.html
This was used to test some code while developing the website.

#### welcome.html
This page welcomes the user and asks for them to log in using Spotify.

#### .env
This contains client id and client secret. 

### app.py
This is the main file of my project.

This file initializes the flask app.

It has routes that the user is directed to.

#### '/'
This sends the user to the welcome page.

#### '/login'
This provides scope with other necessary parameters to spotify to ask the user to autorize to fetch their data and request for 'code'.

#### 'callback'
It the authorization was unsuccessful, an error messge is displayed.
Otherwise, 'code' is attained and it can be used to request for access token to make further api calls.
After all this, the user is sent to the successful.html page.

#### '/refresh-token':
This route check if the access token has expired and uses refresh token to get another access token.

#### '/home':
This route gets the necessary data to display user's top tracks and artists and renders home.html


#### 'song-stats':
This route renders song-stats.html if the request method is get.
If the request method is post, it gets search results and renders songs-list.html

#### 'artist-stats':
This route renders artist-stats.html if the request method is get.
If the request method is post, it gets search results and renders artists-list.html

#### '/artist-stats-details':
This route gets the necessary details about certain artist and renders artist-stats-detail.html to display the data.

#### '/track-stats-details':
This route gets the necessary details about certain track and renders track-stats-detail.html to display the data.


