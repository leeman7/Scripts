#!/usr/bin/python
###########################################################
#	
#
#
###########################################################

# Imports
import sys, os

# Main def
menu_actions = {}

# =========================
#		MENU FUNCTIONS
# =========================

# Main Menu
def main_menu():
	os.system('clear')

	# Print Menu
	print "=========================================\n"
	print "				TRIP APPLICATION			\n"
	print "=========================================\n"
	print "1. Expenses"
	print "2. Travel"
	print "3. Menu 3"
	print "9. Back"
	print "0. Quit"
	choice = raw_input(" >> ")
	exec_menu(choice)

	return

# Execute Menu
def exec_menu(choice):
	os.system('clear')
	ch = choice.lower()
	if ch == '':
		menu_actions['main_menu']()
	else:
		try:
			menu_actions[ch]()
		except KeyError:
			print "Invalid selection, please try again.\n"
			menu_actions['main_menu']()
	return

# Menu 1
def menu1():
	print "Hello Menu 1 !\n"
	print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Menu 1
def menu2():
	print "Hello Menu 2 !\n"
	print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

# Menu 1
def menu3():
	print "Hello Menu 2 !\n"
	print "9. Back"
	print "0. Quit" 
	choice = raw_input(" >>  ")
	exec_menu(choice)
	return

# Back to Main Menu
def back():
	menu_actions['main_menu']()

# Exit Program
def exit():
	sys.exit()

# =========================
#		MENU DEFINITIONS
# =========================

# Menu Definition
menu_actions = {
	'main_menu': main_menu,
	'1': menu1,
	'2': menu2,
	'3': menu3,
	'9': back,
	'0': exit,
}

# =========================
#		MENU PROGRAM
# =========================

# Main Program
if __name__ == "__main__":
# Launch Main Menu
	main_menu()

class Trip(object):
	def __init__(days, lodging, expenses, food, misc):
		self.days = days
		self.lodging = lodging
		self.expenses = expenses
		self.food = food
		self.misc = misc

#	def calculate_trip(self):

class Travel(object):
	def __init__(mpg, speed, tank, miles, time):
		self.mpg = mpg
		self.tank = tank
		self.miles = miles
		self.speed = speed
		self.time = time

	def Travelled(self):
		# Equation for Speed: speed = miles/time
		estimated_speed = miles/time

		# Equation for Distance: miles = speed*time
		distance = speed*time
		estimated_distance

	def displayTrip(self):
		return "Car Stats: %d Miles with %d on %d MPG with a tank of %d Gallons"% (self.miles, self.stops, self.mpg, self.tank)