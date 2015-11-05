#!/usr/bin/python 
###########################################################
#
#
#
###########################################################

import socket
import sys

def reuse_socket():
	# Create a socket to be used
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Get the old state of the SO_REUSEADDR option
	old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
	print "Old Socket State: %s" %old_state

	# Enable the socket address option
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
	print "New Socket State: %s" %new_state

	# Set local port
	local_port = 8282

	# Create a new socket and bind on local port
	srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	srv.bind(('', local_port))
	srv.listen(1)
	print "Listening on Port: %s" %local_port
	while(1):
		try:
			connection, addr = srv.accept()
			print "Connected By %s:%s" % (addr[0], addr[1])
		except KeyboardInterrupt:
			break
		except socket.error, msg:
			print "%s" % (msg)

if __name__ == '__main__':
	reuse_socket()
