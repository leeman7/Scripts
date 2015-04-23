#!/bin/bash
#Filename: success_test.sh
#For testing your commands change whats in parenthesis after CMD
CMD="ls -l" #Substitute with command for which you need to test the
exit status 0
$CMD
if [ $? -eq 0 ];
then
	echo "$CMD executed successfully"
else
	echo "$CMD terminated unsuccessfully"
fi