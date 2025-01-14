# Project: Enhancing Python Skills with ChatGPT

## Introduction

This project aims to improve Python coding skills through debugging, automation, and AI-driven solutions, specifically leveraging ChatGPT.

## Objectives

- **Debugging**: Enhance troubleshooting and error correction.
- **Automation**: Automate repetitive coding tasks for efficiency.
- **Code Quality**: Improve code structure with AI insights.

## Tasks

### 1. Debugging - Python Factorial
```python
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Avoid infinite loop
    return result
2. Debugging - Python Arguments
python
Copier le code
import sys

for i in range(1, len(sys.argv)):
    print(sys.argv[i])
3. Debugging - HTML/JavaScript
html
Copier le code
<button id="colorButton">Change Color</button>
<script>
    document.getElementById("colorButton").addEventListener("click", function() {
        changeBackgroundColor();
    });
</script>
4. Debugging - Python Minesweeper
python
Copier le code
def check_victory(self):
    for y in range(self.height):
        for x in range(self.width):
            if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                return False
    return True

def play(self):
    while True:
        self.print_board()
        if self.check_victory():
            print("Congratulations! You've won the game.")
            break
5. Documentation - Python Factorial
python
Copier le code
def factorial(n):
    """
    Calculate factorial of a number.
    Parameters: n (int)
    Returns: int
    """
    if n == 0:
        return 1
    return n * factorial(n-1)
6. Error Handling - Python Checkbook
python
Copier le code
def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit': break
        if action.lower() == 'deposit':
            try:
                amount = float(input("Enter deposit amount: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input!")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter withdraw amount: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input!")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command.")
7. Debugging - Tic Tac Toe Game
python
Copier le code
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row, col = int(input(f"Enter row for {player}: ")), int(input(f"Enter col for {player}: "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("Invalid move.")
        except ValueError:
            print("Invalid input.")
Grading Criteria
Debugging (0-1 points): Fix the error and match the expected output.
Documentation (0-1 point): Proper comments and explanations.
Error Handling (0-1 point): Handle invalid inputs without crashing.
Resources
Python Docs
PEP8 Style Guide
Conclusion
This project improves Python skills, focusing on debugging, automation, and code documentation with AI assistance.# holbertonschool-higher_level_programming
