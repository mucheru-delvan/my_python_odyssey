import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
filename = BASE_DIR / "expenses.json"


def load_expenses():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)


def view_expenses(expenses):
    if not expenses:
        print("No expenses added yet!")
        return

    print("\n💰 Your Expenses List 💰\n")
    total_spent = 0

    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category'].capitalize()}: "
              f"{expense['description'].capitalize()} - ${expense['amount']}")
        total_spent += expense["amount"]

    print(f"\nTotal expenses: ${total_spent}\n")


def add_expense(expenses):
    while True:
        category = input("Enter the category (food, rent, etc.): ").strip()
        if not category:
            print("Category cannot be empty!")
            continue

        description = input(f"Enter the {category} description: ").strip()
        if not description:
            print("Description cannot be empty!")
            continue

        try:
            amount = float(input(f"Enter the amount for {description}: $"))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        expenses.append({
            "category": category,
            "description": description,
            "amount": amount
        })

        save_expenses(expenses)
        print(f"\nAdded: {category} - {description} @ ${amount}\n")
        break


def remove_expense(expenses):
    if not expenses:
        print("No expenses to remove!")
        return

    view_expenses(expenses)

    try:
        expense_num = int(input("Enter the expense number to remove: "))
        if 1 <= expense_num <= len(expenses):
            removed = expenses.pop(expense_num - 1)
            save_expenses(expenses)
            print(f"{removed['description']} removed successfully.")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    expenses = load_expenses()

    while True:
        print("\n💸 Expense Tracker 💸\n")
        print("1. View expenses")
        print("2. Add expense")
        print("3. Remove expense")
        print("4. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            remove_expense(expenses)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    main()
