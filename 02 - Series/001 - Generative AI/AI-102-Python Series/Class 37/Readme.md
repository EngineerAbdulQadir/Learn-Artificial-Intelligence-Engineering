# Python Series: Class 37 - Building a Simple Web Application

## Overview

In this class, we will learn how to build a basic web application using **Flask**, a lightweight web framework for Python. Flask allows you to build web applications quickly and with minimal overhead.

---

### What You'll Learn:
1. **Introduction to Flask**
2. **Setting up a Flask Application**
3. **Routing in Flask**
4. **Handling HTTP Methods (GET and POST)**
5. **Creating Templates with Jinja2**
6. **Running the Web Application**

---

## 1. Introduction to Flask

**Flask** is a web framework written in Python. It provides tools and libraries for building web applications. It is known for its simplicity and flexibility.

To install Flask, you can use pip:

```bash
pip install flask
```

---

## 2. Setting up a Flask Application

To set up a Flask application, create a new Python file (e.g., `app.py`) and import the Flask library:

```python
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, World!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

To run the application, simply execute the script:

```bash
python app.py
```

This will start a local web server, and you can view your application in the browser at `http://127.0.0.1:5000/`.

---

## 3. Routing in Flask

In Flask, routing allows you to map URLs to Python functions. Each route is associated with a specific view (function) that handles HTTP requests.

Example:

```python
@app.route('/about')
def about():
    return "This is the about page."
```

In this example, when the user visits `http://127.0.0.1:5000/about`, Flask will call the `about()` function.

---

## 4. Handling HTTP Methods (GET and POST)

Flask allows you to handle different HTTP methods, such as **GET** and **POST**. The **GET** method retrieves data, while **POST** is used to send data to the server.

Example of handling both GET and POST requests:

```python
from flask import request

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''
```

In this example:
- When the user visits `http://127.0.0.1:5000/submit` via GET, they see a form.
- When the form is submitted (via POST), the application responds with a personalized message.

---

## 5. Creating Templates with Jinja2

Flask uses **Jinja2** as its templating engine. It allows you to create dynamic HTML pages by embedding Python-like expressions in HTML.

Create a folder named `templates` and place an HTML file inside it (e.g., `index.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask Web App</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

In your Python code, you can render this template with dynamic data:

```python
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('index.html', name=name)
```

When you visit `http://127.0.0.1:5000/greet/John`, the page will display "Hello, John!".

---

## 6. Running the Web Application

To run the Flask application, ensure that your Python file is correct and that Flask is installed. Then, execute the script:

```bash
python app.py
```

This will launch the web server, and you can access your application in a browser.

---

## Task

1. **Create a basic web application** that takes the user's name as input and displays a personalized greeting message.
2. **Implement a form** where users can submit their favorite color, and the page will respond with a message like: "Your favorite color is Blue."
3. **Modify your web application** to use templates and create a homepage that greets users by their name.

---