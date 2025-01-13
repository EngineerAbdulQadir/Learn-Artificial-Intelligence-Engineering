# Python Series: Class 39 - File Compression with Python

## Overview

In this class, we will learn how to compress and extract files using Python. We'll work with the built-in `zipfile` and `tarfile` modules to handle file compression tasks in various formats, including `.zip` and `.tar`.

---

### What You'll Learn:
1. **Introduction to File Compression**
2. **Using the zipfile Module**
3. **Using the tarfile Module**
4. **Compressing and Extracting Files**
5. **Creating Custom Compression Scripts**

---

## 1. Introduction to File Compression

File compression allows you to reduce the size of files, making them easier to store and share. Python provides several modules for file compression, with `zipfile` and `tarfile` being among the most commonly used.

---

## 2. Using the `zipfile` Module

The `zipfile` module provides tools to work with `.zip` files, which are widely used for compressing and archiving files.

### Compressing Files into a Zip Archive

To compress a file into a `.zip` file, you can use the `ZipFile` class.

Example:

```python
import zipfile

# Create a zip file and add files to it
with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('file1.txt')
    zipf.write('file2.txt')
```

In this example:
- The `ZipFile` class is used with mode `'w'` (write) to create a new zip file.
- The `write()` method adds the files `file1.txt` and `file2.txt` to the archive.

### Extracting Files from a Zip Archive

To extract files from a `.zip` archive, you can use the `extractall()` method.

Example:

```python
import zipfile

# Extract all files from the zip archive
with zipfile.ZipFile('example.zip', 'r') as zipf:
    zipf.extractall('extracted_files')
```

In this example:
- The `extractall()` method extracts all files from the `example.zip` file to the directory `extracted_files`.

---

## 3. Using the `tarfile` Module

The `tarfile` module allows you to work with `.tar`, `.tar.gz`, `.tgz`, and other tarball formats.

### Compressing Files into a Tar Archive

Example:

```python
import tarfile

# Create a tar.gz archive and add files to it
with tarfile.open('example.tar.gz', 'w:gz') as tar:
    tar.add('file1.txt')
    tar.add('file2.txt')
```

In this example:
- The `tarfile.open()` method opens a tarball for writing in gzip-compressed format (`'w:gz'`).
- The `add()` method adds files to the archive.

### Extracting Files from a Tar Archive

Example:

```python
import tarfile

# Extract all files from the tar.gz archive
with tarfile.open('example.tar.gz', 'r:gz') as tar:
    tar.extractall('extracted_files')
```

In this example:
- The `tarfile.open()` method opens a tarball for reading.
- The `extractall()` method extracts the contents into the directory `extracted_files`.

---

## 4. Compressing and Extracting Files in Practice

You can use these modules to build custom scripts that automate file compression tasks. Here's an example that lets the user choose to compress or extract files:

```python
import zipfile
import tarfile
import os

def compress_files():
    files = input("Enter files to compress (comma separated): ").split(',')
    archive_name = input("Enter archive name (without extension): ")
    extension = input("Choose format (zip/tar): ").lower()

    if extension == 'zip':
        with zipfile.ZipFile(archive_name + '.zip', 'w') as zipf:
            for file in files:
                zipf.write(file.strip())
        print(f"Files compressed to {archive_name}.zip")

    elif extension == 'tar':
        with tarfile.open(archive_name + '.tar.gz', 'w:gz') as tar:
            for file in files:
                tar.add(file.strip())
        print(f"Files compressed to {archive_name}.tar.gz")
    else:
        print("Invalid format selected.")

def extract_files():
    archive_name = input("Enter archive file name to extract (zip/tar.gz): ")
    extension = archive_name.split('.')[-1]

    if extension == 'zip':
        with zipfile.ZipFile(archive_name, 'r') as zipf:
            zipf.extractall('extracted_files')
        print(f"Files extracted to 'extracted_files' folder.")

    elif extension == 'gz' or extension == 'tar':
        with tarfile.open(archive_name, 'r:gz') as tar:
            tar.extractall('extracted_files')
        print(f"Files extracted to 'extracted_files' folder.")
    else:
        print("Unsupported file format.")

# Main program loop
while True:
    action = input("Choose an action (compress/extract/exit): ").lower()

    if action == 'compress':
        compress_files()
    elif action == 'extract':
        extract_files()
    elif action == 'exit':
        break
    else:
        print("Invalid action selected.")
```

In this script:
- The user can choose to compress or extract files.
- The script handles both `.zip` and `.tar.gz` formats.

---

## 5. Creating Custom Compression Scripts

You can further customize the compression scripts by adding error handling, user prompts for multiple files, or even integrating them with cloud storage systems.

---

## Task

1. **Create a program that compresses all `.txt` files in a folder into a `.zip` file.**
2. **Write a script that extracts all files from a `.tar.gz` archive into a specific directory and handles errors.**

---