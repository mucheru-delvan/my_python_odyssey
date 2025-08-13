import random


questions = {
    "What is the main language for Android development?": "java",
    "Which protocol is used to transfer web pages?": "http",
    "What is the default port for HTTPS?": "443",
    "Which data type is used for true or false in Python?": "bool",
    "Which company developed the Go programming language?": "Google",
    "Which keyword creates a class in Python?": "class",
    "What is the main language for Arduino programming?": "c",
    "Which operator checks equality in Python?": "==",
    "What is the default Python package manager?": "pip",
    "Which version control system uses commits?": "git",
    "Which language is used in web browsers for logic?": "javascript"
}


def play_game():
    print("\n🌟Trivia Game🌟")
    print("----------------\n")
    score = 0
    total_questions = 9
    question_list = list(questions.keys())
    
    selected_questions = random.sample(question_list,total_questions)
    
    for idx,question in enumerate(selected_questions,start=1):
        print(f"{idx}.{question}")

        while True:
            user_answer = input("Enter your answer: ").lower().strip()
            if user_answer:
                break
            print("Answer cannot be blank!")

        correct_answer = questions[question].lower().strip()
        if user_answer == correct_answer:
            print("✅Correct!\n")
            score +=1
        else:
            print(f"❎Wrong!the correct answer is {correct_answer}\n")

    print("="*35)    
    print(f"You have scored {score} out of {total_questions} correct.")
    percentage = round(score/total_questions * 100,2)
    print(f"Your percentage score is {percentage}%.")
    print("="*35)

play_game()