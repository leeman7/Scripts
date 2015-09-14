#!/usr/bin/python
###########################################################
#	PYTHON GUI
# Date: Tue Sep  8 11:27:26 CDT 2015 
# Author: Lee Nardo
###########################################################

# import Tkinter module for GUI
import Tkinter

# create a new window using Tkinter
window = Tkinter.Tk()

# Format our window
window.geometry("300x300")
window.configure(background="SlateBlue4")
window.title("Finance Calculator")
# window.wm_iconbitmap('calculator.ico')
#photo = Tkinter.PhotoImage(file="finance-banner.gif")

# for our button
def callback():
	

label = Tkinter.Label(window, text="Name:", fg="snow", bg="SlateBlue4", font=("Helvetica", 12))
# allow text entry
ent = Tkinter.Entry(window)
# create a button 
btn = Tkinter.Button(window, text="Enter", command=callback, fg="gray25")

# add widgets to the menu
label.pack()
ent.pack()
btn.pack()

# set window
window.mainloop()

