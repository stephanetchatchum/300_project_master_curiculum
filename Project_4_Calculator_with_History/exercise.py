# Initialize an empty list to store the history of calculations
history = []

# Outer try block to catch any unexpected TypeError from bad input
try:

    # Loop forever until the user explicitly types 'quit'
    while True:

        # Ask the user to enter a math operation, 'history', or 'quit', and normalize to lowercase
        choice = input("Enter operation (or 'history'/'undo'/'quit'): ").lower()

        # If the user types 'quit', exit the loop
        if choice == "quit":
            break

        # If the user types 'history', display all past calculations
        elif choice == "history":

            # Only print history if there is at least one saved calculation
            if history:
                print("\nCalculation History:")

                # Loop through history with a 1-based index and print each entry
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")

            # If the history list is empty, let the user know
            else:
                print("No history yet")
        elif choice == "undo":
            if history:
                del history[-1]
            else:
                print("Nothing to undo!")

        # Otherwise, treat the input as a math expression to evaluate
        else:

            # Inner try block to catch invalid math expressions
            try:

                # Evaluate the math expression entered by the user
                ans = eval(choice)

            # If the expression is not valid Python/math syntax, catch the error
            except SyntaxError:
                print("Invalid Operation, Try again")

                # Skip the rest of the loop and prompt the user again
                continue

            # Print the result of the evaluated expression
            print(f"{choice} = {ans}")

            # Save the expression and its result to the history list
            history.append(f"{choice} = {ans}")

# Catch a TypeError in case eval() receives something it can't handle
except TypeError:
    print("Invalid Input! Try again")