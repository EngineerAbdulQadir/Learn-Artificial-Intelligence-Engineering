# Python Series: Class 25 - Multithreading in Python

## Overview

In this class, we will explore the concept of **multithreading** in Python. Multithreading allows a program to run multiple threads concurrently, improving performance in certain tasks, especially I/O-bound tasks like file operations, network communication, and database queries. 

We'll learn how to create and manage threads, and how to avoid common pitfalls like race conditions.

---

### What You'll Learn:
1. **What is Multithreading?**
2. **Creating Threads in Python**
3. **Thread Synchronization**
4. **Threading and Performance**

---

## 1. What is Multithreading?

**Multithreading** is a technique in which multiple threads execute independently but share the same resources. Threads are smaller units of a process, and they run concurrently, allowing you to perform multiple tasks simultaneously.

In Python, the `threading` module provides a way to work with threads.

---

## 2. Creating Threads in Python

You can create a new thread in Python using the `threading` module. To create a thread, you define a function that you want the thread to execute, and then create a thread object using the `threading.Thread()` class.

### Example: Creating a Simple Thread

```python
import threading
import time

# Function to be executed by the thread
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Thread execution complete.")
```

### Output:

```
1
2
3
4
5
Thread execution complete.
```

Here, the `print_numbers` function runs in a separate thread, while the main program waits for the thread to finish using `join()`.

---

## 3. Thread Synchronization

When multiple threads access shared resources, there is a risk of data corruption due to **race conditions**. To avoid this, we can use **locks** to ensure that only one thread accesses the resource at a time.

### Example: Using a Lock for Synchronization

```python
import threading

# Shared resource
counter = 0
lock = threading.Lock()

# Function that updates the counter
def update_counter():
    global counter
    with lock:
        temp = counter
        temp += 1
        counter = temp

# Create multiple threads
threads = []
for _ in range(100):
    thread = threading.Thread(target=update_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Counter:", counter)
```

Here, the lock ensures that only one thread can access and update the counter at a time, preventing race conditions.

---

## 4. Threading and Performance

While multithreading can speed up I/O-bound tasks, Python’s **Global Interpreter Lock (GIL)** prevents multiple threads from executing Python bytecodes at once in CPU-bound tasks. This means that for CPU-intensive tasks, Python may not see a performance improvement with multithreading.

However, for I/O-bound tasks like reading from a file or making network requests, multithreading can significantly improve performance by running multiple tasks concurrently.

---

## Task

1. Write a Python program using multiple threads to:
    - Download multiple web pages concurrently (you can use the `requests` library for this).
    - Print the status of each request once it is completed.
    - Use threading to handle multiple requests concurrently.
    
2. Create a multithreaded Python program that simulates a banking system where multiple customers (threads) access the same account balance and make deposits concurrently. Ensure thread safety using locks.

---