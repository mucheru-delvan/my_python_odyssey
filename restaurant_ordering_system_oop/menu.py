class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        
        self.items[name] = price

    def remove_item(self, name):
        
        if name in self.items:
            del self.items[name]
        else:
            print(f"Item '{name}' not found in the menu.")  

    def get_price(self, name):
        
        return self.items.get(name, None)

    def display_menu(self):
        
        for name, price in self.items.items():
            print(f"{name}: ${price:.2f}")