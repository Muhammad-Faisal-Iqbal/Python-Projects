# Number Guessing Game

This is a number guessing game where the player tries to guess a randomly generated number within a specified range and a limited number of attempts.

## How to Play
1. Run the script using Python.
2. Enter a range of numbers (e.g., `1,100`).
3. Try to guess the randomly generated number within 5 attempts.
4. The game will provide hints if your guess is too high or too low.
5. If you guess correctly, you win! Otherwise, the correct number will be revealed after 5 attempts.

## Dependencies
- Python Standard Library: `random`

## How to Run
```bash
python number_guessing_game.py
```

## Example
```
Enter a range of number Separated by comma like (1,100): 1,100
Enter a number to guess b/w 1 to 100: 50
Too high! You have 4 attempts left.
Enter a number to guess b/w 1 to 100: 25
Too low! You have 3 attempts left.
Enter a number to guess b/w 1 to 100: 37
Congratulation! You guessed the number in 3 attempts.
You are score is: 100
```