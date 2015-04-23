#!/bin/bash
#Simple Automated FTP Session
#open basic ftp session without credentials then quit script
ftp -n [SERVERADDRESS] << EOT
ascii
prompt
passive
user "USERNAME" "PASSWORD"
ls -hal
cd /
lcd /home/
nlist 
mget -f -c "*.pdf" "*.epub"
reset
bye
EOT
