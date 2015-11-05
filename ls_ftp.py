#!/usr/bin/python
FTP_SERVER = 'ftp.kernel.org'

import ftplib
def test_connection(path, user, email):
	ftp = ftplib.FTP(path, user, email)
	
	#List
	ftp.cwd("/pub")
	print "File List: %s" %path
	files = ftp.dir()
	print files
	
	ftp.quit()

if __name__ == '__main__':
	test_connection(path=FTP_SERVER, user='anonymous', email='nobody@nourl.com')
