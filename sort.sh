#!/bin/bash
#Desc: Sort
sort -C sorted.txt ;
if [ $? -eq 0 ]; then
	echo "----SORTED----";
else
	echo "----UNSORTED----";
fi
