# Project 11: Hangman Game

## 📋 Overview
A command-line Hangman game written in Python. The player tries to guess a hidden word one letter at a time before running out of attempts. A simple ASCII hangman figure updates with each incorrect guess.

## 🎮 Features
- Randomly selects a word from a built-in list
- Displays the puzzle with blanks and correctly guessed letters
- Tracks letters already guessed
- Validates user input to accept only single alphabet characters
- Shows a visual hangman drawing that updates on wrong guesses
- Ends the game when the word is guessed or the maximum wrong guesses is reached

## 🚀 How to Run
### Prerequisites
- Python 3.x installed on your system

### Steps
1. Open a terminal and navigate to this project folder:
   ```bash
   cd "Project_11_Hangman_Game"
   ```
2. Run the game with:
   ```bash
   python main.py
   ```
3. Follow the on-screen prompts to guess letters until you win or lose.

## 📖 How to Play
1. The game chooses a secret word from the internal list.
2. A blank word display appears, using `_` for letters you have not guessed yet.
3. Enter a single letter as your guess when prompted.
4. If the guess is correct, the letter fills in all matching positions.
5. If the guess is wrong, the hangman figure advances one stage.
6. You have up to 6 incorrect guesses before the game ends.

## 💻 Code Structure
### `main.py`
- `get_random_word(word_list)`: Selects a random word for the game.
- `draw_hangman(wrong_guesses)`: Prints the ASCII hangman figure based on mistakes.
- `display_state(word, guessed_letters, wrong_guesses)`: Shows the current word progress, guessed letters, and remaining attempts.
- `get_guess(guessed_letters)`: Reads and validates a single letter guess from the player.
- `is_word_complete(word, guessed_letters)`: Checks whether the full word has been guessed.
- `play_game()`: Runs the game loop and tracks wrong guesses.
- `main()`: Entry point executed when the script runs.

## 🎯 Learning Objectives
- Practice reading and validating user input
- Work with loops, conditionals, and sets
- Use random selection in Python
- Build a simple text-based game loop
- Display game state and progress to the player

## 🔄 Possible Enhancements
- Add difficulty levels with longer or shorter words
- Allow the player to choose a category of words
- Keep score across multiple rounds
- Save high scores or game history to a file
- Add a replay prompt after each game
- Support full-word guesses in addition to single-letter guesses

## 📄 License
Educational project for learning Python basics.
