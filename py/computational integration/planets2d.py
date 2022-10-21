from manim import *
import numpy as np
import time
#from ticktock import tick
start=time.time()
width=1080
height=1920
config.frame_size = [width, height]

class Euler(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.camera.frame.scale(1)     

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
        r10 = [0, 0]
        r20 = [7.40522e11, 0]
        r30 = [-7.40522e11, 150000]
        # velocidad inicial [m/s]
        dr10 = [0, 0]
        dr20 = [0, 13720]
        dr30 = [-7252.9479, 10370]

        n= 1300*2
        d=2
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
        def animacion_frames():
            # Graficar
            planet1=Dot(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW)
            planet2=Dot(radius=0.3,fill_opacity=1,stroke_width=0).set_color(GREEN)
            planet3=Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)

            scalingfactor=(8e+11)/4 #distance scaling factor for scene
            scalingfactorv=13720/1.5 #velocity vector scaling factor for scene
            scalingfactorf=np.amax(F1)/1.7 #force vector scaling factor for scene
            scalingfactorf3=np.amax(F3) #the third object varies a lot in force so it is not used

            for i in range(0,n,2):
                print(str(round((i*100/n),2)) + "%")
                pos1=np.array([R1[i][0]/scalingfactor,R1[i][1]/scalingfactor,0])
                pos2=np.array([R2[i][0]/scalingfactor,R2[i][1]/scalingfactor,0])
                pos3=np.array([R3[i][0]/scalingfactor,R3[i][1]/scalingfactor,0])

                planet1.move_to(pos1)
                planet2.move_to(pos2)
                planet3.move_to(pos3)
                #print(dR3[i][:]/scalingfactorv)
                v2=np.array([dR2[i][0]/scalingfactorv,dR2[i][1]/scalingfactorv,0])
                v3=np.array([dR3[i][0]/scalingfactorv,dR3[i][1]/scalingfactorv,0])
                #print(pos2+v2)
                Fm1=np.array([F1[i][0],F1[i][1],0])*1.5/np.linalg.norm(np.array([F1[i][0],F1[i][1],0]))
                Fm2=np.array([F2[i][0],F2[i][1],0])*1.5/np.linalg.norm(np.array([F2[i][0],F2[i][1],0]))
                Fm3=np.array([F3[i][0],F3[i][1],0])*1.5/np.linalg.norm(np.array([F3[i][0],F3[i][1],0]))
                #print(Fm3)

                arrowplanet2=Arrow(pos2, pos2+v2, buff=0,color=GREY_C)
                arrowplanet3=Arrow(pos3, pos3+v3, buff=0,color=GREY_C)

                Fuerza1=Arrow(pos1,pos1+Fm1, buff=0,color=GOLD)
                Fuerza2=Arrow(pos2,pos2+Fm2, buff=0,color=GOLD)
                Fuerza3=Arrow(pos3,pos3+Fm3, buff=0,color=GOLD)
                self.add(arrowplanet2,arrowplanet3,Fuerza1,Fuerza2,Fuerza3)
                self.add(planet1,planet2,planet3)
                self.wait(1/60)
                self.remove(planet1,planet2,planet3,arrowplanet2,arrowplanet3,Fuerza1,Fuerza2,Fuerza3)
            
            #self.add(Text("hi"))
            print(str(time.time()-start) + " seconds")
        
        def animacion_vectores():
            planet1=Dot(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW)
            planet2=Dot(radius=0.3,fill_opacity=1,stroke_width=0).set_color(GREEN)
            planet3=Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)
            for i in range(0,n,20):
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


                planet1.move_to(pos1)
                planet2.move_to(pos2)
                planet3.move_to(pos3)
                arrowplanet2=Arrow(pos2, pos2+v2, buff=0,color=GOLD)
                arrowplanet3=Arrow(pos3, pos3+v3, buff=0,color=GOLD)

                Fuerza1=Arrow(pos1,pos1+Fm1, buff=0,color=RED)
                Fuerza2=Arrow(pos2,pos2+Fm2, buff=0,color=RED)
                Fuerza3=Arrow(pos3,pos3+Fm3, buff=0,color=RED)

                planetpos1=Arrow(ORIGIN,pos1,color=BLACK)
                planetpos3=Arrow(ORIGIN,pos3,color=BLACK)
                planetpos2=Arrow(ORIGIN,pos2,color=BLACK)

                

                if i==200 or i ==220:
                    
                    self.wait()
                    self.play(Create(planet1),Create(planet2),Create(planet3))
                    self.play(Create(planetpos1),Create(planetpos2),Create(planetpos3))
                    self.wait()
                    self.play(Create(Fuerza2),Create(Fuerza3))
                    self.wait()
                    self.play(Create(arrowplanet2),Create(arrowplanet3))
                    self.wait()

                    self.play(Uncreate(Fuerza1),Uncreate(Fuerza2),Uncreate(Fuerza3),
                    Uncreate(planetpos1),Uncreate(planetpos2),Uncreate(planetpos3),
                    Uncreate(arrowplanet2),Uncreate(arrowplanet3))


                    


                
        
        
        #animacion_frames()
        animacion_vectores()

        
