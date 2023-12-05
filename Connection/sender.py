#%%
import socket
import keyboard

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

# Keep the connection open (while loop) untill the user presses 'q'
while True:

    # QUIT
    if keyboard.is_pressed("q"):
        # close the connection
        client_socket.close()
        while keyboard.is_pressed("q"):
            pass

        break

    # ONE
    if keyboard.is_pressed("1"):
        print("1 pressed")
        client_socket.send("1".encode())

        while keyboard.is_pressed("1"):
            pass

    # TWO
    elif keyboard.is_pressed("2"):
        print("2 pressed")
        client_socket.send("2".encode())

        while keyboard.is_pressed("2"):
            pass

    # THREE
    elif keyboard.is_pressed("3"):
        print("3 pressed")
        client_socket.send("3".encode())

        while keyboard.is_pressed("3"):
            pass

    # FOUR
    elif keyboard.is_pressed("4"):
        print("4 pressed")
        client_socket.send("4".encode())

        while keyboard.is_pressed("4"):
            pass

    # if the client side return q quit the connection
    received_message = client_socket.recv(1024).decode()
    print(received_message)

    if received_message == "q":
        print("Connection closed by the client.")
        break
# %%
