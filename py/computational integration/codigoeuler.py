from manim import *

class CodeFromString(Scene):
    def construct(self):
        code = '''import numpy as np

y, x = np.zeros(100), np.zeros(100)
lambda f(x) : -9.81*x

for i in range(tf,ti,dt):
    y[i + 1] = y[i] + dt * f(x[i])
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace", line_spacing=0.8)
        self.add(rendered_code)