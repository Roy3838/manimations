from manim import *
import numpy as np
from random import uniform

class montecarlo(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        ax = Axes(
            x_range=[0, 5], y_range=[0, 3, 1], axis_config={"include_tip": True}
        ).set_color(BLACK)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)

        def func(x):
            return np.sin(x)+1
        graph = ax.plot(func, color=BLACK)

        
        contadorint=0
        contador=ValueTracker(0)
        label=Text("Puntos = "+ str(contadorint))
        label.add_updater(lambda z: z.become(
            Text("Puntos = "+ str(contador.get_value())).move_to(3*UP+3*RIGHT).set_color(BLACK)
        ))
        N=100
        xmin=0
        xmax=5
        ymin=0
        ymax=3
        self.play(Create(graph),Create(ax),Create(labels),Create(label))
        for i in range(N):
            pointx=uniform(xmin,xmax)
            pointy=uniform(ymin,ymax)
            if pointy>=func(pointx):
                contadorint+=1
                contador.set_value(contadorint)
                dot=Dot(color=ORANGE).move_to(ax.c2p(pointx,pointy))
            else:
                dot=Dot(color=PURPLE).move_to(ax.c2p(pointx,pointy))
            self.remove(label)
            label.set_value("Puntos = "+ str(contador.get_value()))
            self.add(label)
            self.add(dot)
            self.wait(0.1)
        self.wait()






        
        