class student:
    def __init__(self, name, student_id, grades=None):
        self.name = name 
        self.student_id = student_id
        self.grades = grades if grades is not None else []

    def add_grade(self,  grade):
        pass

    def get_average(self):
        pass

    def get_letter_grade(self):
        pass
    
    def to_dict(self):
        pass

    def __str__(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()