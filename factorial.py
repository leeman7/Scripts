#!/usr/bin/python 

import sys

n=int(raw_input("Enter a Number: "))

def Factorial(n):
	result = 1
	for x in range (1,n):
		result *= x
	print "Factorial is ", result
	return result
