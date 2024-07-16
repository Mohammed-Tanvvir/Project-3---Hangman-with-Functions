# Hangman Game (Basic Version)

import random

# List of words to guess
words = ["apple", "banana", "cherry"]

# Choose a random word from the list
word = random.choice(words)


# Create a list to store the guessed letters
guessed = ["_"] * len(word)

# Game loop
while True:
    # Show the current state of the word
    print(" ".join(guessed))

    # Ask the user for a guess
    guess = input("Guess a letter: ")

    # Check if the guess is in the word
    if guess in word:
        # Reveal the correct letter
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        # Increment the number of incorrect guesses
        continue

    # Check if the word has been fully guessed
    if "_" not in guessed:
        print("Congratulations! You guessed the word:", word)
        break

