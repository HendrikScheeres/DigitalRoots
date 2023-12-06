"""
DATA COLLECTION SCRIPT
This script is used to collect data from the capacitive sensor.
The data is saved in .npz files, which are numpy arrays.
The data is saved in the following format:
    data = (n, 1, 150)
    target = (n, 1, 4)
    where n is the number of samples
    1 is the number of channels
    150 is the number of samples per channel
    4 is the number of classes	
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
from capacitiveSensor import serialEvent, Voltage3, Time3, test_connection, plot_data

data_dir = 'Data/'
save_seperately = False

def main():

    data_save_iter = 0 # this is the index of the data array
    save_rate = 200 # this is the number of samples saved per keypress
    max_n = 100000 # this is the maximum number of samples that can be saved
    save_delay = 0.10 # this is the delay between each sample saved

    # voltage and target arrays
    data_array = np.zeros((max_n, 1, 150))
    target_array = np.zeros((max_n, 1, 4))

    # gesture indexes
    gest1_index = 0
    gest2_index = 0
    gest3_index = 0
    gest4_index = 0

    # run the serial event for 5 seconds to start up
    start_time = time.time()
    print("starting serial event, 3 seconds startup")
    while (time.time() - start_time) < 5:
        serialEvent()

    # print the first plot
    plot_data()

    # open the serial port and start measuring
    while True:
        Voltage3 = serialEvent()

        # if i press 'p' on the keyboard, plot the data
        if keyboard.is_pressed('p'):
            plot_data()

        # if i press 'q' on the keyboard, quit the program
        if keyboard.is_pressed('q'):
            print("quitting")
            break

        # if i press 's' on the keyboard, save the data array and target array    
        if keyboard.is_pressed('s'):

            # save the data in the Data folder
            print("saving data")
            np.savez(data_dir + "data", data=data_array, target=target_array)
            print("saved data")
            print("Data was saved! Press q to quit")

        # if either 1,2 3 or 4 is pressed
        if keyboard.is_pressed('1'):
            print("saving as gesture 1")
            plot_data()

            for i in range(save_rate):
                # shorten the time and voltage arrays to 150p1
                VoltageSave = Voltage3[:150]
                
                # add the data and target to the arrays and increment
                data_array[data_save_iter, 0 , :] = VoltageSave
                target_array[data_save_iter, 0 ,:] = [1, 0, 0, 0]
                data_save_iter += 1

                #  if save seperately is on
                if save_seperately:
                    # save the time and voltage arrays to a file
                    np.savez("Data/seperateSave/1/"+ str(gest1_index), target= 1, voltage=VoltageSave)
                    gest1_index += 1

                # wait
                time.sleep(save_delay)
            print("done saving 1")
        
        if keyboard.is_pressed('2'):
            print("saving as gesture 2")
            plot_data()

            for i in range(save_rate):
                # shorten the time and voltage arrays to 150
                TimeSave = Time3[:150]
                VoltageSave = Voltage3[:150]

                # add the data and target to the arrays
                data_array[data_save_iter, 0 , :] = VoltageSave
                target_array[data_save_iter, 0 ,:] = [0, 1, 0, 0]
                data_save_iter += 1

                # if save seperately is on
                if save_seperately:
                    # save the time and voltage arrays to a file
                    np.savez("2/"+ str(gest2_index), target= 2, time=TimeSave, voltage=VoltageSave)
                    gest2_index += 1

                # wait 
                time.sleep(save_delay)

            print("done saving 2")

        if keyboard.is_pressed('3'):
            print("saving as gesture 3")
            plot_data()

            for i in range(save_rate):
                # shorten the time and voltage arrays to 150
                TimeSave = Time3[:150]
                VoltageSave = Voltage3[:150]

                # add the data and target to the arrays
                data_array[data_save_iter, 0 , :] = VoltageSave
                target_array[data_save_iter, 0 ,:] = [0, 0, 1, 0]
                data_save_iter += 1

                # if save seperately is on
                if save_seperately:
                    # save the time and voltage arrays to a file
                    np.savez("3/"+ str(gest3_index), target= 3, time=TimeSave, voltage=VoltageSave)
                    gest3_index += 1

                # wait
                time.sleep(save_delay)

            print("done saving 3")

        if keyboard.is_pressed('4'):
            print("saving as gesture 4")
            plot_data()

            for i in range(save_rate):
                # shorten the time and voltage arrays to 150
                TimeSave = Time3[:150]
                VoltageSave = Voltage3[:150]

                # add the data and target to the arrays
                data_array[data_save_iter, 0 , :] = VoltageSave
                target_array[data_save_iter, 0 ,:] = [0, 0, 0, 1]
                data_save_iter += 1

                # if save seperately is on
                if save_seperately:
                    # save the time and voltage arrays to a file
                    np.savez("4/"+ str(gest4_index), target= 4, time=TimeSave, voltage=VoltageSave)
                    gest4_index += 1

                # wait
                time.sleep(save_delay)

            print("done saving 4")

if __name__ == "__main__":
    main()

# %%
