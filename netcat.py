#!/usr/bin/python

import socket
import sys
import getopt
import threading
import subprocess

# GLOBALS
listen = False
command = False
upload = False
execute = ""
target = ""
upload_des = ""
port = 0

def usage():
	print "Net Tool"
	print 
	print "Usage: command.py -t target_host -p port"
	print "-l listen"
	print "-e exeute"
	print "-c --command"
	print "-u --upload=destination"
	print
	print
	sys.exit()
	
def main():
	global listen
	global port
	global execute
	global command
	global upload_des
	global target

	# Read Command line optioons
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu", ["help", "listen", "execute", "target", "port", "command", "upload"])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-l","--listen"):
			listen = True
		elif o in ("-e","--execute"):
			execute = a
		elif o in ("-c", "--commandshell"):
			command = True
		elif o in ("-u", "--upload"):
			upload_des = a
		elif o in ("-t", "--target"):
			target = a
		elif o in ("-p", "--port"):
			port = int(a)
		else:
			assert False, "Unhandled Option"

# Are we going to listen or just send data from stdin?
	if not listen and len(target) and port > 0:
		buffer = sys.stdin.read()
		client_sender(buffer)
	
	if listen:
		server_loop()

def client_sender(buffer):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((target, port))

		if len(buffer):
			client.send(buffer)
		while True:
			recv_len = 1
			response = ""
			while recv_len:
				data = client.recv(4096)
				recv_len = len(data)
				response+= data
				if recv_len < 4096:
					break
			print response,

			buffer = raw_input("")
			buffer+="\n"
			client.send(buffer)

	except:
		print "[*] Exception Exiting"
		client.close()

def server_loop():
	global target

	if not len(target):
		target = "0.0.0.0"
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((target,port))
	server.listen(5)
	
	while True:
		client_socket, addr = server.accept()

		client_thread = threading.Thread(target=client_handler,args=(client_socket,))
		client_thread.start()

def run_command(command):
	command = command.rstrip()

	try:
		output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
	except:
		output = "Failed to execute command.\r\n"

	return output

def client_handler(client_socket):
	global upload
	global execute
	global command

	if len(upload_des):
		file_buffer = ""
		while True:
			data = client_socket.recv(1024)
			if not data:
				break
			else:
				file_buffer+=data
		try:
			file_descriptor = open(upload_destination,"wb")
			file_descriptor.write(file_buffer)
			file_descriptor.close()

			client_socket.send("Successfully saved file to %s\r\n" % upload_des)
		except:
			client_socket.send("Failed to save file %s\r\n" % upload_des)

	# check command for execute
	if len(execute):
		output = run_command(execute)
		client_socket.send(output)

	if command:

		while True:
			client_socket.send("<NETCAT:>")
			cmd_buf = ""
			while "\n" not in cmd_buf:
				cmd_buf += client_socket.recv(1024)
			
			response = run_command(cmd_buf)
			client_socket.send(response)

main()
