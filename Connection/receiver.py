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

# Keep the connection open (while loop) untill the user presses 'q'
while True:

    print('Receiving....')

    # Quit
    if keyboard.is_pressed("q"):
        client_socket.send("q".encode())

        # close the connection
        client_socket.close()
        break

    # Listen if the server sends a message
    received_message = client_socket.recv(1024).decode()

    print(received_message)

    # if a message is sent, print it
    if received_message:
        print(f"Received: {received_message}")

        if received_message == "q":
            print("Connection closed by the server.")
            break

# %%
