#!/bin/sh
#####################################################################
#	UPDATE SCRIPT
# File: update.sh
# Author: Lee
# Summary: This script is intended to be used to quickly update
#  most Linux/UNIX based machines. Used is intended for Ubuntu and
#  Fedora/Red Hat systems.
#
######################################################################

echo "-------------------------CHECKING PACKAGES-------------------------"
sudo apt-get check

echo "-------------------------UPDATING SYSTEM----------------------------"
sudo apt-get -y update

echo "-------------------------UPGRADING SYSTEM---------------------------"
sudo apt-get -y --show-progress upgrade

echo "-------------------------UPGRADING DISTRO---------------------------"
sudo apt-get dist-upgrade
