import random

# Ask the user to enter the number they want the computer to guess
number = int(input("Enter the number you want me to guess: (1-100)"))

# Set the initial upper bound of the search range
high = 100

# Set the initial lower bound of the search range
low = 1

# Track how many guesses the computer has made
count = 0

# Initialize guess to None since the computer hasn't guessed yet
guess = None

# Keep looping until the computer's guess matches the number
while number != guess:

    # Use binary search: guess the midpoint of the current range
    guess = (low + high) // 2

    # Increment the guess counter by 1 each round
    count += 1

    # If the guess is correct, print the result and exit the loop
    if guess == number:
        print(f"Found it! It is {guess}, and I got it after {count} guesses")
        break

    # If the guess is too high, move the upper bound down
    elif guess > number:
        high = guess - 1

    # If the guess is too low, move the lower bound up
    elif guess < number:
        low = guess + 1