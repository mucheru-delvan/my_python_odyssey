
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
filename = BASE_DIR / "items.json"

class SimpleInventory:

    def __init__(self, filename):
        self.filename = filename
        self.items = self.load_items()   

    def load_items(self):
        
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []   

    def save_items(self):
        
        with open(self.filename, "w") as f:
            json.dump(self.items, f, indent=2)

    def add_items(self, name, quantity):
        #I added this feature to check whether the json file is a list before adding items 
        if not isinstance(self.items, list):
            self.items = []

        for item in self.items:
            if item["name"].lower() == name.lower():
                item["quantity"] += quantity
                self.save_items()
                return f"Updated {name} quantity to {item['quantity']}"

        new_item = {"name": name, "quantity": quantity}
        self.items.append(new_item)
        self.save_items()
        return f"Added new item: {name} with quantity {quantity}"

    def search_items(self, name):
        
        for item in self.items:
            if item["name"].lower() == name.lower():
                return f"Found {item['name']} with quantity {item['quantity']}"
        return f"Item {name} not found"

    def remove_items(self, name):
        
        for item in self.items:
            if item["name"].lower() == name.lower():
                self.items.remove(item)
                self.save_items()
                return f"{name} removed from inventory."
        return f"{name} not found in inventory."

    def show_stock(self):
        #I displayed all items and their quantities
        if len(self.items) < 1:
            print("No items added yet!")
        else:
            print("\n📜 Your Items Stock\n")
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item['name']}: {item['quantity']}")


