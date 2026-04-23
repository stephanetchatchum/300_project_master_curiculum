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
        choice = int(input("\n1. Add Contact\n2. View All\n3. Search\n4. Delete\n5. Update\n6. vCard\n7. Quit\n"))

        # Check that the choice is within the valid range 1-7
        if choice >= 1 and choice <= 7:

            # ---- ADD CONTACT ----
            if choice == 1:
                # Ask the user for the new contact's details
                Name = input("Enter contact name:\n")
                number = input("Enter contact number:\n")
                email = input("Enter contact email:\n")
                group = input("Enter contact group(Family, Friend, Work):\n")

                # Ask if this contact should be marked as a favorite and normalize to lowercase
                favorite = input("Put this in Favorite(yes/no):\n").lower()

                # Convert the yes/no answer into a True/False boolean
                if favorite == "yes":
                    fav = True
                elif favorite == "no":
                    fav = False
                else:
                    # If the user types anything other than yes/no, default to not a favorite
                    print("Invalid Input! Automatically set to no")
                    fav = False

                # Store the contact as a dict with all 4 fields
                # e.g. Contact["John"] = {"number": "123", "email": "john@mail.com", "group": "Family", "favorite": False}
                Contact[Name] = {"number": number, "email": email, "group": group, "favorite": fav}

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

                        # details.get('favorite') safely reads the favorite field
                        # if the field doesn't exist it returns False instead of crashing
                        # the ★/☆ icon is chosen based on whether favorite is True or False
                        print(f"Name: {name} | Number: {details['number']} | Email: {details['email']} | Group: {details['group']} | {'★' if details.get('favorite') == True else '☆'}")

            # ---- SEARCH CONTACT ----
            elif choice == 3:
                # Ask which contact the user is looking for
                search_name = input("Enter contact name you are looking for:\n")
                try:
                    # Try to look up the contact by name in the dict
                    details = Contact[search_name]

                    # If found, print their details with the correct star icon
                    print(f"Name: {search_name} | Number: {details['number']} | Email: {details['email']} | Group: {details['group']} | {'★' if details.get('favorite') == True else '☆'}")
                except KeyError:
                    # KeyError means the name wasn't found in the dict
                    print(f"Contact '{search_name}' not found.")

            # ---- DELETE CONTACT ----
            elif choice == 4:
                # Ask which contact the user wants to delete
                del_name = input("Enter contact name you want to delete:\n")
                try:
                    # Try to delete the contact from the dict using the del keyword
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

                    # Ask which specific field the user wants to change
                    field = input("What do you want to update? (number/email/group/favorite):\n").lower()

                    # If they want to update the number
                    if field == "number":
                        new_value = input("Enter new number:\n")
                        # Update just the number field, leaving all other fields untouched
                        Contact[update_name]["number"] = new_value
                        save_contacts()  # save immediately so the change is not lost
                        print("Number updated!")

                    # If they want to update the email
                    elif field == "email":
                        new_value = input("Enter new email:\n")
                        # Update just the email field, leaving all other fields untouched
                        Contact[update_name]["email"] = new_value
                        save_contacts()  # save immediately so the change is not lost
                        print("Email updated!")

                    # If they want to update the group
                    elif field == "group":
                        new_value = input("Enter new group(Family, Friend, Work):\n")
                        # Update just the group field, leaving all other fields untouched
                        Contact[update_name]["group"] = new_value
                        save_contacts()  # save immediately so the change is not lost
                        print("Group updated!")

                    # If they want to update the favorite status
                    elif field == "favorite":
                        new_value = input("Is it a Favorite?(yes/no):\n")

                        # Convert yes/no answer into True/False boolean
                        if new_value == "yes":
                            fav = True
                        elif new_value == "no":
                            fav = False
                        else:
                            # If the user types anything other than yes/no, default to False
                            print("Invalid Input! Automatically set to no")
                            fav = False

                        # Update just the favorite field, leaving all other fields untouched
                        Contact[update_name]["favorite"] = fav
                        save_contacts()  # save immediately so the change is not lost
                        print("Favorite Status updated!")

                    # If they typed something other than the 4 valid field names
                    else:
                        print("Invalid field. Choose 'number', 'email', 'group' or 'favorite'.")

                except KeyError:
                    # KeyError means the contact name wasn't found in the dict
                    print(f"Contact '{update_name}' not found.")

            # ---- EXPORT vCARD ----
            elif choice == 6:
                # Ask which contact the user wants to export
                contact_name = input("Enter the name of the contact you want to export:\n")
                try:
                    # Try to find the contact — KeyError if not found
                    details = Contact[contact_name]

                    # Open a new .vcf file named after the contact (creates it if it doesn't exist)
                    with open(f"{contact_name}.vcf", 'w') as f:
                        f.write("BEGIN:VCARD\n")           # marks the start of the vCard
                        f.write("VERSION:3.0\n")           # specifies the vCard format version
                        f.write(f"FN:{contact_name}\n")    # FN = Full Name, uses the contact's name variable
                        f.write(f"TEL:{details['number']}\n")  # TEL = telephone number from the contact's dict
                        f.write(f"EMAIL:{details['email']}\n") # EMAIL from the contact's dict
                        f.write("END:VCARD\n")             # marks the end of the vCard

                    # Let the user know the file was created successfully
                    print(f"Contact exported to {contact_name}.vcf")

                except KeyError:
                    # KeyError means the contact name wasn't found in the dict
                    print(f"Contact '{contact_name}' not found.")

            # ---- QUIT ----
            elif choice == 7:
                print("Goodbye!")
                break  # exit the while loop, ending the program

        # If the number typed is outside the range 1-7, let the user know
        else:
            print("Wrong input. Enter a number between 1 and 7.")

    except ValueError:
        # ValueError is raised when int() receives something that isn't a number e.g. "abc"
        print("Wrong input type! Please enter a number.")