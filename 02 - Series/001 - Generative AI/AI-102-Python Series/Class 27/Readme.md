# Python Series: Class 27 - Web Scraping with BeautifulSoup

## Overview

In this class, we will explore **web scraping** using Python's `BeautifulSoup` library. Web scraping is the process of extracting data from websites. It’s a powerful tool for gathering information from web pages automatically.

We'll learn how to retrieve a webpage, parse its HTML, and extract specific data from it, such as headings, links, and other elements.

---

### What You'll Learn:
1. **Introduction to Web Scraping**
2. **Installing BeautifulSoup and Requests**
3. **Fetching Web Pages**
4. **Parsing HTML with BeautifulSoup**
5. **Extracting Data (Headings, Links, etc.)**

---

## 1. Introduction to Web Scraping

Web scraping allows you to collect data from websites in an automated manner. It involves sending HTTP requests to a website, retrieving the HTML content, and parsing the HTML to extract useful information.

**Important Consideration:** 
Before scraping a website, always ensure you are not violating the website’s terms of service. Many websites prohibit scraping in their robots.txt file or terms of use.

---

## 2. Installing BeautifulSoup and Requests

To get started with web scraping in Python, we need to install two libraries:
- **BeautifulSoup4**: A library for parsing HTML and XML documents.
- **Requests**: A simple HTTP library to send requests to websites.

You can install both libraries using `pip`:

```bash
pip install beautifulsoup4
pip install requests
```

---

## 3. Fetching Web Pages

Before we can scrape a website, we need to fetch the HTML content of the page. The `requests` library allows us to send HTTP requests and retrieve web pages.

### Example: Fetching a Web Page

```python
import requests

# URL of the page you want to scrape
url = 'https://example.com'

# Send a GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.text)  # Print the raw HTML content of the page
else:
    print("Failed to retrieve the page")
```

This code fetches the HTML content of the specified URL and prints it.

---

## 4. Parsing HTML with BeautifulSoup

Once we have the HTML content, we need to parse it. `BeautifulSoup` makes it easy to navigate and search the HTML document.

### Example: Parsing HTML with BeautifulSoup

```python
from bs4 import BeautifulSoup

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Print the prettified HTML (formatted nicely for reading)
print(soup.prettify())
```

The `prettify()` method formats the HTML code in a readable way.

---

## 5. Extracting Data (Headings, Links, etc.)

Now that we can parse HTML, we can extract specific elements like headings, links, and other data.

### Example: Extracting All Links from a Page

```python
# Find all <a> tags, which define hyperlinks in HTML
links = soup.find_all('a')

# Loop through the links and print the href attribute (URL)
for link in links:
    print(link.get('href'))
```

This code extracts all the links from the page and prints the URLs.

### Example: Extracting Heading Tags (h1, h2, etc.)

```python
# Find the first <h1> tag and print its text content
heading = soup.find('h1')
print(heading.text)
```

This code extracts and prints the text inside the first `<h1>` heading tag.

---

## Task

1. **Create a Python script to scrape a news website**. Extract the titles of the latest articles and print them.
   
2. **Create a Python script to scrape a product listing page**. Extract the product names, prices, and links to the product details.

---