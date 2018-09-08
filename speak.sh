#!/bin/bash

if [ -n "$1" ]; then
        var="$1"
    else
        echo
        printf 'Usage: speak.sh <"phrase to speak">'
        echo 
        printf 'Example - speak.sh "I like fish heads"'
        echo
        exit
    fi

voices=`say -v ? | awk '{print $1}'`
phrase=$1

for i in $voices;do
	echo "This is $i speaking"
	echo
	say -v $i $phrase
done
