#!/bin/bash
##########################################################################
#	MOVE NON-ESSENTIAL FILES
# File: move_files.sh
# Author: Lee Nardo
# Date: Sat Sep 26 21:22:22 CDT 2015
# Summary:
#  This script searches a directory for certain file types and then
#  proceeds to execute a move command them to the indicated folder.
# 
##########################################################################

# Find generic documents with file type: doc, pdf, and text
# then execute a move to indicated directory.
find . -type f -name "*.pdf" -exec mv {} /home/lee/Documents \;
find . -type f -name "*.txt" -exec mv {} /home/lee/Documents \;
find . -type f -name "*.doc" -exec mv {} /home/lee/Documents \;
find . -type f -name "*.rft" -exec mv {} /home/lee/Documents \;
find . -type f -name "*.docx" -exec mv {} /home/lee/Documents \;

# Find generic pictures with the file type: jpg, png, and gif
# then move the files to the Pictures directory.
find . -type f -name "*.jpg" -exec mv {} /home/lee/Pictures \;
find . -type f -name "*.png" -exec mv {} /home/lee/Pictures \;
find . -type f -name "*.gif" -exec mv {} /home/lee/Pictures \;

# Find generic media file types: mp3 and mp4.
# Then execute move all found files to indicated directory.
find . -type f -name "*.mp3" -exec mv {} /home/lee/Music \;
find . -type f -name "*.mp4" -exec mv {} /home/lee/Music \;
find . -type f -name "*.flac" -exec mv {} /home/lee/Music \;

# Find generic media file types: avi and mkv.
# These are standard video files that should be moved to videos.
find . -type f -name "*.avi" -exec mv {} /home/lee/Video \;
find . -type f -name "*.mkv" -exec mv {} /home/lee/Video \;
