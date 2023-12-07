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

        # wait untill you receive "Done" back from the arduino
        while True:
            arduino_data = arduino_serial.readline().decode().strip()
            print(arduino_data)
            if arduino_data == "one":

                # send a reply to the server that 1 was received and action was performed
                client_socket.send("Done".encode())
                print("Arduino Done")
                break

            if keyboard.is_pressed == 'q':
                break
        

    elif data == '2':
        print("Message 2 received, performing action...")
        # Perform action for message 2
        arduino_serial.write(b'2')

        # wait untill you receive "done" back from the arduino
        while True:
            arduino_data = arduino_serial.readline().decode().strip()
            print(arduino_data)
            if arduino_data == "Done":

                # send a reply to the server that 1 was received and action was performed
                client_socket.send("Done".encode())
                print("Arduino done")
                break
            if keyboard.is_pressed == 'q':
                break

    elif data == '3':
        print("Message 3 received, performing action...")
        # Perform action for message 3
        arduino_serial.write(b'3')

         # wait untill you receive "done" back from the arduino
        while True:
            arduino_data = arduino_serial.readline().decode().strip()
            if arduino_data == "Done":

                # send a reply to the server that 1 was received and action was performed
                client_socket.send("Done".encode())
                break
            if keyboard.is_pressed == 'q':
                break

    elif data == '4':
        print("Message 4 received, performing action...")
        # Perform action for message 4
        arduino_serial.write(b'4')

        # wait untill you receive "Done" back from the arduino
        while True:
            arduino_data = arduino_serial.readline().decode().strip()
            if arduino_data == "done":

                # send a reply to the server that 1 was received and action was performed
                client_socket.send("Done".encode())
                break
            if keyboard.is_pressed == 'q':
                break

    elif data == 'q':

        # send a message to the server that the client is closing the connection
        client_socket.send('Closing connection from receiver end'.encode())
        
        # Close the connection
        client_socket.close()
        break  

# Close the connection
client_socket.close()
arduino_serial.close()
# %%
