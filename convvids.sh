#!/bin/bash

# this script is to convert automatically a folder of video files to mp4
# You need to change SRC -- Sourse folder and DEST -- Destination folder
# The mp4 format is 480x270 

SRC=/Volumes/Files/misc/working/to_convert/
DEST=/Volumes/Files/misc/working/MP4/
DEST_EXT=mp4
HANDBRAKE_CLI=HandBrakeCLI

for FILE in `ls $SRC`
do
        filename=$(basename $FILE)
        extension=${filename##*.}
        filename=${filename%.*}

        $HANDBRAKE_CLI -i $SRC/$FILE -o $DEST/$filename.$DEST_EXT --preset="Normal"
done