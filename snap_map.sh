#!/bin/bash
################################################################################
#	SNAP MAP
# File: network_test.sh
# Author: Lee
# Date: 8/19/2015
# Summary: The following script will test an IP address connectivity and 
#  output a log file. The log file will contain information on the network as 
#  well as the the network health connected to that network and what sort of
#  route you have from ISP to their servers.
#
################################################################################

# The lines below will run a Whois on the IP address provided
# This will return any further information on the IP address and whereabouts
echo "-----WHOIS-----"
echo -e "-----WHOIS-----\n" > network_"$1".txt
whois $1 >> network_"$1".txt

# The following will do a traceroute on the IP address provided
echo "-----TRACEROUTE TEST-----"
echo -e "\n\n-----TRACEROUTE TEST-----\n" >> network_"$1".txt
traceroute $1 >> network_"$1".txt

# The following will run a LFT traceroute on the IP address provided
echo "-----LFT TRACE TEST-----"
echo -e "\n\n-----LFT TRACE TEST------\n" >> network_"$1".txt
lft $1 >> network_"$1".txt

# The following will do ping test to the IP address provided
echo "-----PING TEST-----"
echo -e "\n\n-----PING TEST-----\n" >> network_"$1".txt
ping -c 10 $1 >> network_"$1".txt

# The following will run a NS Lookup on all the servers associated with the 
# IP address provided
echo "-----NS LOOKUP-----"
echo -e "\n\n-----NS LOOKUP-----\n" >> network_"$1".txt
nslookup $1 >> network_"$1".txt

# The following line will run a Dig on the IP address provided
# A dig will yield information on the DNS servers for that IP address
echo "-----DIG-----"
echo -e "\n-----DIG-----" >> network_"$1".txt
dig $1 >> network_"$1".txt

# The following will run a nmap on the provided IP address
# Please be warned that this command could give good reason to
# Block your IP address as well as request to provide data 
echo "-----NMAP-----"
echo -e "\n-----NMAP-----" >> network_"$1".txt
sudo nmap -sS $1 >> network_"$1".txt

