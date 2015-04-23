#!/bin/sh
#################################################################
#	CLEAN PACKAGES
# File:clean.sh
# Author: Lee
# Summary: This script is intended to be used for most Ubuntu
#  Linux based systems. The script will check, clean, remove,
#  and auto-clean all missin/broken package dependencies.
#
#################################################################

# The following line will check the system for any changes and
# create a log of all the changes that need to made to the system.
sudo apt-get -y check

# The lines below will clean the memory of any packages
# that may exist in the system  that are leftover from
# system update.
sudo apt-get --list-cleanup clean
sudo apt-get -y autoclean

# The following lines will remove/fix/repair broken/missing
# dependencies. These lines are meant to removed any packages
# that are incomplete or missing.
sudo apt-get -y -f -m  remove
sudo apt-get -yV autoremove

