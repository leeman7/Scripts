#!/bin/bash
#Desc: Illustration of IFS
#Will list what shell a user is operating in
line="root:x:0:0:root:/root:/bin/bash"
oldIFS=$IFS;
#Inline Field Separator set to colon :
IFS=":"
count=0
for item in $line;
do
	[ $count -eq 0 ] && user=$item;
	[ $count -eq 6 ] && shell=$item;
let count++
done;
IFS=$oldIFS
echo $user\'s shell is $shell;
