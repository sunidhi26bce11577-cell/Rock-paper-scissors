class Score:
    """Store and manage game scores."""

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0

    def update_score(self, result):
        """Update the score according to the result."""

        if result == "player":
            self.player_score += 1

        elif result == "computer":
            self.computer_score += 1

        elif result == "draw":
            self.draws += 1

    def display_score(self):
        """Display the current score."""

        print("\n========== SCORE ==========")
        print("Your Score     :", self.player_score)
        print("Computer Score :", self.computer_score)
        print("Draws          :", self.draws)
        print("============================")