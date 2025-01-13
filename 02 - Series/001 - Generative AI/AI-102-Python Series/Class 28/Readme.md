# Python Series: Class 28 - Introduction to Django

## Overview

In this class, we will introduce you to **Django**, a high-level Python web framework that encourages rapid development and clean, pragmatic design. Django makes it easier to build web applications by providing a lot of built-in features like user authentication, database management, and URL routing.

We'll explore the basics of Django, including how to set up a Django project, create views, templates, and work with models.

---

### What You'll Learn:
1. **Introduction to Django**
2. **Setting Up a Django Project**
3. **Creating Views and URLs**
4. **Using Templates in Django**
5. **Working with Models and Databases**

---

## 1. Introduction to Django

Django is a full-stack web framework that allows you to build both the front-end and back-end of web applications. Some of its key features include:

- **Built-in admin panel** for managing data.
- **URL routing** for defining the structure of your web pages.
- **ORM (Object-Relational Mapping)** to interact with databases.
- **Authentication** and **authorization** systems for handling user management.

---

## 2. Setting Up a Django Project

To start using Django, you need to install it first. You can install Django using `pip`:

```bash
pip install django
```

Once installed, you can create a new Django project using the following command:

```bash
django-admin startproject myproject
```

This command creates a new directory `myproject` with all the necessary files for a Django project.

Now, navigate into your project directory and start the development server:

```bash
cd myproject
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the default Django welcome page.

---

## 3. Creating Views and URLs

In Django, views are Python functions that receive web requests and return web responses. Views can render HTML templates, return JSON data, or redirect users to different URLs.

### Example: Creating a Simple View

1. Open the `views.py` file inside the `myproject` directory.
2. Define a simple view that returns a "Hello, World!" message.

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

Next, you need to connect this view to a URL. Open the `urls.py` file and add a URL pattern:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
]
```

Now, visiting `http://127.0.0.1:8000/hello/` will display "Hello, World!" in the browser.

---

## 4. Using Templates in Django

Django uses a templating engine to dynamically generate HTML pages. Templates are HTML files that can contain placeholders for dynamic content.

### Example: Creating a Template

1. Create a `templates` directory inside your project.
2. Inside `templates`, create a new HTML file, `hello.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello, Django!</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
```

3. Modify the `views.py` file to render this template:

```python
from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello.html', {'message': 'Hello, Django!'})
```

Now, when you visit `http://127.0.0.1:8000/hello/`, you will see the "Hello, Django!" message rendered in the template.

---

## 5. Working with Models and Databases

Django includes an ORM (Object-Relational Mapping) system to interact with databases. You can define models that represent your data, and Django automatically handles the SQL queries for you.

### Example: Creating a Model

1. Open `models.py` and create a simple model for a `Post`:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

2. After defining the model, run the following commands to create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

3. You can now interact with the `Post` model through Django's ORM to create, retrieve, update, and delete posts.

---

## Task

1. **Create a Django project with a simple blog** that allows users to submit blog posts. The posts should have a title, content, and a published date.
2. **Create a new view** that displays a list of all blog posts stored in the database.

---