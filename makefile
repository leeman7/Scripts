####################################################################################
#	SCRIPT MAKEFILE
#
#
####################################################################################

# clear the MD5sum for script folder
clean:
	rm MD5sum.txt

# Generate a new MD5sum of current directory. This will create a list of the 
# hashes and the hashes will be saved as a .txt file (MD5sum.txt).
hashes:
	./md5sum.sh
