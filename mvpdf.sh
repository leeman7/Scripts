#!/bin/bash
##########################################################################
#	MOVE NON-ESSENTIAL FILES
# File: move_files.sh
# Author: Lee
# Date: 
# Summary:
# This script searches a directory for certain file types and then
# proceeds to execute a move command them to the indicated folder.
# 
##########################################################################

# Find generic documents with file type: doc, pdf, and text
# then execute a move to indicated directory.
find . -type f -name "*.pdf" -exec mv {} /home/lee/Documents \;
find . -type f -name "*.txt" -exec mv {} /home/lee/Documents \;
find . -type f -name "*.doc" -exec mv {} /home/lee/Documents \;

# Find generic media file types: mp3 and mp4.
# Then execute move all found files to indicated directory.
find . -type f -name "*.mp3" -exec mv {} /home/lee/Music \;
find . -type f -name "*.mp4" -exec mv {} /home/lee/Music \;

# 
find . -type f -name "*.avi" -exec mv {} /home/lee/Music \;
find . -type f -name "*.mkv" -exec mv {} /home/lee/Music \;