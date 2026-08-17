"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 05 - Inheritance, Polymorphism, Abstraction
Practice File

Author: Fajar Naeem Rana
===============================================
"""

# Parent Class
class Employee:
    company_name = "ABC Company"

    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name = new_name

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print("\nEmployee Information: ")
        print(f"Company Name: {self.company_name}")
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

# Child Class: Developer
class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def task(self):
        print(f"{self.name} is writing {self.programming_language} code.")

    def employee_post(self):
        print("Post: Developer")

# Child Class: Manager
class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Team size: {self.team_size} people")

    def task(self):
        print(f"{self.name} manages a team of {self.team_size} people.")

    def employee_post(self):
        print("Post: Manager")

# =======================================================================
# Creating Objects
employee1 = Employee("Ali", "E001", 100000)
employee2 = Employee("Ahmed", "E002", 200000)

Employee.change_company_name("XYZ")

employees = [Developer("Abdullah","E003", 300000, "Python"), Manager("Fajar", "E004", 400000, 5)]

print("All Employees Information: ")
employee1.display_info()
employee2.display_info()

# Polymorphism
for employee in employees:
    employee.display_info()
    employee.employee_post()
    employee.task()