import random

FILENAME = "scores.txt"

# a list of the valid choices in the game
CHOICES = ["rock", "paper", "scissors"]

# a dictionary describing what beats what
# key = a choice, value = the choice it beats
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


# ---------- File Handling ----------

def load_scores():
    scores = {
        "wins": 0,
        "losses": 0,
        "ties": 0
    }

    try:
        file = open(FILENAME, "r")
    except FileNotFoundError:
        return scores  # no file yet, start fresh

    for line in file:
        line = line.strip()
        if line == "":
            continue

        # each line looks like: wins|3
        key, value = line.split("|", 1)
        scores[key] = int(value)

    file.close()
    return scores


def save_scores(scores):
    file = open(FILENAME, "w")

    for key in scores:
        file.write(key + "|" + str(scores[key]) + "\n")

    file.close()


# ---------- Core Game Logic ----------

def get_computer_choice():
    return random.choice(CHOICES)


def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper, or scissors.")


def decide_winner(player, computer):
    if player == computer:
        return "tie"

    if BEATS[player] == computer:
        return "player"

    return "computer"


def play_round(scores):
    player = get_player_choice()
    computer = get_computer_choice()

    print("\nYou chose: " + player)
    print("Computer chose: " + computer)

    result = decide_winner(player, computer)

    if result == "tie":
        print("It's a tie!")
        scores["ties"] += 1
    elif result == "player":
        print("You win this round!")
        scores["wins"] += 1
    else:
        print("Computer wins this round!")
        scores["losses"] += 1


def show_scores(scores):
    print("\n--- Scoreboard ---")
    print("Wins: " + str(scores["wins"]))
    print("Losses: " + str(scores["losses"]))
    print("Ties: " + str(scores["ties"]))


# ---------- Menu ----------

def show_menu():
    print("\n=== Rock, Paper, Scissors ===")
    print("1. Play a round")
    print("2. View scoreboard")
    print("3. Exit")


def main():
    scores = load_scores()

    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            play_round(scores)
        elif choice == "2":
            show_scores(scores)
        elif choice == "3":
            save_scores(scores)
            print("Scores saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()