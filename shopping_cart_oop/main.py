from shopping_cart import ShoppingCart


def main():
    cart = ShoppingCart()
    while True:
        print("\n🛒Welcome to the Shopping Cart Application🛒\n")
        print("1.Add Item")
        print("2.Remove Item")
        print("3.View Cart")
        print("4.Checkout and Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the item's name: ").strip()
            try:

                price = float(input(f"Enter the price of {name}: "))
                quantity = int(input(f"Enter the quantity of {name}: "))
                cart.add_item(name,price,quantity)

            except ValueError:
                print("Please enter valid numbers!") 

        elif choice == "2":
            name = input("Enter the item's name to remove: ").strip()
            cart.remove_item(name)  
            
        else:
            break 

if __name__ == "__main__":
    main()
    