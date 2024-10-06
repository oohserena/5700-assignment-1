# 1. Description of the program

## 1.1 Overview

This is a concurrent server-client program in Python. The server can handle multiple client connections simultaneously using threads. 

## 1.2 Features

- The server generates a random integer between 1 and 100, and return the sum of the integer with a number sent by the client
- The server validates the client's integer input to make sure it’s in the accepted range (1-100).
- The server and client communicate using a simple message format. The server responds with its name and the generated integer.

# 2. Usage

1. Start the server by running `server.py` script in one terminal window.
2. In another terminal window, run the `client.py` script to connect to the server and send requests.
3. The client will ask to input an integer between 1 and 100, send the input to the server, and you can see the server's response.

# 3. Program Design

The program consists of two main components: the **Server** and the **Client.**

## 3.1 Design Principles

- **Concurrency**: The server uses `threading` to handle multiple client connections. Each client request is processed in a separate thread, so that the server can continue to accept new connections while handling existing requests.
    
    **Core logic:**
    
    1. The server binds to a specified host and port using the `socket` library.
    2. It listens for incoming connections.
    3. When a client connects, a new thread is created to handle that client by creating the `threading.Thread class` . Each thread runs the `handle_client()` method.
    4. Each thread processes the client's message independently.
- **Socket Programming**: The program uses TCP sockets for the communication between the server and clients. This can make sure that data is transmitted in the correct order.
- **Input Validation**: The program implements strict input validation for the integer values. If a client sends an out-of-range integer, the server terminates, and sends an error message.
- **Error Catch:** Each class (server and client) encapsulates its functionality by using a separation of concerns.

## 3.2 Libraries Used

`socket` , `threading` , `random`

## 3.2 Server

- Listens for incoming client connections on a specified IP address and port. My IP address is 192.168.86.128 and the port is 65433.
- Uses threading to manage multiple clients concurrently and handle simultaneous requests.
- Validates the integer input from clients to make sure it’s in the range of 1 to 100.
- Generates a random integer and display the sum of client num and the chosen number.
- Sends the results back to the client.

## 3.3 Client

- Starts a connection to the server using a specified IP address and port.
- Asks the user to input an integer and sends it to server with the client's name.
- Receives the server's response (server name, randomly generated integer)
- Displays the sum of its integer and the server's integer.
