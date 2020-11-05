import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from PIL import Image
from io import BytesIO

#scope = "user-library-read"
scope = "user-read-currently-playing"

client_id = "a831916d73eb4060af3fc90a32d330cd"
client_secret = "6fb575f441e54ec18b5034ffbbe52211"
redirect_uri = "https://127.0.0.1/callback"

def get_song_info():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

    result = sp.current_user_playing_track()
    song = result['item']['name']
    artist = result['item']['artists'][0]['name']
    albumArtUrl = result['item']['album']['images'][0]['url']

    r = requests.get(albumArtUrl)

    i = Image.open(BytesIO(r.content))
    i.save("currently_playing.jpg")
    
    return [song, artist]


"""
TO TRY
 + use requests to download the album cover
 + show all in pygame or matplotlib

"""