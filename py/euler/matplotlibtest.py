from manim import *
import numpy as np
import time
import matplotlib.pyplot as plt
#from ticktock import tick
start=time.time()


def fuerza(G,m1,m2,m3,r1,r2,r3):
    F12 = -G*m1*m2/np.linalg.norm(r1 - r2)**3 * (r1 - r2)
    F13 = -G*m1*m3/np.linalg.norm(r1 - r3)**3 * (r1 - r3)
    F=F12+F13
    return F


def compute(
    # """ EARTH SUN ASTEROID"""
    # masa [kg]
    m1 = 20,
    m2 = 1,
    m3 = 0.1,
    # posicion inicial [m]
    r10 = [0, 0],
    r20 = [3, 0],
    r30 = [3, 3],
    # velocidad inicial [m/s]
    dr10 = [0, 0],
    dr20 = [0, 1],
    dr30 = [1, 1],

    n= 10,
    d=2,
    tf=3,
    G=1
    ):

    dt=tf/n
    T=np.arange(0,tf,n)

    #pos

    R1= np.zeros((n,d))
    R2= np.zeros((n,d))
    R3= np.zeros((n,d))
    #vel
    dR1= np.zeros((n,d))
    dR2= np.zeros((n,d))
    dR3= np.zeros((n,d))

    # fuerza en cada cuerpo
    F1 = np.zeros((n,d))
    F2 = np.zeros((n,d))
    F3 = np.zeros((n,d))

    # Valores iniciales
    # pos
    R1[0][:]=r10
    R2[0][:]=r20
    R3[0][:]=r30
    # vel
    dR1[0][:]=dr10
    dR2[0][:]=dr20
    dR3[0][:]=dr30
    # Fuerza
    F1[0][:] = fuerza(G,m1,m2,m3,R1[0][:],R2[0][:],R3[0][:])
    F2[0][:] = fuerza(G,m2,m1,m3,R2[0][:],R1[0][:],R3[0][:])
    F3[0][:] = fuerza(G,m3,m1,m2,R3[0][:],R1[0][:],R2[0][:])
    mEuler = True
    LeapFrog=False

    if mEuler:
        for t in range(0,n-1):
            #print(t)
            R1[t+1][:] = R1[t][:] + dt*dR1[t][:]
            R2[t+1][:] = R2[t][:] + dt*dR2[t][:]
            R3[t+1][:] = R3[t][:] + dt*dR3[t][:]

            F1[t+1][:] = fuerza(G,m1,m2,m3,R1[t+1][:],R2[t+1][:],R3[t+1][:])
            F2[t+1][:] = fuerza(G,m2,m1,m3,R2[t+1][:],R1[t+1][:],R3[t+1][:])
            F3[t+1][:] = fuerza(G,m3,m1,m2,R3[t+1][:],R1[t+1][:],R2[t+1][:])

            dR1[t+1][:]=dR1[t][:]+dt*F1[t+1][:]/m1
            dR2[t+1][:]=dR2[t][:]+dt*F2[t+1][:]/m2
            dR3[t+1][:]=dR3[t][:]+dt*F3[t+1][:]/m3

    return R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30

def compute_and_plot(n):

    R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30= compute(
        m1 = 1.989e30,
        m2 = 1.89819e28,
        m3 = 0.04784e24,
        r10 = [0, 0],
        r20 = [7.40522e11, 0],
        r30 = [-7.40522e11, 150000],
        dr10 = [0, 0],
        dr20 = [0, 13720],
        dr30 = [0, 10370],
        n=n,
        d=2,
        tf=1.3e+09,
        G=6.67e-11
    )

    plot_orbits(R1, R2, R3)

def plot_orbits(R1, R2, R3):

    # # Plot Earth
    # plt.plot(R1[:, 0], R1[:, 1], label="Earth")

    # # Plot Sun
    # plt.plot(R2[:, 0], R2[:, 1], label="Sun")

    # Plot Asteroid
    plt.plot(R3[:, 0], R3[:, 1], label="Asteroid")

plt.figure(figsize=(10, 10))


for n in range(25, 251, 25):  # Step size of 25, from 25 to 250
    compute_and_plot(n)



# Plot only from -8e11 to 8e11
plt.xlim(-16e11, 16e11)
plt.ylim(-16e11, 16e11)

plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.legend()
plt.grid(True)


plt.show()
