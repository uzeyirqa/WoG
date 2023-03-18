import random
import re
import requests
import json

usd_amount = None
answer = None
user_guess = None


def get_money_interval():
    apiKey = "hbEZhk4R0PhGxSKQfZZ5HFhmV9L3QUSB"
    headers = { "apikey": apiKey}
    response = requests.request("GET","https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=ILS",headers=headers)
    parse_response = json.loads(response.text)
    rate = float(parse_response["rates"]["ILS"])
    global usd_amount
    usd_amount=random.randint(1, 100)
    global answer
    answer = usd_amount * rate
    answer = round(answer)


def get_guess_from_user():
    global usd_amount
    global user_guess
    guess= input(f"guess the how much will {usd_amount} USD is in ILS")
    if re.search("^\d+$", guess):
        user_guess = int(guess)
    else:
        print("wrong format please try again later")
        return


def play(difficulty):
    get_money_interval()
    get_guess_from_user()
    global answer
    if user_guess in range(answer-1-(5-difficulty), answer+1+(5-difficulty)):
        print(f"you are very close! the correct answer is {answer} ")
        return True
    else:
        print(f"nice try, but the correct answer is {answer} :(")
        return False
