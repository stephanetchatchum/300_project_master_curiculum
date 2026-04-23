# Calculator with History

A command-line calculator that supports basic mathematical operations and maintains a history of all calculations. This project demonstrates user input handling, expression evaluation, list management, and error handling in Python.

## Features

- **Basic Calculator** (main.py): Perform mathematical operations with history tracking
- **Enhanced Calculator** (exercise.py): Includes history tracking and undo functionality
- Support for all basic math operations (+, -, *, /, **, %)
- Persistent calculation history during session
- View and undo previous calculations
- Error handling for invalid inputs

## Files

- `main.py` - Basic calculator with history feature
- `exercise.py` - Enhanced calculator with history and undo
- `README.md` - This documentation file

## Requirements

- Python 3.x

## Supported Operations

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` = 8 |
| `-` | Subtraction | `10 - 4` = 6 |
| `*` | Multiplication | `6 * 7` = 42 |
| `/` | Division | `15 / 3` = 5 |
| `**` | Exponentiation | `2 ** 3` = 8 |
| `%` | Modulus | `17 % 5` = 2 |

## How to Run

### Basic Calculator
```bash
python main.py
```

### Enhanced Calculator (with Undo)
```bash
python exercise.py
```

## Commands

- **Enter a math expression**: Type any valid mathematical expression to calculate
- `history` - View all past calculations
- `undo` - Remove the last calculation (exercise.py only)
- `quit` - Exit the calculator

## Usage Examples

### Basic Calculator
```
Enter operation (or 'history'/'quit'): 5 + 3
5 + 3 = 8
Enter operation (or 'history'/'quit'): 10 * 2
10 * 2 = 20
Enter operation (or 'history'/'quit'): history

Calculation History:
1. 5 + 3 = 8
2. 10 * 2 = 20
Enter operation (or 'history'/'quit'): quit
```

### Enhanced Calculator with Undo
```
Enter operation (or 'history'/'undo'/'quit'): 15 + 5
15 + 5 = 20
Enter operation (or 'history'/'undo'/'quit'): 100 / 4
100 / 4 = 25.0
Enter operation (or 'history'/'undo'/'quit'): history

Calculation History:
1. 15 + 5 = 20
2. 100 / 4 = 25.0
Enter operation (or 'history'/'undo'/'quit'): undo
Enter operation (or 'history'/'undo'/'quit'): history

Calculation History:
1. 15 + 5 = 20
```

## Error Handling

The calculator handles various error cases:
- **Invalid syntax**: Displays "Invalid Operation, Try again"
- **Division by zero**: Displays error (handled by Python's eval)
- **Empty input**: Prompts again for valid input
- **Type errors**: Displays "Invalid Input! Try again"

## Learning Objectives

This project demonstrates:
- Mathematical expression evaluation using `eval()`
- List operations (append, enumerate, delete)
- Loop control (`while True` with break)
- Input validation and normalization (`.lower()`)
- Exception handling (`try/except` blocks)
- String formatting with f-strings
- Command-based user interface design

## Technical Details

### History Storage
- Calculations are stored in a Python list
- Each entry stores the expression and result as a formatted string
- History persists during the session (cleared on program exit)

### Expression Evaluation
- Uses Python's built-in `eval()` function
- Supports standard Python math syntax
- Results are formatted to 1 decimal place for non-integers

### Undo Feature (exercise.py)
- Removes the most recent calculation from history
- Uses list slicing `del history[-1]` to remove last element
- Displays "Nothing to undo!" if history is empty

## Security Note

The `eval()` function used in this project can execute arbitrary Python code. In production applications, consider using safer alternatives like the `operator` module or a proper expression parser. This project is intended for educational purposes only.