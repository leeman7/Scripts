#!/bin/bash 
###########################################################
# 	BACKUP SCRIPTS
# Date: Sun Oct  4 02:23:32 CDT 2015 
# Author: Lee Nardo
# File: back_up.sh
# Summary: This script is intended to backup any user
#  defined files that exit within the (~) or home 
#  directory of the current Linux System. Once the files
#  are copied they will be moved to the external mass
#  media storage currently hardcoded in.
###########################################################

# Copy recursively all files from following directory to
# the listed source directory.
echo "======DOCUMENTS====="
# cp -R ~/Documents /media/lee/LEEF\ SUPRA/
echo -ne "=====/---------------  25%\r"
sleep 1
echo "======DOWNLOADS====="
# cp -R ~/Downloads /media/lee/LEEF\ SUPRA/
echo -ne "==========/----------  50%\r"
sleep 1
echo "======MUSIC======"
cp -R ~/Music /media/lee/LEEF\ SUPRA/
echo -ne "===============/-----  75%\r"
sleep 1
echo "======PICTURES======"
cp -R ~/Pictures /media/lee/LEEF\ SUPRA/
echo "======BACKUP COMPLETE======"
