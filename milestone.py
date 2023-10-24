#%%
import random
import string
print(string.punctuation)
#%%
word_list = ["mango","cherry","melon","apple","strawberry"]
word_list
# %%
word = random.choice(word_list)
print(word)
# %%
guess =  input("Enter the first letter :")


if len(guess) == 1 and guess in string.ascii_letters:
    print("Good Guess!")
else:
    print("Oops! That is not a valid input")


# %%
