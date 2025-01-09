# Python Series: Class 44 - Command-Line Arguments

## Overview

In this class, we will learn how to use **command-line arguments** in Python. Command-line arguments allow you to pass information to a Python script when running it from the terminal or command prompt. This is a useful feature for making your scripts more flexible, dynamic, and interactive without hardcoding values directly in the code.

---

### What You'll Learn:
1. **What Are Command-Line Arguments?**
2. **Accessing Command-Line Arguments in Python**
3. **Using `sys.argv` to Read Arguments**
4. **Working with Arguments in Python**
5. **Using `argparse` for Advanced Argument Parsing**

---

## 1. What Are Command-Line Arguments?

Command-line arguments are pieces of information you pass to your Python program when you execute it in the terminal. These arguments can be values such as strings, numbers, or file paths that the program uses to control its behavior or perform tasks.

For example:
```
python script.py arg1 arg2 arg3
```

In this case, `script.py` is your Python script, and `arg1`, `arg2`, and `arg3` are the arguments passed to it.

---

## 2. Accessing Command-Line Arguments in Python

Python provides a built-in module called `sys` that allows you to interact with the command-line arguments.

You can access the arguments using `sys.argv`. `sys.argv` is a list where:
- `sys.argv[0]` is the name of the Python script being executed.
- `sys.argv[1]`, `sys.argv[2]`, etc., are the arguments passed to the script.

### Example Code (Accessing Arguments):

```python
import sys

# Print all command-line arguments
print("Arguments passed:", sys.argv)

# Access individual arguments
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])
```

In this example:
- `sys.argv` is printed to show all the arguments.
- We check if any arguments are passed and then access the first argument (`sys.argv[1]`).

### How to Run the Script:
```bash
python script.py hello world 123
```

Output:
```
Arguments passed: ['script.py', 'hello', 'world', '123']
First argument: hello
```

---

## 3. Using `sys.argv` to Read Arguments

In many cases, you'll want to read multiple arguments and use them in your Python program. Here's how to handle that using `sys.argv`.

### Example Code (Using Multiple Arguments):

```python
import sys

# Check if at least two arguments are passed
if len(sys.argv) != 3:
    print("Usage: python script.py <arg1> <arg2>")
else:
    # Access the two arguments
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")
```

In this example:
- The script checks if exactly two arguments are passed.
- If correct, it accesses `sys.argv[1]` and `sys.argv[2]`.

### How to Run the Script:
```bash
python script.py apple banana
```

Output:
```
Argument 1: apple
Argument 2: banana
```

---

## 4. Working with Arguments in Python

You can use command-line arguments in your programs to control different aspects of their behavior. For example, you could use arguments to specify a file to read, a number to process, or an operation to perform.

### Example Code (Processing Command-Line Arguments):

```python
import sys

# Check if correct number of arguments are passed
if len(sys.argv) != 4:
    print("Usage: python script.py <num1> <num2> <operation>")
    sys.exit()

# Get the arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]

# Perform operation based on user input
if operation == "add":
    result = num1 + num2
elif operation == "subtract":
    result = num1 - num2
elif operation == "multiply":
    result = num1 * num2
elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero")
        sys.exit()
else:
    print("Invalid operation")
    sys.exit()

# Display the result
print(f"Result: {result}")
```

In this example:
- The user is prompted to pass two numbers and an operation (add, subtract, multiply, divide).
- The script performs the operation and outputs the result.

### How to Run the Script:
```bash
python script.py 10 5 add
```

Output:
```
Result: 15.0
```

---

## 5. Using `argparse` for Advanced Argument Parsing

For more advanced use cases, Python provides the `argparse` module, which offers more flexibility and better handling of command-line arguments. It allows you to specify required arguments, optional arguments, and argument types, as well as automatically generating help messages.

### Example Code (Using `argparse`):

```python
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description="Simple calculator")

# Add arguments
parser.add_argument('num1', type=float, help="First number")
parser.add_argument('num2', type=float, help="Second number")
parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help="Operation")

# Parse arguments
args = parser.parse_args()

# Perform operation
if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "subtract":
    result = args.num1 - args.num2
elif args.operation == "multiply":
    result = args.num1 * args.num2
elif args.operation == "divide":
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        print("Error: Division by zero")
        exit()

# Display result
print(f"Result: {result}")
```

In this example:
- We use `argparse.ArgumentParser()` to create an argument parser.
- We define three arguments: `num1`, `num2`, and `operation` (which can only be one of `add`, `subtract`, `multiply`, or `divide`).
- We parse the arguments using `parser.parse_args()`, then perform the selected operation.

### How to Run the Script:
```bash
python script.py 10 5 add
```

Output:
```
Result: 15.0
```

To see the help message:
```bash
python script.py --help
```

Output:
```
usage: script.py [-h] num1 num2 {add,subtract,multiply,divide}

Simple calculator

positional arguments:
  num1           First number
  num2           Second number
  operation      Operation {add,subtract,multiply,divide}

optional arguments:
  -h, --help     show this help message and exit
```

---

## Task

1. **Create a script that takes two numbers and an operation (add, subtract, multiply, or divide) and returns the result. Use both `sys.argv` and `argparse` to implement this.**
2. **Build a Python program that accepts a file path from the command line, reads the file, and prints its contents.**

---

## Summary

- **Command-line arguments** allow you to pass values to your Python script when executing it from the terminal.
- You can access command-line arguments using `sys.argv` or use the more advanced `argparse` module for better handling.
- Command-line arguments enable dynamic behavior in your programs and make them more flexible for different use cases.

---
