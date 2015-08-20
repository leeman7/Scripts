#!/bin/sh
#Move all files from the Downloads folder containing the defined file endings
for file in /home/lee/Downloads; do
	find . -type f -name "*.deb" -exec mv -v {} /home/lee/Dropbox \;
	find . -type f -name "*.pdf" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.txt" -exec mv -v {} /home/lee/Dropbox \;
	find . -type f -name "*.rtf" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.epub" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.mobi" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.ppt" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.pptx" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.torrent" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.iso" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.zip" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.tar.gz" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.jpg" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.png" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.gif" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.mp3" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.flac" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.avi" -exec mv {} /home/lee/Dropbox \;
	find . -type f -name "*.mkv" -exec mv {} /home/lee/Dropbox \;
done
exit 0
