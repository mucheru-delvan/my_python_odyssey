
class ShoppingCart:
    
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        for item in self.items:
            if item.name == name:  # if item already in cart, update quantity
                item.quantity += quantity
                print(f"Updated {name} quantity to {item.quantity}.")
                return
        new_item = Item(name, price, quantity)
        self.items.append(new_item)
        print(f"Added {quantity} x {name} to cart.")


    def remove_item(self, item, quantity=1):
        for cart_item in self.items:
            if cart_item['item'] == item:
                if cart_item['quantity'] > quantity:
                    cart_item['quantity'] -= quantity
                else:
                    self.items.remove(cart_item)
                return

    def get_total(self):
        total = 0
        for cart_item in self.items:
            total += cart_item['price'] * cart_item['quantity']
        return total

    def clear_cart(self):
        self.items = []

    def get_items(self):
        return self.items