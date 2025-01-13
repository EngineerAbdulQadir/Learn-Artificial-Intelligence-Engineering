# Python Series: Class 36 - Working with CSV Files

## Overview

In this class, we will learn how to read from and write to **CSV (Comma Separated Values)** files in Python. CSV files are commonly used to store data in tabular form, and Python provides built-in functionality to handle them using the `csv` module.

---

### What You'll Learn:
1. **Introduction to CSV Files**
2. **Reading CSV Files**
3. **Writing to CSV Files**
4. **Handling CSV Files with Pandas**

---

## 1. Introduction to CSV Files

**CSV (Comma Separated Values)** is a simple file format that stores data in tabular form. Each row in the file corresponds to a data record, and each field within that row is separated by a comma.

Example of a CSV file:

```
Name, Age, City
John, 28, New York
Jane, 22, Los Angeles
Sam, 35, Chicago
```

---

## 2. Reading CSV Files

Python provides the `csv` module to read and write CSV files. Here's how you can read data from a CSV file:

```python
import csv

# Open the CSV file
with open('data.csv', mode='r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    
    # Skip the header
    next(csv_reader)
    
    # Read each row
    for row in csv_reader:
        print(row)
```

---

## 3. Writing to CSV Files

You can also write data to a CSV file using Python's `csv` module:

```python
import csv

# Data to write to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 28, 'New York'],
    ['Jane', 22, 'Los Angeles'],
    ['Sam', 35, 'Chicago']
]

# Open the CSV file in write mode
with open('output.csv', mode='w', newline='') as file:
    # Create a CSV writer
    csv_writer = csv.writer(file)
    
    # Write the rows to the CSV file
    csv_writer.writerows(data)
```

---

## 4. Handling CSV Files with Pandas

For more advanced operations, such as data manipulation and analysis, the **Pandas** library is commonly used. Pandas provides a more powerful and flexible way to read and write CSV files.

### Reading CSV with Pandas:

```python
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the contents of the CSV file
print(df)
```

### Writing CSV with Pandas:

```python
import pandas as pd

# Data to write to CSV
data = {'Name': ['John', 'Jane', 'Sam'], 'Age': [28, 22, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('output.csv', index=False)
```

---

## Task

1. **Create a CSV file** containing the details of your favorite books, including columns like Title, Author, and Year.
2. **Read the CSV file** and print each row to the console.
3. **Write a new CSV file** with a list of your favorite movies, including Title, Director, and Release Year.
4. Use **Pandas** to load a CSV file into a DataFrame, then filter the data based on a specific condition (e.g., books published after 2010).

---