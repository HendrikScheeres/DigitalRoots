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

    # min and max voltage for min-max normalization
    min_voltage = 0
    max_voltage = 0 

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
    min_max = np.load(data_dir + 'min_max.npz')
    min_voltage = min_max['min_data']
    max_voltage = min_max['max_data']
    max_volatge = 400
    print("min voltage calculated in training: " + str(min_voltage))
    print("max voltage calculated in training: " + str(max_voltage))

    # test the connection
    #test_connection('Test', 12345)   

    # load the weights
    #w_i_h, w_h_o, b_i_h, b_h_o = load_weights()
    output = np.zeros((4, 1))

    # transform the data
    voltage_copy = np.array(Voltage3)
    voltage_copy = (voltage_copy - min_voltage) / (max_voltage - min_voltage)
    #output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)
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
        # if transform_every == 100:
        #     print("transforming input")
        #     # make an array copy of voltage3
        #     voltage_copy = np.array(Voltage3)
        #     voltage_copy = (voltage_copy - min_voltage) / (max_voltage - min_voltage)
        #     output = transformer(voltage_copy, w_i_h, w_h_o, b_i_h, b_h_o)
        #     transform_every = 0

        #     # print the output
        #     print("output: ")
        #     print(output)

            # send the data to the server
            #send_data('145.137.73.169',12345, output)
        

        # increment the transform_every
        # transform_every += 1
        


if __name__ == "__main__":
    main()
# %%
