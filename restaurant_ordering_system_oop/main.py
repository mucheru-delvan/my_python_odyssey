from menu import Menu
from product import Product


def main():
    
    product1 = Product("Sausages",2.33)
    product2 = Product("Soda",1.99)
    product3 = Product("Burger",2.45)
    product4 = Product("Cheese",1.89)
   
    menu1 = Menu()
    menu1.add_product(product1)
    menu1.add_product(product2)
    menu1.add_product(product3)
    menu1.add_product(product4)
    #menu1.display_menu()

    menu1.remove_product(product2)
    menu1.display_menu()



if __name__ == "__main__":
    main()