# Python Series: Class 06 - Functions in Python

## Overview

In this class, we will explore **functions** in Python. Functions allow us to group code into reusable blocks, making our programs more modular and easier to maintain.

---

### What You'll Learn:
1. **Defining functions** using `def`.
2. **Function parameters and return values**.
3. **Variable scope**.
4. **Lambda functions** (anonymous functions).

---

## 1. Defining Functions

A function in Python is defined using the `def` keyword followed by the function name and parentheses.

### Syntax:
```python
def function_name():
    # code to execute
```

### Example:
```python
def greet():
    print("Hello, welcome to Python!")
    
greet()  # Calling the function
```

---

## 2. Function Parameters and Return Values

Functions can accept input in the form of parameters and can return a value using the `return` keyword.

### Syntax:
```python
def function_name(parameter1, parameter2):
    # code to execute
    return result
```

### Example:
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output will be 8
```

---

## 3. Variable Scope

Variables defined inside a function are local to that function and cannot be accessed outside of it. These variables are called **local variables**. Variables defined outside of any function are called **global variables**.

### Example:
```python
x = 10  # Global variable

def example_function():
    y = 5  # Local variable
    print(x + y)

example_function()
# print(y)  # Uncommenting this line will cause an error since 'y' is local to the function.
```

---

## 4. Lambda Functions (Anonymous Functions)

A **lambda function** is a small anonymous function defined using the `lambda` keyword. These functions can have any number of arguments but only one expression.

### Syntax:
```python
lambda arguments: expression
```

### Example:
```python
add = lambda a, b: a + b
result = add(5, 3)
print(result)  # Output will be 8
```

---

## Task

Write a program that:
1. Defines a function `calculate_area(radius)` that calculates the area of a circle.
2. The function should take the radius as a parameter and return the area.
3. Call the function with a radius value and print the result.

Save the program as `circle_area.py` and run it.

---