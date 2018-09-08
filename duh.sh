#!/bin/bash

list=`du -sk * | sort -n | awk '{print $1}'`
for i in $list;do #	echo $i
	msizes=`bc <<< $i/1024`
	gsizes=`bc <<< $i/1024/1024`
	
	if [ "$1" = "M" ]
	then
		echo "${msizes}M"
	else
		echo "${i}K"
	fi
	if [ "$1" = "G" ]
	then
		echo "${gsizes}G"
	else
		echo "${i}K"
	fi
	
done
