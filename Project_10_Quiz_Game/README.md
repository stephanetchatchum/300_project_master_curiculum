# Project 10: Quiz Game

## 📋 Overview
A command-line quiz game that tests your knowledge across multiple categories: Geography, Math, and Science. Users can select a specific category or tackle a mixed set of questions. The game tracks scores and displays performance statistics at the end.

## 🎮 Features
- **Category Selection**: Choose to be quizzed on Geography, Math, Science, or a mix of all three
- **Randomized Questions**: Questions are shuffled each game for variety
- **Instant Feedback**: Get immediate feedback on whether answers are correct
- **Score Tracking**: Final score displayed with percentage calculation
- **Multiple Question Types**: 15 diverse questions across three categories
  - 5 Geography questions about capitals, rivers, oceans, and continents
  - 5 Math questions covering arithmetic, percentages, powers, and geometry
  - 5 Science questions about chemistry, physics, biology, and astronomy
- **User Input Validation**: Ensures answers are valid (A, B, C, or D only)

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system

### Steps
1. Navigate to the project directory:
   ```
   cd Project_10_Quiz_Game
   ```

2. Run the quiz game:
   ```
   python main.py
   ```

3. Follow the on-screen prompts to select a category and answer questions

## 📖 How to Play

1. **Select a Category**: When the game starts, you'll see the category menu:
   - Enter `1` for Geography questions only
   - Enter `2` for Math questions only
   - Enter `3` for Science questions only
   - Enter `4` for a mix of all categories

2. **Answer Questions**: For each question:
   - Read the question and four options (A, B, C, D)
   - Enter your answer (A, B, C, or D)
   - You'll get instant feedback on whether you're correct

3. **View Results**: After completing all questions, you'll see:
   - Your final score (e.g., 8 out of 15)
   - Your percentage score
   - An encouraging message

## 📚 Question Bank

### Geography (5 Questions)
- Capital of Rwanda
- Longest river in Africa
- Most populous country in Africa
- Capital of Japan
- Largest ocean on Earth

### Math (5 Questions)
- Basic multiplication (7 × 8)
- Square roots (√144)
- Percentage calculations (15% of 200)
- Exponents (2¹⁰)
- Geometry (degrees in a triangle)

### Science (5 Questions)
- Chemical symbols (water/H₂O)
- Solar system (number of planets)
- Plant biology (photosynthesis)
- Physics (speed of light)
- Cell biology (mitochondria)

## 💻 Code Structure

### Functions
- **`pick_category(questions)`**: Prompts user to select a quiz category and returns filtered questions
- **`display_question(question_num, total, question)`**: Displays a question with its four answer options
- **`get_answer()`**: Gets and validates user input (ensures A/B/C/D format)
- **`run_quiz(questions)`**: Main quiz loop that shuffles questions, asks them, tracks score
- **`show_results(score, total)`**: Displays final score with percentage and feedback
- **`main()`**: Entry point that orchestrates the game flow

### Data Structure
Questions are stored as dictionaries with:
- `category`: The subject area (Geography, Math, or Science)
- `question`: The question text
- `options`: List of four answer choices
- `correct_answer`: The correct answer (A, B, C, or D)

## 🎯 Learning Objectives
This project demonstrates:
- User input validation and error handling (try/except)
- List comprehension for filtering data
- Working with lists of dictionaries
- Random shuffling for variety
- String formatting with f-strings
- Function decomposition and modularity
- Game loop implementation

## 🔄 Possible Enhancements
- Add difficulty levels (Easy, Medium, Hard)
- Implement a scoring system with leaderboard
- Add a timer for each question
- Add more questions and categories
- Save quiz results to a JSON file
- Add a review section to show missed questions
- Create a database for questions instead of hardcoded list
- Add explanations for correct answers

## 📝 Example Game Session
```
Pick a category?
1. Geography
2. Math
3. Science
4. All
4
Question 1/15: What is the capital of Rwanda?
 A. Nairobi
 B. Kigali
 C. Lagos
 D. Cairo
Answer(A,B,C,D): B
Correct
Question 2/15: What is 7 x 8?
 A. 54
 B. 56
 C. 64
 D. 49
Answer(A,B,C,D): B
Correct

[... more questions ...]

=== Final Score ===
You got 12 out of 15 (80.0%)
Great job!
```

## 📄 License
Educational project for learning Python basics.

## 👨‍💻 Author
Created as part of the 300 Projects Master Curriculum