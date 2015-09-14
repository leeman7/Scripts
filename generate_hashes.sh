#!/bin/bash 
###########################################################
#	GENERATE HASHES
# Date: Mon Sep  7 10:54:08 CDT 2015
# Author: Lee Nardo
# File: generate_hashes.sh
# Summary: Generates MD5 and SHA1 hashes for all files
#  in the current directory the script is run in.
#
###########################################################

# Generate the MD5 Hashes
ls | sort
echo "##################################################" > hashes.txt
echo "# MD5 HASHES					#" >> hashes.txt
echo "##################################################" >> hashes.txt 
find -exec md5sum "{}" \; >> hashes.txt

# Generate the SHA1 Hashes
# Make sure to append here and not to overwrite the file
echo "##################################################" >> hashes.txt
echo "# SHA1 HASHES                                    #" >> hashes.txt
echo "##################################################" >> hashes.txt
find -exec sha1sum "{}" \; >> hashes.txt

# Come up with a way to remove GIT hooks from the hashes.txt
# sed -e "s/./.git//\n/d" ./hashes.txt
