# Rock Paper Scissors Game

This is a classic two-player game of Rock-Paper-Scissors with a twist: you can play multiple rounds and decide the winner based on a "best of" system.

## How to Play
1. Run the script using Python.
2. Enter the names of both players.
3. Decide the "best of" rounds (e.g., 3, 5, 7).
4. Each player chooses Rock, Paper, or Scissors by entering `r`, `p`, or `s`.
5. The game announces the winner of each round and keeps track of scores.
6. The first player to win the majority of rounds wins the game.

## Dependencies
- None (uses Python Standard Library only)

## How to Run
```bash
python rock_paper_scissor.py
```

## Example
```
Player1: What's your name? Alice
Player2: What's your name? Bob
Enter 'Best of' rounds (e.g. 3, 5, 7): 3
First to 2 wins take the match!

Alice: Rock, paper, or Scissors? (r/p/s): r
Bob: Rock, paper, or Scissors? (r/p/s): p
Alice chose: ✊
Bob chose: 📄
✅ Bob wins this round!

Current Score:
Alice: 0 | Bob: 1 | Ties: 0

Continue? (y/n): y
...
```