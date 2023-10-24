#%%
from milestone import word
import random
import string
from milestone import guess
#%%
class Hangman:
    def __init__(self,word_list,num_lives):
        num_lives = 5

# The letters guessed correctly 

# Checks if your guess is in the word.
    def check_guess(guess):

        if guess in word:
            print(f"Good guess '{guess}' is in the word!")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
#Checks if your input is one character and its only aphabetical letters. 
    def ask_for_input():
        list_of_guesses = []  
        while True:
            guess = input("Input the first aplhabetical character:")
            print(list_of_guesses)
            if len(guess) != 1 and guess in string.ascii_letters:
                print("Invalid letter, Please enter a single aplhabetical character")
                
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                check_guess(guess)
                list_of_guesses.append(guess)
    ask_for_input()   
# %%
