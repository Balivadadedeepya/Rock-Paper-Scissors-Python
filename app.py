import random
import streamlit as st

CHOICES = ["Rock", "Paper", "Scissors"]
WINNING_SCORE = 3

st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮"
)

st.title("🎮 Rock Paper Scissors")
st.write("🏆 Best of 5 — First player to reach 3 wins!")

# Initialize game
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.game_over = False


def determine_winner(user, computer):
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


# Show game status
if st.session_state.game_over:
    if st.session_state.user_score == WINNING_SCORE:
        st.success("🏆 YOU WON THE MATCH!")
    else:
        st.error("💻 COMPUTER WON THE MATCH!")

    st.write(
        f"Final Score: **You {st.session_state.user_score} "
        f"- {st.session_state.computer_score} Computer**"
    )

else:
    user_choice = st.selectbox(
        "Choose your move:",
        CHOICES
    )

    if st.button("▶️ Play Round"):
        computer_choice = random.choice(CHOICES)
        result = determine_winner(user_choice, computer_choice)

        st.write(f"👤 **You:** {user_choice}")
        st.write(f"💻 **Computer:** {computer_choice}")

        if result == "User":
            st.success("🎉 You won this round!")
            st.session_state.user_score += 1

        elif result == "Computer":
            st.error("💻 Computer won this round!")
            st.session_state.computer_score += 1

        else:
            st.info("🤝 It's a tie!")
            st.session_state.ties += 1

        # Check if someone reached 3 wins
        if (
            st.session_state.user_score >= WINNING_SCORE
            or st.session_state.computer_score >= WINNING_SCORE
        ):
            st.session_state.game_over = True

        st.rerun()


# Scoreboard
st.divider()
st.subheader("📊 Scoreboard")

col1, col2, col3 = st.columns(3)

col1.metric("👤 You", st.session_state.user_score)
col2.metric("💻 Computer", st.session_state.computer_score)
col3.metric("🤝 Ties", st.session_state.ties)


# Reset button
if st.button("🔄 New Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0
    st.session_state.game_over = False
    st.rerun()
