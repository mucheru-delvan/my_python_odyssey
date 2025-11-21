import json
import random
from pathlib import Path

BASE_DIRECTORY = Path(__file__).parent
filename = BASE_DIRECTORY / "Questions.json"

import random

def play_game(questions):
    print("\n🎮 WELCOME TO THE ULTIMATE QUIZ GAME!\n")

    # 🔹 Extract categories dynamically
    categories = list(set(q["category"] for q in questions))

    print("📚 Available Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    # 🔹 Choose a category
    while True:
        try:
            choice = int(input("\nSelect a category number: "))
            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\n👉 You selected: {selected_category}")

    # 🔹 Extract difficulty levels inside that category
    difficulties = list(set(
        q["difficulty"] for q in questions if q["category"] == selected_category
    ))

    print("\n🔥 Available Difficulty Levels:")
    for i, level in enumerate(difficulties, 1):
        print(f"{i}. {level}")

    # 🔹 Select difficulty
    while True:
        try:
            diff_choice = int(input("\nSelect a difficulty number: "))
            if 1 <= diff_choice <= len(difficulties):
                selected_difficulty = difficulties[diff_choice - 1]
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Enter a number.")

    print(f"\n🎯 Difficulty Selected: {selected_difficulty}\n")

    # 🔹 Filter questions for BOTH category + difficulty
    filtered_questions = [
        q for q in questions
        if q["category"] == selected_category and q["difficulty"] == selected_difficulty
    ]

    if not filtered_questions:
        print("❌ No questions found for that category/difficulty.")
        return

    random.shuffle(filtered_questions)

    score = 0

    for q in filtered_questions:
        print(f"❓ {q['question']}")
        for opt_key, opt_value in q["options"].items():
            print(f"  {opt_key}. {opt_value}")

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in q["options"]:
                break
            print("Invalid option. Choose A, B, C, or D.")

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was: {q['answer']}\n")

    print("🎉 QUIZ COMPLETE!")
    print(f"🏆 Your Score: {score}/{len(filtered_questions)}")
