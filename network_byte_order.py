#!/usr/bin/python 
###########################################################
#
#
#
###########################################################
 
import socket

def convert_integer():
	data = int(raw_input("Enter a Number to convert Byte Order of: "))

	# 32-bit
	print "Original: %s => Long Host Byte Order: %s, Network Byte Order: %s" % (data, socket.ntohl(data), socket.htonl(data))
	# 16-bit
	print "Original: %s => Short Host Byte Order: %s, Network Byte Order: %s" % (data, socket.ntohs(data), socket.htons(data))
	
if __name__ == '__main__':
	convert_integer()
