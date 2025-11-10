print("🚀Multiplication table generator🚀\n")

number = int(input("Enter a number to generate its table: "))

print(f"\nMultiplication table for {number}:\n")

for i in range(1,13):
    print(f"{number} x {i} = {number*i}")