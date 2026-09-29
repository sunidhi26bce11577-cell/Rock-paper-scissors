# ROCK PAPER SCISSORS GAME

## 1. Project Title

**Rock Paper Scissors Game Using Python**

---

## 2. Introduction

Rock Paper Scissors is a simple game played between a user and a computer. The player chooses one of three options: Rock, Paper, or Scissors. The computer also randomly selects one option. The choices are compared according to the rules of the game, and the winner is displayed.

This project is developed using Python. The program is divided into multiple Python files so that different parts of the application can be managed separately.

---

## 3. Problem Statement

The objective of this project is to develop a simple and interactive Rock Paper Scissors game using Python.

The system should:

* Allow the user to choose Rock, Paper, or Scissors.
* Generate a random choice for the computer.
* Compare the player's choice with the computer's choice.
* Determine whether the player wins, the computer wins, or the round is a draw.
* Maintain the scores.
* Allow the user to play multiple rounds.
* Provide instructions and menu options.

---

## 4. Objectives

The main objectives of the project are:

1. To understand the basic concepts of Python programming.
2. To use functions and conditional statements.
3. To use Python modules and multiple files.
4. To generate random choices using Python.
5. To implement score management.
6. To perform input validation.
7. To develop a simple menu-driven application.
8. To understand how a Python project can be divided into different modules.

---

## 5. Technologies Used

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Programming language    |
| VS Code    | Development environment |
| Git        | Version control         |
| GitHub     | Project repository      |

---

## 6. System Requirements

### Hardware Requirements

* Computer or laptop
* Keyboard
* Minimum 4 GB RAM
* Basic storage space

### Software Requirements

* Python 3.14.7
* Visual Studio Code
* Git
* GitHub account

---

## 7. Main Features

### 7.1 Player Choice

The player can select:

* Rock
* Paper
* Scissors

### 7.2 Computer Choice

The computer generates a random choice using Python's random module.

### 7.3 Winner Detection

The program compares both choices.

Rules:

* Rock beats Scissors.
* Scissors beats Paper.
* Paper beats Rock.
* Same choices result in a draw.

### 7.4 Score Management

The program maintains:

* Player score
* Computer score
* Number of draws

### 7.5 Menu

The main menu provides options to:

1. Play Game
2. View Instructions
3. View Score
4. Exit

### 7.6 Input Validation

The program checks whether the user has entered a valid choice and asks again if the input is invalid.

---

## 8. Project Modules

The project is divided into different Python files.

```text
RockPaperScissors/
│
├── main.py
├── game.py
├── player.py
├── score.py
├── menu.py
├── utils.py
└── README.md
```

### main.py

This is the main program. It connects all other modules and controls the flow of the application.

### player.py

This module handles the player's choice and generates the computer's random choice.

### game.py

This module contains the game logic and determines the winner of each round.

### score.py

This module stores and updates the scores of the player, computer, and draws.

### menu.py

This module displays the main menu and game instructions.

### utils.py

This module contains helper functions such as menu input validation and asking the player whether they want to play again.

---

## 9. Program Workflow

The basic workflow of the application is:

```text
Start
  ↓
Display Main Menu
  ↓
Select an Option
  ↓
Play Game
  ↓
Get Player Choice
  ↓
Generate Computer Choice
  ↓
Compare Choices
  ↓
Determine Winner
  ↓
Update Score
  ↓
Display Result
  ↓
Play Again?
  ↓
Yes ─────────→ New Round
  ↓
No
  ↓
Return to Menu
  ↓
Exit
```

---

## 10. Game Logic

The winner is determined using conditional statements.

```text
If player choice = computer choice
        ↓
      Draw

Otherwise

Rock + Scissors
        ↓
      Player Wins

Paper + Rock
        ↓
      Player Wins

Scissors + Paper
        ↓
      Player Wins

Otherwise
        ↓
   Computer Wins
```

---

## 11. Input and Output

### Input

The user enters:

```text
rock
```

or

```text
paper
```

or

```text
scissors
```

### Output

The program displays the player's choice, computer's choice, result, and updated score.

Example:

```text
Your choice     : rock
Computer choice : scissors
Result          : You Win!

========== SCORE ==========
Your Score     : 1
Computer Score : 0
Draws          : 0
============================
```

---

## 12. Testing

The program should be tested with different combinations of choices.

| Test Case | Player Choice | Computer Choice | Expected Result     |
| --------- | ------------- | --------------- | ------------------- |
| 1         | Rock          | Rock            | Draw                |
| 2         | Rock          | Scissors        | Player Wins         |
| 3         | Rock          | Paper           | Computer Wins       |
| 4         | Paper         | Rock            | Player Wins         |
| 5         | Paper         | Scissors        | Computer Wins       |
| 6         | Scissors      | Paper           | Player Wins         |
| 7         | Scissors      | Rock            | Computer Wins       |
| 8         | Scissors      | Scissors        | Draw                |
| 9         | Invalid input | -               | Ask for valid input |

---

## 13. Error Handling

The application provides basic input validation.

For example, if the user enters:

```text
Enter your choice: apple
```

The program displays:

```text
Invalid choice! Please enter rock, paper, or scissors.
```

Similarly, the menu accepts only options from 1 to 4.

---

## 14. Advantages

* Simple and easy to use.
* Beginner-friendly Python project.
* Uses multiple modules.
* Provides input validation.
* Maintains scores.
* Allows multiple rounds.
* Demonstrates functions, classes, conditions, loops, and modules.

---

## 15. Limitations

* The game is currently text-based.
* It supports only one human player.
* Scores are not permanently stored after the program closes.
* The computer uses random choices rather than an advanced strategy.

---

## 16. Future Enhancements

The project can be improved by adding:

* Graphical User Interface (GUI).
* Multiple human players.
* Difficulty levels.
* Permanent score storage.
* Player name and profile.
* Game statistics.
* Sound effects and animations.
* Database support.
* Online multiplayer functionality.

---

## 17. Learning Outcomes

Through this project, the following concepts were practiced:

* Python variables
* Input and output
* Conditional statements
* Loops
* Functions
* Classes and objects
* Random number generation
* Modules and imports
* Input validation
* File organization
* Basic software testing
* Git and GitHub

---

## 18. Conclusion

The Rock Paper Scissors Game is a simple Python project that demonstrates the implementation of a complete menu-driven application.

The project uses multiple Python modules to separate different responsibilities such as game logic, player input, score management, menu handling, and validation.

This project provides practical experience with Python programming and basic project development using GitHub.

---

## 19. GitHub Repository Structure

The final repository should contain:

```text
RockPaperScissors/
│
├── main.py
├── game.py
├── player.py
├── score.py
├── menu.py
├── utils.py
├── README.md
└── PROJECT_REPORT.md
```

---

## 20. References

* Python documentation
* Python `random` module documentation
* Course/project guidelines provided for the VITyarthi project

