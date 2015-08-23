#!/usr/bin/python
###################################################################
#	REVERSE CIPHER
# Author: Lee Nardo
# Date: 8/22/2015
# Summary: Reverse Cipher script will reverse the order of any
#  phrase or statement in which the user inputs. This is 
#  a basic level of security but still effective for making 
#  Passwords for sites and services.
#
###################################################################

# Prompt user to enter a phrase or statement to be altered
phrase=str(raw_input("Enter Phrase to be Translated: "))
translated=""

i=len(phrase)-1
while i>=0:
	translated+=phrase[i]
	i-=1

print translated 
