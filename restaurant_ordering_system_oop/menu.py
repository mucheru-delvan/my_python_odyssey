class Menu:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        #print(f"Added : {product.name}")
        
    def remove_product(self,product):
        
        if product in self.products:
             self.products.remove(product)
             #print(f"Removed :{product.name}")
        else:
            print(f"Item '{product}' not found in the menu.")  
            
    def display_menu(self):
        if not self.products:
            print("\nNo products !")
            return
        print("\nMENU\n")
        for product in self.products:
            print(f"{product.name}: ${product.price:.2f} each")