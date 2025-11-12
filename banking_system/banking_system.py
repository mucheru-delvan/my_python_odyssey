class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            return "Please enter a positive amount to deposit."
        
        self.balance += amount
        return f"${amount} added to account {self.owner}. New balance: ${self.balance}."

    def withdraw(self, amount):

        if amount <= 0:
            return "Please enter a valid withdrawal amount."
        
        if amount > self.balance:
            return f"Insufficient funds. Your balance is ${self.balance}."
        
        self.balance -= amount
        return f"${amount} withdrawn. New balance: ${self.balance}."

    def check_balance(self):

        return f"Current balance: ${self.balance}"

    def transfer(self, account, amount):

        if amount <= 0:
            return "Please enter a valid transfer amount."
        
        if amount > self.balance:
            return f"You have insufficient funds to transfer ${amount}."
        
        self.balance -= amount
        account.balance += amount
        return f"You have transferred ${amount} to {account.owner}."


account1 = BankAccount("Mark")
account2 = BankAccount("Mary")
account1.deposit(480)
#print(account1.withdraw(100))
#print(account1.check_balance())
print(account1.transfer(account2,200))
print(account2.check_balance())

