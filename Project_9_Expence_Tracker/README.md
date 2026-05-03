# Expense Tracker

A command-line expense tracking application that helps you monitor and manage your spending with budget alerts and monthly reports.

## Features

- **Add Expenses** - Record new expenses with amount, category, date, and description
- **View All Expenses** - Display all recorded expenses in a formatted table
- **Filter by Category** - View expenses for a specific category with totals
- **Last 7 Days** - Quick view of recent expenses from the past week
- **Monthly Report** - Comprehensive breakdown of current month spending:
  - Total spending and daily average
  - Highest expense recorded
  - Category breakdown with percentages
  - Budget status and progress bars
- **Set Monthly Budgets** - Define spending limits per category with warnings
- **Budget Alerts** - Automatic warnings at 80% of budget and alerts when exceeded

## Categories

The following expense categories are available:
- Food
- Transport
- Entertainment
- Bills
- Other

## Installation

1. Ensure you have Python 3.6+ installed
2. Clone or download this project
3. Navigate to the project directory

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

1. **Add Expense** - Create a new expense entry
   - Enter amount (must be positive)
   - Select category
   - Enter date (YYYY-MM-DD format, or press Enter for today)
   - Add a description

2. **View All** - See all expenses in a table format

3. **View by Category** - Filter and sum expenses by category

4. **View Last 7 Days** - Quick review of recent spending

5. **Monthly Report** - Detailed analysis of current month with:
   - Total and daily average spending
   - Highest single expense
   - Category breakdown with progress bars
   - Budget usage per category

6. **Set Budget** - Define a monthly spending limit for any category

7. **Quit** - Exit the application

## Data Storage

The application automatically saves data to JSON files:
- `expenses.json` - All recorded expenses
- `budgets.json` - Monthly budget limits per category

Data persists between sessions.

## Example Workflow

1. Start the app and set budgets for each category
2. Add expenses as you spend money
3. Check "View Last 7 Days" for recent activity
4. Review "Monthly Report" to see spending patterns and budget status
5. Receive automatic alerts if you approach or exceed budget limits

## Tips

- Budget warnings appear at 80% of your limit
- Dates are stored in YYYY-MM-DD format (e.g., 2026-04-28)
- Monthly budgets reset each month
- All amounts are shown in RWF (Rwandan Francs)
