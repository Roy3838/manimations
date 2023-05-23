from itertools import count
from manim import *
import numpy as np
from random import randint, uniform
from ticktock import tick
import pandas as pd

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

        print(i/iterations)


values=np.zeros([230,25])

for i in range(230):
    population=mat[i]
    values[i]=[((0 < population) & (population < c_d)).sum(),
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
                                ]

dataset=pd.DataFrame(values)
#save dataset to csv
dataset.to_csv('matclasses.csv', index=False)

clock.tock()
        
            
            
            
            

