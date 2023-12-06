import random
import os
import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt

style.use('fivethirtyeight')


def load_weights(sort_of_weights): 

    # load the weights from the file
    if sort_of_weights == "min_max":
        weights = np.load('Weights/min_max_weights.npz')
    else:
        weights = np.load('Weights/weights_z-score.npz')

    w_i_h = weights['w_i_h']
    w_h_o = weights['w_h_o']
    b_i_h = weights['b_i_h']
    b_h_o = weights['b_h_o']

    print("weights loaded")
    return w_i_h, w_h_o, b_i_h, b_h_o

def transformer(v, w_i_h, w_h_o, b_i_h, b_h_o):

    #print(v.shape)
    # clip the voltage array to 150
    v = v[:150]
    v = v.T

    #print("this is what v looks like:")
    #print(v.shape)
    # reshape the vector to be a column vector
    v = v.reshape(-1, 1)
    # assert that the vector is (150, 1)
    assert v.shape == (150, 1)
    
    #forward prop. input -> hidden
    h_pre = b_i_h + w_i_h @ v
        
    # sigmoid activation function
    h = 1 / (1 + np.exp(-h_pre))
        
    # forward prop. hidden -> output
    o_pre = b_h_o + w_h_o @ h
    o = 1 / (1 + np.exp(-o_pre))


    #print("o: ")
    #print(o)

    #print("Predicted: ", np.argmax(o))
    
    return o