# Python Series: Class 21 - Testing and Debugging in Python

## Overview

In this class, we will learn about **testing** and **debugging** in Python. These two techniques are essential for ensuring that your Python code runs correctly and is free from errors. We'll cover different types of testing, how to use the built-in `unittest` module, and how to debug your code using Python's debugging tools.

---

### What You'll Learn:
1. **Why Testing is Important**
2. **Unit Testing with `unittest`**
3. **Debugging with Python's Built-in Tools**
4. **Using Assertions in Testing**

---

## 1. Why Testing is Important

Testing is the practice of evaluating code to ensure that it behaves as expected. It's crucial for:

- Catching bugs early.
- Ensuring that changes in the code don't break existing functionality.
- Improving code quality and reliability.

There are different levels of testing, including:

- **Unit Testing**: Testing individual parts (functions or methods) of your code.
- **Integration Testing**: Testing how different parts of your code work together.
- **End-to-End Testing**: Testing the entire application workflow.

In this class, we'll focus on unit testing, which is the most fundamental level of testing.

---

## 2. Unit Testing with `unittest`

Python provides a built-in module called `unittest` for writing and running tests. The `unittest` module allows you to define test cases, run them, and check if the code behaves as expected.

### Writing a Simple Test Case

Here’s how you can create a basic unit test with the `unittest` module:

1. **Create a Python function to test:**

```python
def add(a, b):
    return a + b
```

2. **Create a test case:**

```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()
```

- **`assertEqual(a, b)`**: This checks if `a` is equal to `b`. If not, the test fails.
- **`unittest.main()`**: This runs all the test cases when the script is executed.

### Running the Tests

You can run your tests by executing the script from the command line:

```bash
python test_script.py
```

If all tests pass, you’ll see something like this:
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

## 3. Debugging with Python's Built-in Tools

Debugging is the process of finding and fixing bugs (errors) in your code. Python provides several tools to help you debug your code efficiently:

### Using `print()` for Simple Debugging

One of the simplest debugging methods is adding `print()` statements to check the values of variables or the flow of execution.

```python
def add(a, b):
    print(f"a = {a}, b = {b}")  # Debugging statement
    return a + b
```

### Using the `pdb` (Python Debugger)

Python has a built-in debugger called `pdb` that allows you to step through your code and inspect variables.

- To start the debugger, insert `import pdb; pdb.set_trace()` at the point where you want to start debugging.

Example:

```python
import pdb

def add(a, b):
    pdb.set_trace()  # Debugger starts here
    return a + b

add(2, 3)
```

Once you run this, Python will pause at `pdb.set_trace()` and give you a prompt where you can enter commands like:

- **`n`**: Step to the next line.
- **`s`**: Step into a function.
- **`c`**: Continue execution until the next breakpoint.

---

## 4. Using Assertions in Testing

Assertions are a way of verifying that your code works as expected. They are used in both unit testing and debugging.

### Example:

```python
def multiply(a, b):
    assert isinstance(a, (int, float)), "a must be a number"
    assert isinstance(b, (int, float)), "b must be a number"
    return a * b

print(multiply(3, 4))  # Correct usage
print(multiply("3", 4))  # Incorrect usage, will raise AssertionError
```

Assertions are helpful during development because they catch issues early.

---

## Task

1. Write a function `divide(a, b)` that divides two numbers and handles division by zero using an exception.
2. Create test cases using the `unittest` module to test this function with valid and invalid inputs.
3. Use `assert` statements in your function to validate inputs before performing the division.

---