#!/bin/bash
#This script searches a directory for all .pdf files 
#then moves them  to the Music folder
#find "." type of file with name ending in "anything file type ending" then execute move #f$
find . -type f -name "*.pdf" -exec mv {} /home/lee/Dropbox/Books \;
find . -type f -name "*.txt" -exec mv {} /home/lee/Dropbox/resources \;
find . -type f -name "*.mp3" -exec mv {} /home/lee/Dropbox/Music \;
find . -type f -name "*.epub" -exec mv {} /home/lee/Dropbox/Books \;
find . -type f -name "*.tar.gz" -exec mv {} /home/lee/Dropbox/packages \;
find . -type f -name "*.zip" -exec mv {} /home/lee/Dropbox/packages \;
find . -type f -name "*.jpg" -exec mv {} /home/lee/Dropbox/Photos \;
find . -type f -name "*.png" -exec mv {} /home/lee/Dropbox/Photos \;
find . -type f -name "*.gif" -exec mv {} /home/lee/Dropbox/Photos \;
find . -type f -name "*.ppt" -exec mv {} /home/lee/Dropbox/School \;

