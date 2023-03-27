import re
import random

secret_number = None
difficulty = None
users_selection = None

def generate_number():
    global secret_number
    global difficulty
    secret_number = random.randint(1, difficulty)


def get_guess_from_user():
    global difficulty
    global users_selection
    users_number=input(f"guess a number between 1 to {difficulty}: ")
    if not re.search(f"^[1-{difficulty}]$",users_number):
        print("wrong format try again later")
        return;
    users_selection = int(users_number)


def compare_results():
    global secret_number
    global users_selection
    if secret_number == users_selection:
        return True
    return False


def play(difficulty_level):
    global difficulty
    difficulty = difficulty_level
    generate_number()
    get_guess_from_user()
    result = compare_results()
    if result:
        print("Correct! you won!")
        return result
    print("You lost :(")
    return False