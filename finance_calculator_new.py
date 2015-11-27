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

import sys, os

class Account(object):

	def __init__(self, income, rent, expenses, acct, brokerage):
		self.income = income
		self.rent = rent
		self.expenses = expenses
		self.acct = acct
		self.brokerage = brokerage

	# display Menu
	def menu(self, income, rent, expenses, acct, brokerage):

		print "############################################################"
		print "#		      FINANCE CALCULATOR		   #"
		print "#			 By Lee Nardo                      #"
		print "#						           #"
		print "############################################################\n\n"

		# Tell User to get a job if they dont have income
		income=float(raw_input("1 - Enter Monthly Income: "))
		if income<=0:
		print "ERROR: Please get a Job!"

		# Accept User Percent
		percent=int(raw_input("2 - Enter Percent of Income Towards Savings: "))

		# Accept User Rent (Rent can be equal to 0)
		rent=float(raw_input("3 - Enter Monthly Rent: "))

		# CC can be 0
		credit_card=float(raw_input("4 - Enter Total Monthly Credit Card Statement: "))

		utilities=float(raw_input("5 - Enter Mothly Utilities (Water+Electricity): "))

		misc=float(raw_input("6 - Enter Any additional Expenses: "))

		# Calculate expenses
		expenses=credit_card+utilities+misc

		# User should have an account so make sure
		acct=int(raw_input("7 - Enter Number of Active Accounts (0 for none): "))

		brokerage=int(raw_input("8 - Enter Number of Brokerage Accounts (0 for none): "))

	# net_account function to calculate total of all accounts held
	def net_account(acct):
		account=[]
		account_total=0.0
		print "\n----------------------------------------------\n 7 - Calculating Accounts\n----------------------------------------------\n"
		for x in range(acct):
			account.append(x)
			account[x-1]=float(raw_input("Enter Checking/Saving Account %d Total: " % (x+1)))

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

	def brokerage_net_worth(brokerage):
		diff=0
		net_brokerage=0.0
		print "\n----------------------------------------------\n 8 - Calculating Brokerage Account\n----------------------------------------------\n"
		for x in range(brokerage):
			start=float(raw_input("Enter Month Starting Total: "))
			end=float(raw_input("Enter Month Ending Total: "))
			diff=start-end
			net_brokerage+=end
			if diff<0:
				print "You went Positive on this account"
			elif diff==0:
				print "You Broke Even on this account"
			else: 
				print "You went Negative on this account"
		return net_brokerage

##########################################################################
# VARIABLES
##########################################################################

expenses=0
account_tl=0.0
brokerage_tl=0.0
savings=0

##########################################################################
# Accept User Input
##########################################################################

##########################################################################
# TEST CASES
##########################################################################

# Check expenses
if expenses<0:
	print "ERROR: Cannot have Negative expenses!"

# Check brokerage
if brokerage>5 or brokerage<0:
	print "ERROR: Too many accounts or Invalid Input!"

# Check percent
if percent<0 or percent>100:
	print "Please Enter a Number Between 0 - 100"
else:
	savings=(income*percent)/100

# Check acct
if acct<=0:
	print "ERROR: Open a Savings Account"

##########################################################################
# FUNCTIONS
##########################################################################

##########################################################################
# OUTPUT
##########################################################################

# Call Functions/Initializations
account_tl=net_account(acct)
brokerage_tl=brokerage_net_worth(brokerage)
month_tl=net_month_income(income,rent,expenses)
month_sv=month_tl-savings
net_worth=month_sv+account_tl+brokerage_tl

print "\n----------------------------------------------\n 1-8 Calculating Totals\n----------------------------------------------\n"
# Output the uses Net Account Worth
print "Your Net Account Total: $%.2f " % account_tl
# Oupurt Net Brokerage Account Worth
print "Your Net Brokerage Account Total: $%.2f " % brokerage_tl
# Output Net Monthly Income without Savings deduction
print "Your Net Month Income (Without Savings taken out): $%.2f" % month_tl
# Output Net Monthly Income with Savings deducted
print "Your Net Monthly Income With %d Percent Towards Saving: $%.2f " % (percent, month_sv)
print "Your Net Worth: $%.2f" % net_worth
