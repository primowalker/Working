#!/bin/bash

# Test to see if files exist and, if so, copy them, the remove the originals

if ls /Users/jameswalker/Downloads/*.flv 1> /dev/null 2>&1; then 
	rsync -avP /Users/jameswalker/Downloads/*.flv /Users/jameswalker/Dropbox/Misc/Incoming
	rm /Users/jameswalker/Downloads/*.flv
else
	echo "No FLV files found"
fi

if ls /Users/jameswalker/Downloads/*.mp4 1> /dev/null 2>&1; then 
	rsync -avP /Users/jameswalker/Downloads/*.mp4  /Users/jameswalker/Dropbox/Misc/Incoming
	rm /Users/jameswalker/Downloads/*.mp4
else
	echo "No MP4 files found"
fi

if ls /Users/jameswalker/Downloads/*.wmv 1> /dev/null 2>&1; then 
	rsync -avP /Users/jameswalker/Downloads/*.wmv  /Users/jameswalker/Dropbox/Misc/Incoming
	rm /Users/jameswalker/Downloads/*.wmv
else
	echo "No WMV files found"
	fi
