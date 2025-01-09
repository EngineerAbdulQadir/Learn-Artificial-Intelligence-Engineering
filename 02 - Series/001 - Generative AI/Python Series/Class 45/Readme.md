# Python Series: Class 45 - Introduction to Web Development with Python

## Overview

In this class, we will learn how to build a basic web application using Python. Python offers several libraries and frameworks for web development, with **Flask** being one of the most popular and lightweight frameworks for creating web applications quickly and easily.

We will cover the basics of Flask, how to set up a simple web server, handle routes, and create dynamic content.

---

### What You'll Learn:
1. **Introduction to Web Development**
2. **Installing Flask**
3. **Setting Up a Basic Web Application**
4. **Handling Routes and Views**
5. **Rendering HTML Templates**
6. **Handling Forms in Flask**

---

## 1. Introduction to Web Development

Web development involves creating web applications that users can access through a browser. These applications typically consist of:
- **Frontend:** The user interface (UI), built using HTML, CSS, and JavaScript.
- **Backend:** The server-side logic that processes user requests and sends back responses, often built with programming languages like Python, Ruby, or JavaScript.

Python is an excellent choice for backend development, and frameworks like Flask make it easy to build simple and scalable web applications.

---

## 2. Installing Flask

Flask is a lightweight Python web framework. To get started, you need to install it using **pip**, Python's package installer.

### Steps to Install Flask:

1. Open a terminal or command prompt.
2. Install Flask using pip:
   ```bash
   pip install flask
   ```

---

## 3. Setting Up a Basic Web Application

Now that Flask is installed, let's create a basic web application.

### Example Code (Basic Flask Web Application):

```python
from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# Define a route and the corresponding view function
@app.route('/')
def home():
    return "Hello, World!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### How It Works:
- We create an instance of the Flask class: `app = Flask(__name__)`.
- We define a route using the `@app.route()` decorator. The route `/` refers to the homepage of the web application.
- The function `home()` is executed when the user accesses the homepage, and it returns a simple "Hello, World!" message.
- Finally, `app.run(debug=True)` starts the development server with debugging enabled.

### How to Run the Application:
1. Save the code to a file named `app.py`.
2. Run the application:
   ```bash
   python app.py
   ```
3. Open a web browser and go to `http://127.0.0.1:5000/` to see the message "Hello, World!" displayed.

---

## 4. Handling Routes and Views

In Flask, a **route** is a URL pattern that a user can visit, and a **view** is the function that handles the request for that route. You can add more routes to handle different pages of your application.

### Example Code (Multiple Routes):

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "This is the About Page."

@app.route('/contact')
def contact():
    return "Contact us at contact@example.com."

if __name__ == '__main__':
    app.run(debug=True)
```

### How It Works:
- The `/about` route displays the About Page.
- The `/contact` route shows the Contact Page.
- You can add as many routes as you like to your application.

### How to Run the Application:
1. Save the code to a file named `app.py`.
2. Run the application:
   ```bash
   python app.py
   ```
3. Open a browser and visit:
   - `http://127.0.0.1:5000/` for the Home Page.
   - `http://127.0.0.1:5000/about` for the About Page.
   - `http://127.0.0.1:5000/contact` for the Contact Page.

---

## 5. Rendering HTML Templates

While returning plain text like "Hello, World!" works for simple examples, most web applications use HTML to create a user interface. Flask allows you to render HTML templates dynamically using the **Jinja2** templating engine.

### Steps to Render an HTML Template:
1. Create a folder named `templates` in your project directory.
2. Inside the `templates` folder, create an HTML file (e.g., `home.html`).

### Example Code (Rendering Templates):

**app.py (Python Code):**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="Home Page")

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/home.html (HTML Template):**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to the {{ title }}!</h1>
    <p>This is a simple web application built with Flask.</p>
</body>
</html>
```

### How It Works:
- The `render_template()` function renders the HTML file (`home.html`) and passes the `title` variable to the template.
- Inside the `home.html` template, `{{ title }}` is replaced with the actual value passed from the Python code.

### How to Run the Application:
1. Save the Python code to `app.py`.
2. Create a folder named `templates` and save the HTML file as `home.html` inside it.
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Visit `http://127.0.0.1:5000/` to see the rendered HTML page.

---

## 6. Handling Forms in Flask

Web applications often need to handle user input through forms. Flask provides an easy way to handle form data using the `request` object.

### Example Code (Handling Forms):

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/form.html (HTML Form):**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h1>Enter Your Name</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Your Name">
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### How It Works:
- The form on the webpage allows the user to input their name.
- When the form is submitted (via POST), the name entered by the user is sent to the server, and the server responds with a greeting message.

### How to Run the Application:
1. Save the Python code to `app.py`.
2. Create the `templates/form.html` file with the form code.
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Visit `http://127.0.0.1:5000/` to submit the form and see the response.

---

## Summary

In this class, you learned the basics of web development with Python using the **Flask** framework. We covered how to:
1. Set up a basic Flask application.
2. Handle different routes and views.
3. Render dynamic HTML templates with Jinja2.
4. Process user input through forms.

---