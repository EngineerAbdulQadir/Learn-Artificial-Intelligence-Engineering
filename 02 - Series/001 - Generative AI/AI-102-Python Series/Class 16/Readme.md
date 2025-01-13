# Python Series: Class 16 - Regular Expressions

## Overview

In this class, we will dive into Regular Expressions (regex) in Python. Regular expressions are powerful tools for pattern matching in strings, which allow you to search, match, and manipulate text in a highly efficient way.

---

### What You'll Learn:
1. **What is a Regular Expression**: Understanding the basic concept.
2. **Using Python's `re` module**: How to use Python's built-in `re` module to work with regex.
3. **Common regex patterns**: Learning the most common regex symbols and their usage.
4. **Practical applications**: How to use regex for real-world text processing.

---

## 1. Introduction to Regular Expressions

A regular expression (regex) is a sequence of characters that forms a search pattern. It can be used for:
- Searching for specific patterns in text.
- Replacing parts of a string.
- Splitting strings based on a pattern.

In Python, the `re` module provides a powerful suite of functions to work with regex.

### Example:
```python
import re

# Search for the pattern "hello" in a string
text = "Hello, how are you?"
pattern = "hello"
match = re.search(pattern, text, re.IGNORECASE)  # Ignore case

if match:
    print("Pattern found!")
else:
    print("Pattern not found.")
```

---

## 2. Commonly Used Regex Patterns

Here are some common regex patterns and their meanings:

- `\d`: Matches any digit (0-9).
- `\D`: Matches any non-digit character.
- `\w`: Matches any word character (alphanumeric + underscore).
- `\W`: Matches any non-word character.
- `\s`: Matches any whitespace character (space, tab, newline).
- `\S`: Matches any non-whitespace character.
- `.`: Matches any character except a newline.
- `^`: Matches the start of a string.
- `$`: Matches the end of a string.
- `*`: Matches 0 or more repetitions of the preceding pattern.
- `+`: Matches 1 or more repetitions of the preceding pattern.
- `?`: Matches 0 or 1 repetition of the preceding pattern.
- `{m,n}`: Matches between m and n repetitions of the preceding pattern.

### Example:
```python
# Find all digits in the text
text = "I have 3 apples and 5 oranges."
pattern = r"\d+"  # Match one or more digits
matches = re.findall(pattern, text)
print(matches)
```

### Output:
```
['3', '5']
```

---

## 3. Using `re.match()`, `re.search()`, and `re.findall()`

- `re.match()`: Matches a pattern only at the start of a string.
- `re.search()`: Scans through a string, looking for any location where the pattern matches.
- `re.findall()`: Returns all non-overlapping matches of the pattern in the string.

### Examples:
```python
# Using re.match() to check if a string starts with a pattern
pattern = r"hello"
match = re.match(pattern, "hello world")
if match:
    print("Match found!")
else:
    print("No match.")
```

```python
# Using re.findall() to find all matches in the text
matches = re.findall(r"\d+", "The numbers are 12, 34, and 56.")
print(matches)  # Output: ['12', '34', '56']
```

---

## 4. Using `re.sub()` to Replace Text

You can use the `re.sub()` function to replace parts of a string that match a pattern.

### Example:
```python
# Replace all digits in a string with a "#" symbol
text = "My number is 12345."
result = re.sub(r"\d", "#", text)
print(result)
```

### Output:
```
My number is #####.
```

---

## 5. Practical Application: Email Validation

One common use of regex is to validate email addresses. Here's an example of how to use regex to check if an email address is valid.

### Example:
```python
# Email validation regex pattern
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email = input("Enter your email address: ")

if re.match(email_pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")
```

---

## Task

1. Write a Python program that uses regular expressions to find all the words (sequences of letters) in a given text.
2. Modify the program to count how many words contain at least one vowel (a, e, i, o, u).

---