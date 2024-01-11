import numpy as np
from qutip import destroy, num, ket2dm, squeeze, displace, coherent, mesolve, qfunc, isket

N = 35
w = 1 * np.pi  # oscillator frequency
tlist = np.linspace(0, 9, 101)  # periods
a = destroy(N)
H = w * a.dag() * a
c_ops = []

psi0 =  squeeze(N, 1) * displace(N, 1) * coherent(N, 1.0)
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
