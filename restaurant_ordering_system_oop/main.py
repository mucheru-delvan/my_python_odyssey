from menu import Menu

menu1 = Menu()
menu1.add_item("Burger", 8.99)
menu1.add_item("Fries", 2.99)
menu1.add_item("Soda", 1.49)
menu1.display_menu()
menu1.remove_item("Soda")
menu1.display_menu()
menu2 = Menu()
menu2.add_item("Pizza", 12.99)
menu2.add_item("Salad", 6.49)
menu2.display_menu()