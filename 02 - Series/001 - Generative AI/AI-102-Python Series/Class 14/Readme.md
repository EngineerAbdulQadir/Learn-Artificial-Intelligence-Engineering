# Python Series: Class 14 - Object-Oriented Programming (OOP) - Part 2

## Overview

In this class, we will continue our exploration of Object-Oriented Programming (OOP) in Python. We will dive deeper into more advanced OOP concepts, including inheritance, polymorphism, and encapsulation.

---

### What You'll Learn:
1. **Inheritance**: How to create a new class that inherits attributes and methods from an existing class.
2. **Polymorphism**: How to use methods in different classes with the same name but different behaviors.
3. **Encapsulation**: How to restrict access to certain parts of an object and protect the integrity of the data.

---

## 1. Inheritance

Inheritance is a fundamental concept in OOP that allows one class to inherit the attributes and methods of another class. This promotes code reuse and a hierarchical structure in your classes.

### Example:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Overriding the speak method
        print(f"{self.name} barks")

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):  # Overriding the speak method
        print(f"{self.name} meows")

dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks

cat = Cat("Whiskers")
cat.speak()  # Output: Whiskers meows
```

In this example, both the `Dog` and `Cat` classes inherit from the `Animal` class. They each override the `speak` method to provide specific behavior.

---

## 2. Polymorphism

Polymorphism allows us to use the same method name in different classes, but the method can behave differently depending on which class it is used in. This is possible because of method overriding (shown in the inheritance example).

### Example:
```python
class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps")

bird = Bird("Parrot")
bird.speak()  # Output: Parrot chirps
```

Here, `Bird` also inherits from `Animal` but overrides the `speak` method to print a different message. Despite using the same method name `speak`, the behavior changes depending on the class.

---

## 3. Encapsulation

Encapsulation is the practice of restricting access to certain parts of an object's attributes or methods to protect the integrity of the data. This is typically done by using private and public access modifiers.

- **Public Attributes**: Can be accessed and modified directly.
- **Private Attributes**: Cannot be accessed or modified directly. These are typically used for internal data that should not be exposed.

In Python, we can make attributes private by prefixing them with two underscores `__`.

### Example:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(200)
print(account.get_balance())  # Output: 1300

# The following will result in an error because __balance is private
# print(account.__balance)
```

In this example, the `BankAccount` class uses encapsulation by making the `__balance` attribute private. You can interact with it only through the public methods `deposit`, `withdraw`, and `get_balance`.

---

## Task

1. Create a class called `Vehicle` with the following attributes:
    - `make` (string)
    - `model` (string)
    - `year` (integer)
2. Create two subclasses:
    - `Car` (inherits from `Vehicle`) with an additional attribute `doors` (integer).
    - `Truck` (inherits from `Vehicle`) with an additional attribute `cargo_capacity` (float).
3. Each subclass should override a `description()` method to return a string that describes the vehicle.
4. Create instances of `Car` and `Truck`, and call the `description()` method for both.

---