from manim import *
import numpy as np
import time
#from ticktock import tick
start=time.time()
width=1080
height=1920
config.frame_size = [width, height]
class Planets(ThreeDScene):
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

        d=3

        n= int(1300/10)
        tf=1.3e+08

        dt=tf/n
        #OR FORCE MORE TIME WITH SAME DT
        multiplier=2
        tf = tf*multiplier
        n=n*multiplier


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
        mEuler = False
        LeapFrog=True

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
        planet1=Sphere(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW)
        planet2=Sphere(radius=0.2,fill_opacity=1,stroke_width=0).set_color(GREEN)
        planet3=Sphere(radius=0.1,fill_opacity=1,stroke_width=0).set_color(BLACK)

        scalingfactor=(8e+11)/4
        scalingfactorv=13720


        # Planets and their initial positions
        planet1=Sphere(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW).move_to(R1[0][:]/scalingfactor)
        planet2=Sphere(radius=0.2,fill_opacity=1,stroke_width=0).set_color(GREEN).move_to(R2[0][:]/scalingfactor)
        planet3=Sphere(radius=0.1,fill_opacity=1,stroke_width=0).set_color(BLACK).move_to(R3[0][:]/scalingfactor)

        # Store locations and velocities
        planet1.locations = R1/scalingfactor
        planet2.locations = R2/scalingfactor
        planet3.locations = R3/scalingfactor

        planet1.velocities = dR1/scalingfactorv
        planet2.velocities = dR2/scalingfactorv
        planet3.velocities = dR3/scalingfactorv

        # Initialize time offset
        planet1.t_offset = 0
        planet2.t_offset = 0
        planet3.t_offset = 0


        def planet_updater(mob, dt):
            mob.t_offset += (int(dt * n))
            mob.move_to(mob.locations[mob.t_offset % len(mob.locations)])

        

        # Add updaters to the planets
        planet1.add_updater(planet_updater)
        planet2.add_updater(planet_updater)
        planet3.add_updater(planet_updater)

        # Add planets to the scene
        self.add(planet1,planet2,planet3)
        
        self.wait(n/120)
        self.play(Write(Text("hi")))
        self.wait(n/120)

        # Remove the planets
        self.remove(planet1,planet2,planet3)



        # for i in range(0,n,1):
        #     print(str(round((i*100/n),2)) + "%")
        #     planet1.move_to(R1[i][:]/scalingfactor)
        #     planet2.move_to(R2[i][:]/scalingfactor)
        #     planet3.move_to(R3[i][:]/scalingfactor)
        #     #print(dR3[i][:]/scalingfactorv)
        #     arrowplanet2=Arrow(start=R2[i][:]/scalingfactor, end=R2[i][:]/scalingfactor+dR2[i][:]/scalingfactorv, buff=0,color=GREY_C)
        #     arrowplanet3=Arrow(start=R3[i][:]/scalingfactor, end=R3[i][:]/scalingfactor+dR3[i][:]/scalingfactorv, buff=0,color=GREY_C)
        #     self.add(planet1,planet2)
        #     self.add(planet3)#,arrowplanet2,arrowplanet3)
        #     self.wait(1/60)
        #     self.remove(planet1,planet2,planet3)#,arrowplanet2,arrowplanet3)
        #     # if i==n/2 :
        #     #     #ecuacion de Gravitacion de Newton en LaTeX
        #     #     ecuaciones=MathTex(r"F\left(r\right)=G\frac{mM}{r^{2}}").move_to(UP*2)
        #     #     ecuaciones.set_color(BLACK)
        #     #     self.add_fixed_in_frame_mobjects(ecuaciones)
        
        # #self.add(Text("hi"))
        # print(str(time.time()-start) + " seconds")
        
