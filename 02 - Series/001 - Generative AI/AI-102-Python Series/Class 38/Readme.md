# Python Series: Class 38 - GUI Programming with Tkinter

## Overview

In this class, we will explore **Tkinter**, the standard Python interface to the Tk GUI (Graphical User Interface) toolkit. Tkinter allows you to create desktop applications with a graphical user interface (GUI).

---

### What You'll Learn:
1. **Introduction to Tkinter**
2. **Creating a Simple Window**
3. **Adding Widgets (Buttons, Labels, Text Boxes)**
4. **Handling Events and User Interaction**
5. **Building a Simple GUI Application**

---

## 1. Introduction to Tkinter

Tkinter is the standard Python interface to the Tk GUI toolkit. It provides tools to create windows, buttons, text fields, labels, and other GUI components. Tkinter is simple to use and works across all major platforms.

To install Tkinter, it is usually bundled with Python. However, if you do not have it, you can install it using:

```bash
pip install tk
```

---

## 2. Creating a Simple Window

To create a simple window using Tkinter, you need to initialize the Tkinter class and call the main loop.

Example:

```python
import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the window title
window.title("My First Tkinter App")

# Set window size
window.geometry("400x300")

# Run the window (start the Tkinter event loop)
window.mainloop()
```

In this code:
- We create the window using `tk.Tk()`.
- We set the window title with `.title()`.
- We define the window size with `.geometry()`.
- `window.mainloop()` starts the Tkinter event loop, which waits for user actions (like clicks or typing).

---

## 3. Adding Widgets (Buttons, Labels, Text Boxes)

Widgets are the elements of the GUI that interact with the user. Tkinter provides a variety of widgets like labels, buttons, text boxes, and more.

Example of adding a label and a button:

```python
import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Widgets Example")

# Create a label widget
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 14))
label.pack()

# Create a button widget
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

# Run the window
window.mainloop()
```

In this code:
- A `Label` widget is created to display text.
- A `Button` widget is created, and we use the `command` parameter to call the `on_button_click()` function when the button is clicked.

---

## 4. Handling Events and User Interaction

Events in Tkinter allow the program to respond to user actions like mouse clicks, key presses, or window resizing. In this example, we handle a button click event.

Example:

```python
import tkinter as tk

def on_button_click():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

# Create the main window
window = tk.Tk()
window.title("Event Handling Example")

# Create a label widget
label = tk.Label(window, text="Enter your name:", font=("Arial", 12))
label.pack()

# Create an entry widget (text box)
entry = tk.Entry(window)
entry.pack()

# Create a button widget
button = tk.Button(window, text="Submit", command=on_button_click)
button.pack()

# Run the window
window.mainloop()
```

In this code:
- We use an `Entry` widget to allow the user to input text.
- When the button is clicked, the program retrieves the text from the `Entry` widget and updates the `Label`.

---

## 5. Building a Simple GUI Application

Now let's build a simple GUI application that accepts user input and displays a personalized message.

```python
import tkinter as tk

def on_button_click():
    name = entry.get()
    age = entry_age.get()
    label.config(text=f"Hello, {name}! You are {age} years old.")

# Create the main window
window = tk.Tk()
window.title("Personalized Greeting")

# Create a label and entry for name
label_name = tk.Label(window, text="Enter your name:", font=("Arial", 12))
label_name.pack()

entry = tk.Entry(window)
entry.pack()

# Create a label and entry for age
label_age = tk.Label(window, text="Enter your age:", font=("Arial", 12))
label_age.pack()

entry_age = tk.Entry(window)
entry_age.pack()

# Create a submit button
button = tk.Button(window, text="Submit", command=on_button_click)
button.pack()

# Create a label to display the message
label = tk.Label(window, text="", font=("Arial", 14))
label.pack()

# Run the window
window.mainloop()
```

In this application:
- The user is prompted to enter their name and age.
- Upon clicking "Submit", the program displays a personalized greeting.

---

## Task

1. **Create a simple calculator GUI** that takes two numbers as input and performs addition, subtraction, multiplication, and division based on the user's choice.
2. **Design a GUI application** that allows the user to input their favorite hobby and displays a message saying: "Your favorite hobby is <hobby>."

---