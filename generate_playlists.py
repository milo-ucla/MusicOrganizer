#! /bin/python3.8
import os, sys
from csv import writer
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
USERNAME = os.getenv('SPOTIPY_USERNAME')

#Documentation: https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope='playlist-modify-private'
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

async def main():
    result = []
    track_ids = []
    not_found = []
    comparison = []
    playlist_title = ""

    with open('songs.txt') as f:
        tracks_to_add = f.readlines()

    for title in tracks_to_add:
        if ('#' in title):
            playlist_title = title.split('/')[-1].rstrip()
            playlist = spotify.user_playlist_create(USERNAME, playlist_title, public=False, collaborative=False, description='')
            playlist_id = playlist['id']
            #print("Playlist title: " + str(playlist_title))
        elif not(title == "" or ('jpg' in title)):
            title = title.split('.')[0]
            result = spotify.search(q='track:' + title, type='track',limit=1)
            try:
                comparison.append([str(title) , str(result['tracks']['items'][-1]['name'])])
                track_ids.append([playlist_id, result['tracks']['items'][-1]['uri']])
            except:
                #print("Exception:",title.rstrip(),"not found")
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
        writer_object.writerow(["Album","Original Title", "Spotify Title", "Spotify Artist"])
        # Pass the list as an argument into
        # the writerow()
        for set in comparison:
            writer_object.writerow(set)
        #Close the file object
        f_object.close()
    
    for item in track_ids:
        spotify.playlist_add_items(playlist_id=item[0], items=[item[1]], position=None)
    return 0

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
