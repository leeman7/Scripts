#!/bin/bash
############################################################# 
#	GIT PUSH
#
# File:
# Date:
# Author:
# Summary:
#   
############################################################
DIR=$1
# Gets the current directory your in.
git init

# Add a new repository to add to your Github
git add .

# Commit the current directory to be pushed.
git commit -m "Updated Repo"

# Define the Github directory to push to.
git remote add origin https://github.com/leeman7/DIR

# Pushes the Repository to
git push -f origin master

