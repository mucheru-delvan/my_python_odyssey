from shopping_cart import ShoppingCart


def main():
    
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout & Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter quantity: "))
                cart.add_item(name, price, quantity)
            except ValueError:
                print("Invalid input. Price must be a number, quantity must be an integer.")

        elif choice == "2":
            name = input("Enter item name to remove: ")
            cart.remove_item(name)

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            print("\nFinal Cart:")
            cart.view_cart()
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()