import numpy as np
from scipy.optimize import fsolve
from manim import *

class ImplicitFunction(ThreeDScene):
    def implicit_function(self, rho, theta, phi, n, d, lam):
        return (n * lam) / 2 - np.sqrt(-2 * rho * np.sin(phi) * np.cos(theta) + rho**2) + np.sqrt(2 * rho * np.sin(phi) * np.cos(theta) + rho**2)

    def construct(self):
        # Parameters
        n = 1
        d = 1
        lam = 1

        axes = ThreeDAxes(x_range=[-4, 4], x_length=8)
        self.add(axes)

        # Define the surface
        points = []
        for theta in np.linspace(0, TAU, 50):
            for phi in np.linspace(0, np.pi, 25):
                def equation(rho):
                    return self.implicit_function(rho, theta, phi, n, d, lam)

                rho_solution = fsolve(equation, 1)[0]
                if rho_solution > 0:
                    x = rho_solution * np.sin(phi) * np.cos(theta)
                    y = rho_solution * np.sin(phi) * np.sin(theta)
                    z = rho_solution * np.cos(phi)
                    points.append(axes.c2p(x, y, z))

        surface = Surface(
            points,
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=(len(points), 1)
        )

        self.add(surface)
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        # self.begin_ambient_camera_rotation(rate=0.2)
        # self.wait(8)
