# Lesson taken from Youtube
# "12 Beginner Python Projects - Coding Course"
# https://www.youtube.com/watch?v=8ext9G7xspg

import random

def guess(x): # <x> is a parameter we can pass to the function to work with
    random_number = random.randint(1, x) # generate random number between 1 and <x>
    guess = 0
    while guess != random_number:
        # guess must be integer, otherwise we will never guess
        guess = int(input(f'Guess the correct number between 1 and {x}: ')) # We are trying to guess the correct number
        if guess > random_number:
            print("Wrong, try a lower number.")
        elif guess < random_number:
            print("Wrong, try a higher number.")
    print(f"You are correct! The number is {random_number}.")

x = 20
guess(x)
