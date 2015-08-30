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
# Gets the current directory you in.
git init

# Add a new repository to add to your Github
git add .

# Commit the current directory to be pushed.
git commit -m "Initial commit"

# Define the Github directory to push to.
git remote add origin https://github.com/leeman7/Scripts

# Pushes the Repository to
git push -f origin master

