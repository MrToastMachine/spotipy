import spotipy
import spotipy.util as util

import requests
from io import BytesIO
from PIL import Image

def convertToMinSec(time):
    mins = round(time // 60)
    secs = round(time % 60)
    return f"{mins}:{str(secs).zfill(2)}"

def getSongInfo(username):
    scope = 'user-read-currently-playing'
    token = util.prompt_for_user_token(username,
                           scope,
                           client_id='a831916d73eb4060af3fc90a32d330cd',
                           client_secret='6fb575f441e54ec18b5034ffbbe52211',
                           redirect_uri='https://127.0.0.1/callback')
    if token:
        sp = spotipy.Spotify(auth=token)
        result = sp.current_user_playing_track()

        if result == None:
            print("No Song is currently playing!")
        else:
            song = result["item"]["name"]
            artist = result["item"]["album"]["artists"][0]["name"]
            imageURL = result["item"]["album"]["images"][0]["url"]

            timeLeft = (result["item"]["duration_ms"]/1000) - (result["progress_ms"]/1000)
            response = requests.get(imageURL)
            image = Image.open(BytesIO(response.content))
            
            actualTime = convertToMinSec(timeLeft)

            print(f"Song: {song}")
            print(f"Artist: {artist}")
            print(f"Time Left: {actualTime}")

            ##DISPLAY IMAGE HERE
    else:
        print("Could not get token!")

getSongInfo('11120906237')