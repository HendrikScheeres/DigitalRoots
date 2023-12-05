#%%
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server's IP address and port number
server_ip = '192.168.178.43'  # Change this to the server's IP
server_port = 5555  # Use the same port number as the server

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to the server.")

while True:
    # Send data to the server
    message = input("Enter message to send: ")
    client_socket.send(message.encode())

    # Receive data from the server
    data = client_socket.recv(1024).decode()
    print(f"Received from server: {data}")

# Close the connection
client_socket.close()
