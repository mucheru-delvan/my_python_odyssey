
# 🏪 Simple Inventory Manager

A **Python-based inventory management system** that allows you to **add, remove, search, and view items**.
All inventory data is stored persistently in a JSON file (`items.json`) using the built-in `json` and `pathlib` modules.

---

## 🧰 Features

* **Add new items** or **update existing items**
* **Remove items** from the inventory
* **Search items** by name
* **View current stock** with a neat numbered list
* **Persistent storage** in a JSON file (`items.json`)
* **Case-insensitive** item management

---

## ⚡ How to Use

### Example Script (`main.py`)

```python
from inventory_manager import SimpleInventory

def main():
    inv = SimpleInventory()

    # Add items
    inv.add_items("balls", 9)
    inv.add_items("bats", 5)
    inv.add_items("jersey", 6)
    inv.add_items("gloves", 4)

    # Remove an item
    inv.remove_items("balls")

    # Search for an item
    print(inv.search_items("bats"))

    # Show all stock
    inv.show_stock()

if __name__ == "__main__":
    main()
```

### Sample Output

```
Found bats with quantity 5

📜 Your Items Stock

1. bats: 5
2. jersey: 6
3. gloves: 4
```

---

## 📁 Project Structure

```
├── inventory_manager.py   # Main inventory class
├── items.json             # Inventory data (auto-created)
├── main.py                # Example usage script
└── README.md              # Project documentation
```

---

