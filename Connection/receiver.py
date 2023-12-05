#%%
import socket
import keyboard

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server's IP address and port number
server_ip = '192.168.178.43'  # Change this to the server's IP
server_port = 5555  # Use the same port number as the server

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to the server.")

# Receive a message from the server
received_message = client_socket.recv(1024).decode()

# if the message is Test, send the same message as reply
if received_message == "Test":
    client_socket.send(received_message.encode())
    print("Test message received and sent back.")
else:
    print("Test message not received.")

while True:
    # Receive data from the server
    data = client_socket.recv(1024).decode()
    
    if not data:
        break

    print(f"Received from server: {data}")

    # React based on received message
    if data == '1':
        print("Message 1 received, performing action...")
        # Perform action for message 1

# Close the connection
client_socket.close()

# %%
