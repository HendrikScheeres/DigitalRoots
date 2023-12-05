#%%
import keyboard
import serial
import socket
import time


# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the server's IP address and port number
server_ip = '192.168.178.43'  # Change this to the server's IP
server_port = 5555  # Use the same port number as the server

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to the server.")

# Receive a message from the server
received_message = client_socket.recv(1024).decode()

# if the message is Test, send the same message as reply
if received_message == "Test":
    client_socket.send(received_message.encode())
    print("Test message received and sent back.")
else:
    print("Test message not received.")

#% print all possible com ports
ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

# Initialize serial communication with Arduino (CHANGE THIS TO YOUR OWN COM PORT)
arduino_serial = serial.Serial('COM3', 9600, timeout=1)

# Wait 2 seconds for the communication to get established
time.sleep(2)

while True:
    # Receive data from the server
    data = client_socket.recv(1024).decode()
    
    if not data:
        break

    print(f"Received from server: {data}")

    # React based on received message
    if data == '1':
        print("Message 1 received, performing action...")
        # Perform action for message 1
        arduino_serial.write(b'1')

        # send a reply to the server that 1 was received and action was performed
        client_socket.send('1 was received'.encode())

    elif data == '2':
        print("Message 2 received, performing action...")
        # Perform action for message 2
        arduino_serial.write(b'2')

        # send a reply to the server that 2 was received and action was performed
        client_socket.send('2 was received'.encode())

    elif data == '3':
        print("Message 3 received, performing action...")
        # Perform action for message 3
        arduino_serial.write(b'3')

        # send a reply to the server that 3 was received and action was performed
        client_socket.send('3 was received'.encode())

    elif data == '4':
        print("Message 4 received, performing action...")
        # Perform action for message 4
        arduino_serial.write(b'4')

        # send a reply to the server that 4 was received and action was performed
        client_socket.send('4 was received'.encode())

    # check for messages from arduino
    arduino_data = arduino_serial.readline().decode().strip()
    if arduino_data:
        print(f"Received from Arduino: {arduino_data}")
        client_socket.send(arduino_data.encode())

    elif data == 'q':
        # Close the connection
        client_socket.close()
        break

# Close the connection
client_socket.close()
arduino_serial.close()
# %%
