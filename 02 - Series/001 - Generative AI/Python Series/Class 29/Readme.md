# Python Series: Class 29 - Introduction to Flask

## Overview

In this class, we will introduce you to **Flask**, a lightweight web framework for Python that is often used for building web applications. Flask is known for its simplicity and flexibility, making it an excellent choice for small to medium-sized web projects.

We will go over how to set up a Flask application, create views, and manage routes.

---

### What You'll Learn:
1. **Introduction to Flask**
2. **Setting Up a Flask Project**
3. **Creating Views and Routes**
4. **Using Templates in Flask**
5. **Handling Forms and User Input**

---

## 1. Introduction to Flask

Flask is a micro-framework for Python that allows you to create web applications with minimal setup. Unlike Django, Flask gives you more control over your project structure, making it perfect for smaller applications.

Some of Flask's features include:

- **Routing**: Defining URL patterns and handling requests.
- **Templating**: Rendering HTML templates.
- **Request and Response Handling**: Handling user inputs and sending responses.
- **Minimalistic**: Flask doesn’t come with built-in tools like Django but allows you to add what you need.

---

## 2. Setting Up a Flask Project

First, you need to install Flask. You can do this using `pip`:

```bash
pip install flask
```

Once Flask is installed, create a new Python file (`app.py`) for your application. 

---

## 3. Creating Views and Routes

In Flask, views are created by defining Python functions, and you connect them to URLs using decorators. Flask handles incoming requests to the specified URLs and calls the corresponding view functions.

### Example: Creating a Simple Flask App

1. Create a new file called `app.py`.

2. Add the following code to `app.py` to create a basic Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

3. To run the Flask app, use the following command:

```bash
python app.py
```

4. You can now open your browser and visit `http://127.0.0.1:5000/` to see "Welcome to Flask!" displayed.

---

## 4. Using Templates in Flask

Flask uses Jinja2 as its templating engine. You can create HTML files that include dynamic content, similar to Django’s templating system.

### Example: Using a Template in Flask

1. Create a new directory called `templates`.

2. Inside `templates`, create a new file called `index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Flask</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
```

3. Modify `app.py` to render this template:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message="Hello, Flask!")

if __name__ == '__main__':
    app.run(debug=True)
```

Now, when you visit `http://127.0.0.1:5000/`, the `index.html` template will be rendered with the message "Hello, Flask!".

---

## 5. Handling Forms and User Input

Flask provides tools to handle forms and user input easily. You can use the `request` object to get data submitted by the user.

### Example: Creating a Simple Form

1. Modify `index.html` to add a form:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask Form</title>
</head>
<body>
    <form method="POST">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>

    {% if name %}
        <h2>Hello, {{ name }}!</h2>
    {% endif %}
</body>
</html>
```

2. Modify `app.py` to handle the form submission:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```

Now, when you visit `http://127.0.0.1:5000/`, you can submit a name through the form, and Flask will display a personalized greeting.

---

## Task

1. **Create a Flask web application** with a simple form that accepts a user's name and age. Upon submission, display a personalized message with their name and age.
2. **Add a second route** to your Flask app that shows a "Thank You" message when the user submits the form.

---