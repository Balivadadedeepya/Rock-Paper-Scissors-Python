import random


CHOICES = ["Rock", "Paper", "Scissors"]


def get_user_choice():
    """Get and validate the player's choice."""
    while True:
        user_input = input(
            "\nEnter Rock, Paper, or Scissors: "
        ).strip().capitalize()

        if user_input in CHOICES:
            return user_input

        print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")


def determine_winner(user, computer):
    """Determine the winner of a round."""
    if user == computer:
        return "Tie"

    winning_combinations = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    if winning_combinations[user] == computer:
        return "User"

    return "Computer"


def display_result(user, computer, result):
    """Display the result of the current round."""
    print("\n" + "=" * 40)
    print(f"👤 You chose:      {user}")
    print(f"💻 Computer chose: {computer}")

    if result == "Tie":
        print("🤝 Result: It's a tie!")
    elif result == "User":
        print("🎉 Result: You win!")
    else:
        print("💻 Result: Computer wins!")

    print("=" * 40)


def play_game():
    """Run the Rock Paper Scissors game."""
    user_score = 0
    computer_score = 0
    ties = 0
    round_number = 1

    print("\n🎮 ROCK PAPER SCISSORS")
    print("Welcome to the game!")

    while True:
        print(f"\n🔹 Round {round_number}")

        user = get_user_choice()
        computer = random.choice(CHOICES)

        result = determine_winner(user, computer)

        if result == "User":
            user_score += 1
        elif result == "Computer":
            computer_score += 1
        else:
            ties += 1

        display_result(user, computer, result)

        print(
            f"📊 Score → You: {user_score} | "
            f"Computer: {computer_score} | Ties: {ties}"
        )

        play_again = input(
            "\nPlay another round? (yes/no): "
        ).strip().lower()

        if play_again not in ["yes", "y"]:
            break

        round_number += 1

    print("\n🏁 GAME OVER")
    print("-" * 40)
    print(f"👤 Your score:      {user_score}")
    print(f"💻 Computer score: {computer_score}")
    print(f"🤝 Total ties:      {ties}")
    print(f"🎯 Total rounds:    {round_number}")
    print("-" * 40)

    if user_score > computer_score:
        print("🏆 You won the game!")
    elif computer_score > user_score:
        print("💻 Computer won the game!")
    else:
        print("🤝 The game ended in a tie!")

    print("👋 Thanks for playing!")


if __name__ == "__main__":
    play_game()
