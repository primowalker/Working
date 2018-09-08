 if [ -n "$1" ]; then
        var="$1"
    else
        echo
        echo "Usage: emot.sh <search term>"
        echo 
        echo "Example - emot.sh lol"
        exit
    fi

grep $1 DA_emoticons
