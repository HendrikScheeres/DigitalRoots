"""
TRAINING SCRIPT
This script is used to train the neural network.
The neural network is saved in the weights.npz file.
The weights are loaded in the transformer.py script.
The transformer.py script is used to transform the input data into the output data.
The output data is a one-hot encoded vector.
The one-hot encoded vector is converted to a class label this is send to the receiver
"""

#%% IMPORT
import os
import random
import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt
style.use('fivethirtyeight')

#%%
# Presets
train = "raw"
epochs = 30
learn_rate = 0.01


#%% FUNCTIONS
def train_network(epochs, train_data, train_target, learn_rate):
    #input_neurons = train_data.shape[2]
    #hidden_neurons = 10  # Set your desired number of hidden neurons
    #output_neurons = train_target.shape[2]

    # Initialize weights and biases
    w_i_h = np.random.uniform(-0.5, 0.5, (20, 150))# specify dtype
    w_h_o = np.random.uniform(-0.5, 0.5, (4, 20)) # specify dtype

    b_i_h = np.zeros((20, 1)) # specify dtype
    b_h_o = np.zeros((4, 1)) # specify dtype]
    nr_correct = 0
    for epoch in range(epochs):
        
        for v, l in zip(train_data, train_target):
            #v = v.reshape(-1, 1) # Reshape v to be a column vector
            #l = l.reshape(-1, 1)  # Reshape l to be a column vector
            print(v.shape)
            print(l.shape)
            # transpose the input vector
            v = v.T
            l = l.T
            print(v.shape)
            print(l.shape)

            break
            # Forward propagation
            h_pre = b_i_h + w_i_h @ v
            h = 1 / (1 + np.exp(-h_pre))
            o_pre = b_h_o + w_h_o @ h
            o = 1 / (1 + np.exp(-o_pre))

            # Cost error calculation
            e = 1/ len(0 * np.sum((o-l) ** 2, axis=0))

            nr_correct += int(np.argmax(o) == np.argmax(l))

            # Backpropagation
            delta_o = o - l
            w_h_o += - learn_rate * delta_o @ h.T
            b_h_o += - learn_rate * delta_o

            delta_h = (w_h_o.T @ delta_o) * h * (1 - h)
            w_i_h += - learn_rate * delta_h @ v.T
            b_i_h +=  -learn_rate * delta_h

        accuracy = nr_correct / len(train_data) * 100
        print(f'Epoch: {epoch+1}/{epochs}, Accuracy: {accuracy}%')
        nr_correct = 0

    return w_i_h, b_i_h, w_h_o, b_h_o

def test_network(test_data, test_target, w_i_h, b_i_h, w_h_o, b_h_o):
    nr_correct = 0
    for v, l in zip(test_data, test_target):

        # transpose the input vector
        v = v.T
        l = l.T

        #v = v.reshape(-1, 1) # Reshape v to be a column vector
        #l = l.reshape(-1, 1)  # Reshape l to be a column vector

        # Forward propagation
        h_pre = b_i_h + w_i_h @ v
        h = 1 / (1 + np.exp(-h_pre))
        o_pre = b_h_o + w_h_o @ h
        o = 1 / (1 + np.exp(-o_pre))

        nr_correct += int(np.argmax(o) == np.argmax(l))

    accuracy = nr_correct / len(test_data)
    print(f'Correct predictions: {nr_correct}/{len(test_data)}')
    print("Test Accuracy: ", accuracy)

    return accuracy, w_i_h, b_i_h, w_h_o, b_h_o

#%% LOAD
# Choose the array to load
folder = "Data/"
datafile = np.load(os.path.join(folder, "data.npz"))
print(datafile.files)

#%% INSPECTION

data = datafile["data"]
target = datafile['target']

# get the size of data
print("Current size of the data")
print(data.shape)
print(target.shape)

# find the first target index that corresponds to [0,0,0,0]
# cut the data from there onwards
index = np.where(np.all(target[:,0,:] == [0, 0, 0, 0], axis=1))[0][0]

# cut of the data from the index onwards
data = data[:index, :, :]
target = target[:index, :, :]

print("New size of the data")
print(data.shape)
print(target.shape)

#%%

r_i = random.randint(0, len(data))

# plot the first sample of the data array with the target as title
plt.plot(data[r_i, 0, :])
plt.title("Random: " + str(target[r_i, 0, :]))

#%% Plot the average signal of each condition

# Get the index per conditons
index_1 = np.where(np.all(target[:,0,:] == [1, 0, 0, 0], axis=1))

# check it with one of the data samples
print(len(index_1[0]))
data_1 = data[index_1, 0, :]
data_1 = np.squeeze(data_1)

index_2 = np.where(np.all(target[:,0,:] == [0, 1, 0, 0], axis=1))
print(len(index_2[0]))
data_2 = data[index_2, 0, :]
data_2 = np.squeeze(data_2)

index_3 = np.where(np.all(target[:,0,:] == [0, 0, 1, 0], axis=1))
data_3 = data[index_3, 0, :]
data_3 = np.squeeze(data_3)
print(len(index_3[0]))

index_4 = np.where(np.all(target[:,0,:] == [0, 0, 0, 1], axis=1))
data_4 = data[index_4, 0, :]
data_4 = np.squeeze(data_4)
print(len(index_4[0]))

#%% Mean and standard deviation
mean_1 = np.mean(data_1, axis=0)
len(np.mean(data_1, axis=0))

mean_2 = np.mean(data_2, axis=0)
len(np.mean(data_2, axis=0))

mean_3 = np.mean(data_3, axis=0)
len(np.mean(data_3, axis=0))

mean_4 = np.mean(data_4, axis=0)
len(np.mean(data_4, axis=0))

# Standard deviation
std_1 = np.std(data_1, axis=0)
len(np.std(data_1, axis=0))

std_2 = np.std(data_2, axis=0)
len(np.std(data_2, axis=0))

std_3 = np.std(data_3, axis=0)
len(np.std(data_3, axis=0))

std_4 = np.std(data_4, axis=0)
len(np.std(data_4, axis=0))

#%% Complicated plot
# make 4 different plots for each condition, plot the mean as a thick line and the standard deviation shaded
plt.figure()
plt.plot(mean_1, linewidth=3)
plt.fill_between(np.arange(len(mean_1)), mean_1 - std_1, mean_1 + std_1, alpha=0.5)
plt.ylim(100, 400)

#plt.figure()
plt.plot(mean_2, linewidth=3)
plt.fill_between(np.arange(len(mean_2)), mean_2 - std_2, mean_2 + std_2, alpha=0.5)
plt.ylim(100, 400)

#plt.figure()
plt.plot(mean_3, linewidth=3)
plt.fill_between(np.arange(len(mean_3)), mean_3 - std_3, mean_3 + std_3, alpha=0.5)
plt.ylim(100, 400)

#plt.figure()
plt.plot(mean_4, linewidth=3)
plt.fill_between(np.arange(len(mean_4)), mean_4 - std_4, mean_4 + std_4, alpha=0.5)
# set the y-axis between 100 400
plt.ylim(100, 400)

#add a legend
plt.legend(['1', '2', '3', '4'])
# fixe their colours

#%% Normalizations

# Before scale plot
plt.figure()
plt.plot(data[0, 0, :])
plt.title("No scaling")

# Z-score normalization
data_norm_Z = (data - np.mean(data)) / np.std(data)

# Min-max normalization
data_norm_M = (data - np.min(data)) / (np.max(data) - np.min(data))

# After scale plot
plt.figure()
plt.plot(data_norm_Z[0, 0, :])
plt.title("Z-score scaling")

plt.figure()
plt.plot(data_norm_M[0, 0, :])
plt.title("min-max scaling")

#%% PREPARE FOR TRAINGING

data = data_norm_Z #FIX THIS!

# shuffle the data and the target arrays
index = np.arange(data.shape[0])
np.random.shuffle(index)
data = data[index, :, :]
target = target[index, :, :]

# split the data into training and testing
train_data = data[:int(0.8 * len(data)), :, :]
train_target = target[:int(0.8 * len(target)), :, :]
test_data = data[int(0.8 * len(data)):, :, :]
test_target = target[int(0.8 * len(target)):, :, :]

# print the sizes of the shuffle arrays
print("Training data size: ", train_data.shape)
print("Training target size: ", train_target.shape)
print("Testing data size: ", test_data.shape)
print("Testing target size: ", test_target.shape)

#%% RAW

if train == "raw" or train == "all":
    print("Training with raw data")

    # TRAINING
    [w_i_h, b_i_h, w_h_o, b_h_o] = train_network(epochs=epochs, train_data=train_data, train_target=train_target, learn_rate=learn_rate)

    # TESTING
    test_results = test_network(test_data=test_data, test_target=test_target, w_i_h=w_i_h, b_i_h=b_i_h, w_h_o=w_h_o, b_h_o=b_h_o)

    # save the weights
    np.savez("weights_raw.npz", w_i_h=w_i_h, b_i_h=b_i_h, w_h_o=w_h_o, b_h_o=b_h_o)
if train == "z-score" or train == "all":
    print("Training with z-score normalized data")

    # Z-SCORE
    # TRAINING
    [w_i_h, b_i_h, w_h_o, b_h_o] = train_network(epochs=epochs, train_data=data_norm_Z, train_target=train_target, learn_rate=learn_rate)

    # TESTING
    test_results = test_network(test_data=data_norm_Z, test_target=test_target, w_i_h=w_i_h, b_i_h=b_i_h, w_h_o=w_h_o, b_h_o=b_h_o)

    # save the weights
    np.savez("weights_z-score.npz", w_i_h=w_i_h, b_i_h=b_i_h, w_h_o=w_h_o, b_h_o=b_h_o)
if train == "min-max" or train == "all":
    print("Training with min-max normalized data")
    
    # MIN-MAX
    # TRAINING
    [w_i_h, b_i_h, w_h_o, b_h_o] = train_network(epochs=epochs, train_data=data_norm_M, train_target=train_target, learn_rate=learn_rate)

    # TESTING
    test_results = test_network(test_data=data_norm_M, test_target=test_target, w_i_h=w_i_h, b_i_h=b_i_h, w_h_o=w_h_o, b_h_o=b_h_o)

    # save the weights
    np.savez("weights_min-max.npz", w_i_h=w_i_h, b_i_h=b_i_h, w_h_o=w_h_o, b_h_o=b_h_o)
# %%
