from menu import Menu
from product import Product
from order import Order

def main():
    # Create products 
    product1 = Product("Sausages", 2.33)
    product2 = Product("Soda", 1.99)
    product3 = Product("Burger", 2.45)
    product4 = Product("Cheese", 1.89)

    # Setup menu so you can view products
    menu1 = Menu()
    menu1.add_product(product1)
    menu1.add_product(product2)
    menu1.add_product(product3)
    menu1.add_product(product4)

    print("\nINITIAL MENU:")
    menu1.display_menu()

    # Remove a product 
    menu1.remove_product("Soda")
    print("\nMENU AFTER REMOVAL:")
    menu1.display_menu()

    #create an order 
    order1 = Order()
    order1.add_item(product1, 2)
    order1.add_item(product3, 1)

    print("\nORDER AFTER ADDING ITEMS:")
    order1.view_order()

    # Remove item from order 
    order1.remove_item("Sausages")
    print("\nORDER AFTER REMOVING SAUSAGES:")
    order1.view_order()


if __name__ == "__main__":
    main()

# Project: Restaurant Ordering System OOP
# Author: Delvan Mucheru
# Description: A Python OOP project demonstrating Product, Menu, and Order management.
# Date: 2025-12-22