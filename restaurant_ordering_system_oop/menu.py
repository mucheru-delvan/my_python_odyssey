class Menu:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        print(f"Added : {product.name}")
        

    def remove_product(self,product):
        
        if product in self.products:
             self.products.remove(product)
             print(f"Removed :{product.name}")
        else:
            print(f"Item '{product}' not found in the menu.")  

    #def get_price(self, name):
        
        #return self.products

    def display_menu(self):
        
        for name in self.products:
            print(f"{name}:")