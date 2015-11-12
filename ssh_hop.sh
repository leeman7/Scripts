#!/bin/bash

case "$1" in
	1)
		ssh zeus.cs.txstate.edu
		;;
	2)
		ssh athena.cs.txstate.edu
		;;
	3)
		ssh eros.cs.txstate.edu
		;;
	4)
		ssh hercules.cs.txstate.edu
		;;
	5)
		ssh apollo.cs.txstate.edu
		;;
esac
