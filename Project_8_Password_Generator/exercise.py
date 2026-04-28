import string  # import string module which contains ready-made character sets like uppercase, lowercase, digits and symbols
import secrets  # import secrets module for cryptographically secure random character selection

# A list of words to pick from when generating a passphrase
# secrets.choice() will randomly pick from this list
words = ["Fast", "rapid", "quick", "Boring", "dull", "monotonous", "Good", "excellent", "wonderful", "Scared", "afraid", "terrified", "Interesting", "engaging", "intriguing", "Abnegation", "giving", "up", "Aggrandize", "enhance", "Alacrity", "willingness", "Ambiguous", "unclear", "Athleisure", "fashion", "Uncanny", "mysterious", "Vivid", "bright", "Whimsical", "playful", "Yearning", "desire", "Evasive", "candour", "Circumspect", "cautious", "Clandestine", "secret", "Coerce", "force", "Complacency", "self-satisfied", "Confidant", "trusted", "Connive", "plot", "Cumulative", "increasing", "Arrant", "complete", "Artless", "deceit", "Asperity", "harsh", "Belie", "misrepresent", "Eloquent", "fluent", "Benevolent", "kindly", "Candid", "truthful", "Diligent", "careful", "Frugal", "thrifty", "Gregarious", "sociable", "Perfume", "scent", "Permit", "allow", "Prohibit", "refuse", "Reservation", "arrangement", "Intimate", "mutual", "Flinch", "fear", "Gripe", "complain", "Disenfranchise", "deprive", "Zest", "spicy", "Vamoose", "leave", "Cicerone", "guide", "Honcho", "manager", "Amazing", "incredible", "Anger", "enrage", "Reply", "respond", "Query", "interrogate", "Dreadful", "terrible", "Pleasant", "agreeable"]

# Loop forever until the user chooses to quit
while True:

    # Reset all variables at the start of every loop so each run starts fresh
    char_pool = ""  # will hold all characters the password can be built from
    count = 0       # tracks how many character types the user included (used for strength)
    password = ""   # will hold the final generated password
    length = 0      # will hold the desired password length
    word_list = []  # will hold the randomly picked words for passphrase mode

    try:
        # Print the menu title every loop so the user always sees their options
        print("Password Generator")

        # Ask the user to choose an option and convert it to an integer
        choice = int(input("1. Generate password\n2. Generate passphrase\n3. Quit\n"))

        # ---- GENERATE PASSWORD ----
        if choice == 1:

            # Ask the user how long they want the password to be
            try:
                length = int(input("Enter the desired password length: "))

                # Reject zero or negative lengths since they make no sense
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
                # Increment the type counter — used later for strength calculation
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

            print("Generating password...")

            # Loop 'length' times, each time picking one random character from char_pool
            # secrets.choice() is more secure than random.choice() for passwords
            for i in range(length):
                password += secrets.choice(char_pool)

            # Print the final generated password
            print(f"Generated password: {password}")

            # ---- STRENGTH CALCULATION ----
            print("Determining Password Strength...")

            # Calculate a score out of 100 based on length and character variety
            # length * 5 rewards longer passwords e.g. 12 chars = 60 points
            # count * 10 rewards more character types e.g. 3 types = 30 points
            # min(100, ...) caps the score at 100 so it never exceeds 100%
            score = min(100, (length * 5) + (count * 10))

            # Convert score to number of filled blocks out of 10
            # e.g. score 40 → 40 // 10 = 4 filled blocks
            filled = score // 10

            # The remaining blocks are empty — always adds up to 10 total
            empty = 10 - filled

            # Build the visual bar by repeating the block characters
            # e.g. filled=4, empty=6 → "████░░░░░░"
            bar = ("█" * filled) + ("░" * empty)

            # Determine the strength label based on length and character type count
            if length < 8:
                # Weak: less than 8 characters regardless of character types
                state = "WEAK"
            elif length >= 12 and count >= 3:
                # Strong: 12 or more characters AND at least 3 character types
                state = "STRONG"
            elif length >= 8 and count >= 2:
                # Medium: 8-12 characters AND at least 2 character types
                state = "MEDIUM"
            else:
                # Anything else defaults to weak e.g. 10 chars but only 1 type
                state = "WEAK"

            # Print the full strength result with the visual bar, percentage and label
            print(f"Strength: {bar} {score}% ({state})")

            # Ask if the user wants to generate another password
            cont = input("Generate another? (yes/no): ").lower()

            # If they say no, print goodbye and exit the loop
            if cont == "no":
                print("Goodbye!")
                break  # exit the while loop, ending the program
            # If they say yes, the loop naturally continues from the top

        # ---- GENERATE PASSPHRASE ----
        elif choice == 2:

            # Ask how many words they want in the passphrase
            n_word = int(input("How many words do you want (3-5):\n"))

            # Validate that the number is between 3 and 5
            if n_word < 3 or n_word > 5:
                print("Please choose between 3 and 5 words.")
                continue

            # Pick n_word random words from the words list and add each to word_list
            # secrets.choice() picks one random item from the list each time
            for i in range(n_word):
                word_list.append(secrets.choice(words))

            # Join all the picked words together with dashes between them
            # e.g. ["mountain", "river", "sunset"] → "mountain-river-sunset"
            passphrase = "-".join(word_list)

            # Print the generated passphrase
            print(f"Your Passphrase is: {passphrase}")

            # Passphrases are always very strong due to their length and randomness
            print("Strength: ██████████ 100% (VERY STRONG)")

            # Ask if the user wants to generate another
            cont = input("Generate another? (yes/no): ").lower()

            # If they say no, print goodbye and exit the loop
            if cont == "no":
                print("Goodbye!")
                break  # exit the while loop, ending the program
            # If they say yes, the loop naturally continues from the top

        # ---- QUIT ----
        elif choice == 3:
            print("Goodbye!")
            break  # exit the while loop, ending the program

    except ValueError:
        # ValueError is raised when int() receives something that isn't a number e.g. "abc"
        print("Wrong Input. Try again")