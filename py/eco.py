from itertools import count
from manim import *
import numpy as np
from random import randint, uniform





class eco(Scene):

    def construct(self):

        




        population = np.zeros(10000)
        population.fill(10)

        for i in range(10000000):
            yi=randint(0,10000-1)
            yb=randint(0,10000-1)
            mi=uniform(0,2)
            if population[yi]>0:
                population[yi]+=mi
                population[yb]-=mi
            c_d = 2
            if i%1000000==0:
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
                            ((19*c_d <= population) & (population < 20*c_d)).sum()
                            ],                        
                y_range=[0, 10000, 1000],
                y_length=6,
                x_length=10,
                x_axis_config={"font_size": 36})
                print(i)
                
                self.add(chart)
                self.wait(0.5)
        self.wait()
            
            
            
            

