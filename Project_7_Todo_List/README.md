# Project 7: Todo List

A command-line task management application that allows you to create, track, and manage your daily tasks. Data is persisted to a JSON file for persistent storage between sessions.

## Features

- **Basic Version (main.py)**: Add, view, mark complete, delete tasks, and view statistics
- **Enhanced Version (exercise.py)**: Includes priority levels, due dates, and overdue task detection
- Persistent storage using JSON file
- Task status tracking (pending/complete)
- Task statistics (total, completed, pending)
- Priority levels (High/Medium/Low) - exercise.py only
- Due date tracking with overdue detection - exercise.py only

## Files

- `main.py` - Basic todo list with 6 menu options
- `exercise.py` - Enhanced todo list with priority and due dates
- `todo_list.json` - Data file for storing tasks (created automatically)
- `README.md` - This documentation file

## Requirements

- Python 3.x

## How to Run

### Basic Version
```bash
python main.py
```

### Enhanced Version (with Priority & Due Dates)
```bash
python exercise.py
```

## Menu Options

### Basic Version (main.py)
1. **Add Task** - Create a new task with title and description
2. **View All** - Display all tasks with their status
3. **Mark Complete** - Mark a task as done
4. **Delete Task** - Remove a task
5. **Stats** - View task statistics (total, completed, pending)
6. **Quit** - Exit the application

### Enhanced Version (exercise.py)
1. **Add Task** - Create task with title, description, priority, and due date
2. **View All** - Display all tasks with status and due dates
3. **Mark Complete** - Mark a task as done
4. **Delete Task** - Remove a task
5. **Stats** - View task statistics including overdue tasks
6. **Quit** - Exit the application

## Usage Example

```
Todo list Menu:
1. Add Task
2. View All
3. Mark Complete
4. Delete Task
5. Stats
6. Quit
1
Enter task title:
Learn Python
Enter task description:
Complete 50 Python projects
Task Added!
```

### Enhanced Version (exercise.py)
```
Enter task title:
Finish Report
Enter task description:
Complete quarterly report
Enter task priority (High/Medium/Low):
High
Enter task due date (YYYY-MM-DD):
2025-04-25
Task Added!
```

## Key Concepts
- **JSON file I/O**: Reading and writing data to persistent storage
- **List manipulation**: Adding, updating, and removing tasks
- **User input handling**: Menu-driven interface with input validation
- **Data persistence**: Tasks saved between program sessions
- **Date handling**: Using datetime for due date comparison (exercise.py)