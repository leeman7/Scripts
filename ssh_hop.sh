#!/bin/bash

case "$1" in
	1)
		ssh lrn12@zeus.cs.txstate.edu
		;;
	2)
		ssh lrn12@athena.cs.txstate.edu
		;;
	3)
		ssh lrn12@eros.cs.txstate.edu
		;;
	4)
		ssh lrn12@hercules.cs.txstate.edu
		;;
	5)
		ssh lrn12@apollo.cs.txstate.edu
		;;
esac
