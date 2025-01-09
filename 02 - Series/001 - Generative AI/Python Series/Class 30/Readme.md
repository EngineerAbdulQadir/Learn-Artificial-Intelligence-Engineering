# Python Series: Class 30 - Working with SQLAlchemy

## Overview

In this class, we will introduce **SQLAlchemy**, a powerful ORM (Object-Relational Mapping) library for Python. It allows you to interact with relational databases using Python objects, making it easier to query and manipulate data in the database.

We'll cover the basics of setting up SQLAlchemy, connecting to a database, creating tables, and performing CRUD operations (Create, Read, Update, Delete).

---

### What You'll Learn:
1. **Introduction to SQLAlchemy**
2. **Setting Up SQLAlchemy with a Database**
3. **Creating Tables with SQLAlchemy**
4. **Performing CRUD Operations**
5. **Querying the Database**

---

## 1. Introduction to SQLAlchemy

SQLAlchemy is a library that provides a set of high-level API for managing relational databases. It has two primary components:
- **SQLAlchemy ORM**: This component allows you to work with database records as Python objects.
- **SQLAlchemy Core**: A lower-level component for building queries.

In this class, we'll focus on the ORM, which allows you to define database tables as Python classes and interact with the database using those classes.

---

## 2. Setting Up SQLAlchemy with a Database

First, you need to install SQLAlchemy. You can do this using pip:

```bash
pip install sqlalchemy
```

Once installed, you can start by creating a Python file (`app.py`) and connecting to a database. SQLAlchemy supports many types of databases, including SQLite, PostgreSQL, MySQL, and others. For this example, we will use **SQLite**, which doesn't require a separate server and stores the database in a file.

### Example: Connecting to SQLite

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an SQLite database engine
engine = create_engine('sqlite:///example.db', echo=True)

# Create a base class for our class definitions
Base = declarative_base()

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
```

---

## 3. Creating Tables with SQLAlchemy

With SQLAlchemy, you can define your database tables as Python classes. Each class corresponds to a table in the database, and each attribute of the class corresponds to a column in the table.

### Example: Defining a Table

Let's define a simple `User` table with columns `id`, `name`, and `age`:

```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age})"
```

Once the `User` class is defined, we can create the table in the database by calling `Base.metadata.create_all()`:

```python
# Create all tables
Base.metadata.create_all(engine)
```

This will create the `users` table in the `example.db` SQLite database.

---

## 4. Performing CRUD Operations

With SQLAlchemy, you can easily perform CRUD operations on your database. Let’s go over how to create, read, update, and delete records.

### Create

To add a new user to the `users` table:

```python
# Create a new User
new_user = User(name='Alice', age=30)

# Add the new user to the session
session.add(new_user)

# Commit the transaction
session.commit()
```

### Read

To retrieve all users from the `users` table:

```python
# Query all users
users = session.query(User).all()

# Print all users
for user in users:
    print(user)
```

### Update

To update a user's information:

```python
# Get the user we want to update
user = session.query(User).filter_by(name='Alice').first()

# Update the user's age
user.age = 31

# Commit the transaction
session.commit()
```

### Delete

To delete a user from the `users` table:

```python
# Get the user we want to delete
user = session.query(User).filter_by(name='Alice').first()

# Delete the user
session.delete(user)

# Commit the transaction
session.commit()
```

---

## 5. Querying the Database

SQLAlchemy allows you to write complex queries using its ORM. You can filter, sort, and aggregate data easily.

### Example: Filtering Users

To filter users by age:

```python
# Query users where age is greater than 30
users = session.query(User).filter(User.age > 30).all()

for user in users:
    print(user)
```

### Example: Sorting Users

To sort users by name:

```python
# Query users and sort by name
users = session.query(User).order_by(User.name).all()

for user in users:
    print(user)
```

---

## Task

1. **Create a Flask web application** where users can submit their name and age through a form. The data should be stored in an SQLite database using SQLAlchemy.
2. **Implement CRUD operations**: Create, Read, Update, and Delete user data via the web application.

---