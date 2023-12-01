#%% IMPORTS
import socket
import keyboard
import time
import numpy as np
#%%
# Get the ip address of the computer
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IPv4 Address: {ip_address}")

# if the ip_address is not 192.168.178.43 then change your computer ip address to this number

#%% FUNCTIONS
def send_data(ip, port, variable):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    s.connect((ip, port))
    # send the input to the server
    s.sendall(variable.encode())
    # close the connection
    s.close()

#%% MAIN
if __name__ == "__main__":
    # define the ip and port
    ip = "62.163.195.37"
    port = 12345
    # start a loop and send the number I press to the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((ip_address, port))
        try:
            while True:
                # if a key is pressed, send the key to the server
                if keyboard.is_pressed('1'):
                    # change the variable to '1'
                    variable = '1'
                    # send the input to the server
                    s.sendall(variable.encode())
                    # wait for 1 second
                    time.sleep(1)
                elif keyboard.is_pressed('2'):
                    variable = '2'
                    # send the input to the server
                    s.sendall(variable.encode())
                    # wait for 1 second
                    time.sleep(1)
                elif keyboard.is_pressed('3'):
                    variable = '3'
                    # send the input to the server
                    s.sendall(variable.encode())
                    # wait for 1 second
                    time.sleep(1)
                elif keyboard.is_pressed('4'):
                    variable = '4'
                    # send the input to the server
                    s.sendall(variable.encode())
                    # wait for 1 second
                    time.sleep(1)
        except:
            pass
#%%
import requests

def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            return "Unable to retrieve IP address"
    except requests.RequestException as e:
        return f"Error: {e}"

external_ip = get_external_ip()
print(f"External IP Address: {external_ip}")