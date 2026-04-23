# Project 6: Contact Book

A command-line contact management application that allows you to store, search, update, and delete contacts. Data is persisted to a JSON file for persistent storage between sessions.

## Features

- **Basic Version (main.py)**: Add, view, search, update, and delete contacts
- **Enhanced Version (exercise.py)**: Includes vCard export, contact groups, and favorites
- Persistent storage using JSON file
- Contact details: name, phone number, email
- Search contacts by name
- Update existing contact information

## Files

- `main.py` - Basic contact book with 6 menu options
- `exercise.py` - Enhanced contact book with 7 menu options (includes vCard export)
- `contacts.json` - Data file for storing contacts (created automatically)
- `README.md` - This documentation file

## Requirements

- Python 3.x

## How to Run

### Basic Version
```bash
python main.py
```

### Enhanced Version (with vCard & Groups)
```bash
python exercise.py
```

## Menu Options

### Main Version (main.py)
1. **Add Contact** - Create a new contact with name, phone, and email
2. **View All** - Display all saved contacts
3. **Search** - Find a contact by name
4. **Delete** - Remove a contact
5. **Update** - Edit existing contact information
6. **Quit** - Exit the application

### Enhanced Version (exercise.py)
1. **Add Contact** - Create new contact with name, phone, email, group, and favorite status
2. **View All** - Display all saved contacts
3. **Search** - Find a contact by name
4. **Delete** - Remove a contact
5. **Update** - Edit existing contact information
6. **vCard** - Export contacts as vCard format (.vcf file)
7. **Quit** - Exit the application

## Usage Example

```
Contact Book Menu:

1. Add Contact
2. View All
3. Search
4. Delete
5. Update
6. Quit
1
Enter contact name:
John
Enter contact number:
555-1234
Enter contact email:
john@email.com
Contact Added!
```

## Key Concepts
- **JSON file I/O**: Reading and writing data to persistent storage
- **Dictionary manipulation**: Storing and accessing contact data
- **User input handling**: Menu-driven interface with input validation
- **Data persistence**: Contacts saved between program sessions