# Description
# Well, now let's do something real. Nobody wants the game where you always lose.
# Using the power of the random module, we'll make a truly interesting game.
# You should write a program that reads input from the user, chooses a random option and then says who won, the user or the computer.
# There are a few examples below, providing output for any outcome (<option> is the option chosen by your program):
# Lose -> Sorry, but the computer chose <option>
# Draw -> There is a draw (<option>)
# Win -> Well done. The computer chose <option> and failed
#
# Objectives
# Your program should:
# - read user's input specifying the option that user has chosen
# - choose a random option
# - compare the options and determine the winner
# - output a line depending on the result of the game:
#    Lose -> Sorry, but the computer chose <option>
#    Draw -> There is a draw (<option>)
#    Win -> Well done. The computer chose <option> and failed
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. 
# Notice that it's not the part of the input.
# 
# Example 1
# > rock
# Well done. The computer chose scissors and failed
#
# Example 2
# > scissors
# There is a draw (scissors)
#
# Example 3
# > paper
# Sorry, but the computer chose scissors

import random

allowed_shapes = ['rock', 'paper', 'scissors']
computer_shape = random.choice(allowed_shapes)
allowed = False

while not allowed:
    user_shape = str(input())
    if user_shape in allowed_shapes:
        allowed = True

if user_shape == computer_shape:
    print('There is a draw ({})'.format(user_shape))
else:
    if user_shape == 'rock':
        if computer_shape == 'paper':
            print('Sorry, but the computer chose {}'.format(computer_shape))
        else:
            print('Well done. The computer chose {} and failed'.format(computer_shape))
    elif user_shape == 'paper':
        if computer_shape == 'scissors':
            print('Sorry, but the computer chose {}'.format(computer_shape))
        else:
            print('Well done. The computer chose {} and failed'.format(computer_shape))
    else:
        if computer_shape == 'rock':
            print('Sorry, but the computer chose {}'.format(computer_shape))
        else:
            print('Well done. The computer chose {} and failed'.format(computer_shape))
