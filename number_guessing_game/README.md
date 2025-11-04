# Number Guessing Game 

A fun Python command-line Number Guessing Game!  
Try to guess the secret number in as few attempts as possible, and challenge yourself to set a new best score.

## Features

- Set your own minimum and maximum guessing range.
- Choose how many guesses you get.
- The game keeps track of your best score in the session.
- Play as many rounds as you like.

## How to Play

1. **Run the game:**

   ```sh
   python number_guessing_game.py
   ```

2. **Follow the prompts:**
   - Set the minimum and maximum numbers for the secret number range.
   - Choose the maximum number of guesses you'll get.
   - Try to guess the secret number!
   - After each guess, you'll be told whether your guess is too high or too low.
   - If you guess correctly, your attempt count is compared to your best score.

3. **Play again, or exit the game:**
   - After each round, you can choose to play again and try to beat your best score.

## Example

```text
🎮 Welcome to a Python Number Guessing Game!
Enter the minimum number: 1
Enter the maximum number: 100
Enter the maximum number of guesses: 7
Enter your guess: 50
Too high!
Enter your guess: 25
Too low!
Enter your guess: 37
🎉 Correct! You got it in 3 tries.
🥇 New best score!
🏆 Best score so far: 3
Play again? (y/n): n
👋 Thanks for playing!
```

## Requirements

- Python 3.x
