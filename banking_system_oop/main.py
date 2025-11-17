# main.py
from banking_sys import BankAccount  # Absolute import, works in the same folder

def main():
    #  I created accounts
    account1 = BankAccount("Mark")
    account2 = BankAccount("Mary")

    # Deposit money
    account1.deposit(480)

    # Transferred to  money to another account
    print(account1.transfer(account2, 200))

    # Checked account balances
    #print(account1.check_balance())
    #print(account2.check_balance())

if __name__ == "__main__":
    main()
