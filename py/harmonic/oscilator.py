from manim import *
import numpy as np

class OscillatingSquare(VGroup):
    def __init__(self, phi, w=np.pi, opacity = 0.1, A=2, scale =0.5 , **kwargs):
        super().__init__(**kwargs)
        self.square = Square(color=BLACK, fill_opacity=opacity).set_fill(GREY_C).scale(scale)
        self.add(self.square)
        self.t = 0
        self.phi = phi
        self.w = w
        self.A = A
        self.add_updater(self.oscilator_update)

    def oscilator_update(self, mobject, dt):
        self.t += dt
        self.square.move_to([self.A * np.sin(self.t * self.w + self.phi), 1, 0])

class Oscilator(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        num_squares = 50  # Number of squares
        phis = np.random.normal(0, 1, num_squares)  # Normally distributed phi values
        print(phis)
        for phi in phis:
            square = OscillatingSquare(phi, scale = np.abs( np.sig( 1/phi )))
            self.add(square)

        self.wait(3)

            
