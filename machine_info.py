#!/usr/bin/python 
###########################################################
#	IP Search
# File: ip_search.py
# Author: Lee Nardo
# Date: Sat Sep 26 21:47:04 CDT 2015 
# Summary: 
#  This script is used to give the user a quick summary
#   of the current network they are on. Then prompt the
#  user if they would like to look up a certain address
#  or domain name.
#
###########################################################
 
import socket
from binascii import hexlify

def machine_info():
	host_name=socket.gethostname()
	ip_address=socket.gethostbyname(host_name)
	print "-------------LOCAL HOST---------------"
	print "Host Name: %s" % host_name
	print "IP Address: %s" % ip_address

def remote_info():
	remote_host=str(raw_input("Enter Host Name: "))
	try:
		print "------------SEARCHED HOST-------------"
		print "Host Name: %s" % (remote_host)
		print "IP Address: %s" %socket.gethostbyname(remote_host)
	except socket.error, err_msg:
		print "%s: %s" % (remote_host, err_msg)

def convert_ip4_address():
	for ip_addr in ['127.0.0.1', '192.168.0.1']:
		packed_ip_addr = socket.inet_aton(ip_addr)
		unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
		print "IP Address: %s => Packed: %s, Unpacked: %s" %(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)

def find_service_name():
	protocolname='tcp'
	print "-------------PORTS OPEN--------------"
	for port in [80, 25]:
		print "Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))
	print "Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))

find_service_name()
machine_info()
convert_ip4_address()
remote_info()
