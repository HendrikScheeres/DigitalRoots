#%% IMPORTS
import socket
import keyboard
import time
import numpy as np
#%%
# Get the ip address of the computer
import socket

hostname = socket.gethostname()
ip_address = "25.42.216.73" 

print(f"Hostname: {hostname}")
print(f"IPv4 Address: {ip_address}")

# if the ip_address is not 192.168.178.43 then change your computer ip address to this number
