import numpy as np
import matplotlib.pyplot as plt
from qutip import plot_wigner , wigner, fock, displace, squeeze, coherent, basis 
from matplotlib import transforms
from manim import *
from qutip.states import ket2dm
from qutip.qobj import Qobj, isket
from matplotlib.animation import FuncAnimation

def plot_wigner_modded(rho, fig=None, ax=None, figsize=(6, 6),
                cmap=None, alpha_max=7.5, colorbar=False,
                method='clenshaw', projection='2d'):
    """
    Plot the the Wigner function for a density matrix (or ket) that describes
    an oscillator mode.

    Parameters
    ----------
    rho : :class:`qutip.Qobj`
        The density matrix (or ket) of the state to visualize.

    fig : a matplotlib Figure instance
        The Figure canvas in which the plot will be drawn.

    ax : a matplotlib axes instance
        The axes context in which the plot will be drawn.

    figsize : (width, height)
        The size of the matplotlib figure (in inches) if it is to be created
        (that is, if no 'fig' and 'ax' arguments are passed).

    cmap : a matplotlib cmap instance
        The colormap.

    alpha_max : float
        The span of the x and y coordinates (both [-alpha_max, alpha_max]).

    colorbar : bool
        Whether (True) or not (False) a colorbar should be attached to the
        Wigner function graph.

    method : string {'clenshaw', 'iterative', 'laguerre', 'fft'}
        The method used for calculating the wigner function. See the
        documentation for qutip.wigner for details.

    projection: string {'2d', '3d'}
        Specify whether the Wigner function is to be plotted as a
        contour graph ('2d') or surface plot ('3d').

    Returns
    -------
    fig, ax : tuple
        A tuple of the matplotlib figure and axes instances used to produce
        the figure.
    """

    # if not fig and not ax:
    #     if projection == '2d':
    #         fig, ax = plt.subplots(1, 1, figsize=figsize)
    #     elif projection == '3d':
    #         fig = plt.figure(figsize=figsize)
    #         ax = fig.add_subplot(1, 1, 1, projection='3d')
    #     else:
    #         raise ValueError('Unexpected value of projection keyword argument')

    if isket(rho):
        rho = ket2dm(rho)

    xvec = np.linspace(-alpha_max, alpha_max, 200)
    W0 = wigner(rho, xvec, xvec, method=method)

    W, yvec = W0 if isinstance(W0, tuple) else (W0, xvec)

    wlim = abs(W).max()

    # if projection == '2d':
    #     cf = ax.contourf(xvec, yvec, W, 100,
    #                      norm=mpl.colors.Normalize(-wlim, wlim), cmap=cmap)
    # elif projection == '3d':
    #     X, Y = np.meshgrid(xvec, xvec)
    #     cf = ax.plot_surface(X, Y, W0, rstride=5, cstride=5, linewidth=0.5,
    #                          norm=mpl.colors.Normalize(-wlim, wlim), cmap=cmap)
    # else:
    #     raise ValueError('Unexpected value of projection keyword argument.')


    return xvec, yvec, W , wlim


N = 30
w = 1/4 

def W_q_p(t=0):
    psi =  displace(N,2) * squeeze(N, 1.0) * coherent(N,3*np.exp(1j * w * t))#* np.exp(-1j * w * t)

    
    #psi = displace(N,3) * squeeze(N, 1) * fock(N,0) * np.exp(-1j * w * t)
    psi_t = squeeze(1, 1 ) * coherent(N,3*np.exp(1j * w * t))
    xvec, yvec, W , wlim = plot_wigner_modded(psi)
    return xvec, yvec, W , wlim

fig, ax = plt.subplots()

def update(i):
    ax.clear()
    xvec, yvec, W , wlim = W_q_p(t=i)
    ax.contourf(xvec, yvec, W, 100)

ani = FuncAnimation(fig, update, frames=range(0,10), interval=200)

plt.show()
