#%% IMPORTS
import socket
import keyboard
import time
import numpy as np
#%%
# Get the ip address of the computer
import socket

computer2_ip = '25.42.180.191'  # Replace with the actual IP of computer1
computer2_port = 12345  # Same port as computer1

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to computer1
client_socket.connect((computer2_ip, computer2_port))
print(f"Connected to {computer2_ip}:{computer2_port}")

# Receive data from computer1
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

# Close the socket
client_socket.close()