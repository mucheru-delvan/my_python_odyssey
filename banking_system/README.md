
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


Here’s a **clean, beginner-friendly README section** tailored exactly to your project structure:

---

## 📁 Project Structure

This project includes an `__init__.py` file, which helps Python recognize the folder as a **package**.
Here’s what your directory looks like:

```
banking_system/
├── banking_system.py
├── __init__.py
├── main.py
├── __pycache__/
│   └── banking_system.cpython-312.pyc
└── README.md
```

### 🧩 What `__init__.py` Does

The `__init__.py` file allows this folder (`banking_system/`) to behave like a Python **package**.

Even if it is empty, it serves important purposes:

* ✔ Lets you import modules inside the folder
  Example:

  ```python
  from banking_system import banking_system
  ```
* ✔ Helps structure your code cleanly when the project grows
* ✔ Makes the folder compatible with IDEs and tools that expect packages

### 💡 Optional Use

You *can* also use `__init__.py` to:

* Define what the package exposes (e.g., classes or functions)
* Initialize package-wide variables
* Provide shortcuts like:

  ```python
  from .banking_system import Bank
  ```

But keeping it empty is completely fine for small projects.

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

