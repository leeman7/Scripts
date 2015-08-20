#!/bin/bash
#Desc: Sort
sort -C $1 ;
if [ $? -eq 0 ]; then
	echo "----SORTED----";
else
	echo "----UNSORTED----"; sort $1 > $1
fi
