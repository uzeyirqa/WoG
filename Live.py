import re
from Games import GuessGame, MemoryGame, CurrencyRouletteGame
from Replay import repeat_menu
from Scores.Score import add_score
from Utils import screen_cleaner


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
