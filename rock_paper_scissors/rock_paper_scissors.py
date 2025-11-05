import random

print("\n💫Welcome to a Python Rock Paper Scissors Game💫\n")

def play_game():
    user_score = 0
    computer_score = 0
    ties = 0
    
    choices = ("Rock","Paper","Scissors")
    

    while True:

        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")

            continue
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        if user_choice == computer_choice:
            print("🤝 It's a tie!")
            ties +=1
            
        elif user_choice == "Paper" and computer_choice == "Rock":
            print("You won!")
            user_score +=1

        elif user_choice == "Scissors" and computer_choice == "Paper":
            print("You won!")
            user_score +=1

        elif user_choice == "Rock" and computer_choice == "Scissors":
            print("You won!")
            user_score +=1
        else:
            print("Computer wins")
            computer_score +=1

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again not in ("y","yes"):
            break

            
        
    print("\n🌟 FINAL STATS 🌟")
    print(f"Player wins: {user_score}")
    print(f"Computer wins: {computer_score}")
    print(f"🤝 Ties: {ties}")
    print(f"Total games played: {user_score + computer_score + ties}")
    print("\n👋 Thanks for playing!")

play_game()