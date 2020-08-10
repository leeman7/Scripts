#!/bin/bash
##############################
#   Author: Lee Nardo
#   Date: 8-9-2020
#   Summary: script to unzip
# and unrar multiple files in
# a given directory.
#
#   Todo: recursively handle
# multiple file directories.
#
##############################
DEST=/home/shadow3/Documents/
function unzip_recurse(){
    for zip in `find . -name *.zip`; do
        unzip -o -d "`dirname "$zip"`" "$zip"
    done
}

function unrar_recurse(){
    for rar in `find . -name *.rar`; do 
        unrar e "$rar"; 
    done
}

cd $1
echo "Starting script..."
echo "Unzipping files in $1"
unzip_recurse
echo "Unraring files in $1"
unrar_recurse
echo "Moving files to $DEST"
mv *.epub *.mobi *.pdf $DEST

#sed s/\./-/g *.epub
#find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;
#unrar x *.rar