#%% All the imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import socket
import time
import serial.tools.list_ports 
import matplotlib.pyplot as plt
from matplotlib import style
import keyboard
import numpy as np
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

def load_weights(): 

    # load the weights from the file
    weights = np.load('weights.npz')

    w_i_h = weights['w_i_h']
    w_h_o = weights['w_h_o']
    b_i_h = weights['b_i_h']
    b_h_o = weights['b_h_o']

    print("weights loaded")
    weights_loaded = True
    return w_i_h, w_h_o, b_i_h, b_h_o

def transformer(v, w_i_h, w_h_o, b_i_h, b_h_o):

    #print(v.shape)
    # clip the voltage array to 150
    v = v[:150]

    #print(v)

    # make sure v is a numpy array with dimensions 150,1
    v = np.array(v)
    v = v.reshape((150, 1))

    print("The shape of v is:")
    print(v.shape)
    
    #forward prop. input -> hidden
    h_pre = b_i_h + w_i_h @ v
        
    # sigmoid activation function
    h = 1 / (1 + np.exp(-h_pre))
        
    # forward prop. hidden -> output
    o_pre = b_h_o + w_h_o @ h
    
    o = 1 / (1 + np.exp(-o_pre))
    print("o: ")
    print(o)

    print("Predicted: ", np.argmax(o))
    
    return o

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

def main():

    # data_save_iter
    data_save_iter = 0

    # this is the number of samples averaged per gesture
    transform_every = 0
   
    # this is the number of samples saved per gesture
    save_rate = 200

    # max nr of samples
    max_n = 100000

    # sleep timer
    sleep_timer = 0.05

    # make an empty (n,1,150) array for the voltage data
    data_array = np.zeros((max_n, 1, 150))
    # make an empty (n,1,4) array for the target data
    target_array = np.zeros((max_n, 1, 4))

    gest1_index = 0
    gest2_index = 0
    gest3_index = 0
    gest4_index = 0

    # run the serial event for 10 seconds just to check if it works and to get the min and max voltage for normalization
    start_time = time.time()

    # There are two types of normalization 
    # 1. min-max normalization
    # 2. standardization
    # Make sure the weights are trained with the same normalization method as the input data
    # the min and max voltage are used for normalization

    print("starting serial event, 10 seconds of measurements")
    while (time.time() - start_time) < 10:
        serialEvent()
        # save the minimum and maximum values of the voltage
        if len(Voltage3) > 0:
            min_voltage = min(Voltage3)
            max_voltage = max(Voltage3)
  
    print("min voltage calculated in loop: " + str(min_voltage))
    print("max voltage calculated in loop: " + str(max_voltage))

    # load the min and max voltage from min_max.npz
    min_max = np.load('min_max.npz')
    min_voltage = min_max['min_data']
    max_voltage = min_max['max_data']
    max_volatge = 400
    print("min voltage calculated in training: " + str(min_voltage))
    print("max voltage calculated in training: " + str(max_voltage))

    # test the connection
    test_connection('Test', 12345)   

    # load the weights
    w_i_h, w_h_o, b_i_h, b_h_o = load_weights()
    output = np.zeros((4, 1))

    # transform the data
    voltage_copy = np.array(Voltage3)
    voltage_copy = (voltage_copy - min_voltage) / (max_voltage - min_voltage)
    output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)
    plot_data()

    # make the socket connection -> see test_connection script

    while True:
        serialEvent()

        # if i press 'p' on the keyboard, plot the data
        if keyboard.is_pressed('p'):
            plot_data()

        # if i press 'q' on the keyboard, quit the program
        if keyboard.is_pressed('q'):
            break

        # if i press 's' on the keyboard, save the data array and target array    
        if keyboard.is_pressed('s'):

            # open data.npz and clear it
            np.savez('data', data=data_array, target=target_array)
            print("saved data")
            print("stopping loop")
            break

        # if either 1,2 3 or 4 is pressed
        if keyboard.is_pressed('1'):
            print("saving as gesture 1")
            plot_data()

            for i in range(save_rate):
                # shorten the time and voltage arrays to 150
                TimeSave = Time3[:150]
                VoltageSave = Voltage3[:150]

                # save the time and voltage arrays to a file
                np.savez("1/"+ str(gest1_index), target= 1, time=TimeSave, voltage=VoltageSave)
                gest1_index += 1

                # add the data and target to the arrays
                data_array[data_save_iter, 0 , :] = VoltageSave
                target_array[data_save_iter, 0 ,:] = [1, 0, 0, 0]
                data_save_iter += 1

                # wait 25 ms
                time.sleep(sleep_timer)
            print("done saving 1")
        
        if keyboard.is_pressed('2'):
            print("saving as gesture 2")
            plot_data()

            for i in range(save_rate):
                # shorten the time and voltage arrays to 150
                TimeSave = Time3[:150]
                VoltageSave = Voltage3[:150]

                # save the time and voltage arrays to a file
                np.savez("2/"+ str(gest2_index), target= 2, time=TimeSave, voltage=VoltageSave)
                gest2_index += 1

                # add the data and target to the arrays
                data_array[data_save_iter, 0 , :] = VoltageSave
                target_array[data_save_iter, 0 ,:] = [0, 1, 0, 0]
                data_save_iter += 1

                # wait 25 ms
                time.sleep(sleep_timer)
            print("done saving 2")
        
        if keyboard.is_pressed('3'):
            print("saving as gesture 3")
            plot_data()

            for i in range(save_rate):
                # shorten the time and voltage arrays to 150
                TimeSave = Time3[:150]
                VoltageSave = Voltage3[:150]

                # save the time and voltage arrays to a file
                np.savez("3/"+ str(gest3_index), target= 3, time=TimeSave, voltage=VoltageSave)
                gest3_index += 1

                # add the data and target to the arrays
                data_array[data_save_iter, 0 , :] = VoltageSave
                target_array[data_save_iter, 0 ,:] = [0, 0, 1, 0]
                data_save_iter += 1

                # wait 25 ms
                time.sleep(sleep_timer)
            print("done saving 3")
        
        if keyboard.is_pressed('4'):
            print("saving as gesture 4")
            plot_data()

            for i in range(save_rate):
                # shorten the time and voltage arrays to 150
                TimeSave = Time3[:150]
                VoltageSave = Voltage3[:150]

                # save the time and voltage arrays to a file
                np.savez("4/"+ str(gest4_index), target= 4, time=TimeSave, voltage=VoltageSave)
                gest4_index += 1

                # add the data and target to the arrays
                data_array[data_save_iter, 0 , :] = VoltageSave
                target_array[data_save_iter, 0 ,:] = [0, 0, 0, 1]
                data_save_iter += 1

                # wait 25 ms
                time.sleep(sleep_timer)
            print("done saving 4")

        # transform the input
        if keyboard.is_pressed('t'):
            print("transforming input")

            # make an array copy of voltage3
            voltage_copy = np.array(Voltage3)
            voltage_copy = (voltage_copy - min_voltage) / (max_voltage - min_voltage)
            output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)

            # print the output
            print("output: ")
            print(output)
            plot_data()

        # every 1000 samples translate the signal
        if transform_every == 100:
            print("transforming input")
            # make an array copy of voltage3
            voltage_copy = np.array(Voltage3)
            voltage_copy = (voltage_copy - min_voltage) / (max_voltage - min_voltage)
            output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)
            transform_every = 0

            # print the output
            print("output: ")
            print(output)

            # send the data to the server
            send_data('145.137.73.169',12345, output)
        

        # increment the transform_every
        transform_every += 1
        


if __name__ == "__main__":
    main()
    
#%%