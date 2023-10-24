#%%
import string
from milestone import word

# %%
# Checks if your guess is in the word.
def check_guess(guess):
    if guess in word:
        print(f"Good guess {guess} is in the word!")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
#%%
#Checks if your input is one character and its only aphabetical letters (No punctuation or numbers). 
def ask_for_input():
    while True:
        guess = input("Input the first aplhabetical character:")
        if len(guess) == 1 and guess in string.ascii_letters:
            break
        else:
            print("Invalid letter, Please enter a single aplhabetical character")
    check_guess(guess)
           
ask_for_input()

# %%


# %%
