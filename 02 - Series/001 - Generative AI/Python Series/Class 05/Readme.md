# Python Series: Class 05 - Loops - For and While

## Overview

In this class, we will explore two types of loops in Python: the **`for` loop** and the **`while` loop**. Loops allow us to repeat a block of code multiple times based on certain conditions.

---

### What You'll Learn:
1. **For loops** for iterating over a sequence.
2. **While loops** for repeating a block of code while a condition is true.
3. **Break** and **Continue** statements.
4. **Nested loops**.

---

## 1. For Loops

The `for` loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence.

### Syntax:
```python
for item in sequence:
    # code to execute for each item
```

### Example:
```python
# Iterating over a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

---

## 2. While Loops

The `while` loop repeatedly executes a block of code as long as a given condition is true.

### Syntax:
```python
while condition:
    # code to execute while the condition is true
```

### Example:
```python
# Printing numbers from 1 to 5 using while loop
x = 1
while x <= 5:
    print(x)
    x += 1  # Increment x by 1
```

---

## 3. Break and Continue Statements

- **`break`** is used to stop the loop prematurely.
- **`continue`** is used to skip the current iteration and continue with the next iteration.

### Example with `break`:
```python
for i in range(1, 6):
    if i == 3:
        break  # Exits the loop when i is 3
    print(i)
```

### Example with `continue`:
```python
for i in range(1, 6):
    if i == 3:
        continue  # Skips the iteration when i is 3
    print(i)
```

---

## 4. Nested Loops

Just like we can nest `if` statements, we can also nest loops inside each other. This is known as a **nested loop**.

### Syntax:
```python
for item in sequence:
    for item2 in sequence2:
        # code to execute for each pair of items
```

### Example:
```python
# Printing a 2D grid
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # For a new line after each row
```

---

## Task

Write a program that:
1. Takes a number `n` from the user.
2. Prints the multiplication table for the number `n` using a `for` loop.
3. If the number is greater than 10, stop the loop using the `break` statement.

Save the program as `multiplication_table.py` and run it.

---
