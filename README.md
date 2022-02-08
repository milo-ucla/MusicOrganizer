# MusicOrganizer

## Purpose
Easily manage your spotify library across accounts. Upload an entire library from a txt file, or download your library as a txt file to make a comprehensive list of all your music.

## Set Up
First, run the command

`$python3 -m venv ./.venv` to create a virtual environment in which to store your dependencies. 

Next, run `$source .venv/bin/activate` in the project directory to start your venv. Once you are in a venv, you can install all dependencies for this project by running `$python3 -m pip install -r requirements.txt`. 

After changing any requirements, use `pip freeze > requirements.txt` to update.

Run `./setup.sh` to generate the auxillary text files you can use.

## Scrape Your Local Music Folder
`./get_songs.sh` will work in a folder with the following structure: $TARGET > Subdirectories > Your music files. It can easily be tweaked to your own needs with minimal shell scripting.

## Add to Queue (queue_music.py)
Takes all songs in `songs.txt` as input, treating each line as a Spotify query. Adds top result to user's queue.

## Generate Playlists （generate_playlists.py)
Takes all songs in `songs.txt` as input, treating any word that contains `#` as a playlist title. It will populate each playlist similarly to how it populates the queue. 
Output: Comparison.csv will contain information on song input and output, so you can quickly note which songs did not search correctly. not_found.txt will contain all songs that Spotify couldn't find a result for.

## Maintanence
### Bugs
* Search is a little bit bad
* I had to remove a lot of album art from my songs.txt file, using regex `[a-z0-9_/}/{/-]*.jpg\n` with find-and-replace worked.
* It would be nice to improve search function since Spotify has so many covers/remixes/karaoke versions that contaminate search results.
