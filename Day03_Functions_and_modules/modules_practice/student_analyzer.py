"""
a module with all the student analysis functions, functions analyzing 
student data like their names, cgpas, avg cgpa and their reports
"""
if __name__ == "__main__":
    print("student analyzer loaded")

def get_names(students):
    # Function Docstring
    """
    This function takes a list of students and returns a list of their names.
    """
    names=[]
    for student in students:
        names.append(student["name"])
    return names
    
def get_cgpas(students):
    """
    This function takes a list of students and returns a list of their CGPAs.
    """
    cgpas=[]
    for student in students:
        cgpas.append(student["cgpa"])
    return cgpas

def calculate_average_cgpa(students):
    """
    This function takes a list of students and returns the average CGPA.
    """
    average_cgpa =sum(student["cgpa"] for student in students) / len(students)
    return average_cgpa

def get_top_students(students:list)->list: #Type hinting
    """
    This function takes a list of students and returns a list of names of students whose CGPA is above the average CGPA.
    """
    top_students=[]
    average_cgpa=calculate_average_cgpa(students)
    for student in students:
        if student["cgpa"] > average_cgpa:
            top_students.append(student["name"])
    return top_students
def add_student(students):
    """
    This function takes input from the user to add a new student to the list of students.
    """
    name=input("Enter student name: ")
    cgpa=float(input("Enter student CGPA: "))
    students.append({"name":name,"cgpa":cgpa})

def display_students(students):
    """
    This function displays the list of students.
    """
    for student in students:
        print(f"Name: {student['name']}, CGPA: {student['cgpa']}")

def get_passing_students(students):
    """
    This function returns a list of students who have passed (CGPA >= 2.0).
    """
    passing_students=[]
    for student in students:
        if student["cgpa"]>=2.0:
            passing_students.append(student)
    return passing_students

def generate_report(students):
    """
    This function generates a report of the students, including their names, CGPAs, and whether they have passed or failed.
    """
    print("Student Report")
    print("==============")
    for student in students:
        status="Passed" if student["cgpa"]>=2.0 else "Failed"
        print(f"Name: {student['name']}, CGPA: {student['cgpa']}, Status: {status}")