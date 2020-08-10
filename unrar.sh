#!/bin/bash
find /path/to/downloads -name '*.rar' -execdir unrar e -o- {} \;
