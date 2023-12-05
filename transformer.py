
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