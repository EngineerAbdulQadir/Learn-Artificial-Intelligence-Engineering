# Python Series: Class 10 - File Handling

## Overview

In this class, we will cover how to work with files in Python. File handling is a crucial skill that allows you to read from and write to files, which is essential for many applications, such as data analysis, logging, and configuration management.

---

### What You'll Learn:
1. **Opening Files**: Using Python's built-in `open()` function to open files in different modes.
2. **Reading Files**: Reading file content using various methods.
3. **Writing Files**: Writing content to files, both by overwriting and appending.
4. **File Closing**: Closing files to ensure proper file handling and resource management.

---

## 1. Opening Files

In Python, you can open a file using the built-in `open()` function. The `open()` function requires two arguments:
- **File path**: The location of the file (can be relative or absolute).
- **Mode**: The mode in which the file should be opened. Common modes include:
  - `'r'`: Read mode (default).
  - `'w'`: Write mode (overwrites the file).
  - `'a'`: Append mode (adds content to the end of the file).
  - `'b'`: Binary mode (for non-text files).

```python
# Open a file in read mode
file = open('example.txt', 'r')

# Open a file in write mode
file = open('output.txt', 'w')

# Open a file in append mode
file = open('log.txt', 'a')
```

---

## 2. Reading Files

You can read files using several methods, depending on how you want to handle the file content.

### Reading the Entire File:
```python
# Open file in read mode
file = open('example.txt', 'r')

# Read the entire content of the file
content = file.read()
print(content)

# Close the file
file.close()
```

### Reading Line by Line:
```python
file = open('example.txt', 'r')

# Read one line at a time
line = file.readline()
print(line)  # Output: First line of the file

# Read all lines as a list of strings
lines = file.readlines()
print(lines)  # Output: ['First line of the file\n', 'Second line of the file\n']

file.close()
```

---

## 3. Writing to Files

You can write to files by opening them in write (`'w'`) or append (`'a'`) mode.

### Writing Data:
```python
# Open file in write mode (overwrites the file)
file = open('output.txt', 'w')
file.write("This is a new line in the file.\n")
file.write("Here's another line.\n")
file.close()
```

### Appending Data:
```python
# Open file in append mode (adds to the end of the file)
file = open('output.txt', 'a')
file.write("This is an appended line.\n")
file.close()
```

---

## 4. Closing Files

It is important to close the file after reading or writing to ensure that the file is properly saved and that system resources are released.

```python
file = open('example.txt', 'r')
content = file.read()
file.close()  # Always close the file after use
```

Alternatively, you can use the `with` statement, which automatically closes the file after the block is executed:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to call file.close(), it is done automatically
```

---

## Task

Write a Python program that:
1. Creates a new file called `example.txt` and writes the following lines:
   - "Hello, Python!"
   - "This is your first file handling task."
   - "Enjoy learning Python!"
2. Open the `example.txt` file and read its contents.
3. Append a new line, "Appended text.", to the `example.txt` file.
4. Print the contents of the file to verify the changes.

Save the program as `file_handling.py` and run it.

---