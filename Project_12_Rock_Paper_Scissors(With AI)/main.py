import random


def get_user_choice(): 
    while True:
        try:
            choice = int(input("Choose 0. rock\n1. paper\n2. scissors\n3. quit(enter the number infront): "))
            if choice not in range(4):
                print("Invalid Input. Try again")
            else:
                return choice
        except:
            print("Invalid Input try again")


def get_winner(player_choice, ai_choice):
    Winner = (3+player_choice-ai_choice)%3
    return Winner

def stats(winner, wins, losses, draws, round_num):
    if winner == 0:
        draws += 1
    elif winner == 1:
        wins += 1
    elif winner == 2:
        losses += 1
    percentage_win = (wins/round_num)*100
    print(f"you played {round_num}, won {wins} times, lost {losses} times, and had a draw {draws} times")
    return wins, losses, draws

def gamePlay():
    round_num = 0
    player_choice = None
    wins = 0
    losses = 0
    draws = 0
    while player_choice != 3:
        player_choice = get_user_choice()
        if player_choice == 3:
            break
        round_num += 1
        print(f"=== Rock Paper Scissors ===\nRound {round_num}: ")
        ai_choice = random.choice([0,1,2])
        winner = get_winner(player_choice, ai_choice)
        choices = ["rock", "paper", "scissors"]
        print(f"You: {choices[player_choice]} | Computer: {choices[ai_choice]}")
        if winner == 1:
            print("You win!")
        elif winner == 2:
            print("You lose!")
        else:
            print("Draw!")
        wins, losses, draws = stats(winner, wins, losses, draws, round_num)

    if round_num == 0:
        print("You quit without playing!")
    else:
        percentage = (wins / round_num) * 100
        print(f"\n=== Final Stats ===")
        print(f"Rounds played: {round_num}")
        print(f"Wins:   {wins} ({percentage:.1f}%)")
        print(f"Losses: {losses}")
        print(f"Draws:  {draws}")

def main():
    gamePlay()

if __name__ == "__main__":
    main()