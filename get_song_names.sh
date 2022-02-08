#!/bin/sh
#the unix path to your text file that will hold directory contents
OUTFILE="./songs.txt"
#Directory should end in ' /* ' for "all files in directory"
DIRECTORY="/mnt/d/Milo/Music/Album/*"
echo '## MY SONGS ##' > $OUTFILE;
for FILE in $DIRECTORY; do echo "# FOLDER: ${FILE}" >> $OUTFILE && ls "${FILE}" >> $OUTFILE ; done

cat $OUTFILE | head -5 && echo ". . ."