"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 03 - Functions and Modules
Practice File

Author: Fajar Naeem Rana
===============================================
"""
# ================================
# Functions Practice
# ================================
# Defining functions to perform various operations on the list of students
# ========================================================================
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

students=[
    {"name":"Alice","cgpa":3.5},
    {"name":"Bob","cgpa":2.8},
    {"name":"Charlie","cgpa":3.9},
    {"name":"David","cgpa":2.5},
    {"name":"Eve","cgpa":3.2}
    ]
# Student Analytics Engine
print("===============================")
print("   Student Analytics Engine")
print("===============================")
print("1. Display Students")
print("2. Add Student")
print("3. Get Names of Students")
print("4. Get CGPAs of Students")
print("5. Calculate Average CGPA")
print("6. Get Top Students")
print("7. Get Passing Students")
print("8. Generate Report")

operation=int(input("Select an operation (1-8): "))
if operation==1:
    display_students(students)
elif operation==2:
    add_student(students)
elif operation==3:
    names=get_names(students)
    print(names)
elif operation==4:
    cgpas= get_cgpas(students)
    print(cgpas)
elif operation==5:
    average_cgpa= calculate_average_cgpa(students)
    print(average_cgpa)
elif operation==6:
    top_students= get_top_students(students)
    print(top_students)
elif operation==7:
    passing_students=get_passing_students(students)
    print(passing_students)
elif operation==8:
    generate_report(students)
else:
    print("Invalid option!")