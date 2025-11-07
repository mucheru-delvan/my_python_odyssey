print("Simple Calculator for Noobs\n")

first_number = float(input("Enter the first number: "))
operator = input("Choose an operator (*,/,+,-): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
    print(f"{first_number} {operator} {second_number} = {result}")

elif operator == "-":
    result = first_number - second_number
    print(f"{first_number} {operator} {second_number} = {result}")

elif operator == "*":
    result = first_number * second_number
    print(f"{first_number} {operator} {second_number} = {result}")

elif operator == "/":
    if second_number == 0:
        print("Cannot divide by zero!")
    else:
        result = first_number / second_number
        print(f"{first_number} {operator} {second_number} = {result}")
else:
    print("Invalid input!")
