#!/usr/bin/python 
import argparse
import urllib
import re
from datetime import datetime

URL = 'https://www.google.com/finance?q='

def get_quote(symbol):
	content = urllib.urlopen(URL + symbol).read()
	#name = re.search('<title>(.*?)')
	m = re.search('id="ref_(.*?)">(.*?)<', content)
	if m:
		quote = m.group(2)
	else:
		quote = 'No Quote for: ' + symbol
	return quote

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Stock Quote Search')
	parser.add_argument('-symbol', action="store", dest="symbol", required=True)
	given_args = parser.parse_args()
	print "Searching stock quote for symbol '%s'" %given_args.symbol
	print "Stock quote for %s at %s: $%s" %(given_args.symbol, datetime.today(), get_quote(given_args.symbol))
	#print "%s" %name
