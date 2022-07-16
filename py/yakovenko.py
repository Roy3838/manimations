from tkinter import E
from manim import *
import numpy as np



class Yakovenko(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"



        e=2.718281828459045
        
        def funcexp(x):
            return e**(-x)
        
        def funcnor(x):
            return e**(-(x-2)**2)

        ax = Axes(
            x_range=[0, 4, 0.5],
            y_range=[0, 1, 0.2],
            tips=True,
            axis_config={"include_numbers": True},
            y_axis_config={"scaling": LogBase(custom_labels=True)}
        ).set_color(BLACK)
        
        labels = ax.get_axis_labels(x_label=Tex("\%"), y_label=Tex("\$"))
        labels.set_color(BLACK)

        curve_normal = ax.plot(lambda x: funcnor(x), x_range=[0, 4], color=BLUE_C)

        curve_exp = ax.plot(lambda x: funcexp(x), x_range=[0, 4], color=BLUE_C)


        self.play(Create(ax))
        self.play(Create(labels))

        self.wait()

        self.play(Create(curve_normal))

        self.wait()

        self.play(ReplacementTransform(curve_normal, curve_exp))

        self.wait()


        