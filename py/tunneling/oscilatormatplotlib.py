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

def select_random_points_deprecated(W):
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

def select_random_points(W):
    # Normalize W to make it a probability distribution
    W_normalized = W / np.sum(W)

    # Sum over y-axis to get a 1D probability distribution for x
    prob_x = np.sum(W_normalized, axis=0)
    x_index = np.random.choice(range(len(prob_x)), p=prob_x)

    # Plot using matplotlib, plot the W matrix and the x_index as a line
    # plt.imshow(W_normalized, cmap='hot', interpolation='nearest')
    # plt.axvline(x=x_index, color='blue')
    # plt.title('Probability Density Matrix with Selected X')
    # plt.show()

    # Given the x_index chosen, make sum probability of y in that line
    prob_y_given_x = W_normalized[:, x_index]
    prob_y_given_x /= np.sum(prob_y_given_x)

    # Choose y index given the probability sum of y
    y_index = np.random.choice(range(len(prob_y_given_x)), p=prob_y_given_x)

    # Plot now the probability distribution of y in the x line, then the y point chosen
    # plt.plot(prob_y_given_x)
    # plt.axvline(x=y_index, color='red')
    # plt.title('Probability Distribution of Y given X')
    # plt.show()

    return x_index, y_index




# Update function for the animation
def update(i):
    ax.clear()
    W = W_matrices[i, :, :] / W_matrices[i, :, :].max() * 255
    contour = ax.contourf(xvec, yvec, W, 100)
    
    # select 5 indices 
    for _ in range(40):
        x_index, y_index = select_random_points(W)
        P = xvec[x_index]
        Q = yvec[y_index]
        ax.scatter(P, Q, color='red')
        
    return contour,

# Create the animation
# ani = FuncAnimation(fig, update, frames=range(len(W_matrices)), interval=200)

# Select random points from the first distribution
#fig, ax = plt.subplots()

# Call the update function for the first frame
#update(0)

# Show the plot
#plt.show()


# Plot the Electric Field given the squeezed state
def create_electrical_field_plot(W_matrices):
    

    res = 10
    # Prelocate E_field with size len(W_matrices)*res
    total_cycles = len(W_matrices)*res + 1
    E_field = [0.0 for i in range(total_cycles)]
    quantum = [0.0 for i in range(total_cycles)]
    theoretical = [0.0 for i in range(total_cycles)]

    count = 0
    time = np.linspace(0,2,total_cycles)
    for i in range (len(W_matrices)):
        W = W_matrices[i, :, :] / W_matrices[i, :, :].max()
        # plt.contourf(xvec,yvec,W,100) 
        
        # As a for loop
        for m in range(res):
            count+=1
            x_index, y_index = select_random_points(W)
            Q = xvec[x_index]
            P = yvec[y_index]
            # plt.scatter(Q,P)
            E_field[count] =  P
            # quantum[count] = Q* np.cos(time[count]/np.pi) - P* np.sin(time[count]/np.pi)
            theoretical[count] = np.cos(time[count]*20) - np.sin(time[count]*20)
        # plt.show()
    # plot E_field
    plt.plot(time,E_field)
    plt.plot(time,theoretical)
    #plt.plot(E_field_theoretical)
create_electrical_field_plot(W_matrices)

plt.show()

# To save the animation, uncomment the following line
# ani.save('harmonic_oscillator_animation.mp4')
