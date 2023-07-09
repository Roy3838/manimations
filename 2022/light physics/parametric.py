from manim import *
import numpy as np

class ParametricSurfaceAnimation(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        def funcparametric3d(u, v, lamb = 2, n = 2, d = 3, s = -1):

            # https://www.desmos.com/calculator/lohclpowwf
            # y equals y = -sqrt(-16 d^2 λ^2 n^2 + 256 d^2 u^2 + λ^4 n^4 - 16 λ^2 n^2 u^2 - 16 λ^2 n^2 v^2)/(4 λ n)
            # and x = u and z = v
            x = u
            y = v
            
            z = s*np.sqrt(-16 * d**2 * lamb**2 * n**2 + 256 * d**2 * u**2 + lamb**4 * n**4 - 16 * lamb**2 * n**2 * u**2 - 16 * lamb**2 * n**2 * v**2)/(4 * lamb * n)

            return np.array([x, y, z])

        axes = ThreeDAxes().set_color(BLACK)

        surface = Surface(
            lambda u, v: axes.c2p(*funcparametric3d(u, v)),
            u_range=[9, 10],
            v_range=[-10, 10],
            resolution=5,
        )

        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(Create(axes))
        self.play(Create(surface))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
