
#  Python Restaurant Ordering System (OOP)

A simple and interactive **Python Restaurant Ordering System** that allows you to manage products, menus, and customer orders using clean Object-Oriented Programming (OOP).

This project uses three main classes — **Product**, **Menu**, and **Order** — to simulate a small restaurant ordering system.

---

## Description

This program allows you to:

* Add multiple **products** to the menu
* Remove products from the menu
* View the menu
* Create **customer orders**
* Add products with quantities to an order
* Remove products from an order
* View the updated order and total price
* Practice **OOP**, **composition**, and **modular code structure** in Python

It’s a great beginner-friendly project for understanding **encapsulation**, **class interaction**, and **real-world system modeling**.

---

 Each class handles a **single responsibility**, and objects interact via composition (HAS-A relationships), demonstrating clean OOP principles.

---

## Example Usage

### Initial Menu Setup

```text
Added: Sausages
Added: Soda
Added: Burger
Added: Cheese

INITIAL MENU:
Sausages: $2.33 each
Soda: $1.99 each
Burger: $2.45 each
Cheese: $1.89 each
```

---

### Removing a product

```text
Removed: Soda

MENU AFTER REMOVAL:
Sausages: $2.33 each
Burger: $2.45 each
Cheese: $1.89 each
```

---

### Creating an order

```text
Added 2 of Sausages to order.
Added 1 of Burger to order.

ORDER AFTER ADDING ITEMS:
1. Sausages (x2) - $2.33 each
2. Burger (x1) - $2.45 each
The total is $7.11
```

---

### Removing an item from the order

```text
Sausages removed from order.

ORDER AFTER REMOVING SAUSAGES:
1. Burger (x1) - $2.45 each
The total is $2.45
```

---

## Technologies & Concepts Used

* Python Classes & Objects
* Object-Oriented Programming (OOP)
* Composition (HAS-A relationships)
* Lists & basic data structures
* Clean modular code organization
* Simulated real-world restaurant ordering system

---

## Running the Program

Make sure all `.py` files (`product.py`, `menu.py`, `order.py`, `main.py`) are in the same folder.

Run the program using:

```bash
python3 main.py
```

---

