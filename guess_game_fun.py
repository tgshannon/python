""" guess game fun
Guess game with a fun option
In this project the guess game is recast as a function"""

import random

print ("Guess a number game.")

PROMPT = 'What is your guess? '

# New constants
QUIT = 0
QUIT_TEXT = 'q'
QUIT_MESSAGE = 'Thank you for playing'
CONFIRM_QUIT_MESSAGE = 'Are you sure you want to quit (Y/n)? '

# confirm quit function
def confirm_quit():
    """Ask the uer to confirm they want to quit
    default to yes
    Return True (yes, quit) or False (no, don't quit) """
    spam = raw_input(CONFIRM_QUIT_MESSAGE)
    if spam == 'n':
        return False
    else:
        return True

def do_guess_round():
    """Choose a random number, ask the user for a guess
    check whether the guess is true
    and repeat until the number is correct"""
    computers_number = random.randint(1,100)
    number_of_guesses = 0
    while True:
        players_guess = raw_input(PROMPT)
        if players_guess == QUIT_TEXT:
            if confirm_quit():
                return QUIT
            else:
                continue # that is, do next round of loop
        number_of_guesses = number_of_guesses + 1
        if computers_number == int(players_guess):
            print 'Correct!'
            return number_of_guesses
        elif computers_number > int(players_guess):
            print ('Too low')
        else:
            print ('Too high')

while do_guess_round():
    print 'Play again!'
    
