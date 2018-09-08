#!/bin/bash
# Color List:
#
# Foreground Colors
# 30m = Black
# 31m = Red
# 32m = Green
# 33m = Yellow
# 34m = Blue
# 35m = Purple
# 36m = Cyan
# 37m = White
# Background Colors
# 40m = none
# 41m = Red
# 42m = Green
# 43m = Yellow
# 44m = Blue
# 45m = Purple
# 46m = Cyan
# 47m = White
if [ -n "$1" ]; then
        var="$1"
else
    echo
    echo "Usage: <get> <term>"
    echo
        echo "The get script will search for unix commands based on keywords/tags."
        echo "To find out how to get the top 10 processes using swap space,"
        echo "you can search for one out of several keywords/tags."
        echo
    echo "Example - get swap"
    exit
fi
keyword=$1
echo
grep $keyword ~/bin/cmd_list.dat | awk -F: '{print $2 "\033[1;37m" "\033[41m" "\n" $3 "\033[0m" "\n"}'
