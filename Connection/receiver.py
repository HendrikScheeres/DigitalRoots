#%%
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server machine name and port
host = socket.gethostname()
port = 12345

# Connect to the server
client_socket.connect((host, port))

while True:
    # Send data to the server
    message = input("Enter your message: ")
    client_socket.send(message.encode())

    # Receive a response from the server
    data = client_socket.recv(1024).decode()
    print(f"Received from server: {data}")

client_socket.close()
