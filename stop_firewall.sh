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
echo "--Flushing Chains--"
iptables -X
echo "--Flushing User Defined Chains--"
iptables -t nat -F
echo "--Turning Off NAT--"
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
echo "--Accepting All Traffic--"
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
