"""
MAIN SCRIPT
This script is used to run the neural network.
The neural network is trained in the train.py script.
The weights are saved in the weights.npz file.
The weights are loaded in the transformer.py script.
The transformer.py script is used to transform the input data into the output data.
The output data is a one-hot encoded vector.
The one-hot encoded vector is converted to a class label.
The class label is sent to the receiver.
"""
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

from capacitiveSensor import serialEvent, Voltage3, Time3, test_connection, send_data, plot_data
from transformer import transformer, load_weights
from server import set_connection, send_data

data_dir = 'data/'
sort_of_weights = "min_max" # "min_max" or "z-scored"
sampleRate = 50 # sample rate in Hz


# TO-DO SAVE AND LOAD THE MIN MAX OF THE SCALING FOR COMPARISON
# CREATE THE TRANSFORMER LOGIC


def main():

    plantStatus = "Listening" #  "Listening", "Resting"
    output_sum = np.zeros([4, 1])
    start_time = time.time()
    print("starting serial event, 5 seconds startup")
    while (time.time() - start_time) < 5:
        Voltage3 = serialEvent()


    # connect to the client
    client_socket, client_address = set_connection()


    # run the serial event for 10 seconds just to check if it works and to get the min and max voltage for normalization
    # There are two types of normalization 
    # 1. min-max normalization
    # 2. standardization
    
    # MIN-MAX normalization 
    # measure 10 seconds of data and get the min and max voltage
    start_time = time.time()
    print("scaling the signal, 10 seconds")

    # get the max and min voltage
    max_voltage = 0
    min_voltage = 500

    # print the max and min of Voltage3
    while (time.time() - start_time) < 10:
        
        # if the timer has passed a second, print the max and min voltage
        if (time.time() - start_time) > 1:
            temp_max = max(serialEvent())
            time.sleep(0.01)
            temp_min = min(serialEvent())    

            if temp_max > max_voltage:
                max_voltage = temp_max
            if temp_min < min_voltage:
                min_voltage = temp_min

        # after 5 seconds print once that the user should touch the sensor
        if (time.time() - start_time) > 5 and (time.time() - start_time) < 5.02:
            print("touch the sensor")
            time.sleep(0.01)

    print("max voltage: ", max_voltage)
    print("min voltage: ", min_voltage)
    print("Done with scaling")

    # Import the scaling parameters from the training (Weights/scaling_values.npz)
    # load the scaling values
    scaling_values = np.load('weights/scaling_values.npz')
    print("scaling values in training")
    print("min voltage: ", scaling_values["min"])
    print("max voltage: ", scaling_values["max"])

    # Z-score normalization
    # while (time.time() - start_time) < 5:
    #     time.sleep (0.01)
    #     Voltage3 = serialEvent()
    #     voltage_copy = voltage_copy + np.array(Voltage3)

    # load the weights
    w_i_h, w_h_o, b_i_h, b_h_o = load_weights(sort_of_weights)

    output_sum = np.zeros([4, 1])
    sample_counter = 0 
    sample_threshold = 30000 

    # start the timer
    while True:

        if plantStatus == "Listening":

            Voltage3 = serialEvent()

            # make an array copy of voltage3
            voltage_copy = np.copy(np.array(Voltage3))

            # check if the voltage is not None and is longer than 150
            if voltage_copy is not None and voltage_copy.size > 149:

                # normalize the voltage array
                voltage_copy = (voltage_copy - min_voltage) / (max_voltage - min_voltage)

                output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)

                # add the output to the output sum
                output_sum += output

                # increment the sample counter
                sample_counter += 1

                # if the sample counter is equal to the sample threshold, send the data
                if sample_counter > sample_threshold:
                    # get the average output
                    output_average = output_sum / sample_threshold

                    # get the class label
                    class_label = np.argmax(output_average)

                    # convert the class label to a string
                    class_label = str(class_label)

                    # send the class label
                    print(class_label)

                    # reset the sample counter
                    sample_counter = 0

                    # reset the output sum
                    output_sum = np.zeros([4, 1])

                    # go into rest mode
                    if np.argmax(output_average) != 0:

                        # send the class label
                        send_data(client_socket, class_label)

                        plantStatus = "Resting"

                        print("going into rest mode")

            #KEYPRESSES
            # if i press 'p' on the keyboard, plot the data
            if keyboard.is_pressed('p'):
                plot_data()

            # if i press 'q' on the keyboard, quit the program
            if keyboard.is_pressed('q'):
                print("quitting")
                break
            
            if keyboard.is_pressed('r'):
                print("resting")
                plantStatus = "Resting"

            # transform the input
            if keyboard.is_pressed('t'):
                plot_data()
                print("transforming input")
                Voltage3 = serialEvent()
                # make an array copy of voltage3
                voltage_copy = np.copy(Voltage3)

                # normalize the voltage array
                voltage_copy = (voltage_copy - min_voltage) / (max_voltage - min_voltage)

                output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)

                # print the output
                print("output: ")
                print(np.argmax(output))
    
            #increment the sample counter
            sample_counter += 1
        
        elif plantStatus == "Resting":

            # wait for 4 seconds
            time.sleep(15)

            # if i press 'q' on the keyboard, quit the program
            if keyboard.is_pressed('q'):
                print("quitting")
                break

            print("plant is set to listening again")
            plantStatus = "Listening"

            # # listen untill you receive data back from the client
            # while True:
            #     # receive the data
            #     data = client_socket.recv(1024)
            #     data = data.decode("utf-8")

            #     # if the data is not empty, print it and break the loop
            #     if data:
            #         print(data)
            #         print("It is now listening again")
            #         plantStatus = "Listening"
            #         break        
                    
                
            




    

    


                      

if __name__ == "__main__":
    main()
# %%
