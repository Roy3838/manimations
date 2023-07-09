from random import uniform
import numpy as np
from manim import *
from scipy.special.orthogonal import p_roots

width=1080
height=1920
config.frame_size = [width, height]

class montecarlo(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.camera.frame.scale(1)     

        def func(x): 
            return 2*np.sin(x)+2

        N=10000
        xmin=0
        xmax=5
        ymin=0
        ymax=5
        contadorint=0
        axes = Axes(
            x_range=[xmin, xmax, 1],
            y_range=[ymin, ymax, 1],
            axis_config={"color": GREY_C},
            tips=True,
        )
        funcion=axes.plot(func,color=GOLD)
        self.play(Create(axes),Create(funcion))
        dot1=Dot(color=BLUE).scale(0.5)
        dot2=Dot(color=RED_E).scale(0.5)

        for i in range(N):

            pointx=uniform(xmin,xmax)
            pointy=uniform(ymin,ymax)
            
            if pointy>=func(pointx):
                contadorint+=1
                dot=dot1.copy().move_to(axes.coords_to_point(pointx, pointy))
                self.add(dot)
            else:
                dot=dot2.copy().move_to(axes.coords_to_point(pointx, pointy))
                self.add(dot)
            coefficiente=contadorint/(i+1)
            areatotal=coefficiente*(xmax-xmin)*(ymax-ymin)
            
            #area=Text("Area = "+str(np.round(areatotal,1)),font="Courier").scale(0.5).to_corner(UL)
            if ((((i%20)==0)&(i<=(N/40)))|((i%600==0) & (i>(N/40)))):
                #division=MathTex(r'\frac{Puntos en el area}{Puntos totales} = \frac{' 
                #+ str(contadorint) + '}{' + str(i) + '} = ' + str(np.round(areatotal,1))).scale(0.5).to_corner(UL).shift(RIGHT)
                #self.add(division)
                self.wait(1/60)
                #self.remove(division)
        #self.add(division)
        self.wait()
        
        