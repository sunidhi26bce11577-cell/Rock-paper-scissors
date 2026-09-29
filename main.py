from player import get_player_choice, get_computer_choice
from game import determine_winner, display_result
from score import Score
from menu import display_menu, display_instructions
from utils import get_menu_choice, ask_play_again


def play_game(score):
    """Run the Rock Paper Scissors game."""

    while True:
        print("\n----- NEW ROUND -----")

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(player_choice, computer_choice)

        score.update_score(result)

        display_result(
            player_choice,
            computer_choice,
            result
        )

        score.display_score()

        if not ask_play_again():
            break


def main():
    """Main program."""

    score = Score()

    while True:
        display_menu()

        choice = get_menu_choice()

        if choice == "1":
            play_game(score)

        elif choice == "2":
            display_instructions()

        elif choice == "3":
            score.display_score()

        elif choice == "4":
            print("\nThank you for playing!")
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
