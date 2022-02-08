# MusicOrganizer

## Purpose
Easily manage your spotify library across accounts. Upload an entire library from a txt file, or download your library as a txt file to make a comprehensive list of all your music.

## Set Up
First, run the command

`$python3 -m venv ./.venv` to create a virtual environment in which to store your dependencies. 

Next, run `$source .venv/bin/activate` in the project directory to start your venv. Once you are in a venv, you can install all dependencies for this project by running `$python3 -m pip install -r requirements.txt`. 

After changing any requirements, use `pip freeze > requirements.txt` to update.

## Maintanence
### Bugs
* Search is a little bit bad
* I had to remove a lot of album art from my songs.txt file, using regex `[a-z0-9_/}/{/-]*.jpg\n` with find-and-replace worked.