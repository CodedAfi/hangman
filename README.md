# Python Hangman Game

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Description
**Python Hangman Game** is a console-based word guessing game. Players attempt to build a word by guessing one letter at a time. For each incorrect guess, a part of a hangman figure gets drawn. The player wins if they guess the word before the hangman figure is completed. They lose if the figure is completed first.

**Aim of the Project**: 
To implement a basic text-based game in Python, familiarize with string manipulation, and practice using data structures and user input validation.

**What I Learned**: 
- Game development basics
- String manipulation techniques in Python
- Utilizing Python lists and dictionaries
- Effective handling and feedback of user input 
- Clear instructions and user feedback to ensure an immersive gameplay experience.
- Designed with modularity in mind, allowing for easy addition of features or modifications.

## Prerequisites
- Python 3.11
- Git (for cloning the repository and pushing it into github).



## Instructions:

1. **Starting the Game**: 
   - At the start, the game selects a random word from its database, which becomes the word you're trying to guess.
   - The word is presented as a series of underscores, each representing a letter.

2. **Making a Guess**:
   - Input a single letter that you believe might be in the word.
   - If your chosen letter is in the word, the corresponding underscores will be replaced by that letter.
   - If your chosen letter is not in the word, part of the hangman figure gets drawn.

3. **Rules**:
   - Guess only one letter at a time.
   - Letters that have already been guessed cannot be guessed again.
   - The game continues until the word is completely guessed or the hangman figure is fully drawn.

4. **Game Over Scenarios**:
   - **Win**: Successfully guessing all the letters of the word before completing the hangman figure.
   - **Loss**: The hangman figure is completely drawn before the word is guessed.

5. **Hints and Tips**:
   - Begin with guessing vowels as they are more common in words.
   - Keep track of letters that have already been guessed and the emerging pattern of the word.
   - Make strategic guesses based on typical English letter pairings or word endings.

## File structure:
hangman/hangman/hangman_Template.py, hangman/gitignore, hangman/milestone_2.py, hangman/milestone_3.py, hangman/milestone_4.py, hangman/README.md