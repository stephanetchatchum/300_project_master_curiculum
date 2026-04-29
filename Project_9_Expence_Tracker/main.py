import json
from datetime import datetime, timedelta

EXPENSES_FILE = "expenses.json"
BUDGETS_FILE = "budgets.json"

CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Other"]

def load_data(filepath):
    """Load JSON file, return empty list/dict if not found"""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [] if "expenses" in filepath else {}

def save_data(filepath, data):
    """Save data to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def add_expense(expenses, budgets):
    """Add new expense with validation + budget warning"""
    # Get amount, category, date, description
    # Validate inputs
    # Append to expenses list
    # Check budget warning
    # Save
    pass

def view_all(expenses):
    """Display all expenses formatted"""
    pass

def view_by_category(expenses):
    """Filter expenses by category"""
    pass

def monthly_report(expenses, budgets):
    """Show breakdown for current month"""
    # Filter by current month
    # Calculate totals
    # Calculate per-category breakdown
    # Show budget status if budgets set
    pass

def set_budget(budgets):
    """Set monthly budget per category"""
    pass

def main():
    expenses = load_data(EXPENSES_FILE)
    budgets = load_data(BUDGETS_FILE)
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All")
        print("3. View by Category")
        print("4. Monthly Report")
        print("5. Quit")
        
        try:
            choice = int(input("Choice: "))
            if choice >=1 and choice<=5:
                if choice == 1:
                    add_expense(expenses, budgets)
                elif choice == 2:
                    view_all(expenses)
                elif choice == 3:
                    view_by_category(expenses)
                elif choice == 4:
                    monthly_report(budgets)
                elif choice == 5:
                    print("Goodbye!")
                    break 
            else:
                print("Wrong input. Enter a number between 1 and 5.")
        except ValueError:
            print("Wrong input type! Please enter a number.")

if __name__ == "__main__":
    main()