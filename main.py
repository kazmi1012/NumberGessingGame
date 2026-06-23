import random

DIFFICULTIES = {
    "1": {"name": "Easy", "low": 1, "high": 10, "max_attempts": None},
    "2": {"name": "Medium", "low": 1, "high": 100, "max_attempts": 7},
    "3": {"name": "Hard", "low": 1, "high": 1000, "max_attempts": 10},
}


def get_guess(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def choose_difficulty():
    print("Choose a difficulty:")
    print("1. Easy   (1-10, unlimited attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-1000, 10 attempts)")

    while True:
        choice = input("Enter 1, 2 or 3: ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Invalid choice. Please enter 1, 2 or 3.\n")


def play_round(difficulty, best_attempts):
    low, high = difficulty["low"], difficulty["high"]
    max_attempts = difficulty["max_attempts"]
    right_number = random.randint(low, high)
    attempt = 0

    print(f"\nI've picked a number for you to guess.")
    print(f"The number is between {low} and {high}.")
    if max_attempts:
        print(f"You have {max_attempts} attempts.\n")
    else:
        print()

    while True:
        remaining = f" ({max_attempts - attempt} attempts left)" if max_attempts else ""
        guessed_number = get_guess(f"Guess a number{remaining}: ")
        attempt += 1

        if guessed_number < low or guessed_number > high:
            print(f"Invalid guess. Please enter a number between {low} and {high}.")
        elif guessed_number == right_number:
            print("\nCorrect guess.")
            print("You won. Thank you for playing.")
            print(f"It took {attempt} attempts to guess the number.")

            best = best_attempts.get(difficulty["name"])
            if best is None or attempt < best:
                best_attempts[difficulty["name"]] = attempt
                print("New best score for this difficulty!")
            else:
                print(f"Your best for {difficulty['name']} is {best} attempts.")
            return

        elif guessed_number > right_number:
            print("Choose a lower number.\n")
        else:
            print("Choose a higher number.\n")

        if max_attempts and attempt >= max_attempts:
            print(f"\nOut of attempts. The number was {right_number}.")
            return


def play_game():
    print("Welcome to number guessing game.\n")
    best_attempts = {}

    while True:
        difficulty = choose_difficulty()
        play_round(difficulty, best_attempts)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing. Goodbye!")
            break
        print()


if __name__ == "__main__":
    play_game()
