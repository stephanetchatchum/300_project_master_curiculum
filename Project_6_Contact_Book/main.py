import json
def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_contact():
    with open("contacts.json","w") as f:
        json.dump(Contact, f)

Contact = load_contacts()

print("Contact Book Menu:")
while True:
    try:
        choice = int(input("1. Add Contact\n2. View all\n3. Search\n4. Delete\n5. Update\n6. Quit"))
        if choice<=6 and choice>=1:
            if choice ==1:
                Name = input("Enter contact name:\n")
                number = input("Enter contact number\n")
                email = input("Enter contact Email")
                Contact[Name] = {"number": number, "email": email}
                save_contact()
                print("Contact Added!")
            elif choice == 2:
                print(Contact)
            elif choice == 3:
                search_name = input("Enter contact name you are looking for:\n")
                print(Contact[search_name])
            elif choice == 4:
                del_name = input("Enter contact name you want to delete:\n")
                del Contact[del_name]
            elif choice == 5:
                pass
            elif choice == 6:
                break
        else:
            print("Wrong Input, Enter a number in the range (1-6)")
    except TypeError:
        print("Wrong Input Type!")

