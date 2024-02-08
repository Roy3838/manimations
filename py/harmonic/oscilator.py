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

class Spring(VMobject):
    def __init__(self, start=LEFT, end=RIGHT, num_coils=5, width=2, **kwargs):
        """
        Creates a spring object.

        Parameters:
        - start (np.ndarray): The starting point of the spring. Default is LEFT.
        - end (np.ndarray): The ending point of the spring. Default is RIGHT.
        - num_coils (int): The number of coils in the spring. Default is 5.
        - width (float): The width of the spring. Default is 2.
        - kwargs: Additional keyword arguments to be passed to the VMobject constructor.
        """
        super().__init__(**kwargs)
        self.start = start
        self.end = end
        self.num_coils = num_coils
        self.width = width
        self.draw_spring()

    def draw_spring(self):
        """
        Draws the spring based on the current start, end, num_coils, and width values.
        """
        self.clear_points()
        direction = self.end - self.start
        length = np.linalg.norm(direction)
        direction = direction / length  # Normalize

        # Calculate points for the spring
        points = [self.start]
        for i in range(1, self.num_coils + 1):
            point = self.start + direction * (length / self.num_coils) * i
            if i % 2 == 0:
                points.append(point)
            else:
                offset = np.array([-direction[1], direction[0], 0]) * self.width
                points.append(point + offset)

        # Draw the spring
        self.set_points_as_corners(points)

    def put_start_and_end_on(self, start, end):
        """
        Updates the start and end points of the spring and redraws it.

        Parameters:
        - start (np.ndarray): The new starting point of the spring.
        - end (np.ndarray): The new ending point of the spring.
        """
        self.start = start
        self.end = end
        self.draw_spring()


class OscillatingSquare(VGroup):
    def __init__(self, phi, w=np.pi, opacity=0.1, A=2, scale=0.5, **kwargs):
        super().__init__(**kwargs)
        self.square = Square(color=BLACK, fill_opacity=opacity).set_fill(GREY_C).scale(scale)
        self.spring = Spring().set_color(GREY).stretch_to_fit_height(1)
        self.spring.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], self.square.get_center()))
        self.add(self.spring, self.square)

        self.t = 0
        self.phi = phi
        self.w = w
        self.A = A
        self.add_updater(self.oscillator_update)

    def oscillator_update(self, mobject, dt):
        self.t += dt
        self.square.move_to([self.A * np.sin(self.t * self.w + self.phi), 1, 0])

class Oscillator(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        num_squares = 1  # Number of squares
        phis = np.random.normal(0, 0.5, num_squares)  # Normally distributed phi values
        for phi in phis:
            square = OscillatingSquare(phi, scale=sigmoid(0.3*np.abs(1/phi))-0.4)
            self.add(square)

        self.wait(10)
            
