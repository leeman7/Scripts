#!/bin/bash 
###########################################################
#	SHA1SUM
# Date: Mon Sep  7 10:28:02 CDT 2015 
# Author: Lee Nardo
# File: sha1sum.sh
# Summary: Runs a SHA1 on the current directory and 
#  displays the output of all file hashes in a text file.
#
###########################################################

# Sort our directory
ls | sort
find -exec sha1sum "{}" \; > SHA1sum.txt

# Testing
