def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit() and int(amount) > 0:
            break
        else:
            print("Invalid input. Please enter a positive number.")

    return int(amount)

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-3): ")
        if lines.isdigit() and 1 <= int(lines) <= 3:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

    return int(lines)       

def get_bet_per_line():
    while True:
        bet = input("Enter the bet amount per line: $")
        if bet.isdigit() and int(bet) > 0:
            break
        else:
            print("Invalid input. Please enter a positive number.")

    return int(bet) 

def spin(balance, lines, bet):
    total_bet = lines * bet
    if total_bet > balance:
        print(f"Insufficient balance to place this bet. Your current balance is: ${balance}")
        return balance

    print(f"You have placed a total bet of: ${total_bet} on {lines} lines.")

    # Simulate the spin (this is a placeholder, actual slot machine logic would go here)
    import random
    winnings = random.randint(0, total_bet * 2)  # Random winnings for demonstration

    balance -= total_bet
    balance += winnings

    print(f"You won: ${winnings}")
    print(f"Your new balance is: ${balance}")

    return balance  

def main():                     
    balance = deposit()

    while True:
        print(f"Current balance: ${balance}")
        lines = get_number_of_lines()
        bet = get_bet_per_line()

        balance = spin(balance, lines, bet)

        if balance <= 0:
            print("You have run out of money! Game over.")
            break

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print(f"You are leaving the game with a balance of: ${balance}")        

if __name__ == "__main__":
    main()