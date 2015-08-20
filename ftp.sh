#!/bin/bash
#Simple Automated FTP Session
#open basic ftp session without credentials then quit script
ftp -n 198.27.85.96 << EOT
ascii
prompt
passive
user "my_server727" "ServerPassword"
ls -hal
cd /Shared/Anthony\ Ryan\ -\ Raven's\ Shadow\ 1+2/Tower\ Lord
lcd /home/lee/Downloads
nlist 
mget -f -c "*.pdf" "*.mobi" "*.jpg" "*.opf" "*.epub"
reset
bye
EOT
