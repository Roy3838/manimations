import numpy as np
import matplotlib.pyplot as plt
from qutip import plot_wigner, coherent, ket2dm, wigner, squeeze
from matplotlib.animation import FuncAnimation

# Set the parameters for the SHO
N = 30  # Number of Fock basis states to consider
alpha = 2  # Displacement of the coherent state
w = 1  # Angular frequency

def W_q_p(t=0):
    # Create a coherent state with a time-dependent phase
    psi = squeeze(N,1)* coherent(N, alpha * np.exp(1j * w * t))
    rho = ket2dm(psi)
    # Generate the Wigner function
    xvec = np.linspace(-5, 5, 200)
    W = wigner(rho, xvec, xvec)
    # Calculate the expectation value of the position
    x_expect = np.real(alpha * np.exp(1j * w * t))
    return xvec, W, x_expect

def V(x):
    # Potential of the SHO
    return 0.5 * (w * x) ** 2

fig, ax = plt.subplots(2, 1, figsize=(8, 10))

def update(frame):
    # Update Wigner plot
    ax[0].clear()
    xvec, W, x_expect = W_q_p(t=frame / 10.0)
    ax[0].contourf(xvec, xvec, W, 100, cmap='RdBu')
    ax[0].set_xlim([-5, 5])
    ax[0].set_ylim([-5, 5])
    ax[0].set_xlabel('q')
    ax[0].set_ylabel('p')
    
    # Plot the SHO potential
    ax[1].clear()
    x_potential = np.linspace(-5, 5, 200)
    y_potential = V(x_potential)
    ax[1].plot(x_potential, y_potential, label='V(x) = 1/2 m w^2 x^2')
    ax[1].set_ylim([0, max(y_potential)])
    ax[1].set_xlim([-5, 5])
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('V(x)')
    
    # Plot the particle's position as a dot on the potential curve
    ax[1].plot(x_expect, V(x_expect), 'ro')
    ax[1].legend()

# Create an animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 20*np.pi, 200), interval=50)

plt.show()
