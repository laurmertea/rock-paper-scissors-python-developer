# Description
# People love to see their results as they're running to their goal.
# So, let's learn how to show the user the score of the game.
# When the game starts, the user should enter his/her name. 
# After that, the program should greet the user and read a file namedrating.txt . 
# This is a file containing current scores for different players. 
# You can see the file format below: 
# it's just lines containing user's name and his/her score divided by a single space.
# Tim 350
# Jane 200
# Alex 400
# If there’s a record for the user with the same name in the file, 
# the program should take his/her rating and use it as a reference point for counting current user’s score 
# (for example, if the user entered name Tim, then his score at the start of the game will be 350). 
# If the user's name isn't written in the file, then your program should count user's score from 0.
# You don't need to write anything in the rating.txt file!
# The program should print user's score when the user enters !rating. 
# For example, if your rating is 0 then the program should print:
# Your rating: 0
# Your program should add 50 points to the player for every draw, 
# 100 for every win, and nothing for losing.
#
# Objectives
# Your program should:
# - output a line `Enter your name: `. 
# - note that the user should enter his/her name on the same line (not the one following the output!)
# - read input specifying the user's name and output a new line Hello, <name>
# - read a file named rating.txt and check if there's a record for the user with the same name; 
#    if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. 
#    if no, start counting user's score from 0.
# - play the game by the rules defined on the previous stages:
# - read user's input
#    if the input is !exit, output Bye! and stop the game
#    if the input is the name of the option, then:
# - pick a random option
# - output a line with the result of the game in the following format (<option> is the name of the option chosen by the program):
#    Lose -> Sorry, but the computer chose <option>
#    Draw -> There is a draw (<option>)
#    Win -> Well done. The computer chose <option> and failed
# - for each draw, add 50 point to the score. For each user's win, add 100 to his/her score. 
#    in case the user loses, don't change the score.
#    if the input corresponds to anything else, output Invalid input
# - play the game again
#
# Examples
# The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.
# Example 1
# Enter your name: > Tim
# Hello, Tim
# > !rating
# Your rating: 350
# > rock
# Sorry, but the computer chose paper
# > paper
# Well done. The computer chose rock and failed
# > scissors
# There is a draw (scissors)
# > !rating
# Your rating: 500
# > !exit
# Bye!
#
# Example 2
# Enter your name: > Chuck
# Hello, Chuck
# > scissors
# There is a draw (scissors)
# > rock
# Well done. The computer chose scissors and failed
# > paper
# Well done. The computer chose rock and failed
# > !rating
# Your rating: 250
# > !exit
# Bye!

import sys
import random

def get_score(name, filepath):
    score = 0
    rating_file = open(filepath, "r")
    line_index = -1

    for line in rating_file:
        rating = line.split()
        if rating[0] == name:
            rating_file.close()
            return [int(rating[1]), line_index + 1]
    rating_file.close()    
    return [score, line_index]

def update_score(name, new_score, filepath):
    rating_file = open(filepath, "r")
    scores = rating_file.readlines()
    rating_file.close()    

    score = get_score(name, filepath)
    rating_file = open(filepath, "w")
    print(score[1])
    if score[1] == -1:
        scores.append(new_score)
    else:
        scores[score[1]] = new_score
    print(scores)
    rating_file.writelines(scores)
    rating_file.close()

def finish_game(name, outcome, score, computer_shape, filepath):
    ratings_file_open = open(filepath, "a")

    if outcome == 'draw':
        print('There is a draw ({})'.format(user_option))
        update_score(name, '{} {}\n'.format(name, score + 50), filepath)
    elif outcome == 'won':
        print('Well done. The computer chose {} and failed'.format(computer_shape))
        update_score(name, '{} {}\n'.format(name, score + 100), filepath)
    else:
        print('Sorry, but the computer chose {}'.format(computer_shape))

    ratings_file_open.close()

def get_option(name, filepath):
    allowed = False

    while not allowed:
        user_option = str(input())
        if user_option in allowed_shapes:
            allowed = True
            return user_option
        else:
            if user_option == '!exit':
                sys.exit('Bye!')
            elif user_option == '!rating':
                print('Your rating: {}'.format(get_score(name, filepath)[0]))
            else:
                print('Invalid input')

name = input("Enter your name: ")
print('Hello, {}'.format(name))

ratings_file = "rating.txt"

allowed_commands = ['!rating', '!exit']
allowed_shapes = ['rock', 'paper', 'scissors']
repeat = True

while repeat == True:
    score = get_score(name, ratings_file)[0]
    user_option = get_option(name, ratings_file)
    computer_shape = random.choice(allowed_shapes)
    outcome = False
    
    if user_option == computer_shape:
        outcome = 'draw'
    else:
        if user_option == 'rock':
            if computer_shape == 'paper':
                outcome = 'lost'
            else:
                outcome = 'won'
        elif user_option == 'paper':
            if computer_shape == 'scissors':
                outcome = 'lost'
            else:
                outcome = 'won'
        else:
            if computer_shape == 'rock':
                outcome = 'lost'
            else:
                outcome = 'won'
    
    finish_game(name, outcome, score, computer_shape, ratings_file)
