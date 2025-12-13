class Item:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (x{self.quantity}) - ${self.price:.2f} each"
    


