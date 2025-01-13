# Python Series: Class 35 - Introduction to TensorFlow

## Overview

In this class, we will learn the basics of **TensorFlow**, a powerful open-source library for numerical computation and machine learning. TensorFlow is widely used for building and training machine learning models. We will explore the basic concepts of TensorFlow and how to build a simple model.

---

### What You'll Learn:
1. **Introduction to TensorFlow**
2. **Installing TensorFlow**
3. **Basic Operations with TensorFlow**
4. **Creating Tensors**
5. **Building a Simple Neural Network Model**

---

## 1. Introduction to TensorFlow

**TensorFlow** is a library developed by Google that is used to build machine learning and deep learning models. It provides an easy-to-use API for both research and production-level tasks. TensorFlow can be used for a wide range of applications, such as natural language processing, image recognition, and more.

---

## 2. Installing TensorFlow

To get started with TensorFlow, you need to install it using pip:

```bash
pip install tensorflow
```

After installation, you can import TensorFlow in your code:

```python
import tensorflow as tf
```

---

## 3. Basic Operations with TensorFlow

In TensorFlow, data is represented as **tensors**. A tensor is a multi-dimensional array or matrix that contains elements of a single data type.

### Tensor Operations

```python
import tensorflow as tf

# Creating a tensor
tensor_1 = tf.constant([1, 2, 3, 4])

# Performing basic operations
tensor_2 = tensor_1 + 5
tensor_3 = tensor_1 * 2

# Print tensors
print(tensor_1)
print(tensor_2)
print(tensor_3)
```

---

## 4. Creating Tensors

Tensors can be created in several ways, and TensorFlow provides various functions to work with them.

### Create a Tensor from a NumPy Array

```python
import tensorflow as tf
import numpy as np

# Create a tensor from a NumPy array
numpy_array = np.array([1, 2, 3, 4, 5])
tensor_from_numpy = tf.convert_to_tensor(numpy_array)

# Print the tensor
print(tensor_from_numpy)
```

### Random Tensor

```python
# Create a random tensor of shape (2, 3)
random_tensor = tf.random.normal([2, 3])
print(random_tensor)
```

---

## 5. Building a Simple Neural Network Model

TensorFlow can be used to create machine learning models. In this example, we'll use the **Keras** API (which is part of TensorFlow) to build a simple neural network model for classification.

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Generate some random data
X = np.random.rand(1000, 20)  # 1000 samples, 20 features
y = np.random.randint(0, 2, size=(1000, 1))  # Binary labels (0 or 1)

# Create a simple neural network model
model = Sequential([
    Dense(64, activation='relu', input_dim=20),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10, batch_size=32)
```

---

## Task

1. **Install TensorFlow** and create a simple tensor with your favorite numbers.
2. Perform basic tensor operations like addition, subtraction, and multiplication.
3. Create a random tensor and print it.
4. Build a simple neural network model using the Keras API and train it on random data (as shown above).
5. Experiment with different numbers of layers and neurons in your model.

---