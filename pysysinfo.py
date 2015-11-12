################################
# Python System Information
# Gets the system information and displays #the info
# back out to the user.
# Author: Lee Nardo
################################
#!/usr/bin/env python
#A System Information Gathering Script
import subprocess

#Command 1 "uname -a"
uname = “uname”
uname_arg = “-a”
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])

#Command 2"df -h"
diskspace = "df"
diskspace_arg = "-h"
print "Gathering Diskspace information %s command:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])