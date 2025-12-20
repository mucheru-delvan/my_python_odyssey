class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        """Add a new item to the menu."""
        self.items[name] = price

    def remove_item(self, name):
        """Remove an item from the menu."""
        if name in self.items:
            del self.items[name]

    def get_price(self, name):
        """Get the price of an item."""
        return self.items.get(name, None)

    def display_menu(self):
        """Display the menu items and their prices."""
        for name, price in self.items.items():
            print(f"{name}: ${price:.2f}")