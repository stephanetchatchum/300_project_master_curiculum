# Student Grade Manager

A command-line application for managing student records and tracking their grades efficiently.

## Overview

The Student Grade Manager allows educators to:
- Create and manage student records with unique IDs
- Add grades to students (0-100 scale)
- Calculate individual student averages and letter grades
- View all students and their performance
- Calculate class-wide average performance
- Persist data to a JSON file for future sessions

## Features

- **Add Students**: Create new student records with name and unique ID
- **Add Grades**: Add grades (0-100) to existing students with validation
- **View Individual Student**: Display student information, average, and letter grade
- **View All Students**: List all students with their averages and letter grades at a glance
- **Class Average**: Calculate the overall class average across all students
- **Data Persistence**: Automatically save and load student data from `students.json`

## Letter Grade Scale

- **A**: 90-100
- **B**: 80-89
- **C**: 70-79
- **D**: 60-69
- **E**: 50-59
- **F**: Below 50

## Requirements

- Python 3.x
- No external dependencies required

## Usage

Run the application:

```bash
python main.py
```

### Menu Options

1. **Add Student** - Create a new student record
2. **Add Grade** - Add a grade to an existing student
3. **View Student** - Display a specific student's information and performance
4. **View All** - Display all students with their averages and grades
5. **Class Average** - Calculate the average grade for the entire class
6. **Quit** - Exit the application

## Data Storage

Student data is stored in `students.json` with the following structure:

```json
[
  {
    "name": "John Doe",
    "student_id": 101,
    "grades": [85, 90, 88]
  }
]
```

## Learning Objectives

This project teaches:
- Object-Oriented Programming (OOP) with classes
- File I/O and JSON data manipulation
- Data validation and error handling
- Statistical calculations (mean/average)
- Conditional logic and grading logic
