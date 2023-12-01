#%%
import serial

# Define the serial port and baud rate
ser = serial.Serial('COM1', 9600)  # Change 'COM1' to the appropriate port on your system

while True:
    # Wait for data to be available on the serial port
    if ser.in_waiting > 0:
        # Read the data from the serial port
        received_data = ser.readline().decode().strip()  # Decoding the received data
        print("Received:", received_data)
        break  # Break out of the loop after receiving data

# Close the serial connection
ser.close()