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
    print("1. ")
def main():
    student = {}
    


if __name__ == "__main__":
    main()