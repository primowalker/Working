#!/bin/bash

cd /Volumes/Files/Dropbox/Misc/working/BA/

count=1

for i in `ls | sort -n`;do
	mv $i $count-$i
	count=
done

