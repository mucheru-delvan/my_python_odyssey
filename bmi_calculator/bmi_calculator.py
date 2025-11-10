print("🤩 Python BMI Calculator 🤩\n")

while True:
    try:
        height = float(input("Enter your height in metres: "))
        weight = float(input("Enter your body weight in kg: "))

        if height <= 0 or weight <= 0:
            print("Height and weight must be positive numbers!\n")
            continue
        break
    except ValueError:
        print("Please enter valid numbers!\n")

bmi = weight / (height ** 2)
bmi = round(bmi, 2)

print(f"\nYour BMI is: {bmi}\n")

if bmi < 18.5:
    print("You are underweight!")
elif 18.5 <= bmi <= 24.9:
    print("You are normal weight!")
elif 25 <= bmi <= 29.9:
    print("You are overweight!")
else:
    print("You are obese!")
