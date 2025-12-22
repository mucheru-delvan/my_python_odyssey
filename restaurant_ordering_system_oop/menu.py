class Menu:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        for existing in self.products:
            if existing.name == product.name:
                print(f"{product.name} already exists in menu.")
                return
        self.products.append(product)
        print(f"Added : {product.name}")


    def remove_product(self, product_name):
        
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Removed: {product.name}")
                return
        print(f"Item '{product_name}' not found in the menu.")

    def display_menu(self):
        if not self.products:
            print("\nNo products !")
            return
        print("\nMENU\n")
        for product in self.products:
            print(f"{product.name}: ${product.price:.2f} each")