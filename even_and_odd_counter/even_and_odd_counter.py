print("Even & Odd Counter\n")

start = int(input("Enter start number: "))
end = int(input("Enter end number:"))

even_count = 0
odd_count = 0

for num in range(start,end + 1):
    if num % 2 == 0:
        even_count += 1
    if num % 2 != 0:
        odd_count += 1
print()
print(f"Even numbers from {start} to {end}: {even_count}")
print(f"Odd numbers from {start} to {end}: {odd_count}")