from random import uniform
import numpy as np
from manim import *
from scipy.special.orthogonal import p_roots



class montecarlo(Scene):
    def construct(self):
        def func(x): 
            return 2*np.sin(x)+2
        N=100000
        xmin=0
        xmax=5
        ymin=0
        ymax=5
        contadorint=0
        axes = Axes(
            x_range=[xmin, xmax, 1],
            y_range=[ymin, ymax, 1],
            axis_config={"color": GREEN},
            tips=True,
        )
        funcion=axes.plot(func,color=RED)
        self.play(Create(axes),Create(funcion))
        for i in range(N):
            pointx=uniform(xmin,xmax)
            pointy=uniform(ymin,ymax)
            if pointy>=func(pointx):
                contadorint+=1
                dot=Dot(color=BLUE).move_to(axes.coords_to_point(pointx, pointy)).scale(0.5)
            else:
                dot=Dot(color=RED_E).move_to(axes.coords_to_point(pointx, pointy)).scale(0.5)
            coefficiente=contadorint/(i+1)
            areatotal=coefficiente*(xmax-xmin)*(ymax-ymin)
            
            #area=Text("Area = "+str(np.round(areatotal,1)),font="Courier").scale(0.5).to_corner(UL)
            self.add(dot)
            if ((((i%20)==0)&(i<=(N/40)))|((i%600==0) & (i>(N/40)))):
                division=MathTex(r'\frac{Puntos en el area}{Puntos totales} = \frac{' 
                + str(contadorint) + '}{' + str(i) + '} = ' + str(np.round(areatotal,1))).scale(0.5).to_corner(UL).shift(RIGHT)
                self.add(division)
                self.wait(0.1)
                self.remove(division)
        self.add(division)
        self.wait()
        
        