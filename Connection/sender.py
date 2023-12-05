#%%
import socket
import time
import keyboard

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
print(f"Sender IPv4 Address: {ip_address}")

# Receiver IPv4 Address
receiver_ip_address = "192.168.178.227"

#%% Connect to the server

# Connect to the server
server_socket.connect((receiver_ip_address, port))

# Send data to server
message_to_send = "Connected"
server_socket.send(message_to_send.encode())

# # Bind to the port
# server_socket.bind((host, port))

# # Listen for incoming connections
# server_socket.listen(5)

# print('Waiting for incoming connections...')

# # Establish connection with client
# client_socket, addr = server_socket.accept()
# print('Got connection from', addr)

# # Receive data from client
# data_received = client_socket.recv(1024)
# if data_received.decode() == "Connected":
#     print("Client connected successfully")
# else:
#     print("Client connection failed")   

# # Send a response to client
# message_to_send = "Connected"
# client_socket.send(message_to_send.encode())

#%%
# # While true loop to send data until client presses "q"
# while True:

#     message_to_send = "Hello from server"
#     client_socket.send(message_to_send.encode())
#     print("Message sent to client")
#     time.sleep(1)

#     # if the user presses 0, send 0 to the client
#     if keyboard.is_pressed('0'):
#         message_to_send = "0"
#         client_socket.send(message_to_send.encode())
#         print("Message sent to client")
#         time.sleep(1)

#         # if the user presses 0, send 0 to the client
#     elif keyboard.is_pressed('1'):
#         message_to_send = "1"
#         client_socket.send(message_to_send.encode())
#         print("Message sent to client")
#         time.sleep(1)
    
#     # if the user presses 2, send 2 to the client
#     elif keyboard.is_pressed('2'):
#         message_to_send = "2"
#         client_socket.send(message_to_send.encode())
#         print("Message sent to client")
#         time.sleep(1)

#     # if the user presses 3, send 3 to the client
#     elif keyboard.is_pressed('3'):
#         message_to_send = "3"
#         client_socket.send(message_to_send.encode())
#         print("Message sent to client")
#         time.sleep(1)

#     # Receive data from client
#     data_received = client_socket.recv(1024)

#     if data_received.decode() == "q":
#         print("Client disconnected")
#         break
#     else:
#         print("Message received from client:", data_received.decode())

#     # if q is pressed, break the loop and close the connection
#     if keyboard.is_pressed('q'):
#         print("Server disconnected")
#         break

# #%% Close the connection
# client_socket.close()