import json
from pathlib import Path


file_path = Path(__file__).parent 

filename = file_path / "task master.json"


def load_tasks():

    try:
        with open(filename,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks":[]}
    
def save_tasks(tasks):

    try:
        with open(filename,"w") as file:
            json.dump(tasks,file)
    except FileNotFoundError:
        return {"tasks":[]}
    
def display_tasks(tasks):
    task_list = tasks["tasks"]

    if not task_list:
        print("No tasks available")
    else:
        print("\nYour To Do Tasks\n")
        for idx,task in enumerate(task_list,1):
            task_status = "Completed" if task['complete'] else "Pending"
            print(f"{idx}.{task['task_description']} [{task_status}]")
    
def add_task(tasks):
    
    task_description = input("Enter the task description: ")
    if task_description:
        tasks["tasks"].append({"task_description": task_description,"complete": False})
        save_tasks(tasks)
        print("Task saved successfully")
    else:
        print("Task description cannot be empty!")

def complete_task(tasks):

    display_tasks(tasks)
    if not tasks["tasks"]:
        print("No tasks available to mark as complete")
    
    
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks["tasks"]):
            tasks["tasks"][task_num - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete")
        else:
            print("\nEnter a valid task number!")
    except ValueError:
        print("\nPlease enter valid number!")

def incomplete_task(tasks):

    display_tasks(tasks)
    if not tasks["tasks"]:
        print("No tasks available to mark as incomplete")
    
    try:
        task_num = int(input("Enter the task number to mark as incomplete: "))
        if 1 <= task_num <= len(tasks["tasks"]):
            tasks["tasks"][task_num - 1]["complete"] = False
            save_tasks(tasks)
            print("Task marked as incomplete")
        else:
            print("\nEnter a valid task number!")
    except ValueError:
        print("\nPlease enter valid number!")

def delete_task(tasks):

    display_tasks(tasks)

    if not tasks["tasks"]:
        print("No tasks available")

    try:
        task_num = int(input("\nEnter the task number you want to delete: "))
        if 1 <= task_num <= len(tasks["tasks"]):
            deleted_task = tasks["tasks"].pop(task_num - 1)
            save_tasks(tasks)

            print(f"Deleted: {deleted_task['task_description']} task successfully")
        else:
            print("Please enter a valid task number")
    except ValueError:
        print("Please enter valid number!")

def main():  
    tasks = load_tasks()
   
    while True:
        print("\n✨Task Manager✨\n")
        print("1.View tasks")
        print("2.Add task")
        print("3.Complete task")
        print("4.Incomplete task")
        print("5.Delete task")
        print("6.Exit\n")

        choice = input("Enter your choice (1-6): ").strip()
        print()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            incomplete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("\nGoodbye...👋")
            print("Thank you for using the task master🥳")
            print()
            break
        else :
             print("Please enter a valid number")
        
if __name__ == "__main__":
    main()
