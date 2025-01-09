# Python Series: Class 24 - Working with JSON Data

## Overview

In this class, we will explore how to work with **JSON (JavaScript Object Notation)** data in Python. JSON is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is widely used in APIs, configuration files, and data storage.

---

### What You'll Learn:
1. **What is JSON?**
2. **How to Parse JSON in Python**
3. **Working with JSON Data (Loading and Dumping)**
4. **Converting Python Objects to JSON**
5. **Handling JSON Files**

---

## 1. What is JSON?

JSON (JavaScript Object Notation) is a text-based format used for representing structured data. It is a lightweight, language-independent data format that is easy for both humans and machines to understand. JSON data consists of key-value pairs, similar to Python dictionaries.

### Example of JSON:

```json
{
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
```

---

## 2. How to Parse JSON in Python

Python provides a built-in module called `json` to work with JSON data. You can use the `json` module to parse JSON into Python dictionaries and vice versa.

### Parsing JSON into Python Objects:

Use `json.loads()` to convert a JSON string into a Python dictionary.

```python
import json

# Sample JSON data
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Parse JSON into a Python dictionary
data = json.loads(json_data)

print(data)
```

**Output:**

```python
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

---

## 3. Working with JSON Data (Loading and Dumping)

- **`json.loads()`**: Converts a JSON string into a Python dictionary.
- **`json.dumps()`**: Converts a Python dictionary into a JSON string.

### Converting Python Objects to JSON:

```python
import json

# Sample Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON string
json_string = json.dumps(data, indent=4)

print(json_string)
```

**Output:**

```json
{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
```

---

## 4. Converting Python Objects to JSON

You can also specify additional options when converting Python objects to JSON, such as:

- **`indent`**: Adds indentation to make the JSON output more readable.
- **`sort_keys`**: Sorts the keys in the resulting JSON string.
- **`separators`**: Controls the separators between items.

### Example:

```python
json_string = json.dumps(data, indent=2, sort_keys=True)
print(json_string)
```

**Output:**

```json
{
  "age": 30,
  "city": "New York",
  "name": "John Doe"
}
```

---

## 5. Handling JSON Files

Python's `json` module also allows you to read and write JSON data to files using `json.load()` and `json.dump()`.

### Reading JSON from a File:

```python
import json

# Open the JSON file and load its contents
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
```

### Writing JSON to a File:

```python
import json

data = {
    "name": "Jane Doe",
    "age": 25,
    "city": "San Francisco"
}

# Write JSON to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

---

## Task

1. Write a Python program that:
    - Loads JSON data from a string (or file).
    - Modifies the JSON data (e.g., changes the name).
    - Converts the modified data back to a JSON string.
    - Saves the modified JSON data to a file.

2. Create a Python function that accepts a JSON string representing a list of items and returns the total number of items.

---

This concludes **Class 24**! Let me know when you're ready for **Class 25**. 😊