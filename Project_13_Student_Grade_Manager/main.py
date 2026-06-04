import statistics as s
import json
class Student:
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
        avg = self.get_average()
        letter_grade = None
        if avg>=90:
            letter_grade = "A"
        elif avg>=80 and avg<90:
            letter_grade = "B"
        elif avg>=70 and avg<80:
            letter_grade = "C"
        elif avg>=60 and avg<70:
            letter_grade = "D"
        elif avg>=50 and avg<60:
            letter_grade = "E"
        else:
            letter_grade = "F"

        return letter_grade
    
    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grades": self.grades

        }

    def __str__(self):
        return f"{self.name} ({self.student_id}): {len(self.grades)} grades"

def save_students(students):
    data = [student.to_dict() for student in students.values()]
    with open("Project_13_Student_Grade_Manager/students.json", "w") as f:
        json.dump(data, f)

def load_student():
    try:
        with open("Project_13_Student_Grade_Manager/students.json", "r") as f:
            data = json.load(f)
        students = {}
        for d in data:
            student = Student(d["name"], d["student_id"], d["grades"])
            students[d["student_id"]] = student
        return students
    except FileNotFoundError:
        return {}

def main():
    students = load_student()
    while True:
        print("Welcome to Student grade Manager!\n")
        try:
            choice = int(input("1. Add Student\n2. Add grade\n3. View Student\n4. View all\n5. Class Average\n6. Quit\n"))
            if choice == 1:
                st_name = input("What is the student Name: ")
                st_id = int(input("Enter the Student ID(Make sure it doesn't exist already): "))
                if st_id in students:
                    print("Sorry this ID already exist")
                else:
                    new_student = Student(st_name, st_id)
                    students[st_id] = new_student
                    print(f"Sucessfully added {st_name} with ID: {st_id}")
                    save_students(students)
                
            elif choice == 2:
                st_id = int(input("Enter the Student ID: "))
                if st_id in students:
                    grade = input("Enter grade")
                    students[st_id].add_grade(grade)
                    print(f"Successfully added {grade}")
                    save_students(students)
                else:
                    print("No student Found")
                
            elif choice == 3:
                st_id = int(input("Enter the Student ID: "))
                if st_id in students:
                    print(students[st_id])
                    print(f"Average of {students[st_id].name} is {students[st_id].get_average()} and the grade is {students[st_id].get_letter_grade()}")
                else:
                    print("Student not Found")
            elif choice == 4:
                if students:
                    for student in students.values():
                        print(f"{student} - {student.get_average()} - {student.get_letter_grade()}")
                else:
                    print("No students yet")
            elif choice == 5:
                if students:
                    total = 0
                    for student in students.values():
                        total += student.get_average()
                    class_av = total/len(students)
                    print(f"Class averager is {class_av:.2f}")
                else:
                    print("No students yet")
            elif choice == 6:
                print("Bye!")
                return False
            else:
                print("Enter a number in th range 1-5")
        except ValueError:
            print("Enter a number")

if __name__ == "__main__":
    main()