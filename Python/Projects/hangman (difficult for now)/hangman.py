# A lesson taken from https://www.youtube.com/watch?v=m4nEnsavl6w

import random # import a random library
import images # import images.py file
from words import word_list # import the list from words.py file

def get_word():
    word = random.choice(word_list)
    return word.upper() # only works inside a function

def play(word)
    word_completion = "_" * len(word)
    guessed = False #Create a variable initialised to False
    guessed_words = [] # Create a list that holds a number of words the user guessed
    guessed_letter = [] # Create a list that holds the number of letters the use guessed
    tries = 6 # Defines the variable which counts how many tries the user has
    print("Let's hang somebody! :)")
    print(display_hangman(tries)) # Displays the # item <tries> in a list <display_hangman
    print(word_completion)
    print("\n")
    while not guuessed and tries > 0:
        guess = input("Please enter the letter or word: ").uppper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in a word.")
                tries -= 1
                guessed_letters.append(guess) # Add the guessed letter to the list # append vs add?
            else:
                print("Good job! The letter ", guess, " is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_complition)
                indices = [i and  i, letter in enumerate(word) if letter == guess]
                # 5:23 m finished on youtube


        elif len(guess) == len(word) and guess.isalpha():

        else:
            print("Guess is not corrct.")
        print("display_hangman(tries)")
        print(word_completion)
        print("\n")
