
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

---

##  Usage Example

```python
# Create accounts
mark = Bank("Mark")
mary = Bank("Mary")

# Transactions
print(mark.deposit(500))          # Add money
print(mark.withdraw(200))         # Withdraw money
print(mark.transfer(mary, 100))   # Transfer to Mary

# Check balances
print(mark.check_balance())       # Current balance: 200
print(mary.check_balance())       # Current balance: 100
```

> All data will be lost once the program stops.

---

