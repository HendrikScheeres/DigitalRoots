#%% IMPORTS
import socket
import keyboard
import time
import numpy as np
#%%
# Get the ip address of the computer
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IPv4 Address: {ip_address}")

# if the ip_address is not 192.168.178.43 then change your computer ip address to this number

#%%
import socket

computer1_ip = '25.42.180.191'  # Replace with the actual IP of computer1
computer1_port = 12345

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to computer1's IP and port
server_socket.bind((computer1_ip, computer1_port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Waiting for a connection on {computer1_ip}:{computer1_port}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Send data to computer2
client_socket.sendall(b"Hello from computer 1!")

# Close the sockets
client_socket.close()
server_socket.close()
