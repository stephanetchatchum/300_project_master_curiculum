import random
import json

# -------------------------
# QUESTION BANK
# -------------------------

# Questions stored as dictionaries for easy extensibility - each question can have
# additional metadata like difficulty level or explanations in the future.
# This structure makes it simple to add new questions or modify existing ones.
questions = [
    # --- Geography Category ---
    # Each question is a dictionary with category, question text, multiple choice options, and correct answer
    {
        "category": "Geography",
        "question": "What is the capital of Rwanda?",
        "options": ["Nairobi", "Kigali", "Lagos", "Cairo"],
        "correct_answer": "B"  # B corresponds to index 1 (Kigali)
    },
    {
        "category": "Geography",
        "question": "Which is the longest river in Africa?",
        "options": ["Congo", "Niger", "Nile", "Zambezi"],
        "correct_answer": "C"  # C corresponds to index 2 (Nile)
    },
    {
        "category": "Geography",
        "question": "Which country has the largest population in Africa?",
        "options": ["Ethiopia", "DRC", "South Africa", "Nigeria"],
        "correct_answer": "D"  # D corresponds to index 3 (Nigeria)
    },
    {
        "category": "Geography",
        "question": "What is the capital of Japan?",
        "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
        "correct_answer": "C"  # C corresponds to index 2 (Tokyo)
    },
    {
        "category": "Geography",
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "correct_answer": "D"  # D corresponds to index 3 (Pacific)
    },

    # --- Math Category ---
    {
        "category": "Math",
        "question": "What is 7 x 8?",
        "options": ["54", "56", "64", "49"],
        "correct_answer": "B"
    },
    {
        "category": "Math",
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "14"],
        "correct_answer": "C"
    },
    {
        "category": "Math",
        "question": "What is 15% of 200?",
        "options": ["25", "30", "35", "40"],
        "correct_answer": "B"
    },
    {
        "category": "Math",
        "question": "What is 2 to the power of 10?",
        "options": ["512", "1024", "2048", "256"],
        "correct_answer": "B"
    },
    {
        "category": "Math",
        "question": "How many degrees are in a triangle?",
        "options": ["90", "180", "270", "360"],
        "correct_answer": "B"
    },

    # --- Science Category ---
    {
        "category": "Science",
        "question": "What is the chemical symbol for water?",
        "options": ["CO2", "O2", "H2O", "NaCl"],
        "correct_answer": "C"
    },
    {
        "category": "Science",
        "question": "How many planets are in our solar system?",
        "options": ["7", "8", "9", "10"],
        "correct_answer": "B"
    },
    {
        "category": "Science",
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "correct_answer": "C"
    },
    {
        "category": "Science",
        "question": "What is the speed of light (approximately)?",
        "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "100,000 km/s"],
        "correct_answer": "A"
    },
    {
        "category": "Science",
        "question": "What is the powerhouse of the cell?",
        "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"],
        "correct_answer": "C"
    },
]

# -------------------------
# FUNCTIONS
# -------------------------

def pick_category(questions):
    """Let user pick a category or mixed, return filtered list"""
    # Use try/except to handle cases where user enters non-numeric input
    # This prevents the program from crashing if someone types letters instead of numbers
    try:
        category = int(input("Pick a category?\n1. Geography\n2. Math\n3. Science\n4. All"))
        # Filter questions based on user's choice using list comprehension
        # This creates a new list containing only questions that match the selected category
        if category == 1:
            filtered = [q for q in questions if q['category'] == "Geography"]
        elif category == 2:
            filtered = [q for q in questions if q['category'] == "Math"]
        elif category == 3:
            filtered = [q for q in questions if q['category'] == "Science"]
        elif category == 4:
            filtered = [q for q in questions]  # Return all questions
        else:
            # Handle invalid numbers by defaulting to all questions
            print("Invalid choice, defaulting to All")
            filtered = questions

        return filtered
    except ValueError:
        # This catches errors when int() conversion fails (e.g., user types "abc")
        print("Invalid Input.")

def display_question(question_num, total, question):
    """Display a single question with A/B/C/D options"""
    # Show progress by displaying current question number out of total
    print(f"Question {question_num}/{total}: {question['question']}")
    # Loop through options and display them as A, B, C, D
    for i, option in enumerate(question['options']):
        # chr(65+i) converts index 0,1,2,3 to ASCII letters A,B,C,D
        print(f" {chr(65+i)}. {option}")

def get_answer():
    """Get and validate user answer (A/B/C/D only), return uppercased answer"""
    # Keep asking until we get a valid answer - this ensures data integrity
    while True:
        ans = input("Answer(A,B,C,D): ").upper()
        if ans in ["A", "B", "C", "D"]:
            return ans
        # Show error message and loop again for invalid input
        print("Invalid! Enter A, B, C or D.")
        

def run_quiz(questions):
    """Main quiz loop — shuffle, ask questions, track score"""
    # Early return if no questions available (defensive programming)
    if not questions:
        print("No questions")
        return
    # Shuffle questions to provide variety and prevent memorization patterns
    random.shuffle(questions)
    score = 0
    # Use enumerate to get both index (i) and question for numbering
    for i, question in enumerate(questions, 1):
        display_question(i, len(questions), question)
        ans = get_answer()
        if ans == question['correct_answer']:
            score += 1
            print("✓ Correct!")
        else:
            # Show correct answer so user can learn from mistakes
            print(f"Wrong! Correct answer: {question['correct_answer']}")

    # Return score and total as tuple - allows calling function to access both values
    return score, len(questions)

def show_results(score, total):
    """Display final score, percentage and feedback message"""
    print("=== Final Score ===")
    # Calculate and display percentage with one decimal place formatting
    print(f"You got {score} out of {total} ({(score/total)*100:.1f}%)")
    print("Great job!")

# -------------------------
# MAIN
# -------------------------

def main():
    while True:
        try:
            p = int(input("Welcome to the Quiz game\npress 1 to play, 2 to quit: "))
            if p == 1:
                # Get user's category choice and filter questions accordingly
                q = pick_category(questions)
                # Run the quiz and get back score and total questions
                s, t = run_quiz(q)
                # Display final results
                show_results(s, t)
            elif p == 2:
                break
            else:
                print("Invalid Input, please try again and enter  either 1 or 2")
        except ValueError:
            print("Invalid Input, please try again and enter either 1 or 2")


# Standard Python pattern to ensure this file can be imported or run directly
if __name__ == "__main__":
    main()