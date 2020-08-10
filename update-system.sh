#!/bin/bash
####################
# UPDATE SYSTEM
# Author: Lee Nardo
# Date: 9-7-2019
####################

apt-get update && apt-get upgrade -y
apt-get install -f
apt autoremove -y
