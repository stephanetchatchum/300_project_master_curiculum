import random
import json

# -------------------------
# QUESTION BANK
# -------------------------

questions = [
    # Geography
    {
        "category": "Geography",
        "question": "What is the capital of Rwanda?",
        "options": ["Kigali", "Lagos", "Cairo", "Nairobi"],
        "correct_answer": "A"
    },
    # add at least 9 more questions across Geography, Math, Science
]

# -------------------------
# FUNCTIONS
# -------------------------

def pick_category(questions):
    """Let user pick a category or mixed, return filtered list"""
    pass

def display_question(question_num, total, question):
    """Display a single question with A/B/C/D options"""
    pass

def get_answer():
    """Get and validate user answer (A/B/C/D only), return uppercased answer"""
    pass

def run_quiz(questions):
    """Main quiz loop — shuffle, ask questions, track score"""
    pass

def show_results(score, total):
    """Display final score, percentage and feedback message"""
    pass

# -------------------------
# MAIN
# -------------------------

def main():
    # pick category
    # run quiz
    # show results
    pass

if __name__ == "__main__":
    main()