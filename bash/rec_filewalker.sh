#!/bin/bash

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

walker ()
{
    echo $1
    for file in $1 ; do
        filepath=$(dirname "${file}")
        filename=$(basename "${file}")
        echo "$file"
        if [ -f "$file" ]; then
            [ ! -L "$2""$filename" ] && ln -s "$file" "$2""$filename"
        fi
        if [ -d "$file" ] ; then
            echo "isdir"
            [ ! -d "$2""$filename" ] && mkdir "$2""$filename" && echo "Madedir"
            walker "$file/*" "$2""$filename"/
        fi
    done
}


walker "/home/cada/Desktop/*" "/home/cada/bajstemp/"

IFS=$SAVEIFS