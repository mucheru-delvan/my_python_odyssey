from item import Item


class ShoppingCart:
    def __init__(self):
        self.items = []
  
    def add_item(self,name,price,quantity):
        for item in self.items:
            if item.name == name:
                item.quantity += quantity
                print(f"Updated {item.name} quantity to {item.quantity}")
                return
        new_item = Item(name,price,quantity)
        self.items.append(new_item)
        print(f"\nYou added {new_item} to cart\n")

    def remove_item(self,name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"\nYou removed {item} from cart\n")
                return
        print(f"\nItem {name} not found in cart.\n")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty!")
            return
        print("\nYOUR CART\n")
        for i,item in enumerate(self.items,start=1):
            print(f"{i}.{item}")
        print(f"The total is ${self.total_cost():.2f}")

    def total_cost(self):
        return sum(item.price * item.quantity for item in self.items)