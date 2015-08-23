#!/usr/bin/python 
##########################################################################
#	FINANCE CALCULATOR
# Author: Lee Nardo
# Date: 8/21/2015
# Summary: Finance Calculator that computes a monthly statement over the
#  provided information on your accounts. It then creates an output
#  statement in text form  that lists various information regarding
#  your accounts and overview.
#
##########################################################################

# VARIABLES
expenses=0
account_tl=0.0
savings=0.0

print "############################################################"
print "#		      FINANCE CALCULATOR		   #"
print "#			 By Lee Nardo                      #"
print "#						           #"
print "############################################################\n"

income=float(raw_input("1 - Enter Monthly Income: "))
rent=float(raw_input("2 - Enter Monthly Rent: "))
credit_card=float(raw_input("3 - Enter Total Monthly Credit Card Statement: "))
utilities=float(raw_input("4 - Enter Mobthly Utilities (Water+Electricity):"))
misc=float(raw_input("5 - Enter Any additional Expenses: "))
expenses=credit_card+utilities+misc
acct=int(raw_input("6 - Enter Number of Active Accounts (0 for none): "))
percent=int(raw_input("7 - Enter Percent of Income Towards Savings: "))

if percent<0 or percent>100:
	print "Please Enter a Number Between 0 - 100"
else:
	savings=(income*percent)/100

if acct<=0:
	print "Open a Savings Account"

# FUNCTIONS
# net_account function to calculate total of all accounts held
def net_account(acct):
	account=[]
	account_total=0.0
	for x in range(acct):
		account.append(x)
		account[x-1]=float(raw_input("Enter Account %d Total: " % (x+1)))

		if account[x-1]<=-0:
			print "Account Cannot Be Empty"
		elif account[x-1]>0:
			account_total+=account[x-1]
		else:
			print "Wrong Input!"
	return account_total

# net_month_income function to calculate the net income after rent
# expenses and savings
def net_month_income(income,rent,expenses):
	net_month=0
	net_month=income-(rent+expenses)
	return net_month

account_tl=net_account(acct)
print "Your Net Account Total: "
print account_tl

print "Your Net Month Income (Without Savings taken out): "
print net_month_income(income,rent,expenses)
print "Your Net Monthly Income With %d Percent Towards Saving: " % (percent)
print net_month_income(income,rent,expenses)-savings
