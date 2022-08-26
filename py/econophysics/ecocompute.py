from itertools import count
from manim import *
import numpy as np
from random import randint, uniform
from ticktock import tick


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


print(mat)
print(len(mat))

clock.tock()
        
            
            
            
            

