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
print(f"University: {university_name}")
print(f"Department: {department_name}")
print(f"Email: {email_address}")
print(f"Programming Languages: {', '.join(programming_languages)}")
print(f"CGPA: {cgpa}")