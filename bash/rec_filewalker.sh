#!/bin/bash


includes=("dox*")
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
DEBUG=0


walker ()
{
    [[ -z "$DEBUG" ]] && echo $1
    for file in $1 ; do
        filepath=$(dirname "${file}")
        filename=$(basename "${file}")
        [[ -z "$DEBUG" ]] && echo "$file"
        if [ -f "$file" ]; then
            [ ! -L "$2""$filename" ] && [[ "$filename" == $3 ]] && ln -s "$file" "$2""$filename" && [[ -z "$DEBUG" ]] && echo Symlink "$filename"
        fi
        if [ -d "$file" ] ; then
            [[ -z "$DEBUG" ]]&& echo "isdir"
            [ ! -d "$2""$filename" ] && mkdir "$2""$filename" && echo "Madedir"
            walker "$file/*" "$2""$filename"/
        fi
    done
}



#walker "/home/cada/Desktop/*" "/home/cada/bajstemp/" "*.@(py|fy)"

IFS=$SAVEIFS