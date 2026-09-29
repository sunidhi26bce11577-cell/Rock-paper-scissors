def get_menu_choice():
    """Get a valid menu choice from the user."""

    while True:
        choice = input("Enter your choice (1-4): ").strip()

        if choice in ["1", "2", "3", "4"]:
            return choice

        print("Invalid choice! Please enter a number from 1 to 4.")


def ask_play_again():
    """Ask the player whether they want another round."""

    while True:
        answer = input("\nDo you want to play again? (yes/no): ").lower().strip()

        if answer in ["yes", "y"]:
            return True

        if answer in ["no", "n"]:
            return False

        print("Please enter yes or no.")