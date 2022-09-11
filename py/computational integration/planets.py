from manim import *
import numpy as np
import time
#from ticktock import tick
start=time.time()
width=1080
height=1920
config.frame_size = [width, height]
class Euler(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Calculate force between three bodies
        def fuerza(G,m1,m2,m3,r1,r2,r3):
            F12 = -G*m1*m2/np.linalg.norm(r1 - r2)**3 * (r1 - r2)
            F13 = -G*m1*m3/np.linalg.norm(r1 - r3)**3 * (r1 - r3)
            F=F12+F13
            return F

        G=6.67e-11
        """  Earth Sun Moon  """
        # masa [kg]
        m1 = 1.989e30 
        m2 = 1.89819e28
        m3 = 0.04784e24
        # posicion inicial [m]
        r10 = [0, 0, 0]
        r20 = [7.40522e11, 0, 0]
        r30 = [-5*384.4e7 + 7.405e11, 0, 0]
        # velocidad inicial [m/s]
        dr10 = [0, 0, 0]
        dr20 = [0, 13720, 0]
        dr30 = [0, np.sqrt(G*m2/np.linalg.norm(np.array(r20)-np.array(r30))) + 13720 , 0]

        """ EARTH SUN ASTEROID"""
        # masa [kg]
        m1 = 1.989e30
        m2 = 1.89819e28
        m3 = 0.04784e24
        # posicion inicial [m]
        r10 = [0, 0, 0]
        r20 = [7.40522e11, 0, 0]
        r30 = [-7.40522e11, 150000, 0]
        # velocidad inicial [m/s]
        dr10 = [0, 0, 0]
        dr20 = [0, 13720, 0]
        dr30 = [-7252.9479, 10370, 0]

        n= 1300
        d=3
        tf=1.3e+09
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
        #vel intermedia (para utulizar leapfrog)
        dR1i = np.zeros((n,d))
        dR2i = np.zeros((n,d))
        dR3i = np.zeros((n,d))
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
                print(t)
                R1[t+1][:] = R1[t][:] + dt*dR1[t][:]
                R2[t+1][:] = R2[t][:] + dt*dR2[t][:]
                R3[t+1][:] = R3[t][:] + dt*dR3[t][:]

                F1[t+1][:] = fuerza(G,m1,m2,m3,R1[t+1][:],R2[t+1][:],R3[t+1][:])
                F2[t+1][:] = fuerza(G,m2,m1,m3,R2[t+1][:],R1[t+1][:],R3[t+1][:])
                F3[t+1][:] = fuerza(G,m3,m1,m2,R3[t+1][:],R1[t+1][:],R2[t+1][:])

                dR1[t+1][:]=dR1[t][:]+dt*F1[t+1][:]/m1
                dR2[t+1][:]=dR2[t][:]+dt*F2[t+1][:]/m2
                dR3[t+1][:]=dR3[t][:]+dt*F3[t+1][:]/m3

        elif LeapFrog:
            for t in range(0,n-1):
                dR1i[t+1][:] = dR1[t][:] + 0.5*dt*F1[t][:]/m1
                dR2i[t+1][:] = dR2[t][:] + 0.5*dt*F2[t][:]/m2
                dR3i[t+1][:] = dR3[t][:] + 0.5*dt*F3[t][:]/m3

                R1[t+1][:] = R1[t][:] + dt*dR1i[t+1][:]
                R2[t+1][:] = R2[t][:] + dt*dR2i[t+1][:]
                R3[t+1][:] = R3[t][:] + dt*dR3i[t+1][:]

                F1[t+1][:] = fuerza(G,m1,m2,m3,R1[t+1][:],R2[t+1][:],R3[t+1][:])
                F2[t+1][:] = fuerza(G,m2,m1,m3,R2[t+1][:],R1[t+1][:],R3[t+1][:])
                F3[t+1][:] = fuerza(G,m3,m1,m2,R3[t+1][:],R1[t+1][:],R2[t+1][:])

                dR1[t+1][:] = dR1i[t+1][:] + 0.5*dt*F1[t+1][:]/m1
                dR2[t+1][:] = dR2i[t+1][:] + 0.5*dt*F2[t+1][:]/m2
                dR3[t+1][:] = dR3i[t+1][:] + 0.5*dt*F3[t+1][:]/m3

        # Graficar
        planet1=Sphere(radius=0.3,fill_opacity=1,fill_color=BLUE,stroke_width=0)
        planet2=Sphere(radius=0.3,fill_opacity=1,fill_color=RED,stroke_width=0)
        planet3=Sphere(radius=0.3,fill_opacity=1,fill_color=GREEN,stroke_width=0)
        scalingfactor=(8e+11)/4
        for i in range(n):
            if i % 2 == 0:
                planet1.move_to(R1[i][:]/scalingfactor)
                planet2.move_to(R2[i][:]/scalingfactor)
                planet3.move_to(R3[i][:]/scalingfactor)
                self.add(planet1,planet2,planet3)
                self.wait(1/60)
                self.remove(planet1,planet2,planet3)
        
        #self.add(Text("hi"))
        print(str(time.time()-start) + " seconds")
        
