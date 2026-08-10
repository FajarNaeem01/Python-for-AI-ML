"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 04 - CSV
Practice File

Author: Fajar Naeem Rana
===============================================
"""
import csv
students = [
    {"name": "Alice", "age": 20, "cgpa": 3.5},
    {"name": "Bob", "age": 21, "cgpa": 2.8},
    {"name": "Charlie", "age": 20, "cgpa": 3.9}
]
add_students=["Umais", 21, 3.7],["Abdullah", 23, 3.52]

# DictWriter()
# =======================================================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\students.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "cgpa"]
    writer=csv.DictWriter(file,fieldnames)
    writer.writeheader()
    writer.writerows(students)

# writer(), writerow(), writerows()
# ========================================================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\students.csv", "a", newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Fajar", 20, 3.4])
    writer.writerows(add_students)

# reader()
# =======================================================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
    print("Without headers")

# DictReader()
# ==========================================================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for student in reader:
        print(student)

# average cgpa
# =====================================
with open(r"Day04_File_and_Error_Handling_,JSON_CSV\data\students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    student_data=[]
    for student in reader:
        student_data.append(student)
    average=sum(float(student["cgpa"]) for student in student_data)/len(student_data)
    print(f"Average cgpa: {average}")

    