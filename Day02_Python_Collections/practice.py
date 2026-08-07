"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 02 - Python Collections
Practice File

Author: Fajar Naeem Rana
===============================================
"""

# ===========================================
# 1. LISTS
# ===========================================
languages= ["Python", "Java", "C++"]

languages.append("JavaScript")
languages.extend(["C", "Rust"])
languages.insert(1, "Go")
print(f"First Element: {languages[0]}")
print(f"Last Element: {languages[-1]}")
print(f"List Length: {len(languages)}")
print(f"Is 'Python' in List: {'Python' in languages}")
languages.append("Python")
print(f"Count of 'Python' in List: {languages.count('Python')}")
languages.remove("Java")

id=input("Enter the language you want to remove: ")
if id in languages:
    languages.remove(id)
    print(f"List after removing '{id}': {languages}")
else:
    print(f"'{id}' is not in the list")

# using slicing to get a sublist
numbers = [10, 20, 30, 40, 50]
print(f"First two elements: {numbers[0:2]}")
print(f"Other elements: {numbers[2:]}")
print(f"Reverse order: {numbers[::-1]}")

# ===========================================
numbers = [5, 2, 8, 1, 9, 3]
result = sorted(numbers)
print(f"Sorted List(without modifying original): {result}")
numbers.sort()
print(f"Sorted List(modified original): {numbers}")
numbers.sort(reverse=True)
print(f"Sorted List in Descending Order: {numbers}")
print(f"Minimum Value: {min(numbers)}")
print(f"Maximum Value: {max(numbers)}")
print(f"Sum of Values: {sum(numbers)}")

# ===========================================
# 2. TUPLES
# ===========================================   
student = (
    "Fajar Naeem Rana",
    20,
    "Computer Science",
    2.9
)
#unpacking tuple
name, age, major, cgpa = student
print("Student Information:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Major: {major}")
print(f"CGPA: {cgpa}")
# immutable nature of tuples
# student[0] = "John Doe"  # This will raise an error

#===========================================
# 3. SETS
#===========================================
languages = {"Python", "C++", "Java", "Python", "Java"}
print(f"Languages: {languages}")
print(f"Number of unique languages: {len(languages)}")
languages.add("JavaScript")
languages.update(["C", "Rust"])
languages.discard("Java")
languages.pop()  # removes an arbitrary element
print(f"Languages after modifications: {languages}")

#unique values from a list
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6, 5]
print(f"Unique Numbers: {set(numbers)}")

# set operations
python_students = {"Ali", "Sara", "Fajar", "Ahmed"}
ml_students = {"Fajar", "Ahmed", "Usman", "Ayesha"}

print(("Course Analysis:"))
print(f"Total Students: {len(python_students.union(ml_students))}")
print(f"Students in both courses: {python_students.intersection(ml_students)}")
print(f"Students only in Python course: {python_students.difference(ml_students)}")
print(f"Students only in ML course: {ml_students.difference(python_students)}")
print(f"Students enrolling in only one course: {python_students.symmetric_difference(ml_students)}")

# telling if a student is enrolled in a course
name=input("Enter your name: ")
if name in python_students:
    print(f"Hello {name}, you are enrolled in the Python course.")
elif name in ml_students:
    print(f"Hello {name}, you are enrolled in the ML course.")
elif name in python_students.union(ml_students):
    print(f"Hello {name}, you are enrolled in both courses.")
else:
    print(f"Hello {name}, you are not enrolled in either course.")
