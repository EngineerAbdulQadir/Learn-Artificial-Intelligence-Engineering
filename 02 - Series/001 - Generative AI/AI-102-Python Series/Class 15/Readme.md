# Python Series: Class 15 - Working with Dates and Times

## Overview

In this class, we will explore how to work with dates and times in Python using the `datetime` module. Dates and times are an important part of many applications, so understanding how to manipulate them is crucial.

---

### What You'll Learn:
1. **The `datetime` module**: How to use Python's built-in `datetime` module.
2. **Working with current date and time**: How to retrieve and manipulate the current date and time.
3. **Date formatting**: How to format dates and times into human-readable strings.
4. **Date arithmetic**: How to perform operations like adding and subtracting time.

---

## 1. Introduction to the `datetime` Module

The `datetime` module provides classes for working with dates and times. Some important classes in this module include:
- `datetime`: Combines both date and time.
- `date`: Represents just the date (year, month, day).
- `time`: Represents just the time (hour, minute, second).
- `timedelta`: Represents a difference between two dates or times.

To use the `datetime` module, you need to import it:

```python
import datetime
```

---

## 2. Getting the Current Date and Time

To get the current date and time, you can use the `datetime.now()` method.

### Example:
```python
import datetime

# Get current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)
```

### Output:
```
Current date and time: 2025-01-08 14:35:12.123456
```

You can also access the individual components of the date and time:

```python
print("Current year:", current_datetime.year)
print("Current month:", current_datetime.month)
print("Current day:", current_datetime.day)
print("Current hour:", current_datetime.hour)
print("Current minute:", current_datetime.minute)
print("Current second:", current_datetime.second)
```

---

## 3. Formatting Dates and Times

To display dates and times in a more readable or custom format, we can use the `strftime()` method, which converts a `datetime` object into a string.

### Example:
```python
# Format the current date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_datetime)
```

### Output:
```
Formatted date and time: 2025-01-08 14:35:12
```

Here are some common format codes:
- `%Y`: Year (4 digits)
- `%m`: Month (2 digits)
- `%d`: Day (2 digits)
- `%H`: Hour (24-hour format)
- `%M`: Minute
- `%S`: Second

---

## 4. Date Arithmetic

You can perform arithmetic on `datetime` objects using the `timedelta` class. A `timedelta` represents a duration, the difference between two dates or times.

### Example (Adding and Subtracting Time):
```python
from datetime import timedelta

# Get the current date and time
current_datetime = datetime.datetime.now()

# Add 7 days to the current date
new_datetime = current_datetime + timedelta(days=7)
print("Date after 7 days:", new_datetime)

# Subtract 3 hours from the current time
new_datetime = current_datetime - timedelta(hours=3)
print("Time 3 hours earlier:", new_datetime)
```

### Output:
```
Date after 7 days: 2025-01-15 14:35:12.123456
Time 3 hours earlier: 2025-01-08 11:35:12.123456
```

You can also use `timedelta` to calculate the difference between two `datetime` objects.

```python
# Calculate the difference between two dates
date1 = datetime.datetime(2025, 1, 1)
date2 = datetime.datetime.now()
difference = date2 - date1
print("Difference:", difference)
print("Days difference:", difference.days)
```

### Output:
```
Difference: 7 days, 14:35:12.123456
Days difference: 7
```

---

## Task

1. Create a Python program that asks the user for their birth date (in `YYYY-MM-DD` format).
2. Calculate the age of the user in years, months, and days.
3. Display the age in a user-friendly format (e.g., "You are 25 years, 3 months, and 15 days old").

---