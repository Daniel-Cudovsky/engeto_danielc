"""
bullsxcows.py: druhý projekt do Engeto Online Python Akademie

author: Daniel Čudovský
email: daniel.cudovsky@gmail.com
discord: dannyxc12
"""

import random
from datetime import datetime

def greetings(user):
    hour = datetime.now().hour

    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    elif 18 <= hour < 22:
        greeting = "Good evening"
    else:
        greeting = "Good night"

    print(f"{greeting}, {user}!")

cut = "-" * 40

user_name = input("\nWelcome! What's your name?: ").capitalize()
print(cut)
greetings(user_name)
print("Let's play a bulls and cows game.")
print(cut)
print("I've generated a random 4 digit number for you.")

def split_number(number: str):
    return [int(digit) for digit in number]

random_number = str(random.randint(1000, 9999))
number_list = split_number(random_number)
attempts = 0

def compare_numbers(user_guess, generated_numbers):
    bulls = 0
    cows = 0

    guess_copy = user_guess[:]
    number_copy = generated_numbers[:]

    for i in range(4):
        if guess_copy[i] == number_copy[i]:
            bulls += 1
            guess_copy[i] = number_copy[i] = None


    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in number_copy:
            cows += 1
            number_copy[number_copy.index(guess_copy[i])] = None

    return bulls, cows


def guessing_game():
    global attempts
    while True:
        guess = input("Make your guess on which number I've generated:\n>>> ")
        if not guess.isdigit() or len(guess) != 4:
            print("Please enter a 4-digit number.")
            continue
        
        guess_list = split_number(guess)
        attempts += 1

        if guess_list == number_list:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            break
        else:
            bulls, cows = compare_numbers(guess_list, number_list)
            print(f"{bulls} bull(s), {cows} cow(s).")
        print(cut)

    if attempts < 10:
        print("That's awesome!")
    elif attempts < 20:
        print("That's good!")
    else:
        print("That's okay...")

guessing_game()
