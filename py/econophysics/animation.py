from itertools import count
from manim import *
import numpy as np
from random import randint, uniform
from ticktock import tick


class eco(Scene):

    def construct(self):
        def norm(x):
            #mori haciendo esto https://www.desmos.com/calculator/dvrjjqrzck
            #normal distribution
            #\frac{N}{s\sqrt{2\pi}}e^{\frac{-\left(x-u\right)^{2}}{2s^{2}}}
            N=102000
            s=2.3
            u=4.1
            A=N/(s*np.sqrt(2*np.pi))
            arg=-(x-u)**2 / (2*s**2)
            y=(A)*np.exp(arg)
            return y
        def expo(x):
            #data from desmos
            c=2.5
            A=23000
            b=-0.173


            #direct data from excel 
            """c=0
            A=25690
            b=-0.216 """
            y=A*np.exp(b*(x+c))
            return y
        self.camera.background_color = "#E2E2E2"
        clock = tick()
        iterations=230

        c_d = 2

        #read raw data from csv
        """ print("reading csv")
        mat= np.genfromtxt('mat.csv', delimiter=',')
        print("mat loaded") """

        #read data from classes csv
        print("reading csv")
        matclass= np.genfromtxt('matclasses.csv', delimiter=',')
        print("mat loaded")
        i_cambio=40
        #bar chart animation
        for i in range(230):

            if (i<i_cambio):
                rango=[0, 100000, 10000]
            elif(i==i_cambio):
                rango=[0, 15000, 5000]
                ogchart=chart.copy()
            else:
                rango=[0, 15000, 5000]
            #BARCHART 
            #population=mat[i]
            classes=matclass[i]
            classes=classes[1:]
            chart = BarChart(
                #social class count of people, 20 classes
                values=classes,                        
            y_range=rango,
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36, "color": BLACK},
            y_axis_config={"font_size": 36, "color": BLACK})
            
            #BARCHART

            print(i/iterations)
            if i == i_cambio:
                


                self.add(ogchart)
                normal=ogchart.plot(norm, color=BLUE)
                self.play(Create(normal))
                self.wait(1)
                self.play(Uncreate(normal))
                self.play(ReplacementTransform(ogchart, chart.set_color(BLACK)), run_time=1)
                self.wait()





            self.add(chart.set_color(BLACK))
            
            if i == 1:
                self.wait(2)
            if i<i_cambio:
                self.wait(0.1)
            else:
                self.wait(0.05)
            self.remove(chart)


        self.add(chart)
        expplot=chart.plot(expo, color=BLUE)
        self.play(Create(expplot))
        self.wait()
        self.play(FadeOut(expplot))
        self.wait()
        self.play(FadeOut(chart))
        self.wait()

        clock.tock()
        
            