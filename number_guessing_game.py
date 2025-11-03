import random

def play_game():

    min_num = int(input("Enter the lowest range number for your game: "))
    max_num = int(input("Enter the highest range number for your game: "))

    number_to_guess = random.randint(min_num, max_num)
    attempts = 0
    max_attempts = 10

    print("\n💫Welcome to the Number Guessing Game!💫\n")
    print(f"You have selected a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < min_num or guess > max_num:
                print(f"Please guess a number between {min_num} and {max_num}.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"\n👏Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                if attempts  <= 3 and guess == number_to_guess:
                    print("\nBest score! by guessing the number in less than 3 attempts")
                break
        except ValueError:
            print(f"Invalid input. Please enter a number between {min_num} and {max_num}.")
            
    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
    
    play_again = input("\nDo you want to play again?(y/n): ")
    if play_again == "y":
        play_game()
    else:
       print("\nThank you for playing bye👋....")

play_game()
