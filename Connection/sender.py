#%% IMPORTS
import socket
import keyboard
import time
import numpy as np

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
    ip = "192.168.178.1"
    port = 12345
    # start a loop and send the number I press to the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((ip, port))
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