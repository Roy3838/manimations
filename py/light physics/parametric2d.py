from manim import *
import numpy as np



class parametric(ThreeDScene):


    def construct(self):
        self.camera.background_color = "#E2E2E2"


        def funcparametric3d(u, v, lamb=0.5, d=1.5, n=1, s=1):

            # https://www.desmos.com/calculator/lohclpowwf
            # y equals y = -sqrt(-16 d^2 λ^2 n^2 + 256 d^2 u^2 + λ^4 n^4 - 16 λ^2 n^2 u^2 - 16 λ^2 n^2 v^2)/(4 λ n)
            # and x = u and z = v
            x = u
            y = v
            
            z = s*np.sqrt(-16 * d**2 * lamb**2 * n**2 + 256 * d**2 * u**2 + lamb**4 * n**4 - 16 * lamb**2 * n**2 * u**2 - 16 * lamb**2 * n**2 * v**2)/(4 * lamb * n)

            return np.array([x, y , z])

        def funcs(u, lamb=0.5, d=1.5, n=1, s=1):
            # https://www.desmos.com/calculator/rht8qrfnxi
            x = u
            y = s*np.sqrt(16 * d**2 - lamb**2 * n**2)*np.sqrt( 16 * u**2 - lamb**2 * n**2)/(4 * lamb * n)
            return np.array((x, y, 0))               

        ax1 = ThreeDAxes().set_color(BLACK)

        hyperbolas = VGroup()

        # Create top and bottom hyperbolas of the interference pattern
        # Change dt if lambda, s or d change
        for i in range(1, 12):
            hyp = ax1.plot(
                lambda x: funcs(x, s=1, lamb=0.5, d=1.5, n=i)[1], # ojito que solo regrese el valor de y, y no el vector xyz
                discontinuities=[0],  # discontinuous points
                dt=0.125*i,  # left and right tolerance of discontinuity
                color=RED,
            )
            hyp_ = ax1.plot(
                lambda x: funcs(x, s=-1, lamb=0.5, d=1.5, n=i)[1], # ojito que solo regrese el valor de y, y no el vector xyz
                discontinuities=[0],  # discontinuous points
                dt=0.125*i,  # left and right tolerance of discontinuity
                color=RED,
            )
            hyperbolas.add(hyp, hyp_)


        surface = Surface(
            lambda u, v: ax1.c2p(*funcparametric3d(u, v)),
            u_range=[0.151, 1],
            v_range=[-1, 1],
            resolution=20,
        )

        surface = Surface(
            lambda u, v: ax1.c2p(*funcparametric3d(u, v, s=-1)),
            u_range=[-0.151, -1],
            v_range=[-1, 1],
            resolution=20,
        )


        self.play(Create(ax1))
        self.wait()
        
        self.play(Write(hyperbolas), run_time=3)
        self.play(Write(surface))
        self.move_camera(phi=-30 * DEGREES, theta=-80 * DEGREES)
        self.move_camera(phi=30 * DEGREES, theta=-80 * DEGREES)
        self.move_camera(phi=30 * DEGREES, theta=80 * DEGREES)
        self.wait()