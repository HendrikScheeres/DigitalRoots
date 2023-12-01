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

#%% MAIN

if __name__ == "__main__":
    # define the ip and port
    computer1_ip = "25.42.216.73"   # Replace with the actual IP of computer1
    computer1_port = 12345

    # Start a while loop and print the data received every 10 seconds
    while True:
        # receive the data
        data = server_socket.recv(1024)

        # wait for 3 seconds
        time.sleep(3)
        # print the data
        print(data)