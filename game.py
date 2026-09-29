def determine_winner(player_choice, computer_choice):
    """
    Compare player and computer choices
    and return the result.
    """

    if player_choice == computer_choice:
        return "draw"

    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or
        (player_choice == "paper" and computer_choice == "rock")
        or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "player"

    return "computer"


def display_result(player_choice, computer_choice, result):
    """Display the result of the round."""

    print("\n----------------------------")
    print("Your choice     :", player_choice)
    print("Computer choice :", computer_choice)

    if result == "player":
        print("Result          : You Win! 🎉")

    elif result == "computer":
        print("Result          : Computer Wins!")

    else:
        print("Result          : Draw!")

    print("----------------------------")