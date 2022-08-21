from manim import *
import numpy as np



class eco(Scene):
    def construct(self):
        ax = Axes().add_coordinates()
        def func(x):
            return x+1

        def func1(x):
            return -x+1

        