import random

# Generate a random number between 1 and 100 for the user to guess
number = random.randint(1, 100)

# Initialize guess to None since the user hasn't guessed yet
guess = None

# Track how many guesses the user has made
count = 0

# Keep looping until the user's guess matches the number
while guess != number:

    # Prompt the user for a guess and convert their input to an integer
    guess = int(input("I am thinking of a number from 1-100\nGuess: "))

    # Increment the guess counter by 1 each round
    count += 1

    # Check if the guess is too high
    if guess > number:
        print("Too high! Try again")

    # Check if the guess is too low
    elif guess < number:
        print("Too low! Try again")

# If we've exited the loop, the guess was correct — print the result
print(f"Correct✅ You got it in {count} guesses.")