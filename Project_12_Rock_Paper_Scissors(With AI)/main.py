import random  # import random module to let the computer pick a random choice

def get_user_choice(): 
    # Keep asking until the user gives a valid input (0, 1, 2 or 3)
    while True:
        try:
            # Ask for a number and convert to integer
            choice = int(input("Choose 0. rock\n1. paper\n2. scissors\n3. quit(enter the number in front): "))

            # Check if the number is outside the valid range 0-3
            if choice not in range(4):
                print("Invalid Input. Try again")
            else:
                # Valid input — return it
                return choice
        except ValueError:
            # int() raises ValueError if user types something that isn't a number
            print("Invalid Input try again")

def get_winner(player_choice, ai_choice):
    # Determine the winner using modular arithmetic
    # Returns: 0 = draw, 1 = player wins, 2 = player loses
    # Formula: (3 + player - ai) % 3
    # Rock(0) vs Scissors(2): (3+0-2)%3 = 1 → win ✓
    # Paper(1) vs Rock(0):    (3+1-0)%3 = 1 → win ✓
    # Rock(0) vs Paper(1):    (3+0-1)%3 = 2 → lose ✓
    # Rock(0) vs Rock(0):     (3+0-0)%3 = 0 → draw ✓
    Winner = (3 + player_choice - ai_choice) % 3
    return Winner

def stats(winner, wins, losses, draws, round_num):
    # Update the correct counter based on the round result
    if winner == 0:
        draws += 1   # same choice — draw
    elif winner == 1:
        wins += 1    # player's choice beats computer's choice
    elif winner == 2:
        losses += 1  # computer's choice beats player's choice

    # Calculate win percentage for this point in the game
    percentage_win = (wins / round_num) * 100

    # Print running stats after every round
    print(f"You played {round_num}, won {wins} times, lost {losses} times, and had {draws} draws")

    # Return updated counters so gamePlay() can track them across rounds
    # In Python, integers are passed by value so we must return them to update the originals
    return wins, losses, draws

def gamePlay():
    # Initialize all counters before the game starts
    round_num = 0      # tracks total rounds played
    player_choice = None  # set to None so the while condition works on first check
    wins = 0
    losses = 0
    draws = 0

    # Keep looping until the player quits
    while player_choice != 3:

        # Get a valid choice from the player (0=rock, 1=paper, 2=scissors, 3=quit)
        player_choice = get_user_choice()

        # If player chose quit, exit the loop immediately
        if player_choice == 3:
            break

        # Only increment round number if the player is actually playing
        round_num += 1
        print(f"=== Rock Paper Scissors ===\nRound {round_num}: ")

        # Computer picks randomly from rock(0), paper(1), scissors(2)
        ai_choice = random.choice([0, 1, 2])

        # Determine who won this round
        winner = get_winner(player_choice, ai_choice)

        # Map numbers back to words for display
        choices = ["rock", "paper", "scissors"]
        print(f"You: {choices[player_choice]} | Computer: {choices[ai_choice]}")

        # Print round result
        if winner == 1:
            print("You win!")
        elif winner == 2:
            print("You lose!")
        else:
            print("Draw!")

        # Update stats and capture the returned updated counters
        # We must reassign because integers are passed by value in Python
        wins, losses, draws = stats(winner, wins, losses, draws, round_num)

    # After the loop — print final summary
    if round_num == 0:
        # Player quit without playing a single round
        print("You quit without playing!")
    else:
        # Calculate overall win percentage
        percentage = (wins / round_num) * 100
        print(f"\n=== Final Stats ===")
        print(f"Rounds played: {round_num}")
        print(f"Wins:   {wins} ({percentage:.1f}%)")
        print(f"Losses: {losses}")
        print(f"Draws:  {draws}")

def main():
    # Entry point — just starts the game
    gamePlay()

# Only run main() if this file is run directly, not imported by another file
if __name__ == "__main__":
    main()