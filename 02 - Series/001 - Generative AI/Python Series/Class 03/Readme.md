# Python Series: Class 03 - Operators in Python

## Overview

In this class, we will learn about the various **operators** in Python. Operators allow us to perform operations on variables and values, such as mathematical calculations, comparisons, and logical operations.

---

### What You'll Learn:
1. Arithmetic operators.
2. Comparison operators.
3. Logical operators.
4. Assignment operators.

---

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric values.

### List of Arithmetic Operators:
- **Addition (`+`)**
- **Subtraction (`-`)**
- **Multiplication (`*`)**
- **Division (`/`)**
- **Floor Division (`//`)** – Returns the integer part of the division.
- **Modulus (`%`)** – Returns the remainder of the division.
- **Exponentiation (`**`)** – Raises the number to the power of the second operand.

### Example:
```python
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
```

---

## 2. Comparison Operators

Comparison operators are used to compare two values. They return `True` or `False`.

### List of Comparison Operators:
- **Equal to (`==`)**
- **Not equal to (`!=`)**
- **Greater than (`>`)**
- **Less than (`<`)**
- **Greater than or equal to (`>=`)**
- **Less than or equal to (`<=`)**

### Example:
```python
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True
```

---

## 3. Logical Operators

Logical operators are used to combine conditional statements. They also return `True` or `False`.

### List of Logical Operators:
- **and** – Returns `True` if both statements are true.
- **or** – Returns `True` if one of the statements is true.
- **not** – Returns `True` if the statement is false.

### Example:
```python
x = 5
y = 10

print(x > 0 and y > 5)  # True, both conditions are true
print(x > 0 or y < 5)   # True, at least one condition is true
print(not(x > 0))       # False, since x > 0 is true
```

---

## 4. Assignment Operators

Assignment operators are used to assign values to variables.

### List of Assignment Operators:
- **=`** – Assigns a value to a variable.
- **`+=`** – Adds a value to the variable and assigns it.
- **`-=`** – Subtracts a value from the variable and assigns it.
- **`*=`** – Multiplies the variable by a value and assigns it.
- **`/=`** – Divides the variable by a value and assigns it.
- **`//=`** – Floor divides the variable by a value and assigns it.
- **`%=`** – Applies modulus to the variable and assigns it.
- **`**=`** – Raises the variable to the power of a value and assigns it.

### Example:
```python
a = 5
a += 3  # a = a + 3
print(a)  # 8

b = 10
b *= 2  # b = b * 2
print(b)  # 20
```

---

## Task

Write a program that:
1. Takes two numbers from the user.
2. Perform all the arithmetic operations (addition, subtraction, etc.) on these numbers and prints the results.

Save the program as `basic_operations.py` and run it.

---
