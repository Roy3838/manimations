from manim import *
import numpy as np
import time
#from ticktock import tick
start=time.time()
width=1080
height=1920
config.frame_size = [width, height]
class PlanetsForce(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.camera.frame.scale(0.7)

# Calculate force between three bodies
        def fuerza(G,m1,m2,m3,r1,r2,r3):
            F12 = -G*m1*m2/np.linalg.norm(r1 - r2)**3 * (r1 - r2)
            F13 = -G*m1*m3/np.linalg.norm(r1 - r3)**3 * (r1 - r3)
            F=F12+F13
            return F

        def compute():
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

            n= 1300*2
            d=3
            tf=1.3e+09*2
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

            return R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30

        def twoDplanets():
            R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30 = compute()

            scalingfactor=(8e+11)/4 
            scalingfactorv=13720/1.5

            scalingfactorf=np.amax(F1)/1.7 #force vector scaling factor for scene
            scalingfactorf3=np.amax(F3) #the third object varies a lot in force so it is not used

            planet1=Dot(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW)
            planet2=Dot(radius=0.3,fill_opacity=1,stroke_width=0).set_color(GREEN)
            planet3=Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)

            planet1=Dot(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW).move_to(R1[0][:]/scalingfactor)
            planet2=Dot(radius=0.3,fill_opacity=1,stroke_width=0).set_color(GREEN).move_to(R2[0][:]/scalingfactor)
            planet3=Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C).move_to(R3[0][:]/scalingfactor)

            vel2 = Arrow(ORIGIN,dR2[0][:]/scalingfactorv).set_color(RED).move_to(R2[0][:]/scalingfactor)
            vel3 = Arrow(ORIGIN,dR3[0][:]/scalingfactorv).set_color(RED).move_to(R3[0][:]/scalingfactor)

            force2 = Arrow(ORIGIN,F2[0][:]/scalingfactorf).set_color(BLUE).move_to(R2[0][:]/scalingfactor)
            force3 = Arrow(ORIGIN,F3[0][:]/scalingfactorf).set_color(BLUE).move_to(R3[0][:]/scalingfactor)

            planet1.locations = R1/scalingfactor
            planet2.locations = R2/scalingfactor
            planet3.locations = R3/scalingfactor

            vel2.locations = R2/scalingfactor
            vel3.locations = R3/scalingfactor

            vel2.velocities = dR2/scalingfactorv
            vel3.velocities = dR3/scalingfactorv

            force2.locations = R2/scalingfactor
            force3.locations = R3/scalingfactor

            force2.forces = F2/scalingfactorf
            force3.forces = F3/scalingfactorf

            planet1.t_offset = 0
            planet2.t_offset = 0
            planet3.t_offset = 0

            vel2.t_offsetv = 0
            vel3.t_offsetv = 0

            force2.t_offsetf = 0
            force3.t_offsetf = 0

            def planet_updater(mob, dt):
                mob.t_offset += int(dt*n/12)
                mob.move_to(mob.locations[mob.t_offset % len(mob.locations)])

            def velocity_updater(mob, dt):
                mob.t_offsetv += int(dt*n/12)
                mob.become(
                    Arrow(ORIGIN, mob.velocities[mob.t_offsetv % len(mob.velocities)])
                ).move_to(
                    mob.locations[mob.t_offsetv % len(mob.locations)]
                    + mob.velocities[mob.t_offsetv % len(mob.velocities)]/2
                ).set_color(RED)  # Set arrow color

            def force_updater(mob, dt):
                mob.t_offsetf += int(dt*n/12)
                mob.become(
                    Arrow(ORIGIN, mob.forces[mob.t_offsetf % len(mob.forces)])
                ).move_to(
                    mob.locations[mob.t_offsetf % len(mob.locations)]
                    + mob.forces[mob.t_offsetf % len(mob.forces)]/2
                ).set_color(GOLD)

            planet1.add_updater(planet_updater)
            planet2.add_updater(planet_updater)
            planet3.add_updater(planet_updater)

            vel2.add_updater(velocity_updater)
            vel3.add_updater(velocity_updater)

            force2.add_updater(force_updater)
            force3.add_updater(force_updater)

            trace2 = TracedPath(planet2.get_center, dissipating_time=2).set_color(BLACK)
            trace3 = TracedPath(planet3.get_center, dissipating_time=2).set_color(BLACK)

            example_listing = Code(
                "/home/jay/manimations/py/euler/example.py",
                tab_width=4,
                background="window",
                language="python",
                font="Monospace",
                background_stroke_color= WHITE,
            ).shift(9*UP).scale(1.1)


            # Add planets to the scene
            self.add(planet1,planet2,planet3,vel2,vel3, trace2, trace3, force2, force3)
            
            self.wait(3)

            self.play(Write(example_listing),self.camera.frame.animate.move_to(UP*4))

            self.wait(2)

            # Remove the planets
            self.remove(planet1,planet2,planet3)

                

        twoDplanets()