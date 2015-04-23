#!/bin/bash
#This script searches a directory for all .mp3 files 
#then moves them  to the Music folder
find . -type f -name "*.mp3" -exec mv {} /home/lee/Music \;
