#%%
import random

class Hangman:
    """
    A class representing the game of Hangman.

    Attributes:
    -----------
    num_lives : int
        The number of incorrect guesses the player can make before the game ends.
    word_list : list
        The list of potential words the player has to guess.
    word : str
        The word randomly chosen for the current game.
    word_guessed : list
        A list that keeps track of which letters of the word have been correctly guessed.
    num_letters : int
        The number of unique letters in the word to be guessed.
    list_of_guesses : list
        A list to store letters that have been guessed.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new game of Hangman with the given word list and number of lives.
        """
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if a guessed letter is in the word and updates game state accordingly.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess {guess} is in the word!")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1 
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Asks the player for their guess and checks it.
        """
        while True:
            guess = input("Input the first alphabetical character: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter, Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already entered this letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            break

def play_game(word_list):
    """
    Function to initiate and manage a game of Hangman.
    """
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations, You won the game!")
            break

if __name__ == "__main__":
    words = ["mango", "cherry", "melon", "apple", "strawberry"]
    play_game(words)


# %%
