Rock Paper Scissors Game 🎮

A simple and interactive Rock Paper Scissors game developed using Python. The project is designed using multiple Python modules, with each file responsible for a specific part of the application.

📌 Project Description

Rock Paper Scissors is a game played between a user and the computer. The player selects Rock, Paper, or Scissors, while the computer makes a random choice.

The program compares both choices and determines whether the player wins, the computer wins, or the round is a draw.

The project also keeps track of the scores and provides a simple menu for playing the game, viewing instructions, checking scores, and exiting the application.

🎯 Objectives
Develop a Rock Paper Scissors game using Python.
Practice Python functions, classes, conditions, and loops.
Use multiple Python files/modules.
Generate random choices for the computer.
Maintain player and computer scores.
Validate user input.
Create a simple menu-driven application.
✨ Features
🎮 Play Rock Paper Scissors against the computer.
🤖 Computer makes a random choice.
🏆 Automatically determines the winner.
📊 Keeps track of player score, computer score, and draws.
📖 Displays game instructions.
🔄 Allows the player to play multiple rounds.
✅ Validates incorrect user input.
📋 Simple and easy-to-use menu.
🗂️ Project Structure
RockPaperScissors/
│
├── main.py
├── game.py
├── player.py
├── score.py
├── menu.py
├── utils.py
└── README.md
📁 File Description
File	Description
main.py	Starts and controls the whole program
game.py	Contains Rock-Paper-Scissors game logic
player.py	Handles player and computer choices
score.py	Keeps track of scores
menu.py	Displays menu and instructions
utils.py	Input validation and helper functions
README.md	Project documentation
🎲 Game Rules

The game follows these rules:

Rock beats Scissors
Scissors beats Paper
Paper beats Rock
If both choices are the same, the result is a Draw
Example
Player: Rock
Computer: Scissors

Result: Player Wins!
🛠️ Technologies Used
Python 3
Visual Studio Code
Git
GitHub
▶️ How to Run the Project
1. Install Python

Make sure Python 3 is installed on your computer.

You can check it using:

python --version
2. Open the Project

Open the RockPaperScissors folder in Visual Studio Code.

3. Open the Terminal

In VS Code, select:

Terminal → New Terminal
4. Run the Program

Type:

python main.py

and press Enter.

🖥️ Example Output
==============================
     ROCK PAPER SCISSORS
==============================
1. Play Game
2. View Instructions
3. View Score
4. Exit
==============================

Enter your choice (1-4): 1

----- NEW ROUND -----

Enter your choice (rock/paper/scissors): rock

----------------------------
Your choice     : rock
Computer choice : scissors
Result          : You Win!
----------------------------

========== SCORE ==========
Your Score     : 1
Computer Score : 0
Draws          : 0
============================
🧪 Testing

The program can be tested using different combinations:

Player Choice	Computer Choice	Result
Rock	Rock	Draw
Rock	Paper	Computer Wins
Rock	Scissors	Player Wins
Paper	Rock	Player Wins
Paper	Paper	Draw
Paper	Scissors	Computer Wins
Scissors	Rock	Computer Wins
Scissors	Paper	Player Wins
Scissors	Scissors	Draw

Invalid inputs are also tested to make sure the program asks the user to enter a valid choice.

🔮 Future Enhancements

The project can be improved in the future by adding:

Graphical User Interface (GUI)
Multiple players
Difficulty levels
Permanent score storage
Player names
Game statistics
Sound effects
Animations
Online multiplayer mode
📚 Learning Outcomes

Through this project, the following Python concepts were practiced:

Variables
Input and output
Conditional statements
Loops
Functions
Classes and objects
Random module
Python modules
Input validation
File organization
Basic testing
👨‍💻 Project

Project: Rock Paper Scissors Game
Language: Python
Platform: VITyarthi Project
Repository: GitHub

