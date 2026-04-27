import string  # import string module which contains ready-made character sets like uppercase, lowercase, digits and symbols
import secrets  # import secrets module for cryptographically secure random character selection

# Loop forever until the user chooses to quit
while True:

    # Reset all variables at the start of every loop so each password starts fresh
    char_pool = ""  # will hold all the characters the password can be built from
    count = 0       # tracks how many character types the user included (used for strength)
    password = ""   # will hold the final generated password
    length = 0      # will hold the desired password length

    try:
        # Print the menu title every loop so the user always sees their options
        print("Password Generator")

        # Ask the user to choose an option and convert it to an integer
        choice = int(input("1. Generate password\n2. Quit\n"))

        # ---- GENERATE PASSWORD ----
        if choice == 1:

            # Ask the user how long they want the password to be
            try:
                length = int(input("Enter the desired password length: "))
                if length <= 0:
                    print("Length must be at least 1.")
                    continue
            except ValueError:
                # If they type something that isn't a number, catch it and warn them
                print("Wrong Input. Try again")
                continue

            # Ask about uppercase letters and normalize to lowercase so Yes/YES/yes all work
            upper = input("Should we include uppercase letters? (yes/no): ").lower()
            if upper == "yes":
                # Add all uppercase letters A-Z to the character pool
                char_pool += string.ascii_uppercase
                # Increment the type counter by 1
                count += 1

            # Ask about lowercase letters
            lower = input("Should we include lowercase letters? (yes/no): ").lower()
            if lower == "yes":
                # Add all lowercase letters a-z to the character pool
                char_pool += string.ascii_lowercase
                count += 1

            # Ask about digits
            digits = input("Should we include digits? (yes/no): ").lower()
            if digits == "yes":
                # Add all digits 0-9 to the character pool
                char_pool += string.digits
                count += 1

            # Ask about symbols
            symbols = input("Should we include symbols? (yes/no): ").lower()
            if symbols == "yes":
                # Add all punctuation/symbol characters to the character pool
                char_pool += string.punctuation
                count += 1

            # If the user said no to everything, char_pool is still empty
            # We can't generate a password with no characters so print an error and restart
            if char_pool == "":
                print("Error! Select at least one character type.")
                continue  # jump back to the top of the while loop

            # Let the user know the password is being generated
            print("Generating password...")

            # Loop 'length' times, each time picking one random character from char_pool
            # random.choice() picks a single random item from a sequence
            for i in range(length):
                password += secrets.choice(char_pool)

            # Print the final generated password
            print(f"Generated password: {password}")

            # ---- STRENGTH CALCULATION ----
            print("Determining Password Strength...")

            # Weak: less than 8 characters regardless of character types
            if length < 8:
                state = "WEAK"

            # Strong: 12 or more characters AND at least 3 character types included
            elif length >= 12 and count >= 3:
                state = "STRONG"
            
            # Medium: 8-12 characters AND at least 2 character types included
            elif length >= 8 and count >= 2:
                state = "MEDIUM"

            # Anything that doesn't meet medium or strong requirements defaults to weak
            # e.g. 10 characters but only 1 character type
            else:
                state = "WEAK"

            # Print the strength result
            print(f"Your password is {state}")

            # Ask if the user wants to generate another password
            cont = input("Generate another? (yes/no): ").lower()

            # If they say no, print goodbye and exit the loop
            if cont == "no":
                print("Goodbye!")
                break  # exit the while loop, ending the program
            # If they say yes, the loop naturally continues from the top

        # ---- QUIT ----
        elif choice == 2:
            print("Goodbye!")
            break  # exit the while loop, ending the program

    except ValueError:
        # ValueError is raised when int() receives something that isn't a number e.g. "abc"
        print("Wrong Input. Try again")