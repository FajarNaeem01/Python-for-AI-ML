# Day 02 — Python Collections

## Python for AI/ML Engineering

### Phase 0 — Professional Python

**Author:** Fajar Naeem Rana
**Day:** 02
**Chapter:** 2 — Python Collections

---

# Table of Contents

1. Lists
2. Tuples
3. Sets
4. Dictionaries
5. Nested Collections
6. List Comprehensions
7. Set Comprehensions
8. Dictionary Comprehensions
9. `enumerate()`
10. `zip()`
11. Key Takeaways
12. Day 02 Cheat Sheet

---

# 1. Lists

A list is an ordered, mutable collection that can contain multiple values.

## Syntax

```python
my_list = [item1, item2, item3]
```

Example:

```python
languages = ["Python", "Java", "C++"]
```

Lists:

* Maintain order
* Allow duplicate values
* Are mutable
* Support indexing and slicing
* Can contain different data types

---

## Accessing List Elements

```python
languages = ["Python", "Java", "C++"]

print(languages[0])
print(languages[1])
print(languages[-1])
```

Output:

```text
Python
Java
C++
```

---

## Modifying Lists

Lists are mutable.

```python
languages[1] = "Go"
```

---

## `append()`

Adds one element to the end.

```python
languages.append("JavaScript")
```

---

## `extend()`

Adds multiple elements.

```python
languages.extend(["C", "Rust"])
```

Difference:

```python
languages.append(["C", "Rust"])
```

adds the entire list as one element.

```python
languages.extend(["C", "Rust"])
```

adds each item separately.

---

## `insert()`

Adds an element at a specific position.

```python
languages.insert(1, "Go")
```

---

## `remove()`

Removes the first matching value.

```python
languages.remove("Java")
```

If the value does not exist, Python raises:

```text
ValueError
```

---

## `pop()`

Removes and returns an element.

```python
last = languages.pop()
```

Remove by index:

```python
languages.pop(2)
```

---

## `count()`

Counts occurrences.

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))
```

Output:

```text
3
```

---

## `index()`

Finds the first position of an element.

```python
numbers = [10, 20, 30]

print(numbers.index(20))
```

Output:

```text
1
```

---

## List Length

```python
len(languages)
```

---

## Membership

```python
"Python" in languages
```

Returns:

```text
True
```

or:

```text
False
```

---

# 2. List Slicing

Syntax:

```python
list[start:stop:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0:2])
```

Output:

```text
[10, 20]
```

The `stop` index is excluded.

---

## Omitting Start

```python
numbers[:3]
```

---

## Omitting Stop

```python
numbers[2:]
```

---

## Using Step

```python
numbers[::2]
```

---

## Reversing a List

```python
numbers[::-1]
```

---

# 3. Sorting Lists

## `sort()`

Modifies the original list.

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 5, 8]
```

Descending:

```python
numbers.sort(reverse=True)
```

---

## `sorted()`

Creates a new sorted list without modifying the original.

```python
numbers = [5, 2, 8, 1]

result = sorted(numbers)

print(result)
print(numbers)
```

---

## Important Difference

```text
sort()   → modifies original list
sorted() → returns a new sorted list
```

---

## Useful Functions

```python
min(numbers)
max(numbers)
sum(numbers)
len(numbers)
```

---

# 4. Tuples

A tuple is an ordered, immutable collection.

## Syntax

```python
my_tuple = (item1, item2, item3)
```

Example:

```python
coordinates = (10, 20)
```

Tuples support:

* Indexing
* Slicing
* Iteration
* Duplicate values

But they cannot normally be modified after creation.

---

## Accessing Tuples

```python
coordinates = (10, 20)

print(coordinates[0])
print(coordinates[-1])
```

---

## Tuple Unpacking

```python
coordinates = (10, 20)

x, y = coordinates

print(x)
print(y)
```

This is very useful in Python.

---

## Single-Element Tuple

This is a tuple:

```python
x = (10,)
```

This is not:

```python
x = (10)
```

The comma makes it a tuple.

---

## Tuple Methods

```python
tuple.count(value)
tuple.index(value)
```

---

# 5. Sets

A set is an unordered collection of unique values.

## Syntax

```python
numbers = {1, 2, 3, 4}
```

Sets:

* Do not allow duplicates
* Are useful for membership testing
* Support mathematical set operations

Example:

```python
numbers = {1, 2, 2, 3, 3}

print(numbers)
```

Result:

```text
{1, 2, 3}
```

---

## Adding Elements

```python
numbers.add(5)
```

---

## Removing Elements

```python
numbers.remove(3)
```

`remove()` raises an error if the element does not exist.

Safer alternative:

```python
numbers.discard(3)
```

---

# 6. Set Operations

Suppose:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

## Union

Everything from both sets:

```python
A | B
```

or:

```python
A.union(B)
```

Result:

```text
{1, 2, 3, 4, 5, 6}
```

---

## Intersection

Common elements:

```python
A & B
```

or:

```python
A.intersection(B)
```

Result:

```text
{3, 4}
```

---

## Difference

Elements in A but not B:

```python
A - B
```

Result:

```text
{1, 2}
```

---

## Symmetric Difference

Elements that exist in either set, but not both:

```python
A ^ B
```

Result:

```text
{1, 2, 5, 6}
```

---

# 7. Dictionaries

A dictionary stores data as **key-value pairs**.

## Syntax

```python
student = {
    "name": "Fajar",
    "age": 20,
    "cgpa": 2.9
}
```

Think:

```text
key       value
 ↓          ↓
"name" → "Fajar"
"age"  → 20
"cgpa" → 2.9
```

Dictionaries are extremely important for AI/ML because they are frequently used for structured records, configurations, metadata, and JSON-like data.

---

## Accessing Values

```python
print(student["name"])
```

---

## `get()`

Safer access:

```python
print(student.get("name"))
```

If the key doesn't exist:

```python
student.get("email")
```

returns:

```text
None
```

You can provide a default:

```python
student.get("email", "Not provided")
```

---

## Adding and Updating

```python
student["email"] = "student@example.com"
```

Updating an existing key:

```python
student["cgpa"] = 3.1
```

---

## Removing

```python
student.pop("age")
```

---

## Dictionary Methods

```python
student.keys()
student.values()
student.items()
```

Example:

```python
for key, value in student.items():
    print(key, value)
```

---

# 8. Nested Collections

Python collections can contain other collections.

Example:

```python
students = [
    {
        "name": "Fajar",
        "age": 20,
        "cgpa": 2.9
    },
    {
        "name": "Ahmed",
        "age": 21,
        "cgpa": 3.4
    }
]
```

Access:

```python
print(students[0]["name"])
```

Output:

```text
Fajar
```

This structure is extremely important because it resembles the type of structured data you'll encounter before moving into Pandas.

---

# 9. `enumerate()`

`enumerate()` gives both the index and the value while iterating.

Instead of:

```python
languages = ["Python", "C++", "Java"]

for i in range(len(languages)):
    print(i, languages[i])
```

we can write:

```python
for index, language in enumerate(languages):
    print(index, language)
```

Output:

```text
0 Python
1 C++
2 Java
```

You can choose a starting index:

```python
for index, language in enumerate(languages, start=1):
    print(index, language)
```

Output:

```text
1 Python
2 C++
3 Java
```

---

# 10. List Comprehensions

A list comprehension is a concise way to create a list.

Normal loop:

```python
squares = []

for number in range(1, 6):
    squares.append(number ** 2)
```

List comprehension:

```python
squares = [number ** 2 for number in range(1, 6)]
```

Result:

```text
[1, 4, 9, 16, 25]
```

---

## Basic Structure

```python
[expression for item in iterable]
```

Example:

```python
[x * 2 for x in numbers]
```

---

# 11. List Comprehension with Condition

Example:

```python
even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]
```

Result:

```text
[2, 4, 6, 8, 10]
```

Structure:

```python
[expression for item in iterable if condition]
```

---

# 12. Conditional Expression in Comprehension

You can also use `if/else` inside the expression.

```python
result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in range(1, 6)
]
```

Result:

```text
["Odd", "Even", "Odd", "Even", "Odd"]
```

Notice the difference:

```python
# Filtering
[x for x in numbers if condition]

# Conditional output
[value_if_true if condition else value_if_false for x in numbers]
```

---

# 13. Set Comprehensions

Set comprehensions work similarly.

```python
squares = {x ** 2 for x in range(1, 6)}
```

Result:

```text
{1, 4, 9, 16, 25}
```

Because it is a set, duplicate values are automatically removed.

---

# 14. Dictionary Comprehensions

Dictionary comprehensions create dictionaries.

Example:

```python
squares = {
    x: x ** 2
    for x in range(1, 6)
}
```

Result:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

Structure:

```python
{key: value for item in iterable}
```

---

## Dictionary Comprehension with Condition

```python
even_squares = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}
```

---

# 15. Nested Comprehensions

You can use nested loops inside comprehensions.

Example:

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

Flatten it:

```python
flattened = [
    value
    for row in matrix
    for value in row
]
```

Result:

```text
[1, 2, 3, 4]
```

The equivalent normal loops are:

```python
flattened = []

for row in matrix:
    for value in row:
        flattened.append(value)
```

---

# 16. `zip()`

`zip()` combines elements from multiple iterables based on position.

Example:

```python
names = ["Fajar", "Ahmed", "Sara"]
cgpas = [2.9, 3.4, 3.7]

students = zip(names, cgpas)
```

Convert to a list:

```python
print(list(students))
```

Result:

```text
[
    ("Fajar", 2.9),
    ("Ahmed", 3.4),
    ("Sara", 3.7)
]
```

---

## Using `zip()` in a Loop

```python
names = ["Fajar", "Ahmed", "Sara"]
cgpas = [2.9, 3.4, 3.7]

for name, cgpa in zip(names, cgpas):
    print(name, cgpa)
```

Output:

```text
Fajar 2.9
Ahmed 3.4
Sara 3.7
```

---

## Creating a Dictionary with `zip()`

This is particularly useful.

```python
names = ["Fajar", "Ahmed", "Sara"]
cgpas = [2.9, 3.4, 3.7]

students = dict(zip(names, cgpas))

print(students)
```

Result:

```python
{
    "Fajar": 2.9,
    "Ahmed": 3.4,
    "Sara": 3.7
}
```

---

## Unequal Lengths

Normally, `zip()` stops when the shortest iterable runs out.

```python
names = ["Fajar", "Ahmed", "Sara"]
cgpas = [2.9, 3.4]

print(list(zip(names, cgpas)))
```

Result:

```text
[("Fajar", 2.9), ("Ahmed", 3.4)]
```

`Sara` is not included.

---

# 17. Important Collection Comparison

| Collection | Ordered | Mutable | Duplicates  | Main Use           |
| ---------- | ------- | ------- | ----------- | ------------------ |
| List       | Yes     | Yes     | Yes         | General collection |
| Tuple      | Yes     | No      | Yes         | Fixed data         |
| Set        | No*     | Yes     | No          | Unique values      |
| Dictionary | Yes**   | Yes     | Keys unique | Key-value data     |

* Sets don't provide sequence-style indexing/order semantics.
** Dictionaries preserve insertion order in modern Python.

---

# 18. Key Python Patterns to Remember

### List

```python
items = [1, 2, 3]
```

### Tuple

```python
items = (1, 2, 3)
```

### Set

```python
items = {1, 2, 3}
```

### Dictionary

```python
items = {
    "name": "Fajar",
    "cgpa": 2.9
}
```

### List comprehension

```python
[x ** 2 for x in numbers]
```

### Set comprehension

```python
{x ** 2 for x in numbers}
```

### Dictionary comprehension

```python
{x: x ** 2 for x in numbers}
```

### `enumerate()`

```python
for index, value in enumerate(items):
    ...
```

### `zip()`

```python
for a, b in zip(list1, list2):
    ...
```

---

# 19. AI/ML Connection

These concepts will appear constantly later.

### Lists

Used for:

```text
data
features
predictions
labels
```

### Dictionaries

Used for:

```text
configuration
metadata
records
JSON
API responses
```

### Sets

Useful for:

```text
unique labels
unique categories
membership testing
```

### Comprehensions

Useful for:

```text
data transformation
filtering
feature preparation
```

### `zip()`

Useful for combining:

```text
features + labels
names + predictions
IDs + values
```

### `enumerate()`

Useful when you need:

```text
index + data
```

---

# 20. Day 02 Cheat Sheet

```python
# LIST
items = [1, 2, 3]

items.append(4)
items.extend([5, 6])
items.insert(0, 0)
items.remove(2)
items.pop()
items.count(3)

items[0]
items[-1]
items[1:3]
items[::-1]

sorted(items)
items.sort()

# TUPLE
point = (10, 20)

x, y = point

# SET
A = {1, 2, 3}
B = {3, 4, 5}

A | B       # Union
A & B       # Intersection
A - B       # Difference
A ^ B       # Symmetric difference

# DICTIONARY
student = {
    "name": "Fajar",
    "cgpa": 2.9
}

student["name"]
student.get("cgpa")
student.keys()
student.values()
student.items()

# ENUMERATE
for index, value in enumerate(items):
    print(index, value)

# LIST COMPREHENSION
squares = [x ** 2 for x in range(10)]

# CONDITIONAL COMPREHENSION
even = [x for x in range(10) if x % 2 == 0]

# SET COMPREHENSION
squares = {x ** 2 for x in range(10)}

# DICTIONARY COMPREHENSION
squares = {x: x ** 2 for x in range(10)}

# ZIP
names = ["Fajar", "Ahmed"]
cgpas = [2.9, 3.4]

for name, cgpa in zip(names, cgpas):
    print(name, cgpa)

# ZIP → DICTIONARY
students = dict(zip(names, cgpas))
```

---

# 🎯 Day 02 Final Takeaway

By the end of Day 02, you should be comfortable with:

```text
Lists
   ↓
Tuples
   ↓
Sets
   ↓
Dictionaries
   ↓
Nested Collections
   ↓
Comprehensions
   ↓
enumerate()
   ↓
zip()
```

**Day 02 officially ends here.**

Next:

> **Chapter 3 — Day 03: Functions + Modules**
