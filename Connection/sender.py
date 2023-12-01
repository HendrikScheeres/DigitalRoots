#%%
import socket
import time

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
host = socket.gethostname()
port = 12345

# print the host and port
print(f"Hostname: {host}")
print(f"Port: {port}")

# The IPv4 address of the computer
ip_address = socket.gethostbyname(host)
print(f"IPv4 Address: {ip_address}")

#%%

# Bind to the port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print('Waiting for incoming connections...')

# Establish connection with client
client_socket, addr = server_socket.accept()
print('Got connection from', addr)

# Receive data from client
data_received = client_socket.recv(1024)
print('Received:', data_received.decode())

# Send a response to client
message_to_send = 'Hello, client! Thanks for connecting.'
client_socket.send(message_to_send.encode())

# Close the connection
client_socket.close()