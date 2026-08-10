"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 04 - Exception Handling
Practice File

Author: Fajar Naeem Rana
===============================================
"""

# Safe Division
# ========================
print("Enter two numbers to divide")
try:
    number1=float(input("First number: "))
    number2=float(input("second number: "))
    print(f"Result: {number1/number2}")

except ZeroDivisionError:
    print("Division by zero")

except ValueError:
    print("Invalid input")

else:
    print("Numbers divided withour error")

finally:
    print("Division operation completed")

# Safe File Handling
# ==============================
try:
    with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\students.txt", "r") as file:
        student_data=file.read()

except FileNotFoundError as fileError:
    print("Something went wrong: ", fileError)

else:
    print(student_data)

# Student CGPA Validator- Raising your own exceptions
# =================================
try:
    cgpa=float(input("enter your gpa: "))
    if cgpa < 0:
         raise ValueError("CGPA cannot be negative")
    elif cgpa > 4:
        raise ValueError("CGPA can be from 0-4")
    else:
        print(f"Your cgpa is {cgpa}")

except ValueError as error:
    print("Error found: ", error)

finally:
    print("CGPA Validation Completed")