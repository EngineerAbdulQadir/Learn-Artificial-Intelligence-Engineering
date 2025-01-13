# Python Series: Class 04 - Control Flow - If, Elif, Else

## Overview

In this class, we will learn about **conditional statements** in Python. Conditional statements allow us to make decisions in our code, such as whether a certain condition is true or false.

---

### What You'll Learn:
1. **If statements**.
2. **Elif statements**.
3. **Else statements**.
4. **Nested if statements**.

---

## 1. If Statements

The `if` statement is used to execute a block of code if a condition is true.

### Syntax:
```python
if condition:
    # code to execute if the condition is true
```

### Example:
```python
x = 5
if x > 0:
    print("x is positive")
```

---

## 2. Elif Statements

The `elif` (short for "else if") statement is used when you want to check multiple conditions. If the first `if` condition is false, Python will check the conditions in the `elif` block.

### Syntax:
```python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition1 is false and condition2 is true
```

### Example:
```python
x = 5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
```

---

## 3. Else Statements

The `else` statement is used when none of the previous conditions are true. It provides a fallback option.

### Syntax:
```python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition1 is false and condition2 is true
else:
    # code to execute if both conditions are false
```

### Example:
```python
x = -5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
```

---

## 4. Nested If Statements

You can also use an `if` statement inside another `if` statement, known as a **nested if**.

### Syntax:
```python
if condition1:
    if condition2:
        # code to execute if both condition1 and condition2 are true
```

### Example:
```python
x = 5
y = 10
if x > 0:
    if y > 5:
        print("x is positive and y is greater than 5")
```

---

## Task

Write a program that:
1. Takes a number from the user.
2. Prints whether the number is positive, negative, or zero using `if`, `elif`, and `else`.

Save the program as `number_sign.py` and run it.

---