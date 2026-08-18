"""
===============================================
Python for AI/ML Engineering
Phase 0 - Professional Python

Day 06 - Iterators
Practice File

Author: Fajar Naeem Rana
===============================================
"""

class Counter:
    def __init__(self,limit):
        self.current = limit
        self.limit= 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.limit:
            value=self.current
            self.current -=1
            return value
        else:
            raise StopIteration

counter = Counter(5)

for number in counter:
    print(number)

# iterables
numbers = [10,20,30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))

# Generators 
def numbers():
    yield 1
    yield 2
    yield 3
    yield 4

generator = numbers()

print(next(generator))       # with next()
print(next(generator))

for generator in numbers():  # with for loop
    print(generator)

# Generator Expression
squares = (x ** 2 for x in range(1, 6))
print(next(squares))
print(next(squares))
print(next(squares))

# Generator Pipeline
def numbers():
    for number in range(1, 11):
        yield number

def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number

def squares(numbers):
    for number in numbers:
        yield number ** 2

data = numbers()
evens = even_numbers(data)
result = squares(evens)

for value in result:
    print(value)