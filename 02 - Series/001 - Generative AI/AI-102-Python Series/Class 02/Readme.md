# Python Series: Class 02 - Variables, Data Types, and Input

## Overview

In this class, we will explore the fundamental building blocks of Python programming: **variables**, **data types**, and **input**. These concepts will help you store, process, and interact with data in Python.

---

### What You'll Learn:
1. What are variables?
2. Data types in Python.
3. Taking input from the user.
4. Basic input-output operations.

---

## 1. What are Variables?

A variable is a container for storing data values. In Python, you don’t need to specify the type of a variable explicitly; it is determined automatically.

### Example:
```python
name = "Alice"  # A variable storing a string
age = 25        # A variable storing an integer
height = 5.6    # A variable storing a float
```

### Key Points:
- Variables can hold different types of data.
- Use descriptive names for variables (e.g., `name`, `age`, `height`).

---

## 2. Data Types in Python

Python has several built-in data types, including:
- **String (str):** Text data. Example: `"Hello, World!"`
- **Integer (int):** Whole numbers. Example: `42`
- **Float:** Decimal numbers. Example: `3.14`
- **Boolean (bool):** Logical values `True` or `False`.

### Example:
```python
# String
greeting = "Hi there!"
# Integer
num_apples = 10
# Float
pi_value = 3.14159
# Boolean
is_sunny = True
```

---

## 3. Taking Input from the User

The `input()` function is used to take input from the user as a string.

### Example:
```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

To take numeric input, convert the input using `int()` or `float()`:
```python
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")
```

---

## 4. Basic Input-Output Operations

- Use `print()` to display information.
- Combine strings and variables using the `+` operator or formatted strings:
  ```python
  name = "Alice"
  print("Hello, " + name + "!")
  # OR using f-strings
  print(f"Hello, {name}!")
  ```

---

## Task

Write a program that:
1. Asks the user for their **name**, **age**, and **favorite color**.
2. Displays a message like:
   ```
   Hello, Alice! You are 25 years old and your favorite color is blue.
   ```

Save the program as `user_info.py` and run it.

---