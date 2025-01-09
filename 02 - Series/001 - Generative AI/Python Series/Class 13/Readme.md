# Python Series: Class 13 - Object-Oriented Programming (OOP) - Part 1

## Overview

In this class, we will introduce the concept of Object-Oriented Programming (OOP) in Python. OOP is a programming paradigm based on the concept of "objects," which are instances of classes. We will cover the basics of classes and objects, including how to define classes, create objects, and understand the principles of OOP.

---

### What You'll Learn:
1. **Introduction to Object-Oriented Programming (OOP)**: Understanding the basics of OOP.
2. **Defining Classes**: How to define classes in Python.
3. **Creating Objects**: How to create instances (objects) from a class.
4. **Instance Variables and Methods**: How to use instance variables and methods in classes.
5. **The `__init__` Method**: Understanding the constructor in Python classes.

---

## 1. Introduction to Object-Oriented Programming (OOP)

Object-Oriented Programming is a paradigm that organizes software design around data, or objects, rather than functions and logic. Each object can hold both data and methods (functions) that manipulate the data.

The core concepts of OOP are:
- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.
- **Attributes**: Variables that store data within an object.
- **Methods**: Functions that belong to a class and can manipulate the attributes.

---

## 2. Defining Classes

In Python, a class is defined using the `class` keyword. A class typically contains methods that define the behavior of objects created from the class.

### Example:
```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def bark(self):  # Method
        print(f"{self.name} says Woof!")
```

In this example, `Dog` is a class that has an `__init__` method (constructor) to initialize the `name` and `age` attributes. The `bark` method defines behavior for objects of the `Dog` class.

---

## 3. Creating Objects

Once a class is defined, you can create objects (instances) of that class by calling the class like a function.

### Example:
```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 5

dog1.bark()  # Output: Buddy says Woof!
```

Here, `dog1` and `dog2` are objects (instances) of the `Dog` class. Each object has its own attributes and methods.

---

## 4. Instance Variables and Methods

- **Instance Variables**: These are variables that are specific to each object and hold the state or data of the object. They are defined in the `__init__` method using `self`.
- **Methods**: These are functions that belong to the class and define the behavior of the object. Methods take `self` as the first parameter, which refers to the instance of the object.

### Example:
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make  # Instance variable
        self.model = model  # Instance variable
        self.year = year  # Instance variable

    def start_engine(self):  # Method
        print(f"The {self.year} {self.make} {self.model}'s engine has started.")

car1 = Car("Toyota", "Corolla", 2022)
car1.start_engine()  # Output: The 2022 Toyota Corolla's engine has started.
```

---

## 5. The `__init__` Method

The `__init__` method is a special method in Python classes. It is automatically called when a new object is created from the class, allowing you to initialize the object's attributes.

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def greet(self):  # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

The `__init__` method takes the parameters `name` and `age` and initializes the instance variables `self.name` and `self.age`.

---

## Task

1. Create a class called `Student` with the following attributes:
    - `name` (string)
    - `age` (integer)
    - `grade` (string)
2. Add a method `introduce()` to the class that prints the following:
   - "Hello, my name is [name], I am [age] years old and my grade is [grade]."
3. Create an object of the `Student` class and call the `introduce()` method.

---