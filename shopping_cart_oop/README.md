#  Shopping Cart CLI Application

A simple, clean, and object-oriented **command-line shopping cart application** built using Python. This project demonstrates solid use of **OOP principles**, modular design, and user interaction via a text-based menu.

---

## Features

* Add items to a shopping cart
* Update item quantities automatically if the item already exists
* Remove items from the cart
* View all items in the cart with prices and quantities
* Calculate and display total cost
* Graceful handling of invalid user input

---


##  Project Structure

```text
shopping-cart/
│
├── item.py              # Item class (data model)
├── shopping_cart.py     # ShoppingCart class (business logic)
├── main.py              # CLI interface and program entry point
└── README.md            # Project documentation
```

---

##  How to Run the Project

1. Make sure you have **Python 3.8+** installed
2. Clone or download this repository
3. Navigate to the project directory
4. Run the application:

```bash
python main.py
```

---

##  Example Usage

```text
🛒 Welcome to the Shopping Cart Application 🛒

1. Add Item
2. Remove Item
3. View Cart
4. Checkout and Exit
```

Sample output:

```text
1. Apple (x3) - $10.00 each
2. Milk (x1) - $5.50 each
The total is $35.50
```

---

