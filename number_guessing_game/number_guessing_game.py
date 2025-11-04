import random

def number_guessing_game():
    best_score = None

    while True:
        print("\n🎮 Welcome to a Python Number Guessing Game!")
        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))
        secret_number = random.randint(min_num, max_num)
        max_attempts = int(input("Enter the maximum number of guesses: "))

        attempts = 0

        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            attempts += 1

            if guess == secret_number:
                print(f"🎉 Correct! You got it in {attempts} tries.")
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("🥇 New best score!")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

        if attempts == max_attempts:
            print(f"😢 Out of attempts! The number was {secret_number}.")

        print(f"🏆 Best score so far: {best_score if best_score else 'None'}")
        
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("👋 Thanks for playing!")
            break

number_guessing_game()


