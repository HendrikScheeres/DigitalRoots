#%%
import socket11231231123
import keyboard

def get_key():
    while True:
        key = keyboard.read_event()
        if key.event_type == keyboard.KEY_DOWN:
            return key.name

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

# Test the connection by sending a message
message = "Test"
client_socket.send(message.encode())

# Check if the message was received correctly (compare the sent and received messages)
received_message = client_socket.recv(1024).decode()
print(f"Sent: {message}")
print(f"Received: {received_message}")

while True:
    key_pressed = get_key()

    if key_pressed == 'q':
        # send a message to the client that the server is closing the connection
        client_socket.send('Closing connection from sender end'.encode())
        break

    # Map keys to messages and send to the client
    if key_pressed in ['1', '2', '3']:
        client_socket.send(key_pressed.encode())

        # wait untill the client sends "0" back
        while True:
            data = client_socket.recv(1024).decode()
            print(data)
            if data == "0":
                print("Action performed")
                break
        print("Got out of this loop")

# Close the connection
client_socket.close()

# %%
