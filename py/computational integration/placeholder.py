import numpy as np

ti, tf, dt = 0, 100, 1
y, x = np.zeros(tf), np.zeros(tf)
f = lambda t: -9.81*t + 5
for i in range(ti,tf-1,dt):
    y[i + 1] = y[i] + dt * f(x[i])
    print(y[i])