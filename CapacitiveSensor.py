#%% IMPORTS
import keyboard
import serial
import socket
import time
import numpy as np
import matplotlib.pyplot as plt
import serial.tools.list_ports 
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


# Initialize all variables
ErrorCounter = 0

# List the serial ports:
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

#%% Functions and variables for the serial communication
NumOfSerialBytes = 8  # The size of the buffer array
serialInArray = [0] * NumOfSerialBytes  # Buffer array
Time3 = []
Voltage3 = []
weights_loaded = False

myPort = serial.Serial(port='COM7',  baudrate=115200, timeout=.1)
myPort.reset_input_buffer()
myPort.reset_output_buffer()
myPort.timeout = 0.1
serialCount = 0
TotalReceived = 0


def serialEvent():
    global serialCount, xMSB, xLSB, yMSB, yLSB, Command, xValue, yValue, DataReceived, Error, ErrorCounter, TotalReceived
    
    # Read the serial port
    while myPort.in_waiting > 0:
        inByte = ord(myPort.read(1)) # Read one byte from the serial buffer

        if inByte == 0: # Check if the byte is zero
            serialCount = 0 # Reset the serialCount
    
        if inByte > 255: 
            print(" inByte = " + str(inByte))
            exit()

        serialInArray[serialCount] = inByte
        serialCount += 1

        Error = True

        if serialCount >= NumOfSerialBytes:
            serialCount = 0
            TotalReceived += 1

            Checksum = 0

            for i in range(NumOfSerialBytes - 1):
                Checksum += serialInArray[i]
            
            Checksum = Checksum % 255

            if Checksum == serialInArray[NumOfSerialBytes - 1]: # Checksum OK
                Error = False
                DataReceived = True
            else:
                Error = True
                ErrorCounter += 1
                DataReceived = False
        
        if not Error:
            zeroByte = serialInArray[6]
            xLSB = serialInArray[3]
            if zeroByte & 1 == 1:
                xLSB = 0
            xMSB = serialInArray[2]
            if zeroByte & 2 == 2:
                xMSB = 0
            yLSB = serialInArray[5]
            if zeroByte & 4 == 4:
                yLSB = 0
            yMSB = serialInArray[4]
            if zeroByte & 8 == 8:
                yMSB = 0

            Command = serialInArray[1]

            xValue = (xMSB << 8) | xLSB
            yValue = (yMSB << 8) | yLSB

            switch_command(Command)

            # return the Voltage array
            return Voltage3
        
            
# Define switch_command function
def switch_command(Command):
    global DynamicArrayTime3, DynamicArray3, DynamicArrayTime2, DynamicArray2, current, DynamicArrayTime, DynamicArrayPower, Time3, Voltage3, DataReceived1, DataReceived2, DataReceived3

    # Receive array1 and array2 from chip, update oscilloscope
    if Command == 1:
        DynamicArrayTime3.append(xValue)
        DynamicArray3.append(yValue)

    elif Command == 2:
        DynamicArrayTime3 = []
        DynamicArray3 = []

    elif Command == 3:
        Time3 = DynamicArrayTime3
        Voltage3 = DynamicArray3
        DataReceived3 = True

    # Receive array2 and array3 from chip
    elif Command == 4:
        DynamicArrayTime2.append(xValue)
        DynamicArray2.append((yValue - 16000.0) / 32000.0 * 20.0)

    elif Command == 5:
        DynamicArrayTime2 = []
        DynamicArray2 = []

    elif Command == 6:
        Time2 = DynamicArrayTime2
        current = DynamicArray2
        DataReceived2 = True

    # Receive a value of calculated power consumption & add it to the PowerArray.
    elif Command == 20:
        PowerArray.append(yValue)

    elif Command == 21:
        DynamicArrayTime.append(xValue)
        DynamicArrayPower.append(yValue)

# Interaction functions
def plot_data():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(Time3, Voltage3)
    ax1.set_xlim(0, 160)
    ax1.set_ylim(0, 500)
    plt.show()


# test the connection
def test_connection(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall('Helloo ZHUUUUUU'.encode())
        data = s.recv(1024)
        print('Received', repr(data))
    
# make a send data function that only sends the data once
def send_data(ip, port , variable):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall(variable.encode())

