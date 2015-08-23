#!/usr/bin/python
#####################################################
#	BATTLESHIP (Python)
# Author: Lee Nardo
# Date: 8/21/2015
# Summary: This script starts a small mini-game 
#  called Battleship. In which the script creates
#  a board and randomly hides the ship somewhere on
#  the board. The user is has 7 chances to guess the
#  location and sink the ship before the game ends.
#
#####################################################

from random import randint

board = []

# Battleship board Functions
def generate_board(board):
    for x in range(5):
        board.append(["O"] * 5)

generate_board(board)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Set up Battleship    
print "Let's play Battleship!\n"
print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(7):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            # Print (turn + 1) here!
            print "Turn", turn+1
            print_board(board)
    if turn==6:
        print "Game Over"