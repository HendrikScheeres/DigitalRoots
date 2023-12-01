#%% IMPORTS
import socket
import keyboard
import time
import numpy as np
import subprocess

#%% GET THE IP ADDRESS
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
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
    ip = "62.163.195.37"
    port = 12345

    # Start a while loop and print the data received every 10 seconds
    while True:
        # receive the data
        data = receive_data(ip, port)
        # wait for 3 seconds
        time.sleep(3)
        # print the data
        print(data)