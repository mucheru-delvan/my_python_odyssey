from item import Item


class ShoppingCart:
    def __init__(self):
        self.items = []
  
     #I added default for quantity = 1 in order to allow the user to update
    def add_item(self,name,price,quantity=1):
        for item in self.items:
            if item in self.items:
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