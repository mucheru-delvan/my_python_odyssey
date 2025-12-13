def main():
    from shopping_cart import ShoppingCart
    from item import Item

    cart = ShoppingCart()

    item1 = Item("Apple", 0.5, 4)
    item2 = Item("Banana", 0.3, 6)
    item3 = Item("Orange", 0.8, 3)

    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)

    print("Items in cart:")
    for item in cart.get_items():
        print(f"- {item.name}: ${item.price} x {item.quantity}")

    total = cart.get_total()
    print(f"Total price: ${total:.2f}")

    cart.remove_item("Banana")
    print("\nAfter removing Banana:")
    for item in cart.get_items():
        print(f"- {item.name}: ${item.price} x {item.quantity}")

    total = cart.get_total()
    print(f"Total price: ${total:.2f}")