import numpy as np
from qutip import destroy, num, ket2dm, squeeze, displace, coherent, mesolve, qfunc, isket
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


N = 35
w = 1 * np.pi  # oscillator frequency
tlist = np.linspace(0, 2, 101)  # periods
a = destroy(N)
H = w * a.dag() * a
c_ops = []

psi0 =  squeeze(N, 1) * displace(N, 9) * coherent(N, 1.0)
result = mesolve(H, psi0, tlist, c_ops, [])

alpha_max = 7.5
xvec = np.linspace(-alpha_max, alpha_max, 200)
n_timesteps = len(result.states)
W_matrices = np.zeros((n_timesteps, len(xvec), len(xvec)))

def get_density_f(rho):
    if isket(rho):
        rho = ket2dm(rho)
    W = qfunc(rho, xvec, xvec, g=2)
    return W

for i, state in enumerate(result.states):
    print(i/int(len(result.states)))
    W_matrices[i, :, :] = get_density_f(state)

# Save W matrices as a single binary file
np.save('W_matrices.npy', W_matrices)

def update(i):
    ax.clear()
    W = W_matrices[i, :, :] / W_matrices[i, :, :].max() * 255
    contour = ax.contourf(xvec, xvec, W, 100)
    # Calculate current time
    current_time = tlist[i]
    
    # Add time label to the plot
    ax.text(0.05, 0.95, f'Time: {current_time:.2f}', transform=ax.transAxes, 
            bbox=dict(facecolor='white', alpha=0.8), fontsize=12)
        
    return contour,


fig, ax = plt.subplots()

ani = FuncAnimation(fig, update, frames=range(len(W_matrices)), interval=200)

plt.show()
