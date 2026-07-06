import random

choices = ["Rock", "Paper", "Scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")

while True:
    user = input("\nEnter Rock, Paper, or Scissors: ").capitalize()

    if user not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("🤝 It's a tie!")
    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("👋 Thanks for playing!")
        break
