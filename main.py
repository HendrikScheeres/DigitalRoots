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

def main():

    # this is the number of samples averaged per gesture
    transform_every = 0

    # run the serial event for 10 seconds just to check if it works and to get the min and max voltage for normalization
    start_time = time.time()

    # load the weights
    w_i_h, w_h_o, b_i_h, b_h_o = load_weights()

    # There are two types of normalization 
    # 1. min-max normalization
    # 2. standardization
    # Make sure the weights are trained with the same normalization method as the input data
    # the min and max voltage are used for normalization

    print("starting serial event, 10 seconds of measurements")
    while (time.time() - start_time) < 10:
        serialEvent()

        # 3 seconds print something
        if (time.time() - start_time) > 3 and (time.time() - start_time) < 3.1:
            print("Touch near the electrode")



    while True:
        serialEvent()

        # if i press 'p' on the keyboard, plot the data
        if keyboard.is_pressed('p'):
            plot_data()

        # if i press 'q' on the keyboard, quit the program
        if keyboard.is_pressed('q'):
            break

        # transform the input
        if keyboard.is_pressed('t'):
            print("transforming input")

            # make an array copy of voltage3
            voltage_copy = np.array(Voltage3)
            output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)

            # print the output
            print("output: ")
            print(output)
            plot_data()

if __name__ == "__main__":
    main()
# %%
