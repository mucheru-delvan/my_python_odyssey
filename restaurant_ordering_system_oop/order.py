class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))
        print(f"Added {quantity} of {product.name} to order.")

    def remove_item(self, product_name):
        for product, quantity in self.items:
            if product.name == product_name:
                self.items.remove((product, quantity))
                print(f"{product_name} removed from order.")
                return
        print(f"{product_name} not found in order.")

    def total_price(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def view_order(self):
        if not self.items:
            print("Your order is empty!")
            return

        print("\nYOUR ORDER\n")
        for i, (product, quantity) in enumerate(self.items, start=1):
            print(f"{i}. {product.name} (x{quantity}) - ${product.price:.2f} each")

        print(f"The total is ${self.total_price():.2f}")
