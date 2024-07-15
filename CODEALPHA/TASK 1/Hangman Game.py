# TASK 1
# Design a text-based Hangman game in python. The program
# selects a random word, and the player guesses one
# letter at a time to uncover the word. You can set a
# limit on the number of incorrect guesses allowed.
import random


def select_random_word():
    words = ["python", "hangman", "challenge", "programming", "developer", "software"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = "".join([letter if letter in guessed_letters else "_" for letter in word])
    return display


def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! The word: {display_word(word, guessed_letters)}")
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was: {word}")


if __name__ == "__main__":
    hangman()
