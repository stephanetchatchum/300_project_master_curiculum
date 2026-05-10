# Import the random module to shuffle questions into random order
import random
# Import the json module for potential JSON file handling (not currently used)
import json

# -------------------------
# QUESTION BANK
# -------------------------

# Define a list of question dictionaries containing all quiz questions organized by category
questions = [
    # --- Geography Category ---
    # Dictionary containing a geography question with multiple choice options
    {
        # Specify the category as "Geography"
        "category": "Geography",
        # The actual question text to display to the user
        "question": "What is the capital of Rwanda?",
        # A list of four possible answer options labeled A, B, C, D
        "options": ["Nairobi", "Kigali", "Lagos", "Cairo"],
        # Store the correct answer as letter B (index 1 = Kigali)
        "correct_answer": "B"
    },
    # Another geography question about African geography
    {
        "category": "Geography",
        "question": "Which is the longest river in Africa?",
        "options": ["Congo", "Niger", "Nile", "Zambezi"],
        # Correct answer is C (index 2 = Nile)
        "correct_answer": "C"
    },
    # Geography question about African population
    {
        "category": "Geography",
        "question": "Which country has the largest population in Africa?",
        "options": ["Ethiopia", "DRC", "South Africa", "Nigeria"],
        # Correct answer is D (index 3 = Nigeria)
        "correct_answer": "D"
    },
    # Geography question about Asian capitals
    {
        "category": "Geography",
        "question": "What is the capital of Japan?",
        "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
        # Correct answer is C (index 2 = Tokyo)
        "correct_answer": "C"
    },
    # Geography question about world oceans
    {
        "category": "Geography",
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        # Correct answer is D (index 3 = Pacific)
        "correct_answer": "D"
    },

    # --- Math Category ---
    # Math question about basic multiplication
    {
        "category": "Math",
        "question": "What is 7 x 8?",
        "options": ["54", "56", "64", "49"],
        # Correct answer is B (index 1 = 56)
        "correct_answer": "B"
    },
    # Math question about square roots
    {
        "category": "Math",
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "14"],
        # Correct answer is C (index 2 = 12)
        "correct_answer": "C"
    },
    # Math question about percentages
    {
        "category": "Math",
        "question": "What is 15% of 200?",
        "options": ["25", "30", "35", "40"],
        # Correct answer is B (index 1 = 30)
        "correct_answer": "B"
    },
    # Math question about exponents
    {
        "category": "Math",
        "question": "What is 2 to the power of 10?",
        "options": ["512", "1024", "2048", "256"],
        # Correct answer is B (index 1 = 1024)
        "correct_answer": "B"
    },
    # Math question about geometry
    {
        "category": "Math",
        "question": "How many degrees are in a triangle?",
        "options": ["90", "180", "270", "360"],
        # Correct answer is B (index 1 = 180)
        "correct_answer": "B"
    },

    # --- Science Category ---
    # Science question about chemistry
    {
        "category": "Science",
        "question": "What is the chemical symbol for water?",
        "options": ["CO2", "O2", "H2O", "NaCl"],
        # Correct answer is C (index 2 = H2O)
        "correct_answer": "C"
    },
    # Science question about astronomy
    {
        "category": "Science",
        "question": "How many planets are in our solar system?",
        "options": ["7", "8", "9", "10"],
        # Correct answer is B (index 1 = 8)
        "correct_answer": "B"
    },
    # Science question about biology and photosynthesis
    {
        "category": "Science",
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        # Correct answer is C (index 2 = Carbon Dioxide)
        "correct_answer": "C"
    },
    # Science question about physics
    {
        "category": "Science",
        "question": "What is the speed of light (approximately)?",
        "options": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "100,000 km/s"],
        # Correct answer is A (index 0 = 300,000 km/s)
        "correct_answer": "A"
    },
    # Science question about cell biology
    {
        "category": "Science",
        "question": "What is the powerhouse of the cell?",
        "options": ["Nucleus", "Ribosome", "Mitochondria", "Chloroplast"],
        # Correct answer is C (index 2 = Mitochondria)
        "correct_answer": "C"
    },
]

# -------------------------
# FUNCTIONS
# -------------------------

# Define function to let user select which category of questions to answer
def pick_category(questions):
    # Function docstring explaining what this function does
    """Let user pick a category or mixed, return filtered list"""
    # Begin a try block to handle potential errors when converting user input
    try:
        # Ask user to pick a category and convert their numeric input to an integer
        category = int(input("Pick a category?\n1. Geography\n2. Math\n3. Science\n4. All"))
        # If user chose 1, filter questions to only include Geography category
        if category == 1:
            # Create a new list containing only questions where category equals "Geography"
            filtered = [q for q in questions if q['category'] == "Geography"]
        # Else if user chose 2, filter questions to only include Math category
        elif category == 2:
            # Create a new list containing only questions where category equals "Math"
            filtered = [q for q in questions if q['category'] == "Math"]
        # Else if user chose 3, filter questions to only include Science category
        elif category == 3:
            # Create a new list containing only questions where category equals "Science"
            filtered = [q for q in questions if q['category'] == "Science"]
        # Else if user chose 4, include all questions
        elif category == 4:
            # Create a list containing all the original questions
            filtered = [q for q in questions]
        # If the user chose a number that wasn't 1-4, display an error message
        else:
            # Print a message telling user their choice was invalid and all questions will be used
            print("Invalid choice, defaulting to All")
            # Set filtered list to all questions since choice was invalid
            filtered = questions

        # Return the filtered list of questions to the caller
        return filtered
    # Catch the error if user entered something that can't be converted to an integer
    except ValueError:
        # Print an error message indicating the input was invalid
        print("Invalid Input.")

# Define function to display a single quiz question with its answer options
def display_question(question_num, total, question):
    # Function docstring explaining what this function does
    """Display a single question with A/B/C/D options"""
    # Print the question number, total number of questions, and the question text
    print(f"Question {question_num}/{total}: {question['question']}")
    # Loop through each option in the question's options list with its index
    for i, option in enumerate(question['options']):
        # Print each option formatted as A, B, C, or D followed by the option text
        # chr(65+i) converts numbers 0,1,2,3 to letters A,B,C,D
        print(f" {chr(65+i)}. {option}")

# Define function to get and validate the user's answer
def get_answer():
    # Function docstring explaining what this function does
    """Get and validate user answer (A/B/C/D only), return uppercased answer"""
    # Start an infinite loop that continues until a valid answer is provided
    while True:
        # Ask user to enter their answer (A, B, C, or D) and convert it to uppercase
        ans = input("Answer(A,B,C,D): ").upper()
        # Check if the user's answer is one of the valid options
        if ans in ["A", "B", "C", "D"]:
            # If valid, return the answer to the caller
            return ans
        # If the answer was not valid, display an error message
        print("Invalid! Enter A, B, C or D.")
        

# Define the main function that runs the quiz
def run_quiz(questions):
    # Function docstring explaining what this function does
    """Main quiz loop — shuffle, ask questions, track score"""
    # Check if the questions list is empty
    if not questions:
        # If there are no questions, print a message and return early
        print("No questions")
        return
    # Shuffle the questions list in-place to randomize the order questions appear
    random.shuffle(questions)
    # Initialize a score counter variable to track correct answers
    score = 0
    # Loop through each question in the shuffled list with its position number
    for i, question in enumerate(questions, 1):
        # Call display_question to show the current question to the user
        display_question(i, len(questions), question)
        # Call get_answer to prompt the user for their answer
        ans = get_answer()
        # Check if the user's answer matches the correct answer for this question
        if ans == question['correct_answer']:
            # Increment the score by 1 if the answer was correct
            score += 1
            # Print a message congratulating the user for correct answer
            print("Correct")
        # If the user's answer does not match the correct answer
        else:
            # Print the correct answer so the user can learn
            print(f"Wrong the answer was: {question['correct_answer']}")

    # Return both the final score and total number of questions as a tuple
    return score, len(questions)

# Define function to display the final quiz results
def show_results(score, total):
    # Function docstring explaining what this function does
    """Display final score, percentage and feedback message"""
    # Print a header for the results section
    print("=== Final Score ===")
    # Print the score and calculate the percentage of correct answers
    # (score/total)*100 calculates percentage, :.1f formats it to 1 decimal place
    print(f"You got {score} out of {total} ({(score/total)*100:.1f}%)")
    # Print an encouraging message to the user
    print("Great job!")

# -------------------------
# MAIN
# -------------------------

# Define the main entry point function
def main():
    # Call pick_category to let user choose a category and store the filtered questions
    q = pick_category(questions)
    # Call run_quiz to run the quiz with the selected questions and store score/total
    s, t = run_quiz(q)
    # Call show_results to display the final quiz results
    show_results(s, t)

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # If running directly, call the main function to start the quiz
    main()