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

#%% Connect to the serve
# Send data to server
message_to_send = "Connected"
client_socket.send(message_to_send.encode())

# Receive response from server
data_received = client_socket.recv(1024)
if data_received.decode() == "Connected":
    print("Client connected successfully")
else:
    print("Client connection failed")

#%%
# While true loop to receive data until client presses "q"
while True:
    # Receive data from server
    data_received = client_socket.recv(1024)

    # if q is pressed, break the loop and close the connection
    if data_received.decode() == "q":
        print("Server disconnected")
        break
    else:
        print("Message received from server:", data_received.decode())

    # print the message received from the server
    print("Message received from server:", data_received.decode())
    
    # Send data to server
    message_to_send = "Hello from client"
    client_socket.send(message_to_send.encode())
    print("Message sent to server")

    # if q is pressed, break the loop and close the connection
    if message_to_send == "q":
        break

#%% Close the connection
client_socket.close() 