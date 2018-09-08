#!/bin/sh
if [ -n "$1" ]; then
        var="$1"
    else
        echo
        echo "Usage: get_sum_of_file_sizes.sh <path to search> <file type>"
        echo 
        echo "Example - get_sum_of_file_sizes.sh /home/user/Pictures *.jpg"
        exit
    fi

if [ -n "$2" ]; then
        var="$2"
    else
        echo
        echo "Usage: get_sum_of_file_sizes.sh <path to search> <file type>"
        echo 
        echo "Example - get_sum_of_file_sizes.sh /home/user/Pictures *.jpg"
        exit
    fi


    find $1 -name '$2' -exec du {} \; >> sums.tmp
    awk '{s+=$1} END {print s}' sums.tmp >> total_size
