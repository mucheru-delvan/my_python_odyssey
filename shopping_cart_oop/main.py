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
            break
            

if __name__ == "__main__":
    main()
    