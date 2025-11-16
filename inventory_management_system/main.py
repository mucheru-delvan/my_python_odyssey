from inventory_manager import SimpleInventory

def main():

    inv = SimpleInventory("items.json")

    inv.add_items("balls", 9)
    inv.add_items("bats", 5)
    inv.add_items("jersey", 6)
    inv.add_items("gloves", 4)
    inv.remove_items("balls")

    print(inv.search_items("bats"))
    inv.show_stock()


if __name__ == "__main__":
    main()