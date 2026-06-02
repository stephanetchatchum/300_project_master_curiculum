import statistics as s
class student:
    def __init__(self, name, student_id, grades=None):
        self.name = name 
        self.student_id = student_id
        self.grades = grades if grades is not None else []

    def add_grade(self,  grade):
        try:
            numeric_grade = float(grade)
            if 0 <= numeric_grade <= 100:
                self.grades.append(numeric_grade)
                return True
            print("❌ Error: Grade must be between 0 and 100.")
            return False
        except ValueError:
            print("❌ Error: Grade must be a valid number.")
            return False

    def get_average(self):
        if not self.grades:
            return 0.0
        return s.mean(self.grades)

    def get_letter_grade(self):
        letter_grade = None
        if self.grades<=50 and self.grades>40:
            letter_grade = "E"
        elif self.grades<=60 and self.grades>50:
            letter_grade = "D"
        elif self.grades<=70 and self.grades>60:
            letter_grade = "C"
        elif self.grades<=80 and self.grades>70:
            letter_grade = "B"
        elif self.grades<=90 and self.grades>80:
            letter_grade = "A"
        else:
            letter_grade = "F"

        return letter_grade
    
    # def to_dict(self):
    #     pass

    def __str__(self):
        return f"{self.name} ({self.student_id}): {len(self.grades)} grades"

def menu():
    print("Welcome to Student grade Manager!\n")
    choice = int(input("1. Add Student\n2. "))
def main():
    student = {}
    while True:
        print("Welcome to Student grade Manager!\n")
        try:
            choice = int(input("1. Add Student\n2. Add grade\n3. View Student\n4. View all\n5. Class Average\n6. Quit\n"))
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                return False
            else:
                print("Enter a number in th range 1-5")
        except TypeError:
            print("Enter a number")


if __name__ == "__main__":
    main()