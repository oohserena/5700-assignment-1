import socket

class Client:
    def __init__(self, host='192.168.86.128', port=65433):
        self.host = host
        self.port = port
        self.client_name = "Client of Jiena Wu"
        self.client_integer = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        # Get user input (integer between 1 and 100)
        self.client_integer = self.get_user_input()

        # Connect to the server
        self.socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

        # Send message (name and integer) to the server
        message = f"{self.client_name},{self.client_integer}"
        self.socket.sendall(message.encode())
        print(f"Sent message to server: {self.client_name}, {self.client_integer}")

        # Receive and process the server's response
        self.handle_server_response()

        # Close the connection
        self.socket.close()

    def get_user_input(self):
        while True:
            try:
                user_input = int(input("Enter an integer between 1 and 100: "))
                if 1 <= user_input <= 100:
                    return user_input
                else:
                    print("Please enter a number within the range (1-100).")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def handle_server_response(self):
        try:
            # Receive server response
            data = self.socket.recv(1024).decode()
            if not data:
                print("No data received from server.")
                return

            # Extract server name and server integer from the response
            server_message = data.split(',')
            server_name = server_message[0]
            server_integer = int(server_message[1])

            # Display information
            print(f"Received message from {server_name}")
            print(f"{self.client_name}'s number: {self.client_integer}")
            print(f"{server_name}'s number: {server_integer}")
            print(f"Sum: {self.client_integer + server_integer}")
       

        except Exception as e:
            print(f"Error handling server response: {e}")

# To run the client:
if __name__ == "__main__":
    client = Client()
    client.start()
