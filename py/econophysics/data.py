import matplotlib.pyplot as plt
import numpy as np


# A script that helps me create a data set for the econophysics project


# Cientific notation
x=[10**0,10**0.5,10**1,10**1.5,10**1.75,10**2,10**2.25,10**2.5]
y=[10**2,10**1.8,10**1.65,10**1.5,10**1,10**0.5,10**0.4,10**0.3]
# Non cientific notation
x=[1  , 3.16 , 10   , 31.62, 56.23, 63.09 , 100  , 177.82, 316.22 ]
y=[90 , 80   , 60.66, 25.62, 8    , 3.98  , 3.162, 2.51  , 1.99   ]


# Income distribution in the USA, 1997

# Cientific notation
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# def BoltzManng(x):
#     b = 101.2
#     a = 0.1915
#     return -np.exp(a*x)+b

def BoltzManng(x):
    c = 4.63
    b = 0
    a = 0.0295
    return np.exp(-a*x+c)+b



y=[np.round(BoltzManng(x)) for x in x]
print(y)
plt.scatter(x,y)
plt.show()

