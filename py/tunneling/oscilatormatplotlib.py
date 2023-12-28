import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load W matrices from the binary file
W_matrices = np.load('tunneling/W_matrices.npy')

# Create a figure and axis for the animation
fig, ax = plt.subplots()

# Define the x and y vectors based on the dimensions of the W matrices
alpha_max = 7.5  # This should be consistent with compute.py
xvec = np.linspace(-alpha_max, alpha_max, W_matrices.shape[1])
yvec = np.linspace(-alpha_max, alpha_max, W_matrices.shape[2])

def select_random_points(W):
    # Normalize W to make it a probability distribution
    W_normalized = W / np.sum(W)

    # Sum over y-axis to get a 1D probability distribution for x
    prob_x = np.sum(W_normalized, axis=0)
    # Select a random x coordinate based on this distribution
    x_index = np.random.choice(range(len(prob_x)), p=prob_x)

    # Sum over x-axis to get a 1D probability distribution for y
    prob_y = np.sum(W_normalized, axis=1)
    # Select a random y coordinate based on this distribution
    y_index = np.random.choice(range(len(prob_y)), p=prob_y)

    return x_index, y_index

# Update function for the animation
def update(i):
    ax.clear()
    W = W_matrices[i, :, :] / W_matrices[i, :, :].max() * 255
    contour = ax.contourf(xvec, yvec, W, 100)
    
    # select 5 indices 
    for _ in range(400):
        x_index, y_index = select_random_points(W)
        ax.scatter(xvec[x_index], yvec[y_index], color='red')
    return contour,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(len(W_matrices)), interval=200)

# To display the animation, uncomment the following line
plt.show()

# To save the animation, uncomment the following line
# ani.save('harmonic_oscillator_animation.mp4')
