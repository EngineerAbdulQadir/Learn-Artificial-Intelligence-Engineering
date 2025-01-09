# Python Series: Class 26 - Networking with Python

## Overview

In this class, we will learn about **networking** with Python. Networking allows you to interact with other computers and devices over a network, enabling communication and data exchange. Python provides powerful libraries like `socket` to handle networking tasks.

We will cover how to create simple client-server applications and how data is transmitted over the network.

---

### What You'll Learn:
1. **Introduction to Networking**
2. **Creating a Server using Python**
3. **Creating a Client using Python**
4. **Socket Programming**

---

## 1. Introduction to Networking

Networking involves connecting different devices to exchange data. The basic concept in networking is the **client-server model**, where one device (the client) sends requests, and the other device (the server) responds.

In Python, the `socket` module is used to implement networking features, providing both server and client capabilities.

---

## 2. Creating a Server using Python

A server listens for incoming client requests and responds with the requested data. To create a server in Python, we will use the `socket` module to bind the server to a specific address and port.

### Example: Simple Python Server

```python
import socket

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an IP address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on port 12345...")

# Accept incoming connections
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received from client: {data.decode()}")

# Send a response to the client
client_socket.send(b'Hello from the server!')

# Close the connection
client_socket.close()
server_socket.close()
```

Here, the server listens on port `12345` and waits for a connection from a client. Once connected, it receives data from the client and sends a response.

---

## 3. Creating a Client using Python

A client connects to a server, sends data, and waits for a response. We will create a client that connects to the server we created earlier and sends a message.

### Example: Simple Python Client

```python
import socket

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Send data to the server
client_socket.send(b'Hello from the client!')

# Receive data from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# Close the connection
client_socket.close()
```

In this example, the client connects to the server, sends a message, and prints the server's response.

---

## 4. Socket Programming

Socket programming allows communication between devices over the network using the `socket` library. It involves creating a socket object, binding it to an IP address and port, listening for connections, and sending/receiving data.

### Key Methods in Socket Programming:

- **`socket.socket()`**: Creates a socket object.
- **`bind()`**: Binds the socket to an address and port.
- **`listen()`**: Listens for incoming connections.
- **`accept()`**: Accepts an incoming connection.
- **`recv()`**: Receives data from the client.
- **`send()`**: Sends data to the client.
- **`connect()`**: Connects the client to the server.
- **`close()`**: Closes the socket connection.

---

## Task

1. **Create a server-client chat application** where the server can send and receive messages from multiple clients. Implement a simple loop to keep the communication going between the client and the server.

2. **Create a file transfer application** in which the client sends a file to the server. The server should receive the file and save it on disk. 

---