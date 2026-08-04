class LibraryItem:
    def __init__(self, title, author, item_id):
        self.is_available = True
        self.item_id = item_id
        self.title = title
        self.author = author

    def checkout(self):
        self.is_available = False
        return f"{self.title} is unavailable"

    def return_item(self):
        self.is_available = True

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\n Available: {"Yes" if self.is_available == True else "No"}"

class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages, genre):
        super().__init__(title, author, item_id)
        self.pages = pages
        self.genre = genre

    def display_info(self):
        info = super().display_info()
        new_info = info + f"Number of Pages: {self.pages}\nGenre: {self.genre}\n"

        return new_info

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number

    def display_info(self):
        info = super().display_info()
        new_info = info + f"Issue Number: {self.issue_number}\n"
        return new_info

def menu():
    """Main Menu"""
    print("\n=== Library System ===")
    print("1. Add book\n2. Add magazine\n3. Checkout\n4. Return\n5. View all\n6. Search\n7. Quit\n")
    choice = int(input("Enter your choice(1 - 7): "))
    return choice

def main():
    """Main File"""
    while True:
        try:
            choice = menu()
            if choice == 1:
                """Code"""
            elif choice == 2:
                """Code"""
            elif choice == 3:
                """Code"""
            elif choice == 4:
                """Code"""
            elif choice == 5:
                """Code"""  
            elif choice == 6:
                """Code""" 
            elif choice == 7:
                print("Enjoy your day")
                return False 
            else:
                print("Enter a Number in the range(1 - 7)")
        except ValueError:
            print("Enter a valid number")
            
if __name__ == "__main__":
    main()