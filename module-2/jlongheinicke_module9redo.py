#Jessica Long-Heinicke Module 12 10.11.24

#Student class definition
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grade_point = 0
        self.credits = 0
        self.gpa = 0

#calculate GPA
    def calculate_gpa(self):
        if self.credits != 0:
            self.gpa = self.grade_point / self.credits
#get GPA
    def get_gpa(self):
        return self.gpa

#prompt user for name
first_name = input("Enter the student's first name: ")
last_name = input("Enter the student's last name: ")

#create student object
student = Student(first_name, last_name)

#convert letter grade to GPA
def lettertogpa(grade):
    grade_map = {
        'A+': 4.0, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.1,
        'F': 0.0
    }
    return grade_map.get(grade.upper(), 'Invalid Grade')

#loop for inputting credits and grades
while True:
    try:
        credits = float(input("Enter credits for the course (0 to end): "))
        if credits == 0:
            break
        grade = input("Enter grade for the course: ")
        student.grade_point += lettertogpa(grade) * credits
        student.credits += credits
    except ValueError:
        print("Invalid Input. Please enter a valid number.")

#Calculate cumulative gpa
student.calculate_gpa()

#display cumulative gpa
print(f"{student.first_name} {student.last_name}'s cumulative GPA: {student.get_gpa():.2f}")