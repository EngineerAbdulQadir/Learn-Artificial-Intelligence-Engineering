# Python Series: Class 12 - Modules and Libraries

## Overview

In this class, we will explore how to import and use Python’s built-in modules and third-party libraries. Modules and libraries are essential for organizing code and leveraging existing functionalities, saving you from reinventing the wheel. You'll learn how to import and use standard modules, as well as how to install and use third-party libraries.

---

### What You'll Learn:
1. **What is a Module?**: Understanding what modules are and why they are used.
2. **Importing Modules**: How to import and use Python's built-in modules.
3. **Using Third-Party Libraries**: How to install and use libraries like `requests`, `numpy`, etc.
4. **Creating Your Own Modules**: How to organize your code into modules.
5. **Module Aliases**: Using aliases when importing modules.

---

## 1. What is a Module?

A module in Python is a file containing Python definitions and statements. It allows you to organize your code into logical chunks. Python comes with a large standard library that provides many useful modules to perform various tasks like file I/O, working with dates and times, mathematical operations, and more.

---

## 2. Importing Modules

You can import modules using the `import` statement. There are different ways to import modules depending on your needs:

### Basic Import:
```python
import math
result = math.sqrt(16)
print(result)
```
This imports the `math` module and uses its `sqrt` function to calculate the square root of `16`.

### Importing Specific Functions:
```python
from math import sqrt
result = sqrt(16)
print(result)
```
This imports only the `sqrt` function from the `math` module, saving memory.

### Importing with Aliases:
```python
import math as m
result = m.sqrt(16)
print(result)
```
This imports the `math` module as `m`, allowing you to use a shorter name.

---

## 3. Using Third-Party Libraries

To use third-party libraries, you first need to install them using the `pip` package manager. For example, to install the `requests` library, you can run:
```
pip install requests
```

Once installed, you can import and use the library:
```python
import requests
response = requests.get("https://www.example.com")
print(response.status_code)
```

This code uses the `requests` library to fetch a webpage and prints the HTTP status code of the response.

---

## 4. Creating Your Own Modules

You can create your own Python files that act as modules. For example, create a file called `mymodule.py`:
```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
```

Now, in another Python file, you can import and use this module:
```python
# main.py
import mymodule
print(mymodule.greet("Alice"))
```

This allows you to organize your code into separate, reusable files.

---

## 5. Module Aliases

When importing large libraries, you might want to use shorter names for convenience. You can create aliases using the `as` keyword.

For example:
```python
import pandas as pd
df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, 30]})
print(df)
```

Here, we imported the `pandas` library as `pd` to make the code shorter and more readable.

---

## Task

1. Install the `requests` library using `pip`.
2. Write a Python program that fetches the content from a website (e.g., "https://www.example.com") and prints the first 100 characters of the HTML content.
3. Ensure the program handles any exceptions that may occur while fetching the website (e.g., network error, invalid URL).

---