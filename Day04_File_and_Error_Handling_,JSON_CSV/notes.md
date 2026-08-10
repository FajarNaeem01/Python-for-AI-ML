# 🐍 Python for AI/ML Engineering

## Phase 0 — Professional Python

# Day 04 — File Handling, JSON, CSV & Exception Handling

**Author:** Fajar Naeem Rana

---

# 📚 Day 04 Overview

Today we learned how Python programs can work with external data and handle errors safely.

### Topics Covered

1. File Handling
2. File Modes
3. Reading Files
4. Writing Files
5. Appending Files
6. `with` Statement
7. JSON
8. JSON Serialization & Deserialization
9. CSV
10. `csv.reader()`
11. `csv.writer()`
12. `csv.DictReader()`
13. `csv.DictWriter()`
14. Exceptions
15. `try`
16. `except`
17. `else`
18. `finally`
19. `raise`
20. Common Python Exceptions

---

# 1. File Handling

File handling allows Python programs to create, read, write, and modify files.

This is important because programs often need to work with data stored outside the Python program.

Examples:

* Student records
* Configuration files
* Logs
* Datasets
* Reports
* AI/ML training data

---

# 2. Opening a File

## Syntax

```python
open(filename, mode)
```

Example:

```python
file = open("students.txt", "r")
```

However, it is better to use the `with` statement.

---

# 3. File Modes

| Mode   | Meaning       |
| ------ | ------------- |
| `"r"`  | Read          |
| `"w"`  | Write         |
| `"a"`  | Append        |
| `"x"`  | Create        |
| `"b"`  | Binary        |
| `"t"`  | Text          |
| `"r+"` | Read + Write  |
| `"w+"` | Write + Read  |
| `"a+"` | Append + Read |

---

## `"r"` — Read

Used to read an existing file.

```python
with open("students.txt", "r") as file:
    data = file.read()
```

If the file does not exist:

```text
FileNotFoundError
```

---

## `"w"` — Write

Creates a file if it doesn't exist.

If the file already exists, its previous contents are **overwritten**.

```python
with open("profile.txt", "w") as file:
    file.write("Name: Fajar")
```

---

## `"a"` — Append

Adds content to the end of the existing file.

It does **not** remove existing content.

```python
with open("profile.txt", "a") as file:
    file.write("\nUniversity: QAU")
```

---

## `"x"` — Create

Creates a new file.

If the file already exists:

```text
FileExistsError
```

Example:

```python
with open("student.txt", "x") as file:
    file.write("Hello")
```

---

# 4. `with` Statement

The recommended way to work with files.

## Syntax

```python
with open("filename", "mode") as file:
    # file operations
```

Example:

```python
with open("students.txt", "r") as file:
    data = file.read()
```

### Why use `with`?

It automatically closes the file after the block finishes.

Instead of manually doing:

```python
file = open("students.txt", "r")

data = file.read()

file.close()
```

we can use:

```python
with open("students.txt", "r") as file:
    data = file.read()
```

This is safer and cleaner.

---

# 5. `read()`

Reads the entire file as one string.

## Syntax

```python
file.read()
```

Example:

```python
with open("students.txt", "r") as file:
    data = file.read()

print(data)
```

Output:

```text
Ali
Ahmed
Noor
```

---

# 6. `readline()`

Reads one line at a time.

## Syntax

```python
file.readline()
```

Example:

```python
with open("students.txt", "r") as file:
    line = file.readline()

print(line)
```

Output:

```text
Ali
```

---

# 7. `readlines()`

Reads all lines and returns them as a list.

## Syntax

```python
file.readlines()
```

Example:

```python
with open("students.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Output:

```text
['Ali\n', 'Ahmed\n', 'Noor\n']
```

---

# 8. Iterating Through a File

A file can be directly used in a loop.

```python
with open("students.txt", "r") as file:
    for line in file:
        print(line)
```

This processes the file one line at a time.

This is useful when working with large files because we don't necessarily need to load everything into memory at once.

---

# 9. `write()`

Writes a string to a file.

## Syntax

```python
file.write(string)
```

Example:

```python
with open("profile.txt", "w") as file:
    file.write("Name: Fajar")
    file.write("\nUniversity: QAU")
```

---

# 10. `writelines()`

Writes multiple strings to a file.

## Syntax

```python
file.writelines(iterable)
```

Example:

```python
students = ["Ali\n", "Ahmed\n", "Noor\n"]

with open("students.txt", "w") as file:
    file.writelines(students)
```

Important:

`writelines()` does **not automatically add `\n`**.

Therefore:

```python
["Ali\n", "Ahmed\n"]
```

is better than:

```python
["Ali", "Ahmed"]
```

if we want separate lines.

---

# 11. JSON

JSON stands for:

**JavaScript Object Notation**

It is a common format for storing and exchanging structured data.

Example JSON:

```json
{
    "name": "Fajar",
    "age": 20,
    "cgpa": 3.4
}
```

JSON is extremely important for AI/ML because APIs, configuration files, datasets, and web services frequently use JSON.

---

# 12. Why Convert Python Data to JSON?

Python has its own data structures:

```python
student = {
    "name": "Fajar",
    "age": 20,
    "cgpa": 3.4
}
```

JSON is a standardized text format that other programs and systems can understand.

For example:

```text
Python program
      ↓
Python dictionary
      ↓
JSON
      ↓
API / File / Web service
      ↓
Another program
```

This allows different systems to exchange structured information.

---

# 13. Python → JSON

This process is called:

**Serialization**

The main functions are:

```python
json.dumps()
json.dump()
```

---

# 14. `json.dumps()`

Converts Python data into a JSON **string**.

## Syntax

```python
json.dumps(python_object)
```

Example:

```python
import json

student = {
    "name": "Fajar",
    "age": 20,
    "cgpa": 3.4
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))
```

Output:

```text
{"name": "Fajar", "age": 20, "cgpa": 3.4}
<class 'str'>
```

### Important

`dumps()` means:

**dump string**

It gives us a JSON string.

---

# 15. `json.dump()`

Writes Python data directly into a JSON file.

## Syntax

```python
json.dump(python_object, file)
```

Example:

```python
import json

student = {
    "name": "Fajar",
    "age": 20,
    "cgpa": 3.4
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

The file contains:

```json
{
    "name": "Fajar",
    "age": 20,
    "cgpa": 3.4
}
```

---

# 16. JSON → Python

The reverse process is called:

**Deserialization**

The main functions are:

```python
json.loads()
json.load()
```

---

# 17. `json.loads()`

Converts a JSON string into a Python object.

## Syntax

```python
json.loads(json_string)
```

Example:

```python
import json

json_data = '{"name": "Fajar", "age": 20}'

student = json.loads(json_data)

print(student)
print(type(student))
```

Output:

```text
{'name': 'Fajar', 'age': 20}
<class 'dict'>
```

---

# 18. `json.load()`

Reads JSON data directly from a file.

## Syntax

```python
json.load(file)
```

Example:

```python
import json

with open("student.json", "r") as file:
    student = json.load(file)

print(student)
```

Output:

```text
{'name': 'Fajar', 'age': 20, 'cgpa': 3.4}
```

---

# 19. JSON Function Cheat Sheet

| Function       | Purpose              |
| -------------- | -------------------- |
| `json.dumps()` | Python → JSON string |
| `json.loads()` | JSON string → Python |
| `json.dump()`  | Python → JSON file   |
| `json.load()`  | JSON file → Python   |

Remember:

```text
s = string
no s = file
```

So:

```text
dumps → string
loads → string

dump → file
load → file
```

---

# 20. CSV

CSV stands for:

**Comma-Separated Values**

Example:

```csv
name,age,cgpa
Alice,20,3.5
Bob,21,2.8
Charlie,20,3.9
```

CSV is extremely common for tabular data.

It is especially important for AI/ML because many datasets are distributed as CSV files.

---

# 21. Importing CSV

```python
import csv
```

---

# 22. `csv.writer()`

Used to write rows into a CSV file.

## Syntax

```python
csv.writer(file)
```

Example:

```python
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
```

---

# 23. `writerow()`

Writes **one row**.

## Syntax

```python
writer.writerow(row)
```

Example:

```python
writer.writerow(["Fajar", 20, 3.4])
```

CSV:

```csv
Fajar,20,3.4
```

---

# 24. `writerows()`

Writes **multiple rows**.

## Syntax

```python
writer.writerows(rows)
```

Example:

```python
students = [
    ["Alice", 20, 3.5],
    ["Bob", 21, 2.8]
]

writer.writerows(students)
```

---

# 25. `csv.reader()`

Reads CSV rows as lists.

## Syntax

```python
csv.reader(file)
```

Example:

```python
with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```text
['name', 'age', 'cgpa']
['Alice', '20', '3.5']
['Bob', '21', '2.8']
```

Notice that CSV values are read as **strings**.

---

# 26. `next()`

Can be used to skip the header.

```python
reader = csv.reader(file)

next(reader)

for row in reader:
    print(row)
```

Output:

```text
['Alice', '20', '3.5']
['Bob', '21', '2.8']
```

---

# 27. `csv.DictWriter()`

Writes dictionaries into a CSV file.

This is convenient when our data is already stored as dictionaries.

## Syntax

```python
csv.DictWriter(file, fieldnames)
```

Example:

```python
students = [
    {"name": "Alice", "age": 20, "cgpa": 3.5},
    {"name": "Bob", "age": 21, "cgpa": 2.8}
]

fieldnames = ["name", "age", "cgpa"]

with open("students.csv", "w", newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(students)
```

Output file:

```csv
name,age,cgpa
Alice,20,3.5
Bob,21,2.8
```

---

# 28. `writeheader()`

Writes the field names as the first row.

```python
writer.writeheader()
```

Output:

```csv
name,age,cgpa
```

---

# 29. `csv.DictReader()`

Reads CSV data as dictionaries.

## Syntax

```python
csv.DictReader(file)
```

Example:

```python
with open("students.csv", "r", newline="") as file:

    reader = csv.DictReader(file)

    for student in reader:
        print(student)
```

Output:

```text
{'name': 'Alice', 'age': '20', 'cgpa': '3.5'}
{'name': 'Bob', 'age': '21', 'cgpa': '2.8'}
```

Now we can easily access:

```python
student["name"]
student["age"]
student["cgpa"]
```

---

# 30. Important CSV Data Type Concept

CSV stores values as text.

For example:

```python
student["cgpa"]
```

might return:

```text
'3.5'
```

not:

```text
3.5
```

Therefore, for calculations:

```python
float(student["cgpa"])
```

For integers:

```python
int(student["age"])
```

This is a basic example of **data preprocessing**, which will become extremely important in AI/ML.

---

# 31. Exceptions

An exception is a runtime problem that interrupts normal program execution.

Example:

```python
number = int("hello")
```

Output:

```text
ValueError
```

---

# 32. Syntax Error vs Exception

### Syntax Error

The code itself is invalid.

```python
if x > 5
    print(x)
```

Output:

```text
SyntaxError
```

### Exception

The syntax is valid, but something goes wrong during execution.

```python
int("hello")
```

Output:

```text
ValueError
```

---

# 33. Common Exceptions

| Exception           | Meaning                      |
| ------------------- | ---------------------------- |
| `ValueError`        | Invalid value                |
| `TypeError`         | Wrong data type              |
| `ZeroDivisionError` | Division by zero             |
| `FileNotFoundError` | File doesn't exist           |
| `FileExistsError`   | File already exists          |
| `KeyError`          | Dictionary key doesn't exist |
| `IndexError`        | List index doesn't exist     |
| `NameError`         | Variable/name doesn't exist  |

---

# 34. `try`

Contains code that might produce an exception.

## Syntax

```python
try:
    risky_code
```

Example:

```python
try:
    age = int(input("Enter age: "))
```

---

# 35. `except`

Handles an exception.

## Syntax

```python
try:
    risky_code

except ExceptionType:
    error_handling
```

Example:

```python
try:
    age = int(input("Enter age: "))

except ValueError:
    print("Please enter a valid number.")
```

Input:

```text
abc
```

Output:

```text
Please enter a valid number.
```

---

# 36. Multiple `except` Blocks

```python
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 37. `else`

Runs only when the `try` block succeeds.

## Syntax

```python
try:
    risky_code

except:
    error_handling

else:
    successful_code
```

Example:

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)
```

---

# 38. `finally`

Runs regardless of whether an exception occurred.

## Syntax

```python
try:
    risky_code

except:
    error_handling

finally:
    always_execute
```

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")
```

The final message appears in both success and failure cases.

---

# 39. Complete Exception Structure

```python
try:
    # risky code

except SomeException:
    # handle error

else:
    # runs if successful

finally:
    # always runs
```

Flow:

```text
try
 ↓
Exception?
 ├── YES → except
 │
 └── NO  → else
             ↓
          finally
```

---

# 40. Capturing the Exception

We can store the exception in a variable.

```python
try:
    number = int("hello")

except ValueError as error:
    print("Error:", error)
```

Output:

```text
Error: invalid literal for int() with base 10: 'hello'
```

Syntax:

```python
except ExceptionType as variable:
```

---

# 41. `raise`

`raise` allows us to deliberately create an exception.

## Syntax

```python
raise ExceptionType("message")
```

Example:

```python
cgpa = 5

if cgpa > 4:
    raise ValueError("CGPA must be between 0 and 4.")
```

Output:

```text
ValueError: CGPA must be between 0 and 4.
```

---

# 42. Custom Validation with `raise`

```python
def validate_cgpa(cgpa):

    if cgpa < 0:
        raise ValueError("CGPA cannot be negative.")

    if cgpa > 4:
        raise ValueError("CGPA must be between 0 and 4.")

    return cgpa
```

Valid:

```python
print(validate_cgpa(3.5))
```

Output:

```text
3.5
```

Invalid:

```python
print(validate_cgpa(5))
```

Output:

```text
ValueError: CGPA must be between 0 and 4.
```

---

# 43. Combining `raise` and `except`

```python
def validate_cgpa(cgpa):

    if cgpa < 0:
        raise ValueError("CGPA cannot be negative.")

    if cgpa > 4:
        raise ValueError("CGPA must be between 0 and 4.")

    return cgpa


try:

    cgpa = float(input("Enter CGPA: "))

    valid_cgpa = validate_cgpa(cgpa)

    print("Valid CGPA:", valid_cgpa)

except ValueError as error:

    print("Invalid CGPA:", error)
```

Input:

```text
3.5
```

Output:

```text
Valid CGPA: 3.5
```

Input:

```text
5
```

Output:

```text
Invalid CGPA: CGPA must be between 0 and 4.
```

---

# 44. Why Exception Handling Matters in AI/ML

AI/ML programs work with lots of external data.

Examples:

```text
CSV datasets
JSON APIs
Images
Databases
User input
Model files
Configuration files
Web APIs
```

Any of these can fail.

For example:

```text
Dataset missing
       ↓
FileNotFoundError
       ↓
Handle exception
       ↓
Tell user what happened
```

Instead of:

```text
💥 Program crashed
```

Professional programs should fail **gracefully**.

---

# 🧠 Day 04 Key Concepts

### File Handling

```python
open()
read()
readline()
readlines()
write()
writelines()
```

### File Modes

```text
r → read
w → write/overwrite
a → append
x → create
```

### JSON

```python
json.dumps()
json.loads()
json.dump()
json.load()
```

Remember:

```text
dumps → Python → JSON string
loads → JSON string → Python

dump → Python → JSON file
load → JSON file → Python
```

### CSV

```python
csv.reader()
csv.writer()
csv.DictReader()
csv.DictWriter()

writerow()
writerows()
writeheader()
```

### Exceptions

```python
try
except
else
finally
raise
```

---

# 🔥 Day 04 Revision Cheat Sheet

```text
FILE HANDLING
──────────────────────────────
open("file.txt", "r")
open("file.txt", "w")
open("file.txt", "a")
open("file.txt", "x")

read()
readline()
readlines()

write()
writelines()

with open(...) as file:
    ...


JSON
──────────────────────────────
Python → JSON string
json.dumps()

JSON string → Python
json.loads()

Python → JSON file
json.dump()

JSON file → Python
json.load()


CSV
──────────────────────────────
csv.reader()
csv.writer()

csv.DictReader()
csv.DictWriter()

writerow()
writerows()
writeheader()


EXCEPTIONS
──────────────────────────────
try:
    ...

except ValueError:
    ...

except TypeError:
    ...

else:
    ...

finally:
    ...

raise ValueError("message")
```

---

# 🎯 AI/ML Connection

The concepts from Day 04 form the foundation for handling real-world datasets.

```text
Files
  ↓
JSON / CSV
  ↓
Python Data Structures
  ↓
Validation
  ↓
Exception Handling
  ↓
Data Processing
  ↓
AI/ML
```

Later, when we learn:

```text
NumPy
Pandas
APIs
Databases
Machine Learning
Deep Learning
```

we will repeatedly use the concepts learned today.

---


# 🚀 End of Day 04

Today we learned how Python programs interact with **external data** and how to make them more **reliable and fault-tolerant**.

The next step is to combine these concepts into a practical project rather than learning them in isolation.
