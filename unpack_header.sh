#!/bin/bash
#######################################################
#	UNRAR HEADERS
# File: unpack_header.sh
# Author: Zac
# Date: 4/21/2015
# Summary:
#
#
#######################################################

while true; do
	if dir=$(zenity --title="LinRAR by dExIT" --file-selection --directory); then 
		if [[ ! -d $dir ]]; then
	echo "$dir: Wrong Directory" >&2
else
( cd "$dir" && for f in *.r00; do [[ -f $f ]] || continue; rar e "$f" && rm "${f%00}"[0-9][0-9]; done )
fi
else
	echo "$bold Selection cancelled $bold_off" >&2
		exit 1
fi
	zenity --title="What else...?" --question --text="More work to be done?" || break
done