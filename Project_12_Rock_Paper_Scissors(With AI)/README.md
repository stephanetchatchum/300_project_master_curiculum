# Project 12: Rock Paper Scissors with AI

## 📋 Overview
A command-line implementation of the classic Rock Paper Scissors game where the player competes against the computer. The game uses random selection for the computer's moves and tracks win/loss statistics across multiple rounds.

## 🎮 Features
- **Player vs Computer**: Face off against a randomly choosing AI opponent
- **Input Validation**: Ensures only valid choices (rock, paper, scissors, or quit) are accepted
- **Intelligent Winner Detection**: Uses modular arithmetic for efficient win determination
- **Round Tracking**: Displays results immediately after each round
- **Running Statistics**: Shows wins, losses, draws, and win percentage after each round
- **Final Summary**: Comprehensive statistics displayed when quitting
- **Multiple Rounds**: Play as many rounds as you want in a single session

## 🚀 How to Run
### Prerequisites
- Python 3.x installed on your system

### Steps
1. Open a terminal and navigate to this project folder:
   ```bash
   cd "Project_12_Rock_Paper_Scissors(With AI)"
   ```
2. Run the game with:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu to play

## 📖 How to Play
1. **Start the Game**: The menu displays three choices:
   - `0` for Rock
   - `1` for Paper
   - `2` for Scissors
   - `3` to Quit

2. **Make Your Choice**: Enter the corresponding number when prompted

3. **Computer's Move**: The computer randomly selects rock, paper, or scissors

4. **Determine Winner**:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Same choices result in a Draw

5. **View Round Results**: Immediately see who won and current running statistics

6. **Play Multiple Rounds**: Enter another choice to play again, or enter `3` to quit and see final stats

## 💻 Code Structure
### `main.py`
- **`get_user_choice()`**: Prompts the player and validates input. Returns a number 0–3 or repeats on invalid input.
- **`get_winner(player_choice, ai_choice)`**: Uses modular arithmetic formula `(3 + player - ai) % 3` to determine the outcome:
  - Returns `0` for a draw
  - Returns `1` for a player win
  - Returns `2` for a player loss
- **`stats(winner, wins, losses, draws, round_num)`**: Updates counters and displays running statistics after each round.
- **`gamePlay()`**: Main game loop that orchestrates user input, computer selection, winner determination, and stat tracking.
- **`main()`**: Entry point that calls `gamePlay()`.

## 🎯 Learning Objectives
- Understanding loops and conditional logic
- Input validation and error handling
- Working with random selection
- Using modular arithmetic for game logic
- Tracking game state across multiple rounds
- Formatting output with f-strings
- Function decomposition and parameter passing

## 🔄 Possible Enhancements
- Add difficulty levels (easy computer choices, strategic computer choices)
- Implement best-of-N series (first to X wins)
- Save game history to a file
- Add player statistics persistence across sessions
- Implement a betting/scoring system
- Allow playing against multiple opponents
- Add a leaderboard for high scores
- Create a GUI version with tkinter

## 📝 Example Game Session
```
Choose 0. rock
1. paper
2. scissors
3. quit(enter the number in front): 0
=== Rock Paper Scissors ===
Round 1:
You: rock | Computer: scissors
You win!
You played 1, won 1 times, lost 0 times, and had 0 draws
Choose 0. rock
1. paper
2. scissors
3. quit(enter the number in front): 1
=== Rock Paper Scissors ===
Round 2:
You: paper | Computer: rock
You win!
You played 2, won 2 times, lost 0 times, and had 0 draws
Choose 0. rock
1. paper
2. scissors
3. quit(enter the number in front): 3

=== Final Stats ===
Rounds played: 2
Wins:   2 (100.0%)
Losses: 0
Draws:  0
```

## 📄 License
Educational project for learning Python basics.

## 👨‍💻 Author
Created as part of the 300 Projects Master Curriculum
