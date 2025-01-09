# Python Series: Class 19 - Iterators and Generators

## Overview

In this class, we will cover **Iterators** and **Generators** in Python. These are advanced concepts that allow you to efficiently work with large data sets and lazy evaluation.

---

### What You'll Learn:
1. **What are Iterators?**
2. **Creating Iterators in Python**
3. **What are Generators?**
4. **Creating Generators in Python**
5. **When to Use Iterators and Generators**

---

## 1. What are Iterators?

An **iterator** is an object that represents a stream of data. It provides a way to access elements of a collection, such as a list or tuple, one at a time. In Python, an object is an iterator if it implements two methods:

- `__iter__()` - Returns the iterator object itself.
- `__next__()` - Returns the next element from the collection. If there are no more elements, it raises the `StopIteration` exception.

### Example of an Iterator:

```python
# Creating an iterator from a list
numbers = [1, 2, 3]
iterator = iter(numbers)

# Using the iterator to access elements
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # This will raise StopIteration
```

---

## 2. Creating Iterators in Python

You can create your own iterators by defining a class that implements the `__iter__()` and `__next__()` methods.

### Example:

```python
class CountUp:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Creating an iterator
counter = CountUp(1, 5)

# Using the iterator
for number in counter:
    print(number)
```

---

## 3. What are Generators?

A **generator** is a special type of iterator that is defined using a function with the `yield` keyword. Unlike regular functions that return a value and terminate, a generator yields values one at a time and can be resumed from where it left off.

### Example of a Generator:

```python
# Creating a simple generator
def count_up(start, end):
    while start <= end:
        yield start
        start += 1

# Using the generator
counter = count_up(1, 5)
for number in counter:
    print(number)
```

---

## 4. Creating Generators in Python

You can create generators using functions with `yield` or using generator expressions.

### Example of Generator Expression:

```python
# Creating a generator expression
gen = (x ** 2 for x in range(5))

# Using the generator
for square in gen:
    print(square)
```

---

## 5. When to Use Iterators and Generators

- **Iterators**: Use iterators when you need to traverse through all elements of a collection or data structure multiple times.
- **Generators**: Use generators for large datasets where you don't want to load the entire dataset into memory at once. Generators help in efficient memory management.

---

## Task

1. Create an iterator that generates numbers from 1 to 10.
2. Write a generator function that generates the Fibonacci sequence up to a specified number of terms.
3. Implement a generator expression that yields even numbers from 0 to 20.

---