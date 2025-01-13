# Python Series: Class 20 - Working with APIs

## Overview

In this class, we will explore **APIs (Application Programming Interfaces)** and how to interact with them using Python. APIs allow different software systems to communicate with each other, and in Python, you can make HTTP requests to work with APIs and retrieve data.

---

### What You'll Learn:
1. **What is an API?**
2. **How to Make HTTP Requests in Python**
3. **Working with JSON Data**
4. **Handling API Responses**
5. **Using Python Libraries for API Requests**

---

## 1. What is an API?

An **API** is a set of rules that allows one program to interact with another. APIs can be used to retrieve data, send data, or even perform certain operations on remote systems.

APIs typically provide endpoints to interact with, such as:

- GET: Retrieve data.
- POST: Send data.
- PUT: Update data.
- DELETE: Remove data.

In Python, you can interact with APIs by making HTTP requests using libraries like `requests`.

---

## 2. How to Make HTTP Requests in Python

To interact with an API, you must send an **HTTP request**. The most common types of HTTP requests are:

- **GET**: To retrieve data.
- **POST**: To send data.
- **PUT**: To update existing data.
- **DELETE**: To delete data.

The `requests` library in Python allows you to easily make these requests.

### Installing the Requests Library:
```bash
pip install requests
```

### Making a GET Request:
```python
import requests

# Example of a GET request to fetch data
response = requests.get('https://api.example.com/data')

# Checking the status code of the response
print(response.status_code)  # 200 means successful

# Printing the response content
print(response.json())  # Assuming the API returns JSON data
```

---

## 3. Working with JSON Data

APIs often return data in **JSON** (JavaScript Object Notation) format. You can parse JSON data in Python using the `json()` method from the `requests` library.

### Example:
```python
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()

print(data)
```

The output might look like this:
```python
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
}
```

You can then access specific parts of the data:

```python
title = data["title"]
print(title)  # Output: delectus aut autem
```

---

## 4. Handling API Responses

Once you make an API request, it's important to handle the response properly. Always check the response's status code to ensure the request was successful. Some common status codes include:

- **200**: OK - The request was successful.
- **404**: Not Found - The requested resource could not be found.
- **500**: Internal Server Error - There is an error on the server side.

You can also handle errors with `try-except` blocks.

### Example:
```python
try:
    response = requests.get('https://api.example.com/data')
    response.raise_for_status()  # Raises an error for 4xx/5xx status codes
    data = response.json()
    print(data)
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
```

---

## 5. Using Python Libraries for API Requests

Apart from the `requests` library, there are other libraries and tools you can use to interact with APIs, such as:

- **urllib**: A standard Python library for handling URLs and HTTP requests.
- **http.client**: A low-level HTTP client library.

However, `requests` is the most popular and easiest-to-use library for API interactions.

---

## Task

1. Use the `requests` library to fetch data from a public API (e.g., [JSONPlaceholder](https://jsonplaceholder.typicode.com/)).
2. Extract and display the title of the first todo item from the API response.
3. Write a Python script that fetches the current weather data from a weather API (like OpenWeatherMap) and prints the temperature.

---