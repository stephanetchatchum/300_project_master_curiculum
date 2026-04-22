# Number Guessing Game

An interactive number guessing game with two different approaches: human guessing and computer guessing using binary search. This project demonstrates random number generation, user input handling, loops, and algorithmic thinking.

## Features

- **Human Guessing Mode** (main.py): User tries to guess a randomly generated number
- **Computer Guessing Mode** (exercise.py): Computer uses binary search to efficiently guess a number
- Guess counting and performance tracking
- Helpful feedback ("too high" or "too low")
- Simple command-line interface

## Files

- `main.py` - Human guessing game where player tries to guess computer's number
- `exercise.py` - Computer guessing game using binary search algorithm
- `README.md` - This documentation file

## Requirements

- Python 3.x

## How to Run

### Human Guessing Game
```bash
python main.py
```

### Computer Guessing Game
```bash
python exercise.py
```

## Gameplay

### Human Guessing Mode (main.py)
The computer randomly selects a number between 1 and 100. You try to guess it by entering numbers. The computer provides feedback:

- "Too high! Try again" - Your guess is higher than the target number
- "Too low! Try again" - Your guess is lower than the target number
- "Correct✅ You got it in X guesses." - You guessed correctly!

### Computer Guessing Mode (exercise.py)
You think of a number between 1 and 100, and the computer uses binary search to guess it efficiently. The computer:

1. Starts with a range of 1-100
2. Guesses the midpoint each time
3. Narrows the search range based on whether the guess is too high or too low
4. Continues until it finds the correct number

## Usage Examples

### Human Guessing Game
```
I am thinking of a number from 1-100
Guess: 50
Too high! Try again
Guess: 25
Too low! Try again
Guess: 37
Too high! Try again
Guess: 31
Correct✅ You got it in 4 guesses.
```

### Computer Guessing Game
```
Enter the number you want me to guess: (1-100) 73
Found it! It is 73, and I got it after 7 guesses
```

## Algorithms Used

### Random Guessing (Human Mode)
- Uses `random.randint(1, 100)` to generate a random target number
- Simple trial-and-error approach
- Average guesses needed: ~50 (worst case: 100)

### Binary Search (Computer Mode)
- Efficient search algorithm with O(log n) complexity
- Maximum guesses needed: 7 (for range 1-100)
- Always finds the number in minimal attempts

## Learning Objectives

This project demonstrates:
- Random number generation with `random` module
- Input validation and type conversion (`int()`)
- Loop control structures (`while` loops)
- Conditional statements (`if/elif/else`)
- Binary search algorithm implementation
- Algorithm efficiency comparison
- User interaction and feedback systems

## Game Statistics

### Human Guessing Mode
- **Range**: 1-100 (100 possible numbers)
- **Worst case**: 100 guesses (if guessing sequentially)
- **Average case**: ~7 guesses (using optimal strategy)
- **Best case**: 1 guess

### Computer Guessing Mode
- **Range**: 1-100 (100 possible numbers)
- **Worst case**: 7 guesses (binary search guarantee)
- **Average case**: ~7 guesses
- **Best case**: 1 guess (if number is 50)

## Extensions Ideas

- Add difficulty levels (different ranges)
- Track high scores/best games
- Add time limits
- Implement multiple rounds
- Add hints or clues
- Create a graphical version