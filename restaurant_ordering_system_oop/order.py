from product import Product

class Order(Product):

    def __init__(self,name,price,quantity):
        super().__init__(name,price)
        self.items = []
        self.quantity = quantity

    def add_item(self,product,quantity):
        self.items.append((product,quantity))
        print(f"Added {quantity} of {product.name} to order.")

    def remove_item(self,product):
        for product in self.items:
            if  product.name == product:
                self.items.remove(product)
                print(f"Removed {product.name} from order.")
                return
        print(f"Item '{product.name}' not found in the order.")

    def total_price(self):
        total = 0
        for item,quantity in self.items:
            total += item.price * quantity
        return total        
    
    def view_order(self):
        if not self.items:
            print("Your order is empty!")
            return
        print("\nYOUR ORDER\n")
        for i,(item,quantity) in enumerate(self.items,start=1):
            print(f"{i}. {item.name} (x{quantity}) - ${item.price:.2f} each")
        print(f"The total is ${self.total_price():.2f}")