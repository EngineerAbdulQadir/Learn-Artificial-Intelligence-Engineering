# Python Series: Class 40 - Working with PDFs

## Overview

In this class, we will learn how to manipulate PDF files using Python. We'll use the popular `PyPDF2` library to read, merge, split, and manipulate PDF files. This is useful for automating tasks that involve PDFs, such as generating reports, combining documents, or extracting text.

---

### What You'll Learn:
1. **Introduction to PDF Manipulation**
2. **Reading PDF Files**
3. **Merging PDF Files**
4. **Splitting PDF Files**
5. **Extracting Text from PDFs**
6. **Rotating Pages in PDFs**
7. **Creating PDFs (Optional)**

---

## 1. Introduction to PDF Manipulation

PDF (Portable Document Format) is widely used for presenting documents in a consistent format across various platforms. Python provides libraries like `PyPDF2`, `ReportLab`, and `pdfrw` to work with PDFs.

For this class, we'll focus on the `PyPDF2` library, which allows us to perform basic operations such as reading, merging, splitting, and rotating PDFs.

---

## 2. Installing `PyPDF2`

Before we start, make sure to install the `PyPDF2` library.

```bash
pip install PyPDF2
```

---

## 3. Reading PDF Files

To read a PDF, you can use the `PdfReader` class from `PyPDF2`. This allows you to extract text, information, and metadata from the PDF.

Example: 

```python
import PyPDF2

# Open the PDF file in read-binary mode
with open('example.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Get the number of pages in the PDF
    num_pages = len(reader.pages)
    print(f'The PDF has {num_pages} pages.')

    # Read the text from the first page
    page = reader.pages[0]
    text = page.extract_text()
    print(text)
```

In this example:
- The `PdfReader` is used to read the contents of the `example.pdf` file.
- We extract and print the text of the first page using `extract_text()`.

---

## 4. Merging PDF Files

To combine multiple PDF files into one, you can use the `PdfWriter` class to append pages from each PDF.

Example:

```python
import PyPDF2

# Create a PdfWriter object
writer = PyPDF2.PdfWriter()

# List of PDFs to merge
pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf']

# Loop through each PDF and append its pages
for pdf in pdfs:
    with open(pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)

# Write the merged PDF to a new file
with open('merged.pdf', 'wb') as output:
    writer.write(output)

print("PDFs merged successfully!")
```

In this example:
- The `PdfWriter` class is used to create a new PDF file.
- We read and append pages from each of the specified PDFs, then save the merged result to `merged.pdf`.

---

## 5. Splitting PDF Files

You can split a PDF into separate pages using `PyPDF2`. This is useful when you want to extract specific pages from a large document.

Example:

```python
import PyPDF2

# Open the original PDF file
with open('example.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Get the total number of pages
    num_pages = len(reader.pages)
    
    # Loop through the pages and save each page as a separate PDF
    for page_num in range(num_pages):
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[page_num])
        
        # Save the individual page to a new PDF
        with open(f'page_{page_num + 1}.pdf', 'wb') as output:
            writer.write(output)
        
        print(f'Page {page_num + 1} saved successfully!')
```

In this example:
- We loop through each page of the PDF, extract it, and save it as a separate file.

---

## 6. Extracting Text from PDFs

You can use `extract_text()` to get text from the pages of a PDF. While this method works for most PDFs, it may not be perfect for those with complex formatting.

Example:

```python
import PyPDF2

# Open the PDF file
with open('example.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Extract text from all pages
    full_text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        full_text += page.extract_text()
    
    print(full_text)
```

In this example:
- We iterate through all pages, extract text, and combine it into one string.

---

## 7. Rotating Pages in PDFs

You can rotate pages in a PDF by specifying the rotation angle (90, 180, 270 degrees). This is useful when you need to adjust the orientation of pages.

Example:

```python
import PyPDF2

# Open the original PDF file
with open('example.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Create a PdfWriter object
    writer = PyPDF2.PdfWriter()
    
    # Rotate the first page by 90 degrees
    page = reader.pages[0]
    page.rotate(90)
    writer.add_page(page)
    
    # Write the rotated page to a new PDF
    with open('rotated.pdf', 'wb') as output:
        writer.write(output)

print("Page rotated and saved successfully!")
```

In this example:
- The `rotate()` method rotates the first page by 90 degrees.

---

## 8. Creating PDFs (Optional)

While `PyPDF2` focuses on manipulating existing PDFs, you can create PDFs from scratch using the `ReportLab` library. Here's an example of creating a simple PDF:

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF canvas
c = canvas.Canvas('created.pdf', pagesize=letter)

# Add some text to the PDF
c.drawString(100, 750, "Hello, Python PDF!")

# Save the PDF
c.save()

print("PDF created successfully!")
```

In this example:
- The `ReportLab` library allows you to create new PDFs, add text, and save them.

---

## Task

1. **Create a program that merges multiple PDFs into one.**
2. **Write a script that extracts text from a PDF and saves it to a `.txt` file.**
3. **Create a program that splits a PDF into individual pages and saves them separately.**

---