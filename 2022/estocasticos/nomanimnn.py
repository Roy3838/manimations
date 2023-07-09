import numpy as np
import random as rd
import matplotlib.pyplot as plt

# graph Make a neural net that approximates the function 1 + sin(pix/4) from -2 to 2 using a 1-2-1 network,
# this means that there is 1 hidden layer of 2 neurons, and one output and input neuron.
def func(x):
    return 1 + np.sin(x * np.pi / 4)

# activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

Ntest = 50
x = rd.random(-2,2,Ntest)
y = func(x)

#initialize weights and biases
w1=np.array(2,1)
w2=np.array(2,1)
b1=np.array(2,1)
b2=np.array(1,1)

#fill with numbers from -1 to 1
w1=rd.random(-1,1,2,1)
w2=rd.random(-1,1,2,1)
b1=rd.random(-1,1,2,1)
b2=rd.random(-1,1,1,1)

#Epocas
Ne=50
#learning rate
lr=0.1

#training
for epoca in range(Ne):
    for prueba in range(Ntest):
        #Forward propagation
        # MATLAB z=W*X(:,ii)+b;
        # PYTHON
        x0=x[prueba]
        y1=sigmoid(w1*x0+b1)
        y2=sigmoid(w2*y1+b2)

        
        


        #Error and back propagation


        #update weights and biases

