import random
import json

# -------------------------
# QUESTION BANK
# -------------------------

questions = [
    # --- Geography ---
    {
        "category": "Geography",
        "question": "What is the capital of Rwanda?",
        "options": ["Nairobi", "Kigali", "Lagos", "Cairo"],
        "correct_answer": "B"
    },
    {
        "category": "Geography",
        "question": "Which is the longest river in Africa?",
        "options": ["Congo", "Niger", "Nile", "Zambezi"],
        "correct_answer": "C"
    },
    {
        "category": "Geography",
        "question": "Which country has the largest population in Africa?",
        "options": ["Ethiopia", "DRC", "South Africa", "Nigeria"],
        "correct_answer": "D"
    },
    {
        "category": "Geography",
        "question": "What is the capital of Japan?",
        "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
        "correct_answer": "C"
    },
    {
        "category": "Geography",
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "correct_answer": "D"
    },

    # --- Math ---
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

    # --- Science ---
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
    try:
        category = int(input("Pick a category?\n1. Geography\n2. Math\n3. Science\n4. All"))
        if category == 1:
            filtered = [q for q in questions if q['category'] == "Geography"]
        elif category == 2:
            filtered = [q for q in questions if q['category'] == "Math"]
        elif category == 3:
            filtered = [q for q in questions if q['category'] == "Science"]
        elif category == 4:
            filtered = [q for q in questions]
        else:
            print("Invalid choice, defaulting to All")
            filtered = questions

        return filtered
    except ValueError:
        print("Invalid Input.")

def display_question(question_num, total, question):
    """Display a single question with A/B/C/D options"""
    print(f"Question {question_num}/{total}: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f" {chr(65+i)}. {option}")

def get_answer():
    """Get and validate user answer (A/B/C/D only), return uppercased answer"""
    while True:
        ans = input("Answer(A,B,C,D): ").upper()
        if ans in ["A", "B", "C", "D"]:
            return ans
        print("Invalid! Enter A, B, C or D.")
        

def run_quiz(questions):
    """Main quiz loop — shuffle, ask questions, track score"""
    if not questions:
        print("No questions")
        return
    random.shuffle(questions)
    score = 0
    for i, question in enumerate(questions, 1):
        display_question(i, len(questions), question)
        ans = get_answer()
        if ans == question['correct_answer']:
            score += 1
            print("Correct")
        else:
            print(f"Wrong the answer was: {question['correct_answer']}")

    return score, len(questions)

def show_results(score, total):
    """Display final score, percentage and feedback message"""
    print("=== Final Score ===")
    print(f"You got {score} out of {total} ({(score/total)*100:.1f}%)")
    print("Great job!")

# -------------------------
# MAIN
# -------------------------

def main():
    # pick category
    q = pick_category(questions)
    # run quiz
    s, t = run_quiz(q)
    # show results
    show_results(s, t)

if __name__ == "__main__":
    main()