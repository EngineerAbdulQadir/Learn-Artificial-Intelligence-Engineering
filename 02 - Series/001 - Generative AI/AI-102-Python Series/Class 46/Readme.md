# Python Series: Class 46 - Introduction to Unit Testing

## Overview

In this class, we will learn the basics of **Unit Testing** in Python. Unit testing is a software testing technique in which individual units or components of a program are tested in isolation to ensure that each part of the code functions as expected.

We will focus on using Python's built-in `unittest` framework to write and run unit tests for our Python code. Unit tests are essential for verifying that your code works correctly and for catching bugs early in the development process.

---

### What You'll Learn:
1. **What is Unit Testing?**
2. **Setting Up Unit Tests**
3. **Writing Test Cases**
4. **Running Unit Tests**
5. **Assertions and Test Results**
6. **Mocking in Unit Tests**

---

## 1. What is Unit Testing?

Unit testing is the practice of testing individual units (or components) of code to verify that they perform as expected. A "unit" can be a function, a method, or a class. By writing unit tests, you can catch bugs and errors early in the development process, making it easier to maintain and debug your code.

Unit tests should be small, isolated, and independent of other tests. They should test only one piece of functionality at a time.

---

## 2. Setting Up Unit Tests

Python provides a built-in testing framework called **unittest** that allows you to write and run unit tests. The `unittest` module provides the necessary tools to create test cases, organize them, and execute them.

### Installing `unittest`
The `unittest` module is built into Python, so you don’t need to install it separately. It’s available by default in Python 3.x.

---

## 3. Writing Test Cases

Test cases in Python are written by creating a class that inherits from `unittest.TestCase`. Each test case is defined as a method within this class, and the name of the method must start with the word "test". Inside each test method, you write the code that tests a specific functionality.

### Example Code (Writing Unit Tests):

```python
import unittest

# Code to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test cases
class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-2, -3), -5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(-2, -3), 1)

if __name__ == '__main__':
    unittest.main()
```

### How It Works:
- **TestMathOperations**: A class that contains our test methods. It inherits from `unittest.TestCase`.
- **test_add()** and **test_subtract()**: Methods that test the `add()` and `subtract()` functions, respectively.
- **assertEqual()**: This method is an assertion. It checks if the result of the function being tested matches the expected value. If they don’t match, the test will fail.

---

## 4. Running Unit Tests

To run the unit tests, simply execute the Python script. You can run the tests either from the command line or directly from the IDE.

### Running Tests from the Command Line:
1. Save the code in a file, e.g., `test_math_operations.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the tests:
   ```bash
   python test_math_operations.py
   ```

If all the tests pass, you’ll see an output like this:

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

If any tests fail, you will get an error message indicating which test failed and why.

---

## 5. Assertions and Test Results

In unit testing, **assertions** are used to check if the code behaves as expected. If an assertion fails, the test is considered failed. The most common assertion methods in `unittest` are:
- `assertEqual(a, b)`: Check if `a` is equal to `b`.
- `assertNotEqual(a, b)`: Check if `a` is not equal to `b`.
- `assertTrue(x)`: Check if `x` is `True`.
- `assertFalse(x)`: Check if `x` is `False`.
- `assertIsNone(x)`: Check if `x` is `None`.
- `assertIsNotNone(x)`: Check if `x` is not `None`.
- `assertRaises(exception)`: Check if a specific exception is raised.

### Example of Additional Assertions:

```python
class TestMathOperations(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(2 * 3, 6)
        self.assertNotEqual(5 * 2, 10)
        
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            5 / 0
```

---

## 6. Mocking in Unit Tests

**Mocking** is a technique used in unit testing to simulate the behavior of complex objects or components that are difficult or impractical to test directly. In Python, the `unittest.mock` module provides a way to mock objects and methods for testing purposes.

### Example of Mocking:

```python
from unittest.mock import Mock

# Create a mock object
mock_obj = Mock()
mock_obj.some_method.return_value = 42

# Test the mocked method
class TestMocking(unittest.TestCase):
    
    def test_mock(self):
        result = mock_obj.some_method()
        self.assertEqual(result, 42)
```

---

## Summary

In this class, you learned the basics of **Unit Testing** in Python using the `unittest` framework. We covered:
1. The concept of unit testing and why it's important.
2. How to write test cases using `unittest.TestCase`.
3. Running and interpreting the results of unit tests.
4. Common assertions to verify the expected behavior of your code.
5. How to use mocking to simulate complex objects during testing.

---