import importlib
import re
from Games import GuessGame, MemoryGame, CurrencyRouletteGame
from Scores.Score import add_score
from Utils import screen_cleaner, transfer_and_clear_file


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).", "\n", "Here you can find many cool games to play.")


def load_game(name):
    print("Please choose a game to play:", "\n",
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
          "\n", "2. Guess Game - guess a number and see if you chose like the computer", "\n",
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_selection = input("please enter your selection: ")
    while not re.search("^[1-3]$", game_selection):
        game_selection = input("please enter only numbers from 1 to 3 for game selection: ")

    difficulty = input("please enter only numbers for difficulty selection: ")
    while not re.search("^[1-5]$", difficulty):
        difficulty = input("please enter only numbers from 1 to 5 for difficulty selection: ")

    results = False
    game_module =''

    difficulty_level = int(difficulty)
    if int(game_selection) == 1:
        results = MemoryGame.play(difficulty_level)
        game_module = 'MemoryGame'
    elif int(game_selection) == 2:
        results = GuessGame.play(difficulty_level)
        game_module = 'GuessGame'
    elif int(game_selection) == 3:
        results = CurrencyRouletteGame.play(difficulty_level)
        game_module = 'CurrencyRouletteGame'

    if results:
        add_score(difficulty_level)
        screen_cleaner()
        repeat_menu(name, difficulty_level, prev_game=game_module, prev_difficulty=difficulty_level)


def repeat_menu(user_name, lvl_sel, prev_game=None, prev_difficulty=None):
    while True:  # start a loop that runs indefinitely
        # We made a variable named repeat for the repeat menu
        repeat = input("""Do you want to PLAY AGAIN the SAME GAME with the SAME DIFFICULTY, 
                         OR you want to PLAY ANOTHER GAME?
                                        To CONTINUE PLAYING the SAME GAME     
                                  with the SAME DIFFICULTY please type in >>>:   y.
                                                                                      =========      
                                        To Choose ANOTHER GAME please type in:   n.  
                                                                                  =============
                                        If you want to EXIT please type in:      q. 
                                                                               ================                  
                        >>> YOUR ANSWER HERE >>>:  """)

        if repeat == "" or repeat not in ['y', 'n',
                                          'q']:  # check if the user input is empty or not one of the expected values in the list
            print('Invalid input, try again!')  # Will display an error message in case the input is not in the list
            screen_cleaner()  # this is the function that we imported from Utils module that will clear the screen with 0.7 seconds sleep
            repeat_menu(user_name, lvl_sel, prev_game,
                        prev_difficulty)  # call the "repeat_menu" function with the same arguments

        if repeat.lower().startswith('y'):  # check if the user input starts with 'y' ( to play the same game again)
            if prev_game is None or prev_difficulty is None:  # check if there is a previous game and difficulty level
                print(
                    "There is no previous game to play again. Please choose another game.")  # if there is no game will print this message
                repeat_menu(user_name,
                            lvl_sel)  # if the prev_game and prev_difficulty = None than it will call the repreat_menu funtion from Replay module
            else:
                game_function = getattr(importlib.import_module('Games.' + prev_game),
                                        'play')  # get the game function from the module using "getattr" and "importlib" functions
                game_function(
                    prev_difficulty)  # call the game function with the previous difficulty level if the user will press y

        elif repeat.lower().startswith('n'):  # check if the user input starts with 'n' (choose another game)
            screen_cleaner()  # clear the screen again
            # transfer_and_clear_file("./Scores/Scores.txt", "./Scores/Last_scores.txt") # for when the user will choose n for another game the function for clear the scores will be called and will also save the score to another file for the flask app localhost/last_score
            load_game(
                user_name)  # this will call the function load_game from the Live module to start another game from the beginning

        elif repeat.lower().startswith('q'):  # check if the user input starts with 'q' to quit the game
            print(
                f"Was nice to see you {user_name}!!! Thanks for playing my game, see you next time!")  # will display a message at the end
            transfer_and_clear_file("./Scores/Scores.txt",
                                    "./Scores/Last_scores.txt")  # calling the scores clean and transfer function
            screen_cleaner()  # clear the screen
            exit()  # will exit the program

        else:
            print(
                "Invalid input, try again!")  # if the user will enter some other key except the allowed ones will be prompted to try again
            break  # this break will restart the loop

    # Call the repeat_menu function again with the updated game and difficulty level
    if not repeat.lower().startswith('y'):
        return
# If the user chooses to play again, save the current game and difficulty level
    repeat_menu(user_name, lvl_sel, prev_game, prev_difficulty)