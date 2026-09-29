import random


def get_player_choice():
    """Get a valid choice from the player."""

    choices = ["rock", "paper", "scissors"]

    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower().strip()

        if choice in choices:
            return choice

        print("Invalid choice! Please enter rock, paper, or scissors.")


def get_computer_choice():
    """Generate a random choice for the computer."""

    choices = ["rock", "paper", "scissors"]

    return random.choice(choices)