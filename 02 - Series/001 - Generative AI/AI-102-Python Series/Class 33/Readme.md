# Python Series: Class 33 - Introduction to Numpy

## Overview

In this class, we will dive into **Numpy**, a powerful library for numerical computing in Python. It is especially useful for working with large datasets, arrays, and matrices, and provides many functions for mathematical operations, statistical operations, and linear algebra.

---

### What You'll Learn:
1. **Introduction to Numpy**
2. **Creating Arrays**
3. **Array Indexing and Slicing**
4. **Array Operations**
5. **Mathematical Functions in Numpy**

---

## 1. Introduction to Numpy

**Numpy** is a core library for numerical computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.

To install Numpy, you can run:

```bash
pip install numpy
```

### Importing Numpy
```python
import numpy as np
```

---

## 2. Creating Arrays

### Creating a Numpy Array from a List

```python
import numpy as np

# Create a Numpy array from a Python list
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

### Creating a Numpy Array with Zeros or Ones

```python
import numpy as np

# Create an array of zeros
zeros_array = np.zeros(5)
print(zeros_array)

# Create an array of ones
ones_array = np.ones(5)
print(ones_array)
```

### Creating a Range of Values with `arange()`

```python
import numpy as np

# Create an array with a range of values
range_array = np.arange(0, 10, 2)
print(range_array)
```

---

## 3. Array Indexing and Slicing

Numpy arrays allow for powerful and flexible indexing and slicing.

### Accessing Elements

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Access the first element
print(arr[0])

# Access the last element
print(arr[-1])
```

### Slicing Arrays

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Slice the array from index 1 to 3
print(arr[1:4])

# Slice the array from the start to index 3
print(arr[:4])

# Slice the array from index 2 to the end
print(arr[2:])
```

---

## 4. Array Operations

### Arithmetic Operations

You can perform element-wise operations on Numpy arrays.

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Element-wise addition
print(arr1 + arr2)

# Element-wise multiplication
print(arr1 * arr2)
```

### Universal Functions (ufuncs)

Numpy provides a collection of mathematical functions that can be applied element-wise to arrays.

```python
import numpy as np

arr = np.array([1, 4, 9, 16])

# Calculate the square root of each element
print(np.sqrt(arr))

# Calculate the sine of each element
print(np.sin(arr))
```

---

## 5. Mathematical Functions in Numpy

Numpy includes a vast set of mathematical functions for statistical, algebraic, and matrix operations.

### Basic Statistical Operations

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Calculate the mean
print(np.mean(arr))

# Calculate the median
print(np.median(arr))

# Calculate the standard deviation
print(np.std(arr))
```

---

## Task

1. **Create a Numpy array** from a list of your choice.
2. **Perform element-wise operations** on two arrays.
3. **Slice the array** to get specific portions of the array.
4. **Use mathematical functions** like square root and sine on a Numpy array.
5. **Perform basic statistical operations** like mean, median, and standard deviation on an array.

---