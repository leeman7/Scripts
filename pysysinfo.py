#!/usr/bin/python
import subprocess
uname="uname"
uname_arg="-a"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])

#Command 2"df -h"
diskspace = "df"
diskspace_arg = "-h"
print "Gathering Diskspace information %s command:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])
