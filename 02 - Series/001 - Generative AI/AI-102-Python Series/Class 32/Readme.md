# Python Series: Class 32 - Data Visualization with Matplotlib

## Overview

In this class, we will explore **Matplotlib**, a powerful plotting library in Python that allows you to create a wide variety of static, animated, and interactive plots. We will focus on how to visualize data and create plots to gain insights.

---

### What You'll Learn:
1. **Introduction to Matplotlib**
2. **Creating Basic Plots**
3. **Customizing Plots**
4. **Working with Multiple Plots**
5. **Saving Plots**

---

## 1. Introduction to Matplotlib

**Matplotlib** is the most popular library for data visualization in Python. It allows you to create various types of plots, such as line plots, bar charts, scatter plots, and histograms.

To install Matplotlib, you can run:

```bash
pip install matplotlib
```

---

## 2. Creating Basic Plots

Matplotlib provides a `pyplot` module that contains functions to generate various types of plots.

### Example: Line Plot

```python
import matplotlib.pyplot as plt

# Data for the plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot
plt.plot(x, y)

# Display the plot
plt.show()
```

Output:
- A simple line plot where `x` is plotted on the x-axis and `y` on the y-axis.

### Example: Scatter Plot

```python
import matplotlib.pyplot as plt

# Data for the scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y)

# Display the plot
plt.show()
```

---

## 3. Customizing Plots

Matplotlib provides several customization options to enhance the appearance of your plots.

### Customizing the Line Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot with customization
plt.plot(x, y, color='red', marker='o', linestyle='-', linewidth=2, markersize=8)

# Adding title and labels
plt.title("Line Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the plot
plt.show()
```

### Adding a Grid

```python
plt.plot(x, y)
plt.grid(True)  # Show grid lines
plt.show()
```

---

## 4. Working with Multiple Plots

You can create multiple plots in the same figure using the `subplot` function.

### Example: Multiple Plots in One Figure

```python
import matplotlib.pyplot as plt

# Data for the plots
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Create a subplot with 2 rows and 1 column
plt.subplot(2, 1, 1)  # First plot
plt.plot(x, y1)
plt.title("First Plot")

plt.subplot(2, 1, 2)  # Second plot
plt.plot(x, y2)
plt.title("Second Plot")

# Display the plots
plt.tight_layout()  # Adjust the spacing between plots
plt.show()
```

---

## 5. Saving Plots

You can save your plots as image files using the `savefig()` function.

### Example: Save a Plot as an Image

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y)

# Save the plot as a PNG file
plt.savefig("line_plot.png")

# Display the plot
plt.show()
```

---

## Task

1. **Create a line plot** for a dataset of your choice.
2. **Customize the plot** by changing the color, line style, and adding titles and labels.
3. **Create a subplot** with two different plots and display them in one figure.
4. **Save the plot** you created as a PNG file.

---