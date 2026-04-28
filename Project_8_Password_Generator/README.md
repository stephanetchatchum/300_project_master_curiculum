# Project 8: Password Generator

## Overview
This project is a secure and interactive Password Generator and Passphrase Generator written in Python. It allows users to generate strong, random passwords or memorable passphrases, with customizable options for character types and length. The generator uses the `secrets` module for cryptographically secure randomization.

## Features
- **Password Generation:**
	- Choose password length
	- Include/exclude uppercase, lowercase, digits, and symbols
	- Password strength assessment (Weak, Medium, Strong)
	- Visual strength bar (in `exercise.py`)
- **Passphrase Generation:**
	- Choose 3-5 random words for a strong, memorable passphrase (in `exercise.py`)
- **User-Friendly Menu:**
	- Simple text-based interface
	- Input validation and error handling
	- Option to generate multiple passwords/passphrases in one session

## Files
- `main.py`: Basic password generator with strength assessment.
- `exercise.py`: Extended version with both password and passphrase generation, visual strength bar, and a larger word list.

## How to Run
1. Open a terminal and navigate to the `Project_8_Password_Generator` directory.
2. Run either script:
	 - For the basic password generator:
		 ```bash
		 python main.py
		 ```
	 - For the extended version (recommended):
		 ```bash
		 python exercise.py
		 ```

## Usage
1. Choose an option from the menu:
	 - Generate password
	 - (In `exercise.py`) Generate passphrase
	 - Quit
2. For passwords, select which character types to include and specify the length.
3. For passphrases, choose the number of words (3-5).
4. View the generated password or passphrase and its strength.
5. Optionally, generate another or quit.

## Example
```
Password Generator
1. Generate password
2. Generate passphrase
3. Quit
Enter the desired password length: 12
Should we include uppercase letters? (yes/no): yes
Should we include lowercase letters? (yes/no): yes
Should we include digits? (yes/no): yes
Should we include symbols? (yes/no): no
Generated password: G7kqL2vBzQwT
Strength: █████████░ 90% (STRONG)
```

## Requirements
- Python 3.x (no external libraries required)

## Notes
- The `secrets` module is used for secure randomization.
- Passphrases are always rated as VERY STRONG due to their length and randomness.
- Input validation ensures only valid options are accepted.

## License
This project is for educational purposes.
