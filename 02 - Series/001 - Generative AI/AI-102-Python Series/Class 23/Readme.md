# Python Series: Class 23 - Decorators in Python

## Overview

In this class, we will learn about **decorators** in Python. A decorator is a design pattern in Python that allows us to extend or alter the behavior of a callable (like a function or method) without permanently modifying it. Decorators are commonly used for logging, enforcing access control, instrumentation, caching, and more.

---

### What You'll Learn:
1. **What are Decorators?**
2. **How Decorators Work**
3. **Using Function Decorators**
4. **Decorator Syntax**
5. **Chaining Multiple Decorators**

---

## 1. What are Decorators?

A **decorator** is a function that takes another function and extends or alters its behavior. This is useful because it allows you to add functionality to an existing function without changing its code directly.

For example, you could use a decorator to log every time a function is called, measure the execution time, or check user permissions before executing a function.

---

## 2. How Decorators Work

Decorators in Python work by:

- Taking a function as input.
- Adding some extra functionality to it.
- Returning a new function that behaves in the same way as the original one, but with the added functionality.

### Example:

```python
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    return "Display function executed"

# Applying the decorator to the display function
decorated_display = decorator_function(display)
print(decorated_display())
```

Here, the decorator (`decorator_function`) wraps the `display` function, adding some functionality before it executes.

---

## 3. Using Function Decorators

Python provides a simpler way to apply decorators using the `@decorator_name` syntax. This eliminates the need for manually reassigning the function to a new variable.

### Example:

```python
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    return "Display function executed"

print(display())  # Now, the decorator is applied automatically
```

Here, the `@decorator_function` decorator is applied to the `display` function, which results in the same behavior but with less code.

---

## 4. Decorator Syntax

The syntax for a decorator looks like this:

```python
@decorator_name
def function_to_decorate():
    # function body
```

This is a shorthand for:

```python
function_to_decorate = decorator_name(function_to_decorate)
```

Decorators can also accept arguments if needed. In such cases, you’ll need to define a decorator function that returns another decorator function.

---

## 5. Chaining Multiple Decorators

You can apply multiple decorators to a single function by stacking them on top of each other. Each decorator wraps the function one by one, from bottom to top.

### Example:

```python
def decorator_one(func):
    def wrapper():
        print("Decorator One")
        return func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        return func()
    return wrapper

@decorator_one
@decorator_two
def display():
    return "Display function executed"

print(display())
```

Here, the `display` function is first wrapped by `decorator_two` and then by `decorator_one`.

---

## Task

1. Write a decorator that logs the execution time of a function.
2. Apply this decorator to a function that performs a time-consuming task (e.g., sorting a large list).
3. Create another decorator that prints a message before and after the execution of any function.
4. Apply both decorators to a function and test the result.

---
