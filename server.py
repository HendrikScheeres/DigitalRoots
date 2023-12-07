#%%
import socket
import keyboard

# Check connection function
def set_connection():
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

    return client_socket, client_address


# Send data function that uses client_socket and client_address and a message
def send_data(client_socket, message):
    # Send a message to the client
    client_socket.send(message.encode())

    # wait untill the client sends "0" back
    while True:
        data = client_socket.recv(1024).decode()
        print(data)
        if data == "0":
            print("Action performed")
            break
        print("Got out of this loop")

# %%
