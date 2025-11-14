import json
import statistics
from pathlib import Path

#I added this base dir to make sure the data.json file is 
# created in the same directory as this script
# It avoids issues when running the script from different working directories.
BASE_DIR = Path(__file__).parent
filename = BASE_DIR / "data.json"

def load_students():

    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"data": []}

def save_students(data):

    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    except FileNotFoundError:
        return {"data": []}

def add_student(data):

    while True:
        
        name = input("Enter the student name: ").strip()
        if not name:
            print("Name cannot be blank")
            continue
        try:
            grade = float(input("Enter the student grade: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        data["data"].append({"name": name, "grade": grade})
        save_students(data)
        print(f"{name} with grade {grade} added successfully!")
        break

def view_students(data):
    students = data["data"]
    if not students:
        print("No students added yet!")
    else:
        print("\n🏆 Students Performance 🏆\n")
        sorted_students = sorted(students,key=lambda x:x['grade'],reverse=True)
        for idx, s in enumerate(sorted_students, start=1):
            print(f"{idx}. {s['name'].capitalize()} : {s['grade']}")


        grades = [s['grade'] for s in students]
        average = round(statistics.mean(grades),2)
        print(f"\nAverage grade :{average}")

def remove_student(data):
    view_students(data)

    if not data["data"]:
        print("No students to remove!")
        
    else:
        try:
            student_num = int(input("Enter the student number to remove: "))
            deleted_student = data["data"].pop(student_num - 1)
            save_students(data)
            print(f"{deleted_student['name']} removed successfully!")
        except (ValueError, IndexError):
            print("Invalid selection!")

def main():
    data = load_students()

    while True:
        print("\n🎖️ Student GradeBook App 🎖️\n")
        print("1. View Students")
        print("2. Add Student")
        print("3. Remove Student")
        print("4. Exit\n")

        choice = input("Choose (1-4): ")
        if choice == "1":
            view_students(data)
        elif choice == "2":
            add_student(data)
        elif choice == "3":
            remove_student(data)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
