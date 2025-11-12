class Bank:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):

        if amount < 1:
            return "Please enter positive numbers."
        else:
            self.balance += amount
            return f"${amount} added to account {self.owner} new balance ${self.balance}."
        
    def withdraw(self,amount):

        if amount <= self.balance:
            self.balance -= amount
            return f"${amount} withdrawn new balance ${self.balance}."
        else:
            return f"Insufficient funds try a lower amount your current balance is ${self.balance}."

    def check_balance(self):

        return f"Current balance: ${self.balance}"
    
    def transfer(self,account,amount):

        if amount <= self.balance:
            self.balance -= amount
            account.balance += amount
            return f"You have transferred ${amount} to {account.owner}."
        else:
            return f"You have insufficient funds to transfer ${amount}."
        

account1 = Bank("Mark")
account2 = Bank("Mary")
account1.deposit(480)
#print(account1.withdraw(100))
#print(account1.check_balance())
print(account1.transfer(account2,200))
print(account2.check_balance())

