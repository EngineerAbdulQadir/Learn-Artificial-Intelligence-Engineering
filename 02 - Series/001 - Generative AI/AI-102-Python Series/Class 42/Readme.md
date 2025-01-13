# Python Series: Class 42 - Working with Images (Pillow)

## Overview

In this class, we will learn how to manipulate and process images using the **Pillow** library in Python. Pillow is a powerful image processing library that allows you to open, manipulate, and save many different image file formats. We'll cover basic image operations like resizing, cropping, rotating, and applying filters, as well as more advanced tasks such as drawing on images.

---

### What You'll Learn:
1. **Introduction to Pillow**
2. **Installing Pillow**
3. **Opening and Displaying Images**
4. **Basic Image Operations**
   - Resizing
   - Cropping
   - Rotating
   - Flipping
5. **Applying Filters to Images**
6. **Drawing on Images**
7. **Saving Images**

---

## 1. Introduction to Pillow

**Pillow** is a fork of the Python Imaging Library (PIL) that provides an easy-to-use interface for opening, manipulating, and saving image files. It supports a wide range of formats, such as JPEG, PNG, BMP, GIF, TIFF, and more. Pillow can be used to:
- Open and display images.
- Perform basic image operations (resizing, cropping, rotating).
- Apply filters to improve or modify the appearance of images.
- Draw shapes or text on images.
- Save images in various formats.

---

## 2. Installing Pillow

First, you need to install the **Pillow** library. You can do this using the following command:

```bash
pip install Pillow
```

---

## 3. Opening and Displaying Images

Once you have Pillow installed, you can use it to open and display images.

### Example Code:

```python
from PIL import Image

# Open an image file
image = Image.open('example.jpg')

# Display the image
image.show()
```

In this example:
- We open an image file named `example.jpg` using `Image.open()`.
- The `show()` method opens the image in the default image viewer.

---

## 4. Basic Image Operations

### Resizing Images

You can resize images to a specific width and height.

### Example Code:

```python
# Resize the image to 200x200 pixels
resized_image = image.resize((200, 200))

# Show the resized image
resized_image.show()
```

In this example:
- We use the `resize()` method to resize the image to 200x200 pixels.

### Cropping Images

You can crop an image by specifying a box of coordinates (left, upper, right, lower).

### Example Code:

```python
# Define the coordinates for cropping (left, upper, right, lower)
crop_box = (100, 100, 400, 400)

# Crop the image
cropped_image = image.crop(crop_box)

# Show the cropped image
cropped_image.show()
```

In this example:
- The image is cropped using the box `(100, 100, 400, 400)`.

### Rotating Images

You can rotate an image by a specified number of degrees.

### Example Code:

```python
# Rotate the image by 90 degrees
rotated_image = image.rotate(90)

# Show the rotated image
rotated_image.show()
```

In this example:
- The image is rotated by 90 degrees using the `rotate()` method.

### Flipping Images

You can flip an image horizontally or vertically.

### Example Code:

```python
# Flip the image horizontally
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

# Show the flipped image
flipped_image.show()
```

In this example:
- The image is flipped horizontally using the `transpose()` method with `Image.FLIP_LEFT_RIGHT`.

---

## 5. Applying Filters to Images

Pillow provides several filters that can be used to modify the appearance of an image. You can apply filters such as **blur**, **sharpen**, and **contour** to create different effects.

### Example Code (Applying Blur Filter):

```python
from PIL import ImageFilter

# Apply a blur filter to the image
blurred_image = image.filter(ImageFilter.BLUR)

# Show the blurred image
blurred_image.show()
```

In this example:
- We use the `filter()` method along with `ImageFilter.BLUR` to apply a blur effect to the image.

---

## 6. Drawing on Images

You can draw shapes, lines, or text on images using the `ImageDraw` module.

### Example Code (Drawing Text on an Image):

```python
from PIL import ImageDraw, ImageFont

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Define the text and position
text = "Hello, Pillow!"
position = (100, 100)

# Use a default font
font = ImageFont.load_default()

# Draw the text on the image
draw.text(position, text, font=font, fill="white")

# Show the image with text
image.show()
```

In this example:
- We use `ImageDraw.Draw()` to draw on the image.
- The `text()` method allows us to add text to the image at the specified position.

---

## 7. Saving Images

Once you've manipulated an image, you can save it to a file using the `save()` method.

### Example Code:

```python
# Save the manipulated image
image.save('modified_image.jpg')
```

In this example:
- The image is saved as `modified_image.jpg` in the current working directory.

---

## Task

1. **Resize an image to 500x500 pixels and save it.**
2. **Crop a section from an image and save the cropped part.**
3. **Apply a sharpen filter to an image and display the result.**
4. **Draw a circle and some text on an image, then save it.**

---