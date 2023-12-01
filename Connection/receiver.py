import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
host = socket.gethostname()
port = 12345

# print the host and port
print(f"Hostname: {host}")
print(f"Port: {port}")

# The IPv4 address of the computer
ip_address = socket.gethostbyname(host)
print(f"IPv4 Address: {ip_address}")

# Connect to the server
client_socket.connect((host, port))

# Send data to server
message_to_send = 'Hello, server! This is the client.'
client_socket.send(message_to_send.encode())

# Receive response from server
data_received = client_socket.recv(1024)
print('Received from server:', data_received.decode())

# Close the connection
client_socket.close()