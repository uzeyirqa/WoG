import random
import re
import time
import os

difficulty = None
random_list = []
user_list = []


def generate_sequence():
    global difficulty
    global random_list
    print("remember this list! Good luck!")
    random_list = random.sample(range(1, 101), difficulty)
    print(random_list)
    time.sleep(0.7)
    os.system('cls' if os.name=='nt' else 'clear')


def get_list_from_user():
    print("Now let's check your memory :)", "\n", "make sure list sequence is maintained!")
    global difficulty
    global user_list
    for i in range(1, difficulty+1):
        ele = input(f"enter list element number {i}: ")
        if re.search("^\d+$", ele):
            user_list.append(int(ele))
        else:
            print("wrong format try again later")
            return


def is_list_equal():
    global random_list
    global user_list
    if random_list == user_list:
        print("Correct! Good job!")
        return True
    print("you lost :(")
    return False


def play(difficulty_level):
    global difficulty
    difficulty = difficulty_level
    generate_sequence()
    get_list_from_user()
    result = is_list_equal()
    if result:
        return result
    return False
