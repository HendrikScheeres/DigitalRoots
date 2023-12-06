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

data_dir = 'data/'
sort_of_weights = "min_max" # "min_max" or "z-scored"

def main():

    start_time = time.time()
    print("starting serial event, 5 seconds startup")
    while (time.time() - start_time) < 3:
        serialEvent()

    # run the serial event for 10 seconds just to check if it works and to get the min and max voltage for normalization
    # There are two types of normalization 
    # 1. min-max normalization
    # 2. standardization
    # Make sure the weights are trained with the same normalization method as the input data
    # the min and max voltage are used for normalization

    # get the min and max voltage
    lowest = 1000
    highest = 0

    # load the weights
    w_i_h, w_h_o, b_i_h, b_h_o = load_weights(sort_of_weights)

    while True:
        Voltage3 = serialEvent()

        # if i press 'p' on the keyboard, plot the data
        if keyboard.is_pressed('p'):
            plot_data()

        # if i press 'q' on the keyboard, quit the program
        if keyboard.is_pressed('q'):
            print("quitting")
            break

        # transform the input
        if keyboard.is_pressed('t'):
            plot_data()
            print("transforming input")
            Voltage3 = serialEvent()
            # make an array copy of voltage3
            voltage_copy = np.array(Voltage3)

            # normalize the voltage array
            voltage_copy = (voltage_copy - lowest) / (highest - lowest)

            output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)

            # print the output
            print("output: ")
            print(output)
            

if __name__ == "__main__":
    main()
# %%
