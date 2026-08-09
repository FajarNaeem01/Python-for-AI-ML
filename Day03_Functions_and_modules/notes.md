# Day 03 — Functions & Modules

## Python for AI/ML Engineering

### Phase 0 — Professional Python

**Author:** Fajar Naeem Rana
**Day:** 03
**Chapter:** 3 — Functions & Modules

---

# Table of Contents

1. Functions
2. Defining Functions
3. Parameters and Arguments
4. Return Values
5. `print()` vs `return`
6. Function Docstrings
7. Default Arguments
8. Keyword Arguments
9. Type Hints
10. Function Composition
11. Scope and Global Variables
12. Modules
13. Importing Modules
14. `from ... import ...`
15. Import Aliases
16. Standard Library Modules
17. Creating Your Own Modules
18. `__name__`
19. `if __name__ == "__main__"`
20. Module vs Script
21. AI/ML Connection
22. Day 03 Cheat Sheet
23. Key Takeaways

---

# 1. Functions

A function is a reusable block of code designed to perform a specific task.

Instead of writing the same code repeatedly, we define it once and call it whenever needed.

Example:

```python
def greet():
    print("Hello!")
```

Calling the function:

```python
greet()
```

Output:

```text
Hello!
```

---

# 2. Defining Functions

## Basic Syntax

```python
def function_name():
    # function body
```

Example:

```python
def greet():
    print("Hello, Fajar!")
```

Calling:

```python
greet()
```

---

## Function with Parameters

Parameters allow us to pass information into a function.

```python
def greet(name):
    print(f"Hello, {name}!")
```

Calling:

```python
greet("Fajar")
```

Output:

```text
Hello, Fajar!
```

Here:

```text
name → parameter
"Fajar" → argument
```

---

# 3. Parameters and Arguments

A parameter is the variable defined inside the function declaration.

An argument is the actual value passed when calling the function.

Example:

```python
def add(a, b):
    return a + b
```

Calling:

```python
add(10, 5)
```

Here:

```text
a → parameter
b → parameter

10 → argument
5  → argument
```

---

# 4. Return Values

A function can return a value using `return`.

Example:

```python
def add(a, b):
    return a + b
```

Then:

```python
result = add(10, 5)

print(result)
```

Output:

```text
15
```

The returned value can be stored, modified, or passed to another function.

---

# 5. `print()` vs `return`

This is one of the most important concepts.

## `print()`

```python
def add(a, b):
    print(a + b)
```

This displays the result but does not give the result back to the program.

---

## `return`

```python
def add(a, b):
    return a + b
```

Now we can do:

```python
result = add(10, 5)

print(result)
```

Or:

```python
result = add(10, 5) * 2
```

Or:

```python
if add(10, 5) > 10:
    print("Large")
```

### Important Rule

Use:

```python
return
```

when a function needs to produce data that other parts of the program can use.

Use:

```python
print()
```

when the function's purpose is specifically to display something.

---

# 6. Function Docstrings

A docstring describes what a function does.

Example:

```python
def calculate_average(numbers):
    """
    Calculate and return the average of a list of numbers.
    """
    return sum(numbers) / len(numbers)
```

The docstring appears immediately after the function definition.

Docstrings make code easier to understand and maintain.

---

# 7. Default Arguments

A parameter can have a default value.

```python
def greet(name="Fajar"):
    print(f"Hello, {name}!")
```

Calling:

```python
greet()
```

Output:

```text
Hello, Fajar!
```

Calling:

```python
greet("Ahmed")
```

Output:

```text
Hello, Ahmed!
```

The supplied argument replaces the default value.

---

# 8. Keyword Arguments

Arguments can be passed using parameter names.

```python
def student_info(name, age):
    print(name, age)
```

Instead of:

```python
student_info("Fajar", 20)
```

we can write:

```python
student_info(age=20, name="Fajar")
```

This improves readability and allows arguments to be supplied by name.

---

# 9. Type Hints

Type hints allow us to describe the expected types of parameters and return values.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here:

```text
a: int
b: int
```

means the parameters are expected to be integers.

```text
-> int
```

means the function is expected to return an integer.

---

## Example from Student Analytics

```python
def get_top_students(students: list) -> list:
    ...
```

This tells us:

```text
students → expected to be a list
return value → expected to be a list
```

More advanced type hints will be covered later.

---

# 10. Function Composition

Functions can call other functions.

Example:

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def get_status(numbers):
    average = calculate_average(numbers)

    if average >= 50:
        return "Pass"

    return "Fail"
```

Here:

```text
get_status()
      ↓
calculate_average()
      ↓
returns average
      ↓
get_status() uses result
```

This prevents duplicate logic.

---

## Student Analytics Example

```python
def calculate_average_cgpa(students):
    if not students:
        return 0.0

    return sum(
        student["cgpa"]
        for student in students
    ) / len(students)


def get_top_students(students):
    average_cgpa = calculate_average_cgpa(students)

    return [
        student["name"]
        for student in students
        if student["cgpa"] > average_cgpa
    ]
```

`get_top_students()` reuses `calculate_average_cgpa()`.

This is a good example of modular programming.

---

# 11. Scope and Global Variables

A variable created inside a function normally exists only inside that function.

Example:

```python
def calculate():
    result = 10
    print(result)
```

`result` is local to the function.

Using unnecessary global variables can make programs harder to understand and maintain.

Prefer passing data into functions:

```python
def display_students(students):
    for student in students:
        print(student)
```

Instead of relying on a global:

```python
students = [...]

def display_students():
    for student in students:
        print(student)
```

Passing parameters makes functions more reusable.

---

# 12. Modules

A **module is a Python file containing Python code**.

For example:

```text
project/
│
├── main.py
└── calculator.py
```

`calculator.py` is a module.

Modules allow us to organize code into separate files.

---

# 13. Why Use Modules?

Modules make programs:

* More organized
* Reusable
* Easier to maintain
* Easier to debug
* Easier to test
* Easier to collaborate on

A large AI/ML project might eventually look like:

```text
AI_Project/
│
├── main.py
├── data_loader.py
├── preprocessing.py
├── model.py
├── evaluation.py
└── utils.py
```

Each module can have a specific responsibility.

---

# 14. Importing a Module

Suppose:

### `calculator.py`

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

In `main.py`:

```python
import calculator
```

Now we can use:

```python
calculator.add(10, 5)
```

and:

```python
calculator.subtract(10, 5)
```

The structure is:

```text
module.function()
```

---

# 15. `from ... import ...`

Instead of importing the entire module:

```python
import calculator
```

we can import specific functions:

```python
from calculator import add, subtract
```

Now we can directly write:

```python
add(10, 5)
subtract(10, 5)
```

---

## Difference

### Import module

```python
import calculator

calculator.add(10, 5)
```

### Import specific function

```python
from calculator import add

add(10, 5)
```

Both are valid.

---

# 16. Import Aliases

We can give a module a shorter name using `as`.

```python
import student_analyzer as std
```

Instead of:

```python
student_analyzer.get_names(students)
```

we can write:

```python
std.get_names(students)
```

This is very common in AI/ML.

Examples we'll use later:

```python
import numpy as np
import pandas as pd
```

---

# 17. Avoid `from module import *`

You may see:

```python
from calculator import *
```

This imports everything from the module.

However, it is generally better to avoid this in professional code because it can cause naming conflicts and make it unclear where functions came from.

Prefer:

```python
from calculator import add, subtract
```

or:

```python
import calculator
```

---

# 18. Python Standard Library Modules

Python comes with many built-in modules.

No separate installation is required.

Examples:

```python
import math
import random
import datetime
import os
import json
import csv
import statistics
```

---

## Example: `math`

```python
import math

print(math.sqrt(25))
print(math.pi)
```

Output:

```text
5.0
3.141592653589793
```

---

## Importing a Specific Function

```python
from math import sqrt

print(sqrt(25))
```

---

# 19. Creating Your Own Module

Suppose we have:

```text
project/
│
├── main.py
└── student_utils.py
```

### `student_utils.py`

```python
def get_names(students):
    return [
        student["name"]
        for student in students
    ]


def get_cgpas(students):
    return [
        student["cgpa"]
        for student in students
    ]


def calculate_average_cgpa(students):
    if not students:
        return 0.0

    return sum(
        student["cgpa"]
        for student in students
    ) / len(students)
```

### `main.py`

```python
from student_utils import (
    get_names,
    get_cgpas,
    calculate_average_cgpa
)
```

Then:

```python
students = [
    {"name": "Alice", "cgpa": 3.5},
    {"name": "Bob", "cgpa": 2.8}
]

print(get_names(students))
print(get_cgpas(students))
print(calculate_average_cgpa(students))
```

---

# 20. The `__name__` Variable

Every Python module has a special variable:

```python
__name__
```

Its value depends on how the file is being used.

---

## Running a File Directly

Suppose:

```text
calculator.py
```

contains:

```python
print(__name__)
```

If we directly run:

```text
python calculator.py
```

Python sets:

```python
__name__ = "__main__"
```

Therefore the output is:

```text
__main__
```

---

## Importing a File

Suppose:

```text
main.py
calculator.py
```

and `main.py` contains:

```python
import calculator
```

When running:

```text
python main.py
```

`main.py` has:

```python
__name__ = "__main__"
```

But inside `calculator.py`:

```python
__name__ = "calculator"
```

because it was imported rather than directly executed.

---

# 21. `if __name__ == "__main__"`

This is a very common Python pattern:

```python
if __name__ == "__main__":
    print("This file is being executed directly.")
```

It means:

> Run this code only when this file is executed directly.

---

## Example

### `calculator.py`

```python
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))
```

If we run:

```text
python calculator.py
```

Output:

```text
30
```

But if another file does:

```python
import calculator
```

the `print(add(10, 20))` section will not automatically execute.

The function is still available:

```python
calculator.add(10, 20)
```

---

# 22. Main Function Pattern

A common professional structure is:

```python
def main():
    print("Program starts here.")


if __name__ == "__main__":
    main()
```

This means:

1. Define the program's functions.
2. Define a `main()` function.
3. Execute `main()` only if the file is run directly.

This pattern becomes useful as projects grow.

---

# 23. Module vs Script

### Module

A Python file intended to be imported and reused.

Example:

```text
student_analyzer.py
```

### Script

A Python file intended to execute a program.

Example:

```text
main.py
```

The same `.py` file can technically be used in both ways.

That's why:

```python
if __name__ == "__main__":
```

is useful.

---

# 24. Our Day 03 Student Analytics Example

We separated our project into modules:

```text
Day03/
│
├── main.py
├── student_analyzer.py
└── calculator.py
```

### `calculator.py`

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

### `student_analyzer.py`

Contains functions such as:

```python
get_names()
get_cgpas()
calculate_average_cgpa()
get_top_students()
add_student()
display_students()
get_passing_students()
generate_report()
```

### `main.py`

Imports them:

```python
from calculator import add, subtract
import student_analyzer as std
```

Then uses:

```python
std.get_names(students)
```

and:

```python
add(number1, number2)
```

This demonstrates how separate modules can work together.

---

# 25. AI/ML Connection

Modules become extremely important when building real AI/ML systems.

A project could eventually look like:

```text
image_classifier/
│
├── main.py
├── data_loader.py
├── preprocessing.py
├── model.py
├── training.py
├── evaluation.py
├── config.py
└── utils.py
```

For example:

```python
from preprocessing import clean_data
from model import train_model
from evaluation import evaluate_model
```

This keeps the project organized.

Instead of having thousands of lines in one file, each module handles a specific responsibility.

---

# 26. Key Takeaways

### Functions

```text
Function
   ↓
Reusable block of code
```

### Parameters

```text
Information entering a function
```

### Return

```text
Information leaving a function
```

### Docstring

```text
Description of what a function does
```

### Type Hint

```text
Describes expected data types
```

### Module

```text
Python file containing reusable code
```

### Import

```text
Allows us to use code from another module
```

### Alias

```text
import module as short_name
```

### `__name__`

```text
Special variable identifying how a module is being used
```

### `__main__`

```text
Value of __name__ when a file is executed directly
```

---

# 27. Day 03 Cheat Sheet

## Functions

```python
def greet():
    print("Hello")


def greet(name):
    return f"Hello, {name}"


result = greet("Fajar")
```

---

## Default Argument

```python
def greet(name="Fajar"):
    print(name)
```

---

## Keyword Argument

```python
greet(name="Fajar")
```

---

## Type Hint

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## Docstring

```python
def add(a, b):
    """
    Return the sum of two numbers.
    """
    return a + b
```

---

## Module Import

```python
import calculator

calculator.add(5, 3)
```

---

## Specific Import

```python
from calculator import add

add(5, 3)
```

---

## Multiple Imports

```python
from calculator import add, subtract
```

---

## Alias

```python
import student_analyzer as std

std.get_names(students)
```

---

## Standard Library

```python
import math
import random
import datetime
```

---

## Main Guard

```python
if __name__ == "__main__":
    main()
```

---

# 🎯 Day 03 Completion Checklist

Before marking Day 03 complete, you should be able to:

* [x] Define functions
* [x] Use parameters
* [x] Use arguments
* [x] Return values
* [x] Understand `print()` vs `return`
* [x] Write docstrings
* [x] Use default arguments
* [x] Use keyword arguments
* [x] Write basic type hints
* [x] Call one function from another
* [x] Understand basic variable scope
* [x] Create modules
* [x] Import modules
* [x] Import specific functions
* [x] Use aliases
* [x] Use standard-library modules
* [x] Understand `__name__`
* [x] Understand `__main__`
* [x] Use `if __name__ == "__main__"`

---

# 🧠 Final Mental Model

Think of a Python project like a toolbox.

```text
Project
│
├── main.py
│      → controls the program
│
├── calculator.py
│      → mathematical tools
│
├── student_analyzer.py
│      → student-analysis tools
│
└── other modules
       → other specialized tools
```

Functions are the **individual tools**.

Modules are the **toolboxes that organize those tools**.

A large AI/ML project is essentially many specialized toolboxes working together.

---

# 🚀 Day 03 Status

**Functions → Completed ✅**

**Modules & Imports → Completed ✅**

**Practice → Completed ✅**

