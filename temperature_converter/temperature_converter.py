
def temperature_converter():

    while True:
        print("\n🌟Temperature Converter🌟")
        print("1.Celsius to Fahreinheit")
        print("2.Celsius to Kelvin")
        print("3.Fahreinheit to Kelvin")
        print("4.Exit")

        option = input("Choose: ")
        if option == "4":
            break

        try:

            if option == "1":
                temp = float(input("Enter temperature: "))
                print(f"{temp} Celsius = {(temp * 9/5)+ 32:.2f} Fahreinheit")
                print(f"{temp} Fahreinheit = {(temp - 32)*5/9:.2f} Celsius")
            elif option == "2":
                temp = float(input("Enter temperature: "))
                print(f"{temp} Celsius = {(temp + 273)} Kelvin")
                print(f"{temp} Kelvin = {temp - 273} Celsius")
            elif option == "3":
                temp = float(input("Enter temperature: "))
                print(f"{temp} Fahreinheit = {(temp - 32) * 5/9 + 273:.2f} Kelvin")
                print(f"{temp} Kelvin = {(temp - 273) * 9/5 + 32:.2f} Fahreinheit")

        except ValueError:
            print("Please enter a valid number!")

    print("Goodbye")

temperature_converter()

