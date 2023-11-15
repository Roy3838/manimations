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

# Update function for the animation
def update(i):
    ax.clear()
    W = W_matrices[i, :, :] / W_matrices[i, :, :].max() * 255
    contour = ax.contourf(xvec, yvec, W, 100)
    return contour,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(len(W_matrices)), interval=200)

# To display the animation, uncomment the following line
plt.show()

# To save the animation, uncomment the following line
# ani.save('harmonic_oscillator_animation.mp4')
