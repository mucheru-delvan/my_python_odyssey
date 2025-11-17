from inventory_manager import SimpleInventory

def main():
    #you can add your json file path here if needed else it will use the default items.json
    inv = SimpleInventory()

    inv.add_items("balls", 9)
    inv.add_items("bats", 5)
    inv.add_items("jersey", 6)
    inv.add_items("gloves", 4)
    inv.remove_items("balls")

    print(inv.search_items("bats"))
    inv.show_stock()


if __name__ == "__main__":
    main()