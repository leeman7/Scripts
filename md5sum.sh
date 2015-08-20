#/bin/bash
#filename: MD5sum.sh
PIDARRAY=()
ls | sort
find -exec md5sum "{}" \; > MD5sum.txt|sort

#for file in $DIR; do
#	md5sum $file & PIDARRAY+=("$!")
#done
#wait ${PIDARRAY[@]}
