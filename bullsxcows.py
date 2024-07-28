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
print("I've generated a random number, with 4 unique digits, for you to guess.")


def generate_unique_number():
    digits = list("123456789") 
    random.shuffle(digits)
    first_digit = digits.pop()  # Vyberu první číslo nezačínající 0

    remaining_digits = list("0123456789")
    for digit in first_digit:
        remaining_digits.remove(digit)  # Zajistím unikátnost

    random.shuffle(remaining_digits)
    unique_number = [first_digit] + remaining_digits[:3]

    return unique_number


def split_number(number: str):
    return [int(digit) for digit in number]

random_number = generate_unique_number()
number_list = split_number("".join(random_number))
attempts = 0


def is_unique(number: str):
    return len(number) == len(set(number))


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
        attempts += 1

        if not guess.isdigit() or len(guess) != 4:
            print("Please enter a 4-digit number.")
            print(cut)
            continue
        if not is_unique(guess):
            print("Please enter a number with 4 unique digits.")
            print(cut)
            continue
        
        guess_list = split_number(guess)

        if guess_list == number_list:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            break
        else:
            bulls, cows = compare_numbers(guess_list, number_list)
            bulls_text = "bull" if bulls == 1 else "bulls"
            cows_text = "cow" if cows == 1 else "cows"
            print(f"{bulls} {bulls_text}, {cows} {cows_text}.")
        print(cut)

    if attempts < 15:
        print("That's awesome!")
        print(cut)
    elif attempts < 25:
        print("That's good!")
        print(cut)
    elif attempts < 35:
        print("That's okay...")
        print(cut)
    else:
        print("Honestly, you didn't do well...")
        print(cut)

def main():
    while True:
        guessing_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            break

main()
