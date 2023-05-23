from itertools import count
from manim import *
import numpy as np
from random import randint, uniform
from ticktock import tick



class eco(Scene):

    def construct(self):

        self.camera.background_color = "#E2E2E2"
        clock = tick()
        population = np.zeros(100000)
        population.fill(10)
        iterations=40000000
        mat=np.zeros([230,100000])
        contador=0
        
        for i in range(int(iterations)):
            yi=randint(0,len(population)-1)
            yb=randint(0,len(population)-1)
            mi=uniform(0,1)
            if population[yb]>0:
                population[yi]+=mi
                population[yb]-=mi

            
            c_d = 2
            if ((i%(iterations/500)==0 and i<=iterations/10)  # 500 y 200
            or (i%(iterations/200)==0 and i>iterations/10)):
                mat[contador]=population
                contador+=1
                if (i<iterations/10):
                    rango=[0, 100000, 10000]
                elif(i==iterations/10):
                    rango=[0, 15000, 5000]
                    ogchart=chart.copy()
                else:
                    rango=[0, 15000, 5000]
                #BARCHART 
                chart = BarChart(
                    #social class count of people, 20 classes
                    values=[((0 < population) & (population < c_d)).sum(),
                            ((c_d <= population) & (population < 2*c_d)).sum(),
                            ((2*c_d <= population) & (population < 3*c_d)).sum(),
                            ((3*c_d <= population) & (population < 4*c_d)).sum(),
                            ((4*c_d <= population) & (population < 5*c_d)).sum(),
                            ((5*c_d <= population) & (population < 6*c_d)).sum(),
                            ((6*c_d <= population) & (population < 7*c_d)).sum(),
                            ((7*c_d <= population) & (population < 8*c_d)).sum(),
                            ((8*c_d <= population) & (population < 9*c_d)).sum(),
                            ((9*c_d <= population) & (population < 10*c_d)).sum(),
                            ((10*c_d <= population) & (population < 11*c_d)).sum(),
                            ((11*c_d <= population) & (population < 12*c_d)).sum(),
                            ((12*c_d <= population) & (population < 13*c_d)).sum(),
                            ((13*c_d <= population) & (population < 14*c_d)).sum(),
                            ((14*c_d <= population) & (population < 15*c_d)).sum(),
                            ((15*c_d <= population) & (population < 16*c_d)).sum(),
                            ((16*c_d <= population) & (population < 17*c_d)).sum(),
                            ((17*c_d <= population) & (population < 18*c_d)).sum(),
                            ((18*c_d <= population) & (population < 19*c_d)).sum(),
                            ((19*c_d <= population) & (population < 20*c_d)).sum(),
                            ((20*c_d <= population) & (population < 21*c_d)).sum(),
                            ((21*c_d <= population) & (population < 22*c_d)).sum(),
                            ((22*c_d <= population) & (population < 23*c_d)).sum(),
                            ((23*c_d <= population) & (population < 24*c_d)).sum(),
                            ((24*c_d <= population) & (population < 25*c_d)).sum(),
                            ],                        
                y_range=rango,
                y_length=6,
                x_length=10,
                x_axis_config={"font_size": 36, "color": BLACK},
                y_axis_config={"font_size": 36, "color": BLACK})
                
                #BARCHART

                print(i/iterations)
                if i == iterations/10:
                    self.add(ogchart)
                    self.play(ReplacementTransform(ogchart, chart.set_color(BLACK)))
                    self.wait()
                self.add(chart.set_color(BLACK))
                self.wait(0.05)
                self.remove(chart)
                
        self.add(chart)
        self.wait()
        print(mat)

        clock.tock()
        
            
            
            
            

