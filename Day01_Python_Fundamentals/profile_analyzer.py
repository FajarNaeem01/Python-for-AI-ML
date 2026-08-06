"""
===============================================
Day 01 - Python Fundamentals
Mini Project: Profile Analyzer
Description: This program analyzes a user's profile information and provides insights based on the data provided.
Author: Fajar Naeem Rana
===============================================
"""
# ===========================================
# Taking user input for profile information
# ===========================================
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
birth_date = input("Enter your birth date (DD-MMS): ")
university_name = input("Enter your university name: ")
department_name = input("Enter your department name: ")
email_address = input("Enter your email address: ")
programming_languages = input("Enter your favorite programming languages (comma-separated): ").split(',')
cgpa = float(input("Enter your CGPA: "))

# ===========================================
# Formatted output of the user's profile information
# ===========================================
print("\nProfile Information:")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print("Birth month:", birth_date.split('-')[1])
print(f"University: {university_name}")
print(f"Department: {department_name}")
print(f"Email: {email_address}")
print(f"Programming Languages: {', '.join(programming_languages)}")
print(f"CGPA: {cgpa}")

# ===========================================
# Analyzing the user's profile information  
# ===========================================
print("\nProfile Analysis:")
print("Name Length:", len(student_name))
print("Name in Uppercase:", student_name.upper())
print("Title Case Name:", student_name.title())
print("Email Domain:", email_address.split('@')[-1])
print("First character of Name:", student_name[0])
print("Last character of Name:", student_name[-1])
print("Initials:", ''.join([name[0].upper() for name in student_name.split()]))
print("Reversed Name:", student_name[::-1])

# ===========================================
# Age and CGPA Analysis
# ===========================================
if student_age < 18:
    print("You are a minor.")
elif 18 <= student_age < 25:
    print("You are a young adult.")
else:
    print("You are an adult.")
if student_age <= 30:
    print("How many years until you turn 30:", 30 - student_age)
# ===========================================
print("Current CGPA out of 4:", cgpa)
print("CGPA Percentage:", (cgpa / 4) * 100, "%")
print("How's your CGPA?")
if cgpa >= 3.5:
    print("Excellent! You have a high CGPA.")
elif cgpa >= 3.0:
    print("Good! You have a decent CGPA.")
else:
    print("You need to work harder to improve your CGPA.")

# ===========================================
# Bonus: Greeting based on the time of day and calculating the users birth year based on their age
# ===========================================
from datetime import datetime

current_time = datetime.now().hour
if 5 <= current_time < 12:
    print("Good morning, {}!".format(student_name))
elif 12 <= current_time < 18:
    print("Good afternoon, {}!".format(student_name))
else:
    print("Good evening, {}!".format(student_name))

# checking if the birthday has passed this year or not and then calculating the birth year based on the age
birth_month = int(birth_date.split('-')[1])
birth_date = int(birth_date.split('-')[0])
current_year = datetime.now().year
current_month = datetime.now().month
current_day = datetime.now().day
if (current_month > birth_month) or (current_month == birth_month and current_day >= birth_date):
    birth_year = current_year - student_age
else:
    birth_year = current_year - student_age - 1
print("You were born in {}.".format(birth_year))

# ===========================================
# Final message
# ===========================================
print("\nThank you for using the Profile Analyzer, {}!".format(student_name))