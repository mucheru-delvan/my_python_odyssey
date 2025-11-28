
def report_generator():
    print("\n🏁Student Marks Report Generator🏁\n")
    print("⚖️ Enter the students marks in the subjects provided\n")

    data = []
    
    while True:
        name = input("Enter your name: ")
        if name:
            break
        print("You must have a name student!")


    while True:
        
        subject = input("Enter the unit name ('q' to finish ): ").lower().strip()
       
        if subject == "q":
            print("Thank you for using the marks generator bye👋")
            
            break

        if not subject:
            print("Subject cannot be empty!")

            continue

        try:

            grade = float(input(f"Enter the grade you scored for {subject} %: "))

        except ValueError:
            print("Please enter a valid grade!")

            continue
        
        data.append({"name":name,"subject":subject,"grade":grade})
        print(f"\nAdded {subject} with {grade}%\n")
        
    if not data:
        print("\nNo data to generate report!")
        return
      
    print(f"\n🏆{name.capitalize()}'s Marks Report🏆\n")

    sorted_data = sorted(data,key=lambda x:x['grade'],reverse= True)

    for idx, mark in enumerate(sorted_data,1):
        print(f"{idx}.{mark['subject'].title()} — {mark['grade']}%")
   
    linear_gpa = [mark['grade']/100 * 4.0 for mark in sorted_data]
    overall_gpa = sum(linear_gpa)/len(linear_gpa)
    print(f"\nLinear GPA:{round(overall_gpa,2)}")

report_generator()


