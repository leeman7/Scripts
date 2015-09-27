#!/bin/bash
############################################################# 
#	GIT PUSH
#
# File:get-push.sh
# Date:Sat Sep 26 21:39:29 CDT 2015
# Author:Lee Nardo
# Summary:
#  Push to a repository of your choice or creates a new
#   repository if it does not already exist. It will push
#   all files within your current working directory.
############################################################
DIR=$1
# Gets the current directory your in.
git init

# Add a new repository to add to your Github
git add .

# Commit the current directory to be pushed.
git commit -m "Updated Repository"

# Define the Github directory to push to.
git remote add origin https://github.com/leeman7/DIR

# Pushes the Repository to
git push -f origin master
