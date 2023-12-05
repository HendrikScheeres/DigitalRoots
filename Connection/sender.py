import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server's IP address and port number
server_ip = '192.168.178.43'  # Change this to the server's IP
server_port = 5555  # Choose a port number

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (max 1)
server_socket.listen(1)
print("Server is listening...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    if not data:
        break

    print(f"Received from client: {data}")

    # Send data back to the client
    message = input("Enter message to send: ")
    client_socket.send(message.encode())

# Close the connection
client_socket.close()
