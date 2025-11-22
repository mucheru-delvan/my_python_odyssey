

# 🎯 Trivia Game (Python CLI)

A simple and fun **command-line trivia quiz game** built in Python.
The game selects random questions, checks your answers, and displays your score and percentage at the end.

---

## Features

*  Random selection of trivia questions
*  Variety of tech-related questions
*  User input validation (no blank answers)
*  Score and percentage calculation
*  Simple and beginner-friendly Python code

---

## 📂 Project Structure

```
trivia_game/
│── trivia_game.py
│── README.md
```

---

##  How It Works

* A dictionary stores questions as **keys** and correct answers as **values**
* `random.sample()` selects 9 unique questions
* The user answers each question
* The program compares the answer and tallies the score
* A final score out of 9 and a percentage are displayed

---


## Sample Output

```
🌟Trivia Game🌟
----------------

1. Which protocol is used to transfer web pages?
Enter your answer: http
✅Correct!

...
===================================
You have scored 7 out of 9 correct.
Your percentage score is 77.78%.
===================================
```

---

##  Future Improvements (Try for Yourself)

* Add multiple-choice questions
* Add categories (Tech, Math, General Knowledge, etc.)
* Add difficulty levels
* Load questions from a JSON file instead of a Python dictionary

---
