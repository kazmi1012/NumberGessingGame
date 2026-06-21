import random


def get_guess(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def play_game():
    print("Welcome to number guessing game.\n")
    right_number = random.randint(1, 10)
    attempt = 0

    print("I've picked a number for you to guess.")
    print("The number is between 1 and 10.\n")

    guessed_number = get_guess("Guess a number: ")
    attempt += 1

    while guessed_number != right_number:
        if guessed_number < 1 or guessed_number > 10:
            print("Invalid guess. Please enter a number between 1 and 10.")
        elif guessed_number > right_number:
            print("\nYour guess is not correct.")
            print("Give it another shot.")
            print("Choose a lower number.\n")
        else:
            print("\nYour guess is not correct.")
            print("Give it another shot.")
            print("Choose a higher number.\n")

        guessed_number = get_guess("Guess a number again: ")
        attempt += 1

    print("\nCorrect guess.")
    print("You won. Thank you for playing.")
    print(f"It took {attempt} attempts to guess a number ")


if __name__ == "__main__":
    play_game()
