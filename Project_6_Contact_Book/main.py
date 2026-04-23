import json  # import json module to save and load contacts from a file

# -------------------------
# LOAD & SAVE FUNCTIONS
# -------------------------

def load_contacts():
    # Try to open the contacts file and read it
    try:
        # Open contacts.json in read mode
        with open("contacts.json", "r") as f:
            return json.load(f)  # convert the JSON file contents back into a Python dict and return it
    except FileNotFoundError:
        return {}  # if the file doesn't exist yet, return an empty dict to start fresh

def save_contacts():
    # Open contacts.json in write mode (creates the file if it doesn't exist)
    with open("contacts.json", "w") as f:
        json.dump(Contact, f)  # convert the Contact dict into JSON format and write it to the file

# -------------------------
# LOAD CONTACTS AT START
# -------------------------

# Call load_contacts() once at the start so we don't lose data from previous sessions
Contact = load_contacts()

# Print the menu title when the program starts
print("Contact Book Menu:")

# -------------------------
# MAIN LOOP
# -------------------------

# Loop forever until the user chooses to quit
while True:
    try:
        # Show the menu options and get the user's choice, converting it to an integer
        choice = int(input("\n1. Add Contact\n2. View All\n3. Search\n4. Delete\n5. Update\n6. Quit\n"))

        # Check that the choice is within the valid range
        if choice >= 1 and choice <= 6:

            # ---- ADD CONTACT ----
            if choice == 1:
                # Ask the user for the new contact's details
                Name = input("Enter contact name:\n")
                number = input("Enter contact number:\n")
                email = input("Enter contact email:\n")

                # Store the contact as a dict so we can update individual fields later
                # e.g. Contact["John"] = {"number": "123", "email": "john@mail.com"}
                Contact[Name] = {"number": number, "email": email}

                # Save immediately so the new contact isn't lost if the program closes
                save_contacts()
                print("Contact Added!")

            # ---- VIEW ALL CONTACTS ----
            elif choice == 2:
                # Check if there are any contacts to display
                if len(Contact) == 0:
                    print("No contacts yet.")
                else:
                    print("\n--- All Contacts ---")
                    # Loop through every contact in the dict
                    # .items() gives us each (name, details) pair
                    for name, details in Contact.items():
                        # Print each contact's name, number and email in a readable format
                        print(f"Name: {name} | Number: {details['number']} | Email: {details['email']}")

            # ---- SEARCH CONTACT ----
            elif choice == 3:
                # Ask which contact the user is looking for
                search_name = input("Enter contact name you are looking for:\n")
                try:
                    # Try to look up the contact by name in the dict
                    details = Contact[search_name]
                    # If found, print their details
                    print(f"Name: {search_name} | Number: {details['number']} | Email: {details['email']}")
                except KeyError:
                    # KeyError means the name wasn't found in the dict
                    print(f"Contact '{search_name}' not found.")

            # ---- DELETE CONTACT ----
            elif choice == 4:
                # Ask which contact the user wants to delete
                del_name = input("Enter contact name you want to delete:\n")
                try:
                    # Try to delete the contact from the dict
                    del Contact[del_name]
                    # Save immediately so the deletion is reflected in the file
                    save_contacts()
                    print(f"Contact '{del_name}' deleted.")
                except KeyError:
                    # KeyError means the name wasn't found so nothing was deleted
                    print(f"Contact '{del_name}' not found.")

            # ---- UPDATE CONTACT ----
            elif choice == 5:
                # Ask which contact the user wants to update
                update_name = input("Enter the name of the contact you want to update:\n")
                try:
                    # Try to find the contact first — if it doesn't exist, KeyError is raised
                    details = Contact[update_name]

                    # Ask which field the user wants to change
                    field = input("What do you want to update? (number/email):\n").lower()

                    # If they want to update the number
                    if field == "number":
                        new_value = input("Enter new number:\n")
                        # Update just the number field, leaving email untouched
                        Contact[update_name]["number"] = new_value
                        # Save immediately so the update is reflected in the file
                        save_contacts()
                        print("Number updated!")

                    # If they want to update the email
                    elif field == "email":
                        new_value = input("Enter new email:\n")
                        # Update just the email field, leaving number untouched
                        Contact[update_name]["email"] = new_value
                        # Save immediately so the update is reflected in the file
                        save_contacts()
                        print("Email updated!")

                    # If they typed something other than 'number' or 'email'
                    else:
                        print("Invalid field. Choose 'number' or 'email'.")

                except KeyError:
                    # KeyError means the contact name wasn't found in the dict
                    print(f"Contact '{update_name}' not found.")

            # ---- QUIT ----
            elif choice == 6:
                print("Goodbye!")
                break  # exit the while loop, ending the program

        # If the number is outside 1-6, tell the user
        else:
            print("Wrong input. Enter a number between 1 and 6.")

    except ValueError:
        # ValueError is raised when int() receives something that isn't a number e.g. "abc"
        print("Wrong input type! Please enter a number.")