from manim import *
import numpy as np
from random import uniform

class inv(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        epsilon=0.001

        w0=6
        def func(x):
            return 1/((w0*x)**2+1)
        def invfunc(x):
            return (1/w0)*np.tan(w0*x)   #nunca olvides epsilon ;)
        
        axes=Axes(x_range=[-2,2],y_range=[0,2]).set_color(BLACK)
        graph=axes.plot(func,color=MAROON, x_range=[-1.3,1.3])
        graph2=axes.plot(invfunc,color=MAROON, x_range=[-0.23,0.23])
        #graphconstante=axes.plot(lambda x: 1,color=MAROON)

        N=1000
        x=np.zeros(N)
        x_2=np.zeros(N)
        a=-2
        b=2
        dots=VGroup()
        dotsnuevos=VGroup()
        self.play(Create(axes),Create(graph))
        for i in range(N):
            x[i]=uniform(a,b)
            dots.add(*[
                Dot(axes.c2p(x[i],0)).set_color(BLACK).scale(0.4)
            ])
        for m in range(N):
            x_2[m]=invfunc(x[m])
            dotsnuevos.add(*[
                Dot(axes.c2p(x_2[m],0)).set_color(BLACK).scale(0.4)
            ])
        self.play(Create(dots))
        self.play(Create(graph2))
        self.play(FadeOut(dots))
        self.play(Create(dotsnuevos))
        self.wait()
