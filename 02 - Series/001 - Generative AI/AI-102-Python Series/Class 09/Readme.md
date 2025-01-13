# Python Series: Class 09 - String Manipulation

## Overview

In this class, we will cover string manipulation in Python. Strings are one of the most commonly used data types, and Python provides a rich set of operations to work with them.

---

### What You'll Learn:
1. **String Basics**: Creating and accessing strings.
2. **String Methods**: Built-in methods for manipulating strings.
3. **String Formatting**: Formatting strings using different techniques.

---

## 1. String Basics

A string is a sequence of characters enclosed in quotes. Python supports both single quotes (`'`) and double quotes (`"`).

### Creating Strings:
```python
# Single line string
str1 = 'Hello, World!'

# Multi-line string using triple quotes
str2 = '''This is a 
multi-line string.'''
```

### Accessing String Characters:
You can access individual characters using indexing. Remember that Python uses **0-based indexing**.

```python
greeting = "Hello"
print(greeting[0])  # Output: H
print(greeting[1])  # Output: e
```

Negative indexing is also supported, where `-1` is the last character.

```python
print(greeting[-1])  # Output: o
```

---

## 2. String Methods

Python provides many built-in methods to manipulate strings.

### Example Methods:
```python
text = "python programming"

# Converting to uppercase
print(text.upper())  # Output: PYTHON PROGRAMMING

# Converting to lowercase
print(text.lower())  # Output: python programming

# Capitalizing the first letter of each word
print(text.title())  # Output: Python Programming

# Checking if the string starts with a specific substring
print(text.startswith("python"))  # Output: True

# Checking if the string ends with a specific substring
print(text.endswith("programming"))  # Output: True

# Replacing a substring
print(text.replace("python", "java"))  # Output: java programming

# Finding the index of a substring
print(text.find("programming"))  # Output: 7

# Splitting a string into a list of words
print(text.split())  # Output: ['python', 'programming']
```

---

## 3. String Formatting

Python provides several ways to format strings, allowing for better readability and flexibility.

### Using f-strings (Python 3.6+):
```python
name = "Alice"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
# Output: My name is Alice and I am 25 years old.
```

### Using `str.format()` method:
```python
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
# Output: My name is Alice and I am 25 years old.
```

### Using the `%` operator (older method):
```python
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)
# Output: My name is Alice and I am 25 years old.
```

---

## Task

Write a Python program that:
1. Takes an input string from the user.
2. Converts the string to uppercase and lowercase.
3. Replaces any occurrences of the word "Python" with "Java".
4. Counts the number of times "Python" appears in the string.
5. Formats a sentence that includes the string and its length.

Save the program as `string_manipulation.py` and run it.

---