# Python Series: Class 22 - Python and Databases

## Overview

In this class, we will learn how to interact with **databases** using **Python**. Databases are essential for storing and managing data in applications. We'll focus on **SQLite**, a lightweight, file-based database that comes built into Python, and cover basic operations like creating, reading, updating, and deleting data (CRUD operations).

---

### What You'll Learn:
1. **Introduction to Databases and SQLite**
2. **Setting Up SQLite in Python**
3. **CRUD Operations with SQLite**
4. **Connecting to a Database**
5. **Executing Queries**

---

## 1. Introduction to Databases and SQLite

A **database** is a collection of data that is stored and managed systematically. There are different types of databases, such as:

- **Relational Databases**: Store data in tables with rows and columns (e.g., MySQL, PostgreSQL, SQLite).
- **NoSQL Databases**: Store data in a more flexible, document-oriented format (e.g., MongoDB).

For this class, we will work with **SQLite**, which is a **relational database**. SQLite is built into Python, so there is no need for separate installation or setup. It stores data in a single file and is commonly used in small-scale applications and for learning purposes.

---

## 2. Setting Up SQLite in Python

SQLite comes with the `sqlite3` module, which allows Python to interact with SQLite databases. You don’t need to install anything extra if you're using Python's standard library.

To interact with SQLite, you need to:

- Connect to the database file.
- Create a cursor object to execute SQL queries.
- Perform CRUD operations using SQL statements.

### Example of Importing SQLite:

```python
import sqlite3
```

---

## 3. CRUD Operations with SQLite

The basic CRUD operations allow you to:

1. **Create** data (Insert).
2. **Read** data (Select).
3. **Update** data.
4. **Delete** data.

### Create: Inserting Data into a Table

Here’s how to create a table and insert data:

```python
import sqlite3

# Connect to a database (creates a new file if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object
cursor = connection.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
```

- **`CREATE TABLE IF NOT EXISTS`**: Creates the table only if it doesn’t already exist.
- **`INSERT INTO`**: Inserts data into the table. The `?` is a placeholder for parameterized queries to avoid SQL injection.

### Read: Fetching Data from a Table

To fetch data, you can use `SELECT` statements:

```python
# Reconnect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Fetch all rows from the users table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the connection
connection.close()
```

- **`SELECT * FROM users`**: Retrieves all columns from the `users` table.
- **`fetchall()`**: Retrieves all rows of the query result.

### Update: Modifying Data

To update data, use the `UPDATE` statement:

```python
# Reconnect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Update a user's information
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, 'Alice'))

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
```

- **`UPDATE`**: Modifies existing data in the table.

### Delete: Removing Data

To delete data, use the `DELETE` statement:

```python
# Reconnect to the database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Delete a user
cursor.execute("DELETE FROM users WHERE name = ?", ('Alice',))

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
```

- **`DELETE`**: Removes data from the table.

---

## 4. Connecting to a Database

You can connect to a database by using `sqlite3.connect('database_name.db')`. If the database file does not exist, SQLite will create it.

---

## 5. Executing Queries

You can execute any SQL query using the `cursor.execute()` method. For example:

- **Creating Tables**: `cursor.execute("CREATE TABLE ...")`
- **Inserting Data**: `cursor.execute("INSERT INTO ...")`
- **Reading Data**: `cursor.execute("SELECT ...")`
- **Updating Data**: `cursor.execute("UPDATE ...")`
- **Deleting Data**: `cursor.execute("DELETE FROM ...")`

You can also use **parameterized queries** to safely pass values into your SQL statements, which helps protect against SQL injection attacks.

---

## Task

1. Create a database named `store.db`.
2. Create a table `products` with the columns: `id`, `name`, `price`, and `quantity`.
3. Insert at least 3 products into the `products` table.
4. Fetch and print all products from the `products` table.
5. Update the price of one product and print the updated list of products.
6. Delete a product from the table and print the remaining products.

---