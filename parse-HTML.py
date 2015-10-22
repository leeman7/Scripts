#!/usr/bin/python
import os
import sys
import re

def pattern(data):
	name = re.match('(- )([^<]+)(<)')

	email = re.match('(user=)([^.]+)(&)') + "@txstate.edu"

	website = "http://" + re.match('(\cs.*)(.+?)(\">)')

	research = re.match('(<p>)([^.]+)(</p>)')

	school = re.match('(<p>)([^.]+)(</p>)')

def main():

	dict = {}

	with open("*.html", 'r') as file:
		data = file.readlines()

	pattern(data)

	file.close()

if __name__ == "__main__": main()
