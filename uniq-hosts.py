#!/usr/bin/env python3
import os
import glob
import re

list=[]
with open("/etc/hosts",'r') as fin:
        for addr in re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', fin.read()):
                print(addr)