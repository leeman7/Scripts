#!/usr/bin/python
#############################
#
#
#
#
#############################

#

def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def mul(x,y):
	return x*y

def div(x,y):
	return x/y

while True:
	print "1: ADDITION"
	print "2: SUBTRATION"
	print "3: MULTIPLICATION"
	print "4: DIVISION"
	print "5: QUIT"

	choice=int(raw_input("Enter a number to run  Operand: "))
	a=int(raw_input("Enter 1st Number: "))
	b=int(raw_input("Enter 2nd Number: "))

	if choice==1:
		print "ADDING NUMBERS: "
		print add(a,b)
	elif choice==2:
		print "SUBTRACTING NUMBERS: "
		print sub(a,b)
	elif choice==3:
		print "MULTIPYING NUMBERS: "
		print mult(a,b)
	elif choice==4:
		print "DIVIDING NUMBERS: "
		print div(a,b)
	elif choice==5:
		print "QUITTING PROGRAM"
		exit()
	else:
		print "ENTER A NUMBER 1-5:"
	
