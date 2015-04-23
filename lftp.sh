#!/bin/bash
####################################
# LFTP SCRIP
# lftp is another method to get
# files from a server using TLS
# and SSL connections.
# 
####################################
# Please note this is SSL off
# Username: leeman727
# Password: 112091lrn
# Server: 95.22.168.38
lftp -e "set ftp:ssl-allow off;" -u leeman7,112091lrn 95.211.168.38

# Implementation for SSL on
lftp -p 21 -e "set ssl:verify-certificate no" -u leeman7,112091lrn 95.211.168.38

# list directories in server
ls -hal

# change directories locally and remotely
# locally -> remotely
lcd /home/lee/Downloads/
cd /downloads/iptorrents/server/ 

# using mget to download all pdf/epub from 
nlist -hal
mget -f -c "*.pdf" "*.epub"

# close the connection
reset
bye
EOT
 
