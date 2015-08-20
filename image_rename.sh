#!/bin/bash
#Filename: image_rename.sh
#Desc: Rename jpg and png files
count=1;
#for any image found while ignoring name with type png or jpg in the directory
for img in `find . -iname '*.png' -o -iname '*.jpg' -o -iname '*gif' -type f -maxdepth 1`
do
	#create a new image name defined here that adds a number to the end and associated type
	new=image-$count.${img##*.}
	echo "Renaming $img to $new"
	mv "$img" "$new"
	let count++
done
