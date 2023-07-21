from manim import *
import numpy as np
import time
#from ticktock import tick
start=time.time()
width=1080
height=1920
config.frame_size = [width, height]
class PlanetsForce(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

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

            return R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30
        
        def threeDplanets():
            # Set camera orientation
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            # Move camera closer
            self.move_camera(zoom=1.5)

            R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30 = compute()

            # Graficar
            planet1=Sphere(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW)
            planet2=Sphere(radius=0.2,fill_opacity=1,stroke_width=0).set_color(GREEN)
            planet3=Sphere(radius=0.1,fill_opacity=1,stroke_width=0).set_color(BLACK)

            scalingfactor=(8e+11)/4
            scalingfactorv=13720/1.2


            # Planets and their initial positions
            planet1=Sphere(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW).move_to(R1[0][:]/scalingfactor)
            planet2=Sphere(radius=0.2,fill_opacity=1,stroke_width=0).set_color(GREEN).move_to(R2[0][:]/scalingfactor)
            planet3=Sphere(radius=0.1,fill_opacity=1,stroke_width=0).set_color(BLACK).move_to(R3[0][:]/scalingfactor)

            # Store locations and velocities
            planet1.locations = R1/scalingfactor
            planet2.locations = R2/scalingfactor
            planet3.locations = R3/scalingfactor

            #vel1 = Arrow(ORIGIN,dR1[0][:]/scalingfactorv).set_color(YELLOW).move_to(R1[0][:]/scalingfactor)
            vel2 = Arrow(ORIGIN,dR2[0][:]/scalingfactorv).set_color(GREEN).move_to(R2[0][:]/scalingfactor)
            vel3 = Arrow(ORIGIN,dR3[0][:]/scalingfactorv).set_color(BLACK).move_to(R3[0][:]/scalingfactor)

            #vel1.locations = R1/scalingfactor
            vel2.locations = R2/scalingfactor
            vel3.locations = R3/scalingfactor

            #vel1.velocities = dR1/scalingfactorv
            vel2.velocities = dR2/scalingfactorv
            vel3.velocities = dR3/scalingfactorv

            # Initialize time offset
            planet1.t_offset = 0
            planet2.t_offset = 0
            planet3.t_offset = 0

            # Initialize time offset
            #vel1.t_offsetv = 0
            vel2.t_offsetv = 0
            vel3.t_offsetv = 0

            def planet_updater(mob, dt):
                # Convert to time
                mob.t_offset += int(dt*n/12)
                mob.move_to(mob.locations[mob.t_offset % len(mob.locations)])

            def velocity_updater(mob, dt):
                # Convert to time
                mob.t_offsetv += int(dt*n/12)
                mob.become(
                    Arrow(ORIGIN,mob.velocities[mob.t_offsetv % len(mob.velocities)])
                    ).move_to(
                    mob.locations[mob.t_offsetv % len(mob.locations)]
                    + mob.velocities[mob.t_offsetv % len(mob.velocities)]/2
                    ).set_color(BLACK)

            # Add updaters to the planets
            planet1.add_updater(planet_updater)
            planet2.add_updater(planet_updater)
            planet3.add_updater(planet_updater)

            #vel1.add_updater(velocity_updater)
            vel2.add_updater(velocity_updater)
            vel3.add_updater(velocity_updater)

            example_listing = Code(
                "/home/jay/manimations/py/euler/example.py",
                tab_width=4,
                background="window",
                language="python",
                font="Monospace",
                background_stroke_color= WHITE,
            ).shift(6*UP).scale(1.5)


            # Add planets to the scene
            self.add(planet1,planet2,planet3,vel2,vel3)
            
            self.wait(3)

            self.add_fixed_in_frame_mobjects(example_listing)
            self.play(Write(example_listing))

            self.wait(1)

            # Remove the planets
            self.remove(planet1,planet2,planet3)

            # for i in range(0,int(n/5),10):
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

        def twoDplanets():
            
            R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30 = compute()
            
            axesss = NumberPlane().set_color(GREY_C).scale(1.5).rotate(PI/2)
            planetas2=VGroup()
            posiciones2=VGroup()
            velocidades2=VGroup()
            fuerzas2=VGroup()
            scene_completa = VGroup()
            
            planet1=Dot(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW)
            planet2=Dot(radius=0.3,fill_opacity=1,stroke_width=0).set_color(GREEN)
            planet3=Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)
            path = TracedPath(planet2.get_center, stroke_color=RED, dissipating_time=0.5,stroke_opacity=[1, 0])

            self.add(planet1,planet2,planet3)
            # range (200, 320, 30) para lo normal
            for i in range(200,1300,1):
                # DO SOME CALCULATIONS
                scalingfactor=(8e+11)/4 #distance scaling factor for scene
                scalingfactorv=13720/1.5 #velocity vector scaling factor for scene
                scalingfactorf=np.amax(F1)/1.7 #force vector scaling factor for scene
                scalingfactorf3=np.amax(F3) #the third object varies a lot in force so it is not used
                pos1=np.array([R1[i][0]/scalingfactor,R1[i][1]/scalingfactor,0])
                pos2=np.array([R2[i][0]/scalingfactor,R2[i][1]/scalingfactor,0])
                pos3=np.array([R3[i][0]/scalingfactor,R3[i][1]/scalingfactor,0])
                v2=np.array([dR2[i][0]/scalingfactorv,dR2[i][1]/scalingfactorv,0])
                v3=np.array([dR3[i][0]/scalingfactorv,dR3[i][1]/scalingfactorv,0])
                Fm1=np.array([F1[i][0],F1[i][1],0])*1.5/np.linalg.norm(np.array([F1[i][0],F1[i][1],0]))
                Fm2=np.array([F2[i][0],F2[i][1],0])*1.5/np.linalg.norm(np.array([F2[i][0],F2[i][1],0]))
                Fm3=np.array([F3[i][0],F3[i][1],0])*1.5/np.linalg.norm(np.array([F3[i][0],F3[i][1],0]))
                """             MOBJECTS           """
                
                
                # CREATE ARROWS VGROUP
                # planetas
                #planetas2.add(planet2)
                # velocidades
                arrowplanet2=Arrow(pos2, pos2+v2, buff=0,color=GOLD)
                #velocidades2.add(arrowplanet2)
                # fuerzas
                planetpos2=Arrow(pos1,pos2,color=BLACK, buff=0)   
                Fuerza2=Arrow(pos2,pos2+Fm2, buff=0,color=RED)
                #fuerzas2.add(Fuerza2)
                # posiciones
                
                #posiciones2.add(planetpos2) 
                #scene_completa.add(velocidades2,fuerzas2,posiciones2,planet1,planet2,planet3)
                
                # MOVE PLANETS
                self.add(arrowplanet2,planetpos2,Fuerza2)
                self.play(
                    planet1.animate.move_to(pos1),
                    planet2.animate.move_to(pos2),
                    planet3.animate.move_to(pos3),
                    run_time=1/60
                )
                if i == 200:
                    self.add(path)
                self.remove(arrowplanet2,planetpos2,Fuerza2)

                

        threeDplanets()