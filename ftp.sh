#!/bin/bash
#Simple Automated FTP Session
#open basic ftp session without credentials then quit script
ftp -n [HOST] << EOT
ascii
prompt
passive
user "USER" "PASSWORD"
ls -hal
cd [DIR]
lcd /home
nlist 
mget -f -c "*.pdf" "*.mobi" "*.jpg" "*.opf" "*.epub"
reset
bye
EOT
