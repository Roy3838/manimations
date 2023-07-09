from manim import *
import numpy as np
import random as rd


class GammaBetaDist(Scene):

    def construct(self):
    
        # set seed of numpy and random
        np.random.seed(0)
        rd.seed(0)

        # set background color
        self.camera.background_color = "#E2E2E2"

        # generate gamma distribution numbers
        gamma = np.random.gamma(2, 2, 10)
        x=np.linspace(0, 10, 10)

        # Create Axes
        ax = Axes(
            x_range=[0, 2, 0.5],
            y_range=[0, 2, 0.5],
            tips=True,
            axis_config={"include_numbers": True}
            ).set_color(BLACK)

        plot1=ax.plot_line_graph(
            x_values=x,
            y_values=gamma,
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4
        ).set_color(BLACK)

        self.play(Create(ax),Create(plot1))

        