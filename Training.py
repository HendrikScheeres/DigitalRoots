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
plt.plot(data[0, 0, :])
plt.title("No scaling")

# Z-score normalization
data_norm_Z = (data - np.mean(data)) / np.std(data)

# Min-max normalization
data_norm_M = (data - np.min(data)) / (np.max(data) - np.min(data))

# After scale plot
plt.plot(data_norm_Z[0, 0, :])
plt.title("Z-score scaling")

plt.plot(data_norm_M[0, 0, :])
plt.title("min-max scaling")

#%% PREPARE FOR TRAINGING

# initialize the weights
w_i_h = np.random.uniform(-0.5, 0.5, (20, 150)) 
w_h_o = np.random.uniform(-0.5, 0.5, (4, 20)) 

w_i_h = np.random.uniform(-0.5, 0.5, (20, 150))
w_h_o = np.random.uniform(-0.5, 0.5, (4, 20)) 

b_i_h = np.zeros((20, 1)) 
b_h_o = np.zeros((4, 1))

# FIRST THE RAW SIGNAL

# THEN THE Z-SCORE NORMALIZED SIGNAL

# THEN THE MIN-MAX NORMALIZED SIGNAL

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

#%% Network training
# set th training parameters
learn_rate = 0.01  
nr_correct = 0
epochs = 30

for epoch in range(epochs):

     #innerloop
    for v, l in zip(train_data, train_target):

        # transpose the input vector
        v = v.T
        l = l.T

        # forward prop. input -> hidden
        # @ means matrix multiplication
        h_pre = b_i_h + w_i_h @ v

        # sigmoid activation function
        h = 1 / (1 + np.exp(-h_pre))

        # forward prop. hidden -> output
        o_pre = b_h_o + w_h_o @ h
        o = 1 / (1 + np.exp(-o_pre))

        # Cost error calculation
        e = 1/ len(0 * np.sum((o-l) ** 2, axis=0))

        # if the neruron with the highest output is the same as the label, then it is correct and we add 1 to the counter
        nr_correct += int(np.argmax(o) == np.argmax(l))

        # backprop. output -> hidden (cost function derivative)
        delta_o = o - l
        w_h_o +=  - learn_rate * delta_o @ h.T
        b_h_o += - learn_rate * delta_o

        # backprop. hidden -> input (activation functino derivative)
        delta_h = (w_h_o.T @ delta_o) * h * (1 - h)
        w_i_h += - learn_rate * delta_h @ v.T
        b_i_h += - learn_rate * delta_h

        
    print(f'Epoch: {epoch+1}/{epochs}, Accuracy: {nr_correct/len(train_data)*100}%')
    nr_correct = 0

#%%
# test the network
nr_correct = 0
for v, l in zip(test_data, test_target):
    
        # transpose the input vector
        v = v.T
        l = l.T
    
        # forward prop. input -> hidden
        h_pre = b_i_h + w_i_h @ v
    
        # sigmoid activation function
        h = 1 / (1 + np.exp(-h_pre))
    
        # forward prop. hidden -> output
        o_pre = b_h_o + w_h_o @ h
        o = 1 / (1 + np.exp(-o_pre))
    
        # if the neruron with the highest output is the same as the label, then it is correct and we add 1 to the counter
        nr_correct += int(np.argmax(o) == np.argmax(l))

print(nr_correct)
print("Accuracy: ", nr_correct / len(test_data))

# Save the weights
#np.savez('weights.npz', w_i_h=w_i_h, w_h_o=w_h_o, b_i_h=b_i_h, b_h_o=b_h_o)
#np.savez('min_max.npz', min_data=min_data, max_data=max_data)
#%%

# load the weights
weights = np.load('weights.npz')

w_i_h = weights['w_i_h']
w_h_o = weights['w_h_o']
b_i_h = weights['b_i_h']
b_h_o = weights['b_h_o']


# select a random index
index = random.randint(0, len(test_data))

# plot the data corresponding to the index
plt.plot(test_data[index].T)

# ylim between -2 and 2
plt.ylim(-2, 2)

#showcase one forward pass
v = test_data[index].T

# print the shape of v
#print(v.shape)

l = test_target[index].T

# forward prop. input -> hidden
h_pre = b_i_h + w_i_h @ v

# sigmoid activation function
h = 1 / (1 + np.exp(-h_pre))

# forward prop. hidden -> output
o_pre = b_h_o + w_h_o @ h
o = 1 / (1 + np.exp(-o_pre))
print("o: ")
print(o)

print("Predicted: ", np.argmax(o))
print("Label: ", np.argmax(l))