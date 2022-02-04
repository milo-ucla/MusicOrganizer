#!/bin/sh
#the unix path to your text file that will hold directory contents
OUTFILE=""
DIRECTORY=""
echo '## MY DIRECTORY FILES ##' > $OUTFILE;
for FILE in $DIRECTORY; do echo "[FOLDER: ${FILE}]" >> $OUTFILE && ls $FILE >> $OUTFILE ; done

cat $OUTFILE | head -5 && echo ". . ."