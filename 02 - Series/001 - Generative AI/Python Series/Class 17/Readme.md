# Python Series: Class 17 - Lambda Functions

## Overview

In this class, we will learn about **lambda functions** in Python. Lambda functions are small anonymous functions defined using the `lambda` keyword. They are often used for short, simple functions that are needed temporarily, especially when passing them as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

---

### What You'll Learn:
1. **What is a Lambda Function?**
2. **Syntax of Lambda Functions**
3. **Using Lambda Functions in Practice**
4. **Lambda Functions with `map()`, `filter()`, and `sorted()`**
5. **Advantages of Lambda Functions**

---

## 1. What is a Lambda Function?

A lambda function is a small anonymous function defined by the `lambda` keyword. Unlike a regular function, it doesn't require a name or a return statement. It can accept any number of arguments but can only have one expression.

### Syntax:
```python
lambda arguments: expression
```

- **arguments**: The parameters you pass to the function.
- **expression**: A single expression that is evaluated and returned by the function.

### Example:
```python
# Lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
```

---

## 2. Using Lambda Functions in Practice

Lambda functions are useful in situations where you need a simple function for a short period of time, such as in sorting, filtering, or mapping operations.

### Example with `sorted()`:
You can use a lambda function to sort a list of tuples based on the second element.

```python
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])  # Sort by the second element (value)
print(sorted_pairs)
```

### Output:
```
[(3, 'three'), (2, 'two'), (1, 'one')]
```

---

## 3. Using Lambda Functions with `map()`, `filter()`, and `reduce()`

### `map()`

The `map()` function applies a given function to each item in an iterable (like a list) and returns a map object (which is an iterator).

### Example with `map()`:
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
```

### `filter()`

The `filter()` function filters elements from an iterable based on a condition (the function returns either `True` or `False`).

### Example with `filter()`:
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
```

### `reduce()` (from the `functools` module)

The `reduce()` function reduces a list to a single value by applying a function cumulatively to the elements of the list.

### Example with `reduce()`:
```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (1 * 2 * 3 * 4)
```

---

## 4. Advantages of Lambda Functions

- **Concise**: Lambda functions are shorter and more readable for simple operations.
- **Anonymous**: Lambda functions do not require a name, making them ideal for temporary use.
- **Functional Programming**: Lambda functions work well in functional programming paradigms like `map()`, `filter()`, and `reduce()`.

---

## Task

1. Write a lambda function that calculates the square of a number.
2. Create a list of numbers and use the `map()` function with your lambda to calculate the squares of all numbers in the list.
3. Write a lambda function to check if a number is divisible by 3 and use it with the `filter()` function to find all numbers divisible by 3 in a given list.

---