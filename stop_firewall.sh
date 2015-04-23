#!/bin/bash
################################################################################
#	STOP FIREWALL
# File: stop_firewall.sh
# Author: Lee
# Date: 4/21/2015
# Summary: The following script will stop a Firewall running on a Linux system.
#  The script is meant to bring down the Firewall and flush all chains.
#
################################################################################

# The following lines will flush all chains and all user defined chains.
# Then proceed to stop all chains associated with incoming and outgoing
# connections on the system.
echo "----------WARNING STOPPING FIREWALL----------"
echo "Stopping Firewall now and allowing everyone access..."
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
