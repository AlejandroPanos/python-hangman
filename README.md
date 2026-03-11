# Python Hangman Game

A classic hangman word guessing game implemented in Python. Players attempt to guess a randomly selected word letter by letter before running out of attempts.

## Description

This is a command-line hangman game where players have 10 attempts to guess a programming-related word. Each correct letter is revealed in its position, while incorrect guesses reduce the remaining attempts.

## Features

- 10 programming-themed words
- 10 attempts per game
- Letter tracking to prevent duplicate guesses
- Visual word display with underscores for unguessed letters
- Replay option after each game
- Case-insensitive input

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/python-hangman.git
cd python-hangman
```

No additional dependencies are required. This project uses only Python's standard library.

## Usage

Run the game:

```bash
python hangman.py
```

### How to Play

1. The game displays underscores representing each letter in the hidden word
2. Guess one letter at a time
3. Correct guesses reveal the letter(s) in their position(s)
4. Incorrect guesses reduce your remaining attempts
5. Win by guessing all letters before running out of attempts
6. Choose to play again or exit after each game

### Example Gameplay

```
_ _ _ _ _ _
Guess a letter: p
Correct!
p _ _ _ _ _
Guess a letter: y
Correct!
p y _ _ _ _
Guess a letter: t
Correct!
p y t h _ _
Guess a letter: o
Correct!
p y t h o _
Guess a letter: n
Correct!
p y t h o n
You won!
Would you like to play again (y/n):
```

## Word List

The game includes 10 programming-related words:

- python
- programming
- developer
- algorithm
- function
- variable
- computer
- keyboard
- software
- database

## Customization

You can easily customize the word list by editing the `words` array in the code:

```python
words = [
    "your",
    "custom",
    "words",
    "here",
]
```

You can also adjust the number of attempts by changing the `attempts` variable.
