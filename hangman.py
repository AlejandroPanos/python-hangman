import random

words = [
    "developer"
    # "python",
    # "programming",
    # "developer",
    # "algorithm",
    # "function",
    # "variable",
    # "computer",
    # "keyboard",
    # "software",
    # "database",
]

# Set number of attempts
attempts = 10

# Select a random word from list
word = random.choice(words)
guessed_letters = set()
lines = ["_" for char in word]
print(" ".join(lines))

while attempts > 0 and "_" in lines:
    answer = input("Guess a letter: ").lower()

    if answer in guessed_letters:
        print("Already guessed that letter")
        continue

    guessed_letters.add(answer)

    if answer in word:
        for i, char in enumerate(word):
            if char == answer:
                lines[i] = answer
        print("Correct!")
    else:
        attempts -= 1
        print(f"Wrong guess: {attempts} attempts remaining.")

    print(" ".join(lines))

if not "_" in lines:
    print("You won!")
else:
    print(f"Game over! The correct word was {word}")
