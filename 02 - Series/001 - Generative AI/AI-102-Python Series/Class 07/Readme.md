# Python Series: Class 07 - Lists and Tuples

## Overview

In this class, we will explore **lists** and **tuples**, two important collection types in Python. Both allow you to store multiple items in a single variable, but they differ in how they handle data and their use cases.

---

### What You'll Learn:
1. **Lists**: How to create, modify, and manipulate lists.
2. **Tuples**: How to create and use immutable sequences.
3. **List and Tuple operations**: Adding, removing, and accessing elements.

---

## 1. Lists

A list is an ordered collection that is mutable (can be modified). Lists can store items of different data types, and you can change the elements after the list is created.

### Syntax:
```python
my_list = [element1, element2, element3]
```

### Example:
```python
# Creating a list
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Modifying a list
fruits.append('orange')  # Adds 'orange' to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Accessing elements
print(fruits[0])  # Output: 'apple'

# Removing elements
fruits.remove('banana')  # Removes 'banana' from the list
print(fruits)  # Output: ['apple', 'cherry', 'orange']
```

---

## 2. Tuples

A tuple is similar to a list, but it is **immutable**. Once created, its elements cannot be changed, added, or removed. Tuples are typically used for data that shouldn't be modified.

### Syntax:
```python
my_tuple = (element1, element2, element3)
```

### Example:
```python
# Creating a tuple
coordinates = (10, 20, 30)
print(coordinates)  # Output: (10, 20, 30)

# Accessing elements
print(coordinates[1])  # Output: 20

# Tuples cannot be modified
# coordinates[1] = 25  # Uncommenting this line will cause an error
```

---

## 3. List and Tuple Operations

### Adding elements:
- Lists can use the `append()` method to add elements.
- Tuples cannot be modified once created, but you can concatenate tuples to form a new one.

### Example:
```python
# Adding elements to a list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Concatenating tuples
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)
```

### Removing elements:
- Lists can use the `remove()` method or `pop()` method to remove elements.

### Example:
```python
# Removing elements from a list
my_list = [1, 2, 3, 4]
my_list.remove(3)  # Removes the first occurrence of 3
print(my_list)  # Output: [1, 2, 4]

# Using pop() to remove the last item
my_list.pop()
print(my_list)  # Output: [1, 2]
```

---

## Task

Write a program that:
1. Creates a list of five numbers.
2. Adds two more numbers to the list.
3. Removes the first number from the list.
4. Creates a tuple with the same numbers as the list.
5. Print both the list and the tuple.

Save the program as `list_tuple_operations.py` and run it.

---