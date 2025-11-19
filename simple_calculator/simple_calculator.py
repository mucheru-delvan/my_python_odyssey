print("🪙 Simple Python Calculator🪙\n")

def simple_calc(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: division by zero!"
        else:
            return a / b
    else:
        return "Error: Invalid operator!"


while True:
    num1 = float(input("Enter the first number: "))
    the_operator = input("Choose the operator (*,+,-,/): ").strip()
    num2 = float(input("Enter the second number: "))
    
    result = simple_calc(num1, num2, the_operator)
    print(f"\n{num1} {the_operator} {num2} = {result}\n")
    
    # Ask if user wants to continue calculating
    again = input("Calculate again? (yes/no): ").strip().lower()
    if again not in ["y","yes"]:
        print("Thanks for using the calculator! Goodbye! 🪙")
        break