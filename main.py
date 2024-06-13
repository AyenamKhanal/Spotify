from requests import post, get

from utils.helpers import access_required, session_expiry, generate_headers
from utils.oauth import API_BASE_URL, app

@app.route('/saved-tracks')
@access_required
@session_expiry
def get_saved_tracks():

    # generate headers
    headers = generate_headers()

    # request data to spotify and store get response
    response = get(API_BASE_URL + 'me/tracks?limit=50', headers=headers)

    # parse json
    saved_tracks = response.json()

    for track in saved_tracks["items"]:
        print(track["track"]["name"])

    return saved_tracks

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
