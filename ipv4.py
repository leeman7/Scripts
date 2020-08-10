#!/usr/bin/env python
import socket
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.0.1','192.168.0.1']:
        pack_ip_addr=socket.inet_aton(ip_addr)
        unpack_ip_addr=socket.inet_ntoa(pack_ip_addr)
        print "IP Adress: %s => Packed: %s, Unpacked: %s" %(ip_addr,hexlify(pack_ip_addr),unpack_ip_addr)
        
if __name__=='__main__':
    convert_ip4_address()