#!/usr/bin/env python
import socket

thost="www.google.com"
tport=80

# create a socket object DGRAM for UDP
client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect the client
client.connect((thost,tport))

# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response=client.recv(4096)
print response