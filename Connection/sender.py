import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name and specify a port
host = socket.gethostname()
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server listening...")

# Accept incoming connections
client_socket, addr = server_socket.accept()
print(f"Connection from {addr} established.")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Received from client: {data}")

    # Send a response back to the client
    response = input("Enter your response: ")
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
