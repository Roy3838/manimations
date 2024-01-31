from manim import *
import numpy as np
import termplotlib as tp

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def terminalplot(x,y=None):
    if y is None:
        y = x
        x = np.arange(len(y))
    fig = tp.figure()
    fig.plot(x,y)
    fig.show()

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
        phis = np.random.normal(0, 0.5, num_squares)  # Normally distributed phi values
        for phi in phis:
            square = OscillatingSquare(phi, scale =sigmoid(0.3*np.abs(1/phi))-0.4)
            self.add(square)


        #plot in order from low to high
        terminalplot(np.sort(phis))
        self.wait(10)

            
