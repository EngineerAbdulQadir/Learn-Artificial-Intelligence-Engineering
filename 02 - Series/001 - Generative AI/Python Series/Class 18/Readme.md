# Python Series: Class 18 - List Comprehensions

## Overview

In this class, we will explore **list comprehensions** in Python. List comprehensions provide a concise way to create and manipulate lists. They offer a more compact syntax for creating lists compared to traditional for loops.

---

### What You'll Learn:
1. **What are List Comprehensions?**
2. **Basic Syntax of List Comprehensions**
3. **List Comprehensions with Conditions**
4. **Nested List Comprehensions**
5. **Advantages of List Comprehensions**

---

## 1. What are List Comprehensions?

List comprehensions allow you to create a new list by applying an expression to each element in an iterable (such as a list, tuple, or string). The result is a list containing the transformed elements.

---

## 2. Basic Syntax of List Comprehensions

The syntax of a basic list comprehension is as follows:

```python
[expression for item in iterable]
```

- **expression**: The operation or transformation that will be applied to each item.
- **item**: Each element from the iterable.
- **iterable**: The collection of items to iterate over.

### Example:
```python
# Traditional for loop
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)  # Output: [0, 1, 4, 9, 16]

# List comprehension
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

## 3. List Comprehensions with Conditions

List comprehensions can also include conditions, allowing you to filter items before applying the expression.

### Syntax with condition:
```python
[expression for item in iterable if condition]
```

### Example:
```python
# Get even numbers from the range 0-9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]
```

---

## 4. Nested List Comprehensions

List comprehensions can also be nested, meaning you can use a list comprehension inside another list comprehension.

### Example:
```python
# Create a 2D matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten the matrix using nested list comprehension
flat_list = [item for sublist in matrix for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 5. Advantages of List Comprehensions

- **Concise**: List comprehensions can replace longer for loop code, making the code more readable and concise.
- **Efficient**: List comprehensions are often faster than traditional loops due to their optimization in Python's internal implementation.
- **Readability**: They make your code more elegant and easier to understand when used appropriately.

---

## Task

1. Create a list of numbers from 1 to 20 using a list comprehension.
2. Use a list comprehension to filter out all the numbers that are divisible by 4 from the list.
3. Write a list comprehension to create a list of squares of only the even numbers from 1 to 20.

---