
#  Simple Bank Account App (In-Memory)

A **Python Bank Account application** that allows you to:

* Deposit money
* Withdraw money
* Check account balance
* Transfer money between accounts

> ⚠️ **Note:** This version does **not save data**. All balances exist only in memory and will be lost when the program exits.

---

##  Features

* **Deposit:** Add money to your account (must be positive).
* **Withdraw:** Remove money from your account (cannot exceed balance).
* **Check Balance:** View current balance.
* **Transfer:** Move money from one account to another (in memory only).


##  Usage Example

```python
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

```

> All data will be lost once the program stops.

---

