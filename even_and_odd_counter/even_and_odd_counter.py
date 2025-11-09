print("🌠 Even & Odd Counter 🌠\n")

try:
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
except ValueError:
    print("❌ Please enter valid integers.")
    exit()

even_numbers = []
odd_numbers = []

for num in range(start, end + 1):
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


print(f"\nEven numbers from {start} to {end}: {len(even_numbers)}")
print(f"{even_numbers if even_numbers else 'None'}")

print(f"\nOdd numbers from {start} to {end}: {len(odd_numbers)}")
print(f"{odd_numbers if odd_numbers else 'None'}")
