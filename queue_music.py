#! /bin/python3.8
import os, sys
from csv import writer
#from pprint import pprint
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
    not_found = []
    comparison = []

    with open('songs.txt') as f:
        tracks_to_add = f.readlines()

    for title in tracks_to_add[0:100]:
        if not(title == "" or ('#' in title) or ('jpg' in title)):
            title = title.split('.')[0]
            result = spotify.search(q='track:' + title, type='track',limit=1)
            try:
                comparison.append([str(title) , str(result['tracks']['items'][-1]['name'])])
                track_uris.append(result['tracks']['items'][-1]['uri'])
            except:
                print("Exception:",title.rstrip(),"not found")
                not_found.append(title)
    stdout = sys.stdout
    with open('not_found.txt', 'w') as f:
        sys.stdout = f
        for title in not_found:
            print(title)
    sys.stdout = stdout

    with open('comparison.csv', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
        writer_object.writerow(["Original Title", "Spotify Title", "Spotify Artist"])
        # Pass the list as an argument into
        # the writerow()
        for set in comparison:
            writer_object.writerow(set)
        #Close the file object
        f_object.close()
    

                

    #for uri in track_uris:
        #spotify.add_to_queue(uri=uri, device_id=None)
    
    return 0

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())