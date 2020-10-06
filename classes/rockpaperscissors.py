import sys
import random
import constants

class RockPaperScissors:
    def __init__(self, menu_options=constants.DEFAULT_MENU_OPTIONS, rating_file_path=constants.DEFAULT_RATING_FILE_PATH):
        self.name = str(input(constants.DEFAULT_NAME_INPUT_MESSAGE))
        self.greet_player()
        self.options_str = str(input())
        if self.options_str == "":
            self.options_str = constants.DEFAULT_GAME_OPTIONS
        self.options = self.set_options()
        self.menu = menu_options
        self.rating_file = rating_file_path
        self.user_choice = None
        self.computer_choice = None
        self.score_list = self.get_score()
        self.repeat = True
        self.outcome = None

    def set_options(self, sep=constants.DEFAULT_GAME_OPTIONS_SEP):
        return self.options_str.split(sep)

    def greet_player(self):
        print(constants.DEFAULT_GAME_GREETING_MESSAGE + '{}'.format(self.name))

    def get_score(self):
        score = 0
        rating_file = open(self.rating_file, "r")
        line_index = -1
        for line in rating_file:
            rating = line.split()
            if rating[0] == self.name:
                rating_file.close()
                return [int(rating[1]), line_index + 1]
        rating_file.close()    
        return [score, line_index]

    def update_score(self, new_score):
        rating_file = open(self.rating_file, "r")
        scores = rating_file.readlines()
        rating_file.close()    
        rating_file = open(self.rating_file, "w")
        if self.score_list[1] == -1:
            scores.append(new_score)
        else:
            scores[self.score_list[1]] = new_score
        rating_file.writelines(scores)
        rating_file.close()

    def show_score(self):
        print(constants.DEFAULT_GAME_RATING_MESSAGE + '{}'.format(self.get_score()[0]))

    def exit_game(self, message=constants.DEFAULT_GAME_EXIT_MESSAGE):
        sys.exit(message)

    def get_user_choice(self):
        allowed = False
        while not allowed:
            user_input = str(input())
            if user_input in self.options:
                allowed = True
                self.user_choice = user_input
            else:
                if user_input == '!exit':
                    self.exit_game()
                elif user_input == '!rating':
                    self.show_score()
                else:
                    print(constants.DEFAULT_INVALID_INPUT_MESSAGE)

    def get_choice_relationships(self, choice):
        return self.options[(self.options.index(choice) + 1)::] + self.options[0:self.options.index(choice)]

    def set_outcome(self):
        if self.user_choice == self.computer_choice:
            self.outcome = 'draw'
        else:
            choice_relationships_list = self.get_choice_relationships(self.user_choice)
            if choice_relationships_list.index(self.computer_choice) < len(choice_relationships_list) / 2:
                self.outcome = 'lost'
            else:
                self.outcome = 'won'

    def interpret_outcome(self):
        rating_file = open(self.rating_file, "a")
        if self.outcome == 'draw':
            print('There is a draw ({})'.format(self.user_choice))
            self.score_list[0] += 50
            self.update_score('{} {}\n'.format(self.name, self.score_list[0]))
        else:
            if self.outcome == 'won':
                print('Well done. The computer chose {} and failed'.format(self.computer_choice))
                self.score_list[0] += 100
                self.update_score('{} {}\n'.format(self.name, self.score_list[0]))
            else:
                print('Sorry, but the computer chose {}'.format(self.computer_choice))
        rating_file.close()

    def main(self):
        print(constants.DEFAULT_START_GAME_MESSAGE)
        while self.repeat == True:
            self.computer_choice = random.choice(self.options)
            self.get_user_choice()
            self.set_outcome()
            self.interpret_outcome()

    def __repr__(self):
        return "Game inputs(name: {}, score: {} points, file: {})".format(
            self.name, 
            self.score_list[0], 
            self.rating_file
        )

    def __str__(self):
        return """
        Current inputs: player name is `{}`, player score is `{}`, rating file is saved at `{}`, game options are {}.
        Current choices: player choice is `{}`, computer choice is `{}`.
        """.format(
            self.name, 
            self.score_list[0], 
            self.rating_file,
            self.options,
            self.user_choice,
            self.computer_choice
            )