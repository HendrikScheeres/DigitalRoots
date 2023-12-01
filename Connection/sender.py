import serial
import time

# Define the serial port and baud rate
ser = serial.Serial('COM1', 9600)  # Change 'COM1' to the appropriate port on your system

# Wait for the serial connection to be established
time.sleep(2)

# Send data
data_to_send = "Hello, Computer B!"
ser.write(data_to_send.encode())  # Sending encoded data

# Close the serial connection
ser.close()