#!/bin/bash
while read host
do
	ping -c 4 "$host" >> output.txt
	echo "Pinging: $host"
done < list.txt
grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.' output.txt > ips.txt
