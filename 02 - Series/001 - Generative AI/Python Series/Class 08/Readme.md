# Python Series: Class 08 - Dictionaries and Sets

## Overview

In this class, we will delve into **dictionaries** and **sets** in Python. These two are powerful data structures used to store collections of data, but they have distinct characteristics and use cases.

---

### What You'll Learn:
1. **Dictionaries**: How to work with key-value pairs in Python.
2. **Sets**: Understanding unique collections and set operations.
3. **Dictionary and Set Operations**: Adding, accessing, and removing items.

---

## 1. Dictionaries

A dictionary in Python is an unordered collection of key-value pairs. Each key must be unique, and values can be of any data type.

### Syntax:
```python
my_dict = {key1: value1, key2: value2, key3: value3}
```

### Example:
```python
# Creating a dictionary
person = {"name": "John", "age": 25, "city": "New York"}

# Accessing dictionary values
print(person["name"])  # Output: John

# Adding a new key-value pair
person["job"] = "Developer"
print(person)  # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'job': 'Developer'}

# Removing a key-value pair
del person["age"]
print(person)  # Output: {'name': 'John', 'city': 'New York', 'job': 'Developer'}
```

### Dictionary Methods:
- `keys()`: Returns a view of all the keys.
- `values()`: Returns a view of all the values.
- `items()`: Returns a view of all the key-value pairs.
- `get()`: Returns the value associated with the key (or a default value if the key is not found).

### Example:
```python
# Accessing keys, values, and items
print(person.keys())   # Output: dict_keys(['name', 'city', 'job'])
print(person.values()) # Output: dict_values(['John', 'New York', 'Developer'])
print(person.items())  # Output: dict_items([('name', 'John'), ('city', 'New York'), ('job', 'Developer')])

# Using get() method
print(person.get("name"))  # Output: John
print(person.get("age", "Not Found"))  # Output: Not Found
```

---

## 2. Sets

A set is an unordered collection of unique elements. Sets are mutable and are commonly used for membership tests, removing duplicates, and performing set operations like union, intersection, and difference.

### Syntax:
```python
my_set = {element1, element2, element3}
```

### Example:
```python
# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding elements to a set
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Removing elements from a set
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}

# Trying to remove a non-existent element (will raise an error)
# fruits.remove("grapes")  # Uncommenting this line will cause an error

# Discarding an element (no error if the element does not exist)
fruits.discard("grapes")  # Does nothing if "grapes" does not exist
```

### Set Operations:
- **Union (`|`)**: Combine two sets.
- **Intersection (`&`)**: Get common elements between two sets.
- **Difference (`-`)**: Get elements in one set but not in the other.

### Example:
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}
```

---

## Task

Write a program that:
1. Creates a dictionary with at least three key-value pairs.
2. Adds two new key-value pairs to the dictionary.
3. Removes one key-value pair from the dictionary.
4. Creates a set with at least five elements (some duplicate values).
5. Removes any duplicates from the set.
6. Prints both the dictionary and the set.

Save the program as `dict_set_operations.py` and run it.

---