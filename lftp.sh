#!/bin/bash
####################################
# LFTP SCRIPT
# lftp is another method to get
# files from a server using TLS
# and SSL connections.
# 
####################################
# Please note this is SSL off
# Username:
# Password: 
# Server: 
lftp -e "set ftp:ssl-allow off;" -u USER,PASSWORD HOST

# Implementation for SSL on
lftp -p 21 -e "set ssl:verify-certificate no" -u USER,PASSWORD HOST

# list directories in server
ls -hal

# change directories locally and remotely
# locally -> remotely
lcd 
cd 

# using mget to download all pdf/epub from 
nlist -hal
mget -f -c "*.pdf" "*.epub"

# close the connection
reset
bye
EOT
 
