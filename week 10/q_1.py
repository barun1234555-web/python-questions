class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90: return "A+"
        elif self.marks >= 75: return "A"
        elif self.marks >= 50: return "B"
        else: return "F"

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}, Grade: {self.calculate_grade()}")

s1 = Student("Alice", 101, 85)
s1.display()