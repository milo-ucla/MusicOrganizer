#!/bin/python3
import os
from pprint import pprint
import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials #this is only for non-user API calls
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import asyncio

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

#Documentation: https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope='streaming'

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
async def main():
    result = []
    track_uris = []

    with open('songs.txt') as f:
        tracks_to_add = f.readlines()

    for title in tracks_to_add:
        if not(title == "" or ('#' in title)):
            result = spotify.search(q='track:' + title, type='track',limit=1)
            track_uris.append(result['tracks']['items'][-1]['uri'])

    for uri in track_uris:
        spotify.add_to_queue(uri=uri, device_id=None)
    
    return 0

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())