#!/usr/bin/env python

import numpy as np
from scipy import integrate
from scipy import sparse

import matplotlib.pyplot as plt
from matplotlib import animation
from manim import *

class quantum(Scene):
        def construct(self):
            dx = 0.005                  # spatial separation
            x = np.arange(0, 10, dx)    # spatial grid points
            kx = 50                     # wave number
            m = 1                       # mass
            sigma = 0.5                 # width of initial gaussian wave-packet
            x0 = 3.0                    # center of initial gaussian wave-packet
            # Initial Wavefunction
            A = 1.0 / (sigma * np.sqrt(np.pi))  # normalization constant
            psi0 = np.sqrt(A) * np.exp(-(x-x0)**2 / (2.0 * sigma**2)) * np.exp(1j * kx * x)
            # Potential V(x)
            V_hight = 1000
            magnitud=1650
            squish=5
            def potential(x):
                return magnitud*np.arctan(squish*x-squish*5)*(np.exp(-0.1*(squish*x-squish*5)**2)) + 300
            V = magnitud*np.arctan(squish*x-squish*5)*(np.exp(-0.1*(squish*x-squish*5)**2)) + 300
            # Make a plot of psi0 and V
            fig = plt.figure(figsize=(15, 5))
            plt.plot(x, V*0.01, "k--", label=r"$V(x) (x0.01)")
            plt.plot(x, np.abs(psi0)**2, "r", label=r"$\vert\psi(t=0,x)\vert^2$")
            plt.plot(x, np.real(psi0), "g", label=r"$Re\{\psi(t=0,x)\}$")
            plt.legend(loc=1, fontsize=8, fancybox=False)
            fig.savefig('step_initial@2x.png')
            # Laplace Operator (Finite Difference)
            D2 = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(x.size, x.size)) / dx**2
            # Solve Schrodinger Equation
            hbar = 1
            # RHS of Schrodinger Equation
            def psi_t(t, psi):
                return -1j * (- 0.5 * hbar / m * D2.dot(psi) + V / hbar * psi)
            # Solve the Initial Value Problem
            dt = 0.002  # time interval for snapshots
            t0 = 0.0    # initial time
            tf = 0.4    # final time
            t_eval = np.arange(t0, tf, dt)  # recorded time shots

            print("integrating...")
            sol = integrate.solve_ivp(psi_t,
                                    t_span=[t0, tf],
                                    y0=psi0,
                                    t_eval=t_eval,
                                    method="RK23")

            axes=Axes(x_range=[0,10,1],y_range=[-1,3,0.1])
            axes.plot(lambda x: potential(x), color=BLUE)

            