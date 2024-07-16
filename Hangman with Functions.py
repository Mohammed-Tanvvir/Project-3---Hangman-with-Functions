import random

def random_word():
    word_list = ["abyss", "blizzard", "caliph", "duplex", "equip", "flopping", "galaxy", "haphazard", "ivory", "jackpot"]
    randomizer = random.randint(0,9)
    chosen_word = word_list[randomizer]
    return chosen_word

def print_hidden_word(hidden_word, letters_guessed):
    displayed_word = ''
    for letter in hidden_word:
        if letter in letters_guessed:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    print(displayed_word.strip())

def is_game_over(chosen_word, letters_guessed, incorrect_guesses, max_incorrect=6):
    if all(letter in letters_guessed for letter in chosen_word):
        return True, "Congratulations! You've guessed the word correctly."
    if incorrect_guesses >= max_incorrect:
        return True, f"Game Over! The correct word was '{chosen_word}'."
    return False, ""

print("🪢 Welcome to Hangman 🪢")
chosen_word = random_word()
letters_guessed = []
incorrect_guesses = 0

while True:
    print("Guess the word:")
    print_hidden_word(chosen_word, letters_guessed)
    guess = input("Enter a letter: ").lower()

    if guess in letters_guessed:
        print("You've already guessed that letter. Try a different one.")
        continue
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single alphabetic character.")
        continue

    letters_guessed.append(guess)
    if guess not in chosen_word:
        incorrect_guesses += 1

    game_over, message = is_game_over(chosen_word, letters_guessed, incorrect_guesses)
    if game_over:
        print(message)
        if input("Play again? (y/n): ").lower() == 'y':
            chosen_word = random_word()
            letters_guessed = []
            incorrect_guesses = 0
            continue
        else:
            break


