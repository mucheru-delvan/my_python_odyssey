class Item:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (x{self.quantity}) - ${self.price:.2f} each"
    

new_item = Item("apple", 3, 0.99)
print(new_item)  # Output: apple (x3) - $0.99 each