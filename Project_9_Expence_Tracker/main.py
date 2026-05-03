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
    date = input("Date (YYYY-MM-DD or press Enter for today):\n")
    if date == "":
        # strftime formats today's date as a string e.g. "2026-04-28"
        date = datetime.today().strftime("%Y-%m-%d")

    # Ask for a short description of the expense
    description = input("Description:\n")

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

    # Get current month and year for monthly budget check
    now = datetime.today()

    # Calculate how much has been spent in this category THIS MONTH ONLY
    # This fixes the all-time bug — budget warnings now reflect monthly spending
    category_total = sum(
        e["amount"] for e in expenses
        if e["category"] == category
        and datetime.fromisoformat(e["date"]).month == now.month
        and datetime.fromisoformat(e["date"]).year == now.year
    )

    # Check if a budget exists for this category and if it has been exceeded
    if category in budgets:
        budget_limit = budgets[category]
        # Warn at 80% of budget
        if category_total >= budget_limit * 0.8 and category_total < budget_limit:
            print(f"⚠️ WARNING: You've used {(category_total/budget_limit)*100:.0f}% of your {category} budget!")
        # Warn when fully exceeded
        elif category_total >= budget_limit:
            print(f"🚨 ALERT: You exceeded your {category} budget!")
            print(f"Spent: {category_total:,.0f} RWF | Budget: {budget_limit:,.0f} RWF")

    print("✓ Expense added!")

def view_all(expenses):
    """Display all expenses formatted"""
    # If there are no expenses yet, let the user know
    if not expenses:
        print("No expenses yet.")
    else:
        print("\n--- All Expenses ---")
        print(f"{'#':<4} {'Date':<12} {'Category':<15} {'Amount':>10} Description")
        print("-" * 60)

        # Loop through every expense with a 1-based index and print each one
        # :,.0f formats numbers with commas e.g. 15000 → 15,000
        for i, e in enumerate(expenses, 1):
            print(f"{i:<4} [{e['date']}] {e['category']:<15} {e['amount']:>8,.0f} RWF  {e['description']}")

def view_by_category(expenses):
    """Filter and display expenses for a specific category"""

    # Ask which category to filter by and normalize to lowercase
    category = input("Category:(Food/Transport/Entertainment/Bills/Other)\n").lower()

    # Validate the category against the CATEGORIES list
    if category not in [c.lower() for c in CATEGORIES]:
        print(f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
        return

    # Filter expenses to only those matching the chosen category
    filtered = [e for e in expenses if e['category'] == category]

    # If no expenses match, let the user know
    if not filtered:
        print(f"No expenses found in {category.capitalize()}")
    else:
        # .capitalize() makes first letter uppercase for display
        print(f"\n--- {category.capitalize()} Expenses ---")
        print(f"{'Date':<12} {'Amount':>10} Description")
        print("-" * 50)

        # Print each matching expense
        for e in filtered:
            print(f"[{e['date']}] {e['amount']:>8,.0f} RWF  {e['description']}")

        # Show total for this category
        total = sum(e['amount'] for e in filtered)
        print(f"\nTotal: {total:,.0f} RWF")

def view_last_7_days(expenses):
    """Filter and display expenses from the last 7 days"""

    # Calculate the cutoff date — 7 days ago from today
    # timedelta(days=7) subtracts 7 days from today's date
    seven_days_ago = datetime.today() - timedelta(days=7)

    # Filter expenses where the date is on or after 7 days ago
    filtered = [
        e for e in expenses
        if datetime.fromisoformat(e['date']) >= seven_days_ago
    ]

    # If no expenses in the last 7 days, let the user know
    if not filtered:
        print("No expenses in the last 7 days.")
    else:
        print("\n--- Last 7 Days ---")
        print(f"{'Date':<12} {'Category':<15} {'Amount':>10} Description")
        print("-" * 60)

        # Print each matching expense
        for e in filtered:
            print(f"[{e['date']}] {e['category']:<15} {e['amount']:>8,.0f} RWF  {e['description']}")

        # Show total for the last 7 days
        total = sum(e['amount'] for e in filtered)
        print(f"\nTotal (last 7 days): {total:,.0f} RWF")

def monthly_report(expenses, budgets):
    """Show full breakdown for current month"""

    # Get today's date and extract month and year
    now = datetime.today()
    current_month = now.month  # e.g. 4 for April
    current_year = now.year    # e.g. 2026

    # Filter expenses to only those from the current month and year
    # Parse date once per expense to avoid calling fromisoformat() twice
    filtered = []
    for e in expenses:
        expense_date = datetime.fromisoformat(e['date'])  # parse once
        if expense_date.month == current_month and expense_date.year == current_year:
            filtered.append(e)

    # If no expenses found this month, let the user know and stop
    if not filtered:
        print(f"No expenses found in {now.strftime('%B %Y')}")
        return

    # Calculate grand total of all expenses this month
    grand_total = sum(e['amount'] for e in filtered)

    # Calculate daily average — how many days have elapsed so far this month
    # datetime.today().day gives the current day number e.g. 28 for April 28th
    days_elapsed = datetime.today().day
    daily_avg = grand_total / days_elapsed  # total divided by days elapsed

    # Find the single highest expense using max() with a key function
    # lambda e: e['amount'] means "compare expenses by their amount field"
    highest = max(filtered, key=lambda e: e['amount'])

    # Print the report header
    print(f"\n=== {now.strftime('%B %Y')} Report ===")
    print(f"Total:         {grand_total:>10,.0f} RWF")
    print(f"Daily average: {daily_avg:>10,.0f} RWF")
    print(f"Highest:       {highest['amount']:>10,.0f} RWF ({highest['category'].capitalize()} - {highest['description']})")

    # Build totals dict — group expenses by category and sum amounts
    totals = {}
    for e in filtered:
        cat = e['category']
        if cat not in totals:
            totals[cat] = 0  # initialize category if first time seeing it
        totals[cat] += e['amount']

    # Print the category breakdown
    print("\nBreakdown:")
    for cat, amount in totals.items():
        # Calculate percentage of total spending this category represents
        percentage = (amount / grand_total) * 100

        # Print category line with right-aligned amounts and percentage
        print(f"  {cat.capitalize():<16} {amount:>8,.0f} RWF ({percentage:>3.0f}%)")

        # If a budget is set for this category, show remaining or overspend
        if cat in budgets:
            budget_limit = budgets[cat]
            remaining = budget_limit - amount
            used_pct = (amount / budget_limit) * 100

            # Build a simple text progress bar — 10 blocks total
            filled = int(used_pct / 10)
            bar = "█" * filled + "░" * (10 - filled)

            if remaining < 0:
                # abs() converts negative to positive for display
                print(f"  Budget:  [{bar}] {used_pct:.0f}% — ⚠️ Over by {abs(remaining):,.0f} RWF")
            else:
                print(f"  Budget:  [{bar}] {used_pct:.0f}% — {remaining:,.0f} RWF remaining")

    # Print grand total at the bottom
    print(f"\n{'Total':<16} {grand_total:>10,.0f} RWF")

def set_budget(budgets):
    """Set monthly budget per category"""

    # Show available categories so the user knows what to type
    print(f"Categories: {', '.join(CATEGORIES)}")

    # Ask which category to set a budget for and normalize to lowercase
    cat_chosen = input("Choose your category: ").lower()

    # Validate the chosen category
    if cat_chosen not in [c.lower() for c in CATEGORIES]:
        print(f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
        return

    try:
        # Ask for the budget amount and convert to float
        amount = float(input("Enter the budget amount (RWF): "))
        if amount <= 0:
            print("Budget must be positive.")
            return

        # Store the budget in the budgets dict with the category as the key
        budgets[cat_chosen] = amount

        # Save immediately so the budget persists after the program closes
        save_data(BUDGETS_FILE, budgets)
        print(f"✓ Budget set: {cat_chosen.capitalize()} → {amount:,.0f} RWF/month")

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
        print("4. View Last 7 Days")
        print("5. Monthly Report")
        print("6. Set Budget")
        print("7. Quit")

        try:
            # Get the user's choice and convert to integer
            choice = int(input("Choice: "))

            # Check the choice is within the valid range
            if choice >= 1 and choice <= 7:
                if choice == 1:
                    add_expense(expenses, budgets)
                elif choice == 2:
                    view_all(expenses)
                elif choice == 3:
                    view_by_category(expenses)
                elif choice == 4:
                    view_last_7_days(expenses)  # new function
                elif choice == 5:
                    monthly_report(expenses, budgets)
                elif choice == 6:
                    set_budget(budgets)
                elif choice == 7:
                    print("Goodbye!")
                    break  # exit the while loop, ending the program
            else:
                print("Wrong input. Enter a number between 1 and 7.")

        except ValueError:
            # ValueError is raised when int() receives something that isn't a number
            print("Wrong input type! Please enter a number.")

# Only run main() if this file is being run directly, not imported by another file
if __name__ == "__main__":
    main()