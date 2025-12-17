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
            name = input("Enter the item's name: ").strip().capitalize()
            try:

                price = float(input(f"Enter the price of {name}: "))
                quantity = int(input(f"Enter the quantity of {name}: "))
                cart.add_item(name,price,quantity)

            except ValueError:
                print("Please enter valid numbers!") 

        elif choice == "2":
            name = input("Enter the item's name to remove: ").strip().capitalize()
            cart.remove_item(name)  

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            print("\nChecking out...\n")
            cart.view_cart()
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    