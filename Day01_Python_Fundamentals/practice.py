"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 01 - Python Fundamentals
Practice File

Author: Fajar Naeem Rana
===============================================
"""

# ===========================================
# 1. VARIABLES
# ===========================================

name = "Fajar"
age = 20
cgpa = 2.9
is_student = True

print(name)
print(age)
print(cgpa)
print(is_student)

print("-" * 40)

# ===========================================
# 2. DATA TYPES
# ===========================================

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

print("-" * 40)

# ===========================================
# 3. TYPE CASTING
# ===========================================

number = "25"

print(int(number))
print(float(number))
print(str(100))
print(bool(1))
print(bool(0))

print("-" * 40)

# ===========================================
# 4. ARITHMETIC OPERATORS
# ===========================================

a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

print("-" * 40)

# ===========================================
# 5. COMPARISON OPERATORS
# ===========================================

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

print("-" * 40)

# ===========================================
# 6. LOGICAL OPERATORS
# ===========================================

x = True
y = False

print(x and y)
print(x or y)
print(not x)

print("-" * 40)

# ===========================================
# 7. MEMBERSHIP OPERATORS
# ===========================================

language = "Python"

print("P" in language)
print("Java" not in language)

print("-" * 40)

# ===========================================
# 8. IDENTITY OPERATORS
# ===========================================

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 == list3)

print("-" * 40)

# ===========================================
# 9. STRING INDEXING
# ===========================================

text = "Artificial Intelligence"

print(text[0])
print(text[-1])
print(text[5])

print("-" * 40)

# ===========================================
# 10. STRING SLICING
# ===========================================

print(text[:10])
print(text[11:])
print(text[0:10:2])
print(text[::-1])

print("-" * 40)

# ===========================================
# 11. STRING METHODS
# ===========================================

sentence = "python for ai"

print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.capitalize())

print(sentence.replace("ai", "machine learning"))

print(sentence.split())

print("-" * 40)

# ===========================================
# 12. METHOD CHAINING
# ===========================================

name = "   FAJAR naeem rana   "

formatted = name.strip().title()

print(formatted)

print("-" * 40)

# ===========================================
# 13. BUILT-IN FUNCTIONS
# ===========================================

numbers = [5, 2, 8, 1]

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sorted(numbers))

print(abs(-25))
print(round(3.14159, 2))

print("-" * 40)

# ===========================================
# 14. EMAIL DOMAIN EXTRACTION
# ===========================================

email = "student@qau.edu.pk"

domain = email.split("@")[1]

print(domain)

print("-" * 40)

# ===========================================
# 15. SUBSTRING CHECK
# ===========================================

text = "Artificial Intelligence"

print("AI" in text)
print("Intelligence" in text)

print("-" * 40)

# ===========================================
# 16. TRUTHY & FALSY
# ===========================================

username = ""

if username:
    print("Username exists")
else:
    print("Username is empty")

print("-" * 40)

# ===========================================
# 17. DEBUGGING HELPERS
# ===========================================

value = "Python"

print(type(value))
print(len(value))
print(repr(value))

print("-" * 40)

# ===========================================
# End of Day 01 Practice
# ===========================================