from manim import *

class CodeFromString(Scene):
    def construct(self):
        code = '''import numpy as np

xi, xf, dx, vi = 0, 1, 0.1, 5

x = np.linspace(xi, xf, int((xf - xi) / dx))
y = np.zeros(len(x))
v = lambda t: -9.81*t + vi

for i in range(xi, len(x)-1, 1):
    y[i + 1] = y[i] + dx * v(x[i])
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace", line_spacing=0.8)
        self.add(rendered_code)