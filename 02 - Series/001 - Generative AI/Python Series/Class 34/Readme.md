# Python Series: Class 34 - Working with Excel Files (openpyxl)

## Overview

In this class, we will explore how to work with **Excel files** in Python using the **openpyxl** library. Excel files are widely used for data storage, and being able to manipulate them programmatically is a valuable skill. We will cover reading from and writing to Excel files and performing basic operations with Excel sheets.

---

### What You'll Learn:
1. **Introduction to openpyxl**
2. **Reading Data from Excel**
3. **Writing Data to Excel**
4. **Modifying Excel Files**
5. **Saving Excel Files**

---

## 1. Introduction to openpyxl

**openpyxl** is a Python library for reading and writing Excel (xlsx) files. It allows you to interact with Excel files without needing Excel installed on your machine.

To install `openpyxl`, you can run:

```bash
pip install openpyxl
```

### Importing openpyxl

```python
import openpyxl
```

---

## 2. Reading Data from Excel

To read data from an existing Excel file, we need to open the file and access the sheets.

```python
import openpyxl

# Load an existing Excel file
workbook = openpyxl.load_workbook('example.xlsx')

# Select the active sheet (the first sheet in the workbook)
sheet = workbook.active

# Access specific cell
value = sheet['A1'].value
print(value)
```

### Iterating Over Rows and Columns

```python
import openpyxl

# Load the workbook and sheet
workbook = openpyxl.load_workbook('example.xlsx')
sheet = workbook.active

# Iterate over rows
for row in sheet.iter_rows(min_row=2, max_row=5, min_col=1, max_col=3):
    for cell in row:
        print(cell.value)
```

---

## 3. Writing Data to Excel

You can also write data to an Excel file by assigning values to cells.

```python
import openpyxl

# Load the workbook (create a new one if not exists)
workbook = openpyxl.Workbook()

# Select the active sheet
sheet = workbook.active

# Write to a specific cell
sheet['A1'] = "Hello, Excel!"

# Save the workbook
workbook.save('new_file.xlsx')
```

---

## 4. Modifying Excel Files

You can modify existing data in Excel files.

```python
import openpyxl

# Load an existing workbook
workbook = openpyxl.load_workbook('example.xlsx')

# Select the active sheet
sheet = workbook.active

# Modify the value of a cell
sheet['A1'] = 'Updated Value'

# Save the modified file
workbook.save('example_modified.xlsx')
```

---

## 5. Saving Excel Files

You can save the modified or new Excel files under a different name.

```python
import openpyxl

# Create a new workbook
workbook = openpyxl.Workbook()

# Save the workbook to a specific file
workbook.save('new_workbook.xlsx')
```

---

## Task

1. **Create a new Excel file** and add some sample data (names, ages, etc.) to multiple cells.
2. **Read the data** from the Excel file you just created.
3. **Modify a cell** and save the modified file.
4. **Write some new data** to another sheet in the same Excel file.
5. **Iterate through rows** to extract data from the file.

---