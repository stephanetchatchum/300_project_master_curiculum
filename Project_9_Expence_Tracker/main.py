import json  # import json module to save and load data from files
from datetime import datetime, timedelta  # import datetime for date handling and timedelta for date calculations

# File paths for storing expenses and budgets persistently
EXPENSES_FILE = "expenses.json"
BUDGETS_FILE = "budgets.json"

# Valid categories for expenses — used for validation throughout the program
CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Other"]

def load_data(filepath):
    """Load JSON file, return empty list/dict if not found"""
    try:
        # Open the file in read mode and convert JSON contents back to Python
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist yet, return empty list for expenses or empty dict for budgets
        return [] if "expenses" in filepath else {}

def save_data(filepath, data):
    """Save data to JSON file"""
    # Open the file in write mode and convert Python data to JSON format
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)  # indent=2 makes the JSON file human-readable

def add_expense(expenses, budgets):
    """Add new expense with validation + budget warning"""

    # Ask for the amount and convert to float, catch non-numeric input
    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return  # exit the function early if amount is invalid
    except ValueError:
        print("Invalid amount. Enter a number.")
        return

    # Ask for category and normalize to lowercase for consistent storage
    category = input("Category:(Food/Transport/Entertainment/Bills/Other)\n").lower()

    # Check if the category is valid by comparing against lowercase version of CATEGORIES
    if category not in [c.lower() for c in CATEGORIES]:
        print(f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
        return

    # Ask for date — if user presses enter, default to today's date
    date = input("date(YYYY-MM-DD or press 'Enter' if today):\n")
    if date == "":
        # strftime formats today's date as a string e.g. "2026-04-28"
        date = datetime.today().strftime("%Y-%m-%d")

    # Ask for a short description of the expense
    description = input("Description: \n")

    # Add the new expense as a dict to the expenses list
    expenses.append(
        {
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        }
    )

    # Save immediately so the expense isn't lost if the program closes
    save_data(EXPENSES_FILE, expenses)

    # Calculate how much has been spent in this category across all expenses
    # sum() adds up amounts where the category matches
    category_total = sum(e["amount"] for e in expenses if e["category"] == category)

    # Check if a budget exists for this category and if it has been exceeded
    if category in budgets:
        if category_total > budgets[category]:
            print(f"⚠️ WARNING: You exceeded your {category} budget!")
            print(f"Spent: {category_total} | Budget: {budgets[category]}")

    print("✓ Expense added!")

def view_all(expenses):
    """Display all expenses formatted"""
    # If there are no expenses yet, let the user know
    if not expenses:
        print("No expenses found")
    else:
        print("\n--- All Expenses ---")
        print("Date       | Category      | Amount | Description")
        print("-" * 60)

        # Loop through every expense with a 1-based index and print each one
        for i, expense in enumerate(expenses, 1):
            print(f"[{expense['date']}] - {expense['category']} - {expense['amount']} - {expense['description']}")

def view_by_category(expenses):
    """Filter and display expenses for a specific category"""

    # Ask which category to filter by and normalize to lowercase
    category = input("Category:(Food/Transport/Entertainment/Bills/Other)\n").lower()

    # Validate the category against the CATEGORIES list
    if category not in [c.lower() for c in CATEGORIES]:
        print(f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
        return

    # Filter expenses to only those matching the chosen category
    # This is a list comprehension — it builds a new list from matching items
    filtered = [e for e in expenses if e['category'] == category]

    # If no expenses match, let the user know
    if not filtered:
        print(f"No expenses found in {category}")
    else:
        # .capitalize() makes the first letter uppercase for display e.g. "food" → "Food"
        print(f"\n--- {category.capitalize()} Expenses ---")
        print("Date       | Amount | Description")
        print("-" * 60)

        # Print each matching expense
        for expense in filtered:
            print(f"[{expense['date']}] - {expense['amount']} - {expense['description']}")

def monthly_report(expenses, budgets):
    """Show breakdown for current month"""

    # Get today's date and extract the current month and year numbers
    now = datetime.today()
    current_month = now.month  # e.g. 4 for April
    current_year = now.year   # e.g. 2026

    # Filter expenses to only those from the current month and year
    # datetime.fromisoformat() converts the stored string "2026-04-28" back to a date object
    # so we can compare .month and .year
    filtered = [e for e in expenses if datetime.fromisoformat(e['date']).month == current_month and datetime.fromisoformat(e['date']).year == current_year]

    # Dict to hold total spending per category e.g. {"food": 15000, "transport": 8000}
    totals = {}

    # Calculate grand total of all expenses this month
    grand_total = sum(e['amount'] for e in filtered)

    # If no expenses found this month, let the user know
    if not filtered:
        print(f"No expenses found on {current_month}")
    else:
        # Group expenses by category and sum up amounts
        for e in filtered:
            cat = e['category']
            if cat not in totals:
                totals[cat] = 0  # initialize the category if first time seeing it
            totals[cat] += e['amount']  # add this expense's amount to the category total

        # Print the breakdown for each category
        for cat, amount in totals.items():
            # Calculate what percentage of total spending this category represents
            percentage = (amount / grand_total) * 100
            print(f"{cat}: {amount} RWF ({percentage:.1f}%)")

            # If a budget is set for this category, show how much is remaining or if exceeded
            if cat in budgets:
                remaining = budgets[cat] - amount
                if remaining < 0:
                    # abs() converts negative number to positive for display
                    print(f"  ⚠️ Over budget by {abs(remaining)} RWF!")
                else:
                    print(f"  ✓ {remaining} RWF remaining")

        # Print the grand total at the bottom of the report
        print(f"\nTotal: {grand_total} RWF")

def set_budget(budgets):
    """Set monthly budget per category"""

    # Show available categories so the user knows what to type
    print(f"Categories: {', '.join(CATEGORIES)}")

    # Ask which category to set a budget for and normalize to lowercase
    cat_chosen = input("Choose your category...").lower()

    # Validate the chosen category
    if cat_chosen not in [c.lower() for c in CATEGORIES]:
        print(f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
        return

    try:
        # Ask for the budget amount and convert to float
        amount = float(input("Enter the Budget Amount: "))
        if amount < 0:
            print("Enter a Positive number...")
            return

        # Store the budget in the budgets dict with the category as the key
        # e.g. budgets["food"] = 20000
        budgets[cat_chosen] = amount

        # Save immediately so the budget persists after the program closes
        save_data(BUDGETS_FILE, budgets)
        print("✓ Budget added!")

    except ValueError:
        print("Invalid amount. Enter a number.")
        return

def main():
    # Load existing expenses and budgets from file when the program starts
    expenses = load_data(EXPENSES_FILE)
    budgets = load_data(BUDGETS_FILE)

    # Loop forever until the user chooses to quit
    while True:
        # Print the menu every loop so the user always sees their options
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All")
        print("3. View by Category")
        print("4. Monthly Report")
        print("5. Set Budget")
        print("6. Quit")

        try:
            # Get the user's choice and convert to integer
            choice = int(input("Choice: "))

            # Check the choice is within valid range
            if choice >= 1 and choice <= 6:
                if choice == 1:
                    add_expense(expenses, budgets)  # pass both lists so function can read and update them
                elif choice == 2:
                    view_all(expenses)
                elif choice == 3:
                    view_by_category(expenses)
                elif choice == 4:
                    monthly_report(expenses, budgets)
                elif choice == 5:
                    set_budget(budgets)  # pass budgets dict so function can update it
                elif choice == 6:
                    print("Goodbye!")
                    break  # exit the while loop, ending the program
            else:
                print("Wrong input. Enter a number between 1 and 6.")

        except ValueError:
            # ValueError is raised when int() receives something that isn't a number
            print("Wrong input type! Please enter a number.")

# Only run main() if this file is being run directly, not imported by another file
if __name__ == "__main__":
    main()