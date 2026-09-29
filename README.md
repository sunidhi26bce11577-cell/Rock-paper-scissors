# Rock Paper Scissors Game

## 1. Project Description

Rock Paper Scissors is a simple Python-based game in which the player plays against the computer.

The computer randomly chooses Rock, Paper, or Scissors. The player also chooses one option, and the program compares both choices to determine the winner.

The project is divided into different Python modules so that each part of the program has a specific responsibility.

## 2. Features

* Play Rock Paper Scissors against the computer
* Computer makes a random choice
* Player score tracking
* Computer score tracking
* Tie tracking
* Game history
* Save and load game history
* View game statistics
* Player win percentage
* Input validation
* Menu-based interface
* Multiple Python modules

## 3. Rules of the Game

The rules are:

* Rock beats Scissors
* Scissors beats Paper
* Paper beats Rock
* If both players choose the same option, the game is a tie

## 4. Technologies Used

* Python
* JSON
* Visual Studio Code
* Git
* GitHub

## 5. Project Structure

```text
Rock-Paper-Scissors/
│
├── main.py
├── game.py
├── score.py
├── validation.py
├── history.py
├── storage.py
├── statistics.py
├── display.py
├── README.md
└── game_history.json
```

## 6. Description of Files

### main.py

The main file of the project. It controls the menu and connects all the different modules.

### game.py

Contains the main game logic. It generates the computer's choice and determines the winner.

### score.py

Keeps track of player wins, computer wins, and ties.

### validation.py

Checks whether the player's input is valid.

### history.py

Stores and displays the results of the games played.

### storage.py

Saves and loads game history using a JSON file.

### statistics.py

Calculates total games, player wins, computer wins, ties, and player win percentage.

### display.py

Contains functions for displaying the title, menu, round information, and game results.

### game_history.json

Stores the game history so that it can be accessed again when the program is run.

## 7. How to Run the Project

### Step 1

Install Python on your computer.

### Step 2

Open the project folder in Visual Studio Code.

### Step 3

Open the VS Code terminal.

### Step 4

Run the following command:

```text
python main.py
```

### Step 5

Select an option from the menu.

## 8. Main Menu

The program provides the following options:

```text
1. Play Game
2. View Score
3. View Game History
4. View Statistics
5. Exit
```

## 9. Example

```text
================================
      ROCK PAPER SCISSORS
================================

---------- MENU ----------
1. Play Game
2. View Score
3. View Game History
4. View Statistics
5. Exit

Enter your choice: 1

Enter rock, paper, or scissors: rock

You chose: rock
Computer chose: scissors
You win!
```

## 10. Future Improvements

The project can be improved in the future by adding:

* Graphical user interface
* Different game modes
* Player names
* Sound effects
* More detailed statistics
* Multiplayer mode

## 11. Conclusion

The Rock Paper Scissors project demonstrates the use of basic Python programming concepts such as functions, classes, conditional statements, loops, modules, file handling, JSON, and input validation.

The project also demonstrates how a Python program can be divided into multiple modules to make the code easier to understand and maintain.

