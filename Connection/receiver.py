#%%
import socket

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

#%% FUNCTIONS
def receive_data(ip, port):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to the port
    s.bind((ip, port))
    # listen for incoming connections
    s.listen(1)
    # accept the connection
    conn, addr = s.accept()
    # print the address of the connection
    print("Connection address:", addr)
    # receive the data
    data = conn.recv(1024)
    # decode the data
    data = data.decode()
    # print the data
    print("Received data:", data)
    # close the connection
    conn.close()
    # return the data
    return data

#%% MAIN

if __name__ == "__main__":
    # define the ip and port
    computer1_ip = "25.42.216.73"   # Replace with the actual IP of computer1
    computer1_port = 12345

    # Start a while loop and print the data received every 10 seconds
    while True:
        # receive the data
        data = receive_data(computer1_ip, computer1_port)
        # wait for 3 seconds
        time.sleep(3)
        # print the data
        print(data)