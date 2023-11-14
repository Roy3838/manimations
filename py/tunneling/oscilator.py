from manim import *
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from matplotlib.animation import FuncAnimation
from qutip import *

class HarmonicOscillator(Scene):
    def construct(self):
         
        N = 35
        w = 0.75 * np.pi               # oscillator frequency
        tlist = np.linspace(0, 4, 101)  # periods
        # operators
        a = destroy(N)
        n = num(N)
        x = (a + a.dag())/np.sqrt(2)
        p = -1j * (a - a.dag())/np.sqrt(2)
        # the quantum harmonic oscillator Hamiltonian
        H = w * a.dag() * a
        c_ops = []


        def get_density_f(rho, fig=None, ax=None, figsize=(6, 6),
                            cmap=None, alpha_max=7.5, colorbar=False,
                            method='clenshaw', projection='2d'):
            if isket(rho):
                rho = ket2dm(rho)
            xvec = np.linspace(-alpha_max, alpha_max, 200)
            W0 = qfunc(rho, xvec, xvec, g=2)
            W, yvec = W0 if isinstance(W0, tuple) else (W0, xvec)
            wlim = abs(W).max()

            return xvec, yvec, W, wlim

        # Create initial state
        psi0 = squeeze(N, 1) * displace(N, 1) * coherent(N, 1.0)

        # Solve Hamiltonian with psi0
        result = mesolve(H, psi0, tlist, c_ops, [])
        N = 30  # Tamanyo del espacio Hilbert


        def W_q_p(i=0):
            # Assuming result.states[i] gives you the state for the ith value
            xvec, yvec, W, wlim = get_density_f(result.states[i])
            return xvec, yvec, W, wlim

        def function_updater(image, dt):
            density = image.funcs[int(dt*30)]
            image.become(ImageMobject(density))



        img = ImageMobject([0]).scale(5)
        img.funcs = []

        for i in range(len(result.states)):
            xvec, yvec, W, wlim = W_q_p(i)
            W = W/wlim
            W = W*255
            img.funcs.append(W)
        self.add(img)
        img.add_updater(function_updater)
        self.wait(1)

