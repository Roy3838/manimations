#matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from qutip import *
N = 35
w = 1 * 2 * np.pi              # oscillator frequency
tlist = np.linspace(0, 4, 101) # periods
# operators
a = destroy(N)
n = num(N)
x = (a + a.dag())/np.sqrt(2)
p = -1j * (a - a.dag())/np.sqrt(2)
# the quantum harmonic oscillator Hamiltonian
H = w * a.dag() * a
c_ops = []

def plot_wigner_modded(rho, fig=None, ax=None, figsize=(6, 6),
                cmap=None, alpha_max=7.5, colorbar=False,
                method='clenshaw', projection='2d'):
    if isket(rho):
        rho = ket2dm(rho)

    xvec = np.linspace(-alpha_max, alpha_max, 200)
    #W0 = wigner(rho, xvec, xvec, method=method)
    W0 = qfunc(rho, xvec, xvec, g=2)

    W, yvec = W0 if isinstance(W0, tuple) else (W0, xvec)

    wlim = abs(W).max()


    return xvec, yvec, W , wlim


# uncomment to see how things change when disspation is included
# c_ops = [np.sqrt(0.25) * a]
def plot_expect_with_variance(N, op_list, op_title, states):
    """
    Plot the expectation value of an operator (list of operators)
    with an envelope that describes the operators variance.
    """
    
    fig, axes = plt.subplots(1, len(op_list), figsize=(14,3))

    for idx, op in enumerate(op_list):
        
        e_op = expect(op, states)
        v_op = variance(op, states)

        axes[idx].fill_between(tlist, e_op - np.sqrt(v_op), e_op + np.sqrt(v_op), color="green", alpha=0.5);
        axes[idx].plot(tlist, e_op, label="expectation")
        axes[idx].set_xlabel('Time')
        axes[idx].set_title(op_title[idx])

    return fig, axes



psi0 = squeeze(N,1) * coherent(N, 2.0)
result = mesolve(H, psi0, tlist, c_ops, [])
# plot_expect_with_variance(N, [n, x, p], [r'$n$', r'$x$', r'$p$'], result.states)
# xvec, yvec, W , wlim=plot_wigner_modded(result.states)
xvec = np.linspace(-7.5, 7.5, 200)
 
W = qfunc(ket2dm(result.states[9]),xvec,xvec)
plt.contourf(W,10)
plt.show()
print(W)
# print(W.shape)
# plt.contourf(xvec, yvec, W[0], 100)
# plt.show()



# fig, axes = plt.subplots(1, 2, figsize=(10,5))
# def update(n):
#     axes[0].cla()
#     plot_wigner_fock_distribution(result.states[n], fig=fig, axes=axes)

# anim = FuncAnimation(fig, update, frames=len(result.states), blit=True)

# plt.show()

#anim.save('/tmp/animation-coherent-state.mp4', fps=20, writer="avconv", codec="libx264")

# plt.close(fig)
# display_embedded_video("/tmp/animation-coherent-state.mp4")
# psi0 = squeeze(N, 1.0) * basis(N, 0)
# result = mesolve(H, psi0, tlist, c_ops, [])
# plot_expect_with_variance(N, [n, x, p], [r'$n$', r'$x$', r'$p$'], result.states);
# fig, axes = plt.subplots(1, 2, figsize=(10,5))

# def update(n):
#     axes[0].cla()
#     plot_wigner_fock_distribution(result.states[n], fig=fig, axes=axes)

# anim = animation.FuncAnimation(fig, update, frames=len(result.states), blit=True)

# anim.save('/tmp/animation-squeezed-vacuum.mp4', fps=20, writer="avconv", codec="libx264")

# plt.close(fig)
# display_embedded_video("/tmp/animation-squeezed-vacuum.mp4")
# psi0 = displace(N, 2) * squeeze(N, 1.0) * basis(N, 0)  # first squeeze vacuum and then displace
# result = mesolve(H, psi0, tlist, c_ops, [])
# plot_expect_with_variance(N, [n, x, p], [r'$n$', r'$x$', r'$p$'], result.states);
# fig, axes = plt.subplots(1, 2, figsize=(10,5))

# def update(n):
#     axes[0].cla()
#     plot_wigner_fock_distribution(result.states[n], fig=fig, axes=axes)

# anim = animation.FuncAnimation(fig, update, frames=len(result.states), blit=True)

# anim.save('/tmp/animation-squeezed-coherent-state.mp4', fps=20, writer="avconv", codec="libx264")

# plt.close(fig)
# display_embedded_video("/tmp/animation-squeezed-coherent-state.mp4")
# from qutip.ipynbtools import version_table; version_table()