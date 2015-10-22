#!/usr/bin/python
import os
import sys
import re

def main():
		
def pattern(dict):

	#name
	name = re.sub('(- )([^<]+)(<)')
	#email
	email = re.sub('(user=)([^.]+)(&)') + "@txstate.edu"
	#website
	website = "http://" + re.sub('(\cs.*)(.+?)(\">)')
	#research
	research = re.sub('(<p>)([^.]+)(</p>)')
	#school
	school = re.sub('(<p>)([^.]+)(</p>)')
	#return dict[Name][Research][School][Email][Website]

def matcher():

def main():
	dict = {};
	try:
	   with open('*.htm', 'r+') as a, open('*.html', 'r+') as b:

   except IOError as e:
       print 'Operation failed: %s' % e.strerror