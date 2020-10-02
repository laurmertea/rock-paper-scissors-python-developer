# Description
# Wasn't that pretty cool?
# But the game is really short so far: nobody plays just a single shot of rock-paper-scissors. 
# We need to do some literally unstoppable game for unstoppable players. 
# Not literally unstoppable, of course: let's implement a way to stop your program.
# Improve your program so it would take an unlimited number of inputs until the user enters `!exit`. 
# After entering 1 the program should print `Bye!` and terminate. 
# Also, let's try to handle invalid inputs: 
# your program should be ready that there may be a typo in user's input, 
# or that a user may just enter complete gibberish instead of a normal command. 
# So, in case the input doesn't correspond to any known command (option name or `!exit`), 
# your program should output the line `Invalid input`.
#
# Objectives
# Your program should:
# - take an input from the user
# - if the input is !exit, output Bye! and stop the game
# - if the input is the name of the option, then:
# - pick a random option
# - output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
#    Lose -> Sorry, but the computer chose <option>
#    Draw -> There is a draw (<option>)
#    Win -> Well done. The computer chose <option> and failed
# - if the input corresponds to anything else, output Invalid input
# - do it all over again
#
# Example
# The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.
# > rock
# Well done. The computer chose scissors and failed
# > paper
# Well done. The computer chose rock and failed
# > paper
# There is a draw (paper)
# > scissors
# Sorry, but the computer chose rock
# > rokc
# Invalid input
# > xit!
# Invalid input
# > !exit
# Bye!

import sys
import random

def get_option():
    allowed = False

    while not allowed:
        user_option = str(input())
        if user_option in allowed_shapes:
            allowed = True
            return user_option
        else:
            if user_option == '!exit':
                sys.exit('Bye!')
            else:
                print('Invalid input')

allowed_commands = ['!exit']
allowed_shapes = ['rock', 'paper', 'scissors']
repeat = True

while repeat == True:
    user_option = get_option()
    computer_shape = random.choice(allowed_shapes)
    
    if user_option == computer_shape:
        print('There is a draw ({})'.format(user_option))
    else:
        if user_option == 'rock':
            if computer_shape == 'paper':
                print('Sorry, but the computer chose {}'.format(computer_shape))
            else:
                print('Well done. The computer chose {} and failed'.format(computer_shape))
        elif user_option == 'paper':
            if computer_shape == 'scissors':
                print('Sorry, but the computer chose {}'.format(computer_shape))
            else:
                print('Well done. The computer chose {} and failed'.format(computer_shape))
        else:
            if computer_shape == 'rock':
                print('Sorry, but the computer chose {}'.format(computer_shape))
            else:
                print('Well done. The computer chose {} and failed'.format(computer_shape))