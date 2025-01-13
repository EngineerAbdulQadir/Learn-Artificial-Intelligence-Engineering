# Python Series: Class 31 - Introduction to Pandas

## Overview

In this class, we will explore **Pandas**, one of the most powerful and widely used libraries in Python for data manipulation and analysis. Pandas provides high-performance data structures like **DataFrames** and **Series**, which allow you to easily handle, manipulate, and analyze data in Python.

We will cover the basics of using Pandas for reading, manipulating, and analyzing structured data.

---

### What You'll Learn:
1. **Introduction to Pandas**
2. **Creating DataFrames and Series**
3. **Reading Data from Different Formats (CSV, Excel, SQL)**
4. **Basic DataFrame Operations**
5. **Data Cleaning and Transformation**

---

## 1. Introduction to Pandas

Pandas is a library that provides easy-to-use data structures and data analysis tools. It is built on top of NumPy and is often used for:
- Working with **structured data** (e.g., tabular data).
- Data **cleaning and manipulation**.
- Performing data **aggregation** and **grouping**.
- **Time series** analysis.
- **Merging** and **joining** datasets.

Pandas primarily uses two data structures:
- **Series**: A one-dimensional array.
- **DataFrame**: A two-dimensional table (similar to a spreadsheet).

To install Pandas, you can run:

```bash
pip install pandas
```

---

## 2. Creating DataFrames and Series

### Series

A **Series** is essentially a column in a DataFrame. It can be created from a list, NumPy array, or dictionary.

#### Example: Creating a Series

```python
import pandas as pd

# Creating a Series from a list
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)
```

Output:
```
0    1
1    2
2    3
3    4
4    5
dtype: int64
```

### DataFrame

A **DataFrame** is a two-dimensional table, which is the most commonly used data structure in Pandas.

#### Example: Creating a DataFrame

```python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print(df)
```

Output:
```
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   40      Houston
```

---

## 3. Reading Data from Different Formats

Pandas allows you to read data from various formats, such as CSV, Excel, and SQL databases.

### Reading a CSV File

```python
df = pd.read_csv('data.csv')
print(df)
```

### Reading an Excel File

```python
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print(df)
```

### Reading from a SQL Database

```python
import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('database.db')

# Read data from a SQL query
df = pd.read_sql('SELECT * FROM users', conn)
print(df)
```

---

## 4. Basic DataFrame Operations

You can perform various operations on DataFrames, such as selecting columns, filtering rows, and summarizing data.

### Selecting Columns

```python
# Select a single column
ages = df['Age']
print(ages)

# Select multiple columns
name_city = df[['Name', 'City']]
print(name_city)
```

### Filtering Rows

```python
# Filter rows based on a condition
young_users = df[df['Age'] < 30]
print(young_users)
```

### Summarizing Data

```python
# Get basic statistics for numeric columns
print(df.describe())

# Get the number of unique values in each column
print(df.nunique())
```

---

## 5. Data Cleaning and Transformation

Data cleaning involves handling missing values, transforming data types, and performing operations like grouping.

### Handling Missing Values

```python
# Check for missing values
print(df.isnull())

# Fill missing values with a specified value
df.fillna(0, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)
```

### Changing Data Types

```python
# Convert a column to a different data type
df['Age'] = df['Age'].astype(float)
```

### Grouping Data

```python
# Group data by a column and calculate the mean of each group
grouped = df.groupby('City')['Age'].mean()
print(grouped)
```

---

## Task

1. **Load a CSV file into a Pandas DataFrame** and display the first few rows using `df.head()`.
2. **Clean the data** by filling missing values with appropriate values (e.g., 0 or the mean).
3. **Group the data by a specific column** (e.g., `City`) and calculate the average of another column (e.g., `Age`).

---