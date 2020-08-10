#!/usr/bin/env python
import sys
import socket
import getopt
import threading
import subprocess

# define some global variables
listen=False
command=False
upload=False
execute=""
target=""
upload_destination=""
port=0

def usage():
    print "NETCAT TOOL"
    print 
    print "Usage: -t target -p port"
    print "-l --listen              - listen on [host]:[port] for incoming connections"
    print "-e --execute=file        - execute the given file upon receiving a connection"
    print "-c --command             - initialize a command shell"
    print "-u --upload=destination  - upon receiving connection upload a file and write to [destination]"
    print 
    print
    sys.exit(0)

# Client sender takes in our buffer and creates a TCP socket to the target and port
def client_sender(buffer):
    # TCP socket stream
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # connect to our target host with given port
        client.connect((target,port))
        if len(buffer):
            client.send(buffer)
            
        while True:
            # now wait for data back
            recv_len=1
            response=""
            while recv_len:
                data=client.recv(4096)
                recv_len=len(data)
                response+=data # appending to our received data buffer
                if recv_len < 4096:
                    break
            print response,
            
            buffer=raw_input("")
            buffer+="\n"
            client.send(buffer)
                
    except:
        print "[*] Exception Exiting"
        
        # tear down the connection
        client.close()

def server_loop():
    global target
    global port
    
    # if nop target is defined, we listen on all interfaces
    if not len(target):
        target="0.0.0.0" # default ip address
        
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port)) # bind to the target IP and Port
    server.listen(5)
    while True:
        client_socket, addr=server.accept() # accept connections
        # spin off a thread to handle our new client
        client_thread=threading.Thread(target=client_handler,args=(client_socket,))
        client_thread.start()
        
def run_command(command):
    # trim the newline
    command=command.rstrip()
    # run the command and get the output back
    try:
        output=subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        output="Failed to execute command.\r\n"
        
    # send the output back to the client
    return output

def client_handler(client_socket):
    global upload
    global execute
    global command
    # check for upload data
    if len(upload_destination):
        # read in all the bytes and write to our destination
        file_buffer=""
        # keep reading data until none is available
        while True:
            data=client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer+=data
        try:
            file_descriptor=open(upload_destination,"wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()
            # acknowledge that we wrote the file out
            client_socket.send("Successfully saved file to %s\r\n" %upload_destination)
        except:
            client_socket.send("Failed to save file to %s\r\n" %upload_destination)
    
    # check for command execution
    if len(execute):
        # run the command
        output=run_command(execute)
        client_socket.send(output)
        
    # now we go into another loop if a command shell was requested
    if command:
        while True:
            # show a simple prompt
            client_socket.send("<NET:#>")
            # now we receive until we see a linefeed enter key
            cmd_buffer=""
            while "\n" not in cmd_buffer:
                cmd_buffer+=client_socket.recv(1024)
                
            # send back the command output
            response=run_command(cmd_buffer)
            # send back the response
            client_socket.send(response)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
    
    if not len(sys.argv[1:]):
        usage()
        
    # read the commandline options
    try:
        opts, args=getopt.getopt(sys.argv[1:],"hle:t:p:cu",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        
    for o,a in opts:
        if o in ("h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen=True
        elif o in ("-e","--execute"):
            execute=a
        elif o in ("-c","--commandshell"):
            command=True
        elif o in ("-u","--upload"):
            upload_destination=a
        elif o in ("-t","--target"):
            target=a
        elif o in ("-p","--port"):
            port=int(a)
        else:
            assert False,"Unhandled Option"
        
    # are we going to listen or just send data from stdin?
    if not listen and len(target) and port > 0:
        # read in the buffer from the commandline
        # this will block, so send CTRL-D if not sending input
        # to stdin
        buffer=sys.stdin.read()
        
        # send data off
        client_sender(buffer)
        
    if listen:
        server_loop()
           
main()