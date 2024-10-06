import socket
import threading
import random

class Server:
    def __init__(self, host='192.168.86.128', port=65433):
        self.host = host
        self.port = port
        self.server_name = "Server of Jiena Wu"
        self.server_integer = random.randint(1, 100)  # Server-chosen number
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create an INET, STREAMing socket

    def start(self):
        # Bind and listen for incoming connections
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"{self.server_name} is listening on {self.host}:{self.port}...")

        while True:
            connection, address = self.socket.accept()
            with connection:
                print(f"Connected by {address}")
                # create a new thread for each client connection
                client_thread = threading.Thread(target=self.handle_client, args=(connection,))
                client_thread.start()

    def handle_client(self, conn):
        try:
            # Receive message from client
            data = conn.recv(1024).decode()
            if not data:
                print("No data received.")
                return

            # Extract client name and client integer from the message
            client_message = data.split(',')
            client_name = client_message[0]
            client_integer = int(client_message[1])

            # Check if the client's integer is out of range
            if client_integer < 1 or client_integer > 100:
                print(f"Received out of range value ({client_integer}). Shutting down server.")
                self.shutdown()
                return

            # Display client and server info
            print(f"Received message from {client_name}")
            print(f"{client_name}'s number: {client_integer}")
            print(f"{self.server_name}'s number: {self.server_integer}")
            print(f"Sum: {client_integer + self.server_integer}")

            # Send server's name and integer back to the client
            response = f"{self.server_name},{self.server_integer}"
            conn.sendall(response.encode())
            print(f"Sent message back to {client_name}")

        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            conn.close() # close the connection after handling the client

    def shutdown(self):
        print("Shutting down the server...")
        self.socket.close()

# To run the server:
if __name__ == "__main__":
    server = Server()
    server.start()
