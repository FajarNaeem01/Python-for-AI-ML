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
