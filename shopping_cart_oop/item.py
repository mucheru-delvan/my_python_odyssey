class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def __str__(self):
        return f"{self.name} (x{self.quantity}) - ${self.price:.2f} each"
    


