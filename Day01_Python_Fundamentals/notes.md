# 📘 Python for AI/ML Engineering

## Phase 0 - Professional Python

# Day 01 - Python Fundamentals

---

## Topics Covered

- Variables
- Data Types
- Input & Output
- Type Casting
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- Identity Operators
- Membership Operators
- String Indexing
- String Slicing
- String Methods
- Method Chaining
- Built-in Functions
- Truthy & Falsy Values
- Pythonic Programming

---

# Variables

Variables store data in memory.

```python
name = "Fajar"
age = 20
cgpa = 2.9
```

Python is dynamically typed, so there is no need to declare variable types.

---

# Data Types

```python
int
float
str
bool
None
```

Check a variable's type:

```python
type(variable)
```

---

# Type Casting

```python
int("25")

float("3.14")

str(100)

bool(1)

bool(0)
```

---

# Arithmetic Operators

```python
+

-

*

/

//

%

**
```

---

# Comparison Operators

```python
==

!=

>

<

>=

<=
```

Return either `True` or `False`.

---

# Logical Operators

```python
and

or

not
```

Used for combining multiple conditions.

---

# Membership Operators

```python
in

not in
```

Example:

```python
"Python" in sentence
```

---

# Identity Operators

```python
is

is not
```

`is` checks whether two variables refer to the same object in memory.

---

# String Indexing

```python
text[0]

text[-1]
```

Positive indexing starts from the left.

Negative indexing starts from the right.

---

# String Slicing

```python
text[start:end]

text[:]

text[::-1]
```

Useful for extracting parts of a string.

---

# Important String Methods

```python
upper()

lower()

title()

capitalize()

strip()

replace()

split()

find()

count()

startswith()

endswith()
```

Strings are immutable.

Methods return new strings.

---

# Method Chaining

```python
name.strip().title()
```

Multiple methods can be applied in a single statement.

---

# Built-in Functions

```python
len()

type()

isinstance()

id()

min()

max()

sum()

sorted()

abs()

round()

range()

enumerate()

zip()

any()

all()

dir()

repr()
```

---

# Truthy & Falsy Values

Falsy values:

```python
False

0

0.0

None

""

[]

{}

set()
```

Everything else is generally Truthy.

---

# Pythonic Programming

Instead of

```python
if len(name) > 0:
```

Write

```python
if name:
```

Instead of

```python
if x == True:
```

Write

```python
if x:
```

Write meaningful variable names.

Follow PEP 8 naming conventions.

---

# Common Errors

```python
SyntaxError

TypeError

ValueError

IndexError

NameError
```

Read the error message carefully before debugging.

---

# Key Takeaways

- Python is dynamically typed.
- Strings are immutable.
- Everything in Python is an object.
- Built-in functions simplify common tasks.
- Clean and readable code is preferred over clever code.
- Understanding error messages is an essential programming skill.

---

## Next Topic

**Day 02 - Python Collections**

- Lists
- Tuples
- Sets
- Dictionaries (Introduction)
- Nested Collections
- Copying vs Referencing