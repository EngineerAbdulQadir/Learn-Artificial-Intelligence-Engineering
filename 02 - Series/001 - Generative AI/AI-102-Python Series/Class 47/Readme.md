# Python Series: Class 47 - Introduction to Cloud Services with Python

## Overview

In this class, we will explore how to use **Python** for interacting with **cloud services**. Cloud computing provides scalable resources over the internet, and being able to work with cloud services allows developers to store data, run applications, and perform various other tasks without maintaining physical hardware.

Python has several libraries and SDKs that help you interact with popular cloud providers like **AWS**, **Google Cloud**, and **Microsoft Azure**. We will focus on how to use Python to interact with cloud services for tasks such as uploading files to storage, managing virtual machines, and accessing cloud databases.

---

### What You'll Learn:
1. **What is Cloud Computing?**
2. **Cloud Providers Overview**
3. **Working with AWS S3 Storage using Python**
4. **Using Google Cloud Storage with Python**
5. **Working with Azure Blob Storage**
6. **Interacting with Cloud Databases using Python**

---

## 1. What is Cloud Computing?

Cloud computing refers to the delivery of computing services such as servers, storage, databases, networking, software, and more over the internet (the cloud). This allows businesses and developers to access powerful resources without having to maintain physical hardware.

Common types of cloud computing include:
- **Infrastructure as a Service (IaaS)**: Virtual machines, networking, and storage.
- **Platform as a Service (PaaS)**: Development frameworks and environments.
- **Software as a Service (SaaS)**: Ready-to-use software applications.

Popular cloud providers:
- **Amazon Web Services (AWS)**
- **Google Cloud Platform (GCP)**
- **Microsoft Azure**

In this class, we will focus on interacting with cloud storage services, which are commonly used for file storage, backups, and media hosting.

---

## 2. Cloud Providers Overview

Let's take a look at the major cloud providers and their respective services that you can interact with using Python.

- **AWS**: Amazon offers various cloud services like AWS S3 for storage, EC2 for virtual machines, Lambda for serverless functions, and RDS for managed databases.
- **Google Cloud**: Google offers cloud services like Google Cloud Storage, Google Compute Engine, and Google Cloud Firestore.
- **Microsoft Azure**: Microsoft provides services like Azure Blob Storage, Azure Virtual Machines, and Azure SQL Database.

For the purpose of this class, we will focus on **cloud storage services**, which are commonly used in many applications.

---

## 3. Working with AWS S3 Storage using Python

Amazon S3 (Simple Storage Service) is one of the most popular cloud storage services that allows you to store and retrieve data from the cloud. Python has a great library called `boto3`, which is the official AWS SDK for Python, allowing you to interact with AWS services.

### Steps to Use AWS S3 with Python:

1. **Install `boto3`**:
   ```bash
   pip install boto3
   ```

2. **Set up AWS credentials**:
   To interact with AWS services, you need to configure your AWS credentials. You can do this via the AWS CLI or by manually setting up the `~/.aws/credentials` file.

3. **Code to Upload Files to S3**:

```python
import boto3

# Set up AWS S3 client
s3_client = boto3.client('s3')

# Upload file to S3
def upload_file_to_s3(file_name, bucket_name):
    try:
        s3_client.upload_file(file_name, bucket_name, file_name)
        print(f"File {file_name} uploaded to {bucket_name} successfully!")
    except Exception as e:
        print(f"Error uploading file: {e}")

upload_file_to_s3('example.txt', 'my-s3-bucket')
```

4. **Code to List Files in a Bucket**:

```python
def list_files_in_s3(bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        for obj in response.get('Contents', []):
            print(f"File: {obj['Key']}")
    except Exception as e:
        print(f"Error listing files: {e}")

list_files_in_s3('my-s3-bucket')
```

---

## 4. Using Google Cloud Storage with Python

Google Cloud Storage (GCS) is a scalable and highly durable object storage service. You can interact with GCS using the `google-cloud-storage` library in Python.

### Steps to Use Google Cloud Storage:

1. **Install the Google Cloud Storage client**:
   ```bash
   pip install google-cloud-storage
   ```

2. **Set up Google Cloud credentials**:
   You can authenticate using the Google Cloud SDK or service account keys.

3. **Code to Upload Files to GCS**:

```python
from google.cloud import storage

# Set up GCS client
storage_client = storage.Client()

def upload_file_to_gcs(bucket_name, file_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)
    print(f"File {file_name} uploaded to {bucket_name} successfully!")

upload_file_to_gcs('my-gcs-bucket', 'example.txt')
```

4. **Code to List Files in a Bucket**:

```python
def list_files_in_gcs(bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    for blob in blobs:
        print(f"File: {blob.name}")

list_files_in_gcs('my-gcs-bucket')
```

---

## 5. Working with Azure Blob Storage

Azure Blob Storage is a service for storing large amounts of unstructured data, such as text, images, videos, and backups.

### Steps to Use Azure Blob Storage with Python:

1. **Install Azure Storage Blob library**:
   ```bash
   pip install azure-storage-blob
   ```

2. **Set up Azure credentials**:
   You will need an Azure storage account and access keys.

3. **Code to Upload Files to Azure Blob Storage**:

```python
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Set up Azure Blob service client
blob_service_client = BlobServiceClient.from_connection_string('YOUR_AZURE_CONNECTION_STRING')

def upload_file_to_azure(container_name, file_name):
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(file_name)
    with open(file_name, 'rb') as data:
        blob_client.upload_blob(data)
    print(f"File {file_name} uploaded to Azure Blob Storage successfully!")

upload_file_to_azure('my-container', 'example.txt')
```

4. **Code to List Files in Azure Blob Storage**:

```python
def list_files_in_azure(container_name):
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    for blob in blobs:
        print(f"File: {blob.name}")

list_files_in_azure('my-container')
```

---

## 6. Interacting with Cloud Databases using Python

Cloud databases, such as **Amazon RDS**, **Google Cloud SQL**, and **Azure SQL Database**, can be accessed via Python libraries like **PyMySQL**, **psycopg2**, or the specific SDKs provided by the cloud providers.

### Example for Connecting to MySQL Database on AWS RDS:

```python
import pymysql

# Connect to AWS RDS MySQL database
def connect_to_rds():
    connection = pymysql.connect(host='your-rds-endpoint',
                                 user='your-username',
                                 password='your-password',
                                 database='your-database')

    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM your_table')
            for row in cursor.fetchall():
                print(row)
    finally:
        connection.close()

connect_to_rds()
```

---

## Summary

In this class, we have learned how to use Python to interact with cloud services such as **Amazon S3**, **Google Cloud Storage**, and **Azure Blob Storage**. Additionally, we explored how to connect to cloud databases using Python. These skills will help you integrate cloud storage and computing resources into your applications, allowing for more scalable and robust systems.

Cloud services provide easy access to powerful infrastructure, and with Python, you can automate many tasks such as file storage, virtual machine management, and database interactions.

By learning how to work with cloud services, you can leverage the power of the cloud to build, deploy, and manage applications more effectively.

---
