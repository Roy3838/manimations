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

            return R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30
        
        R1,R2,R3,dR1,dR2,dR3,F1,F2,F3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30 = compute()

        def animacion_frames():
            # Graficar
            planet1=Dot(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW)
            planet2=Dot(radius=0.3,fill_opacity=1,stroke_width=0).set_color(GREEN)
            planet3=Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)

            scalingfactor=(8e+11)/4 #distance scaling factor for scene
            scalingfactorv=13720/1.5 #velocity vector scaling factor for scene
            scalingfactorf=np.amax(F1)/1.7 #force vector scaling factor for scene
            scalingfactorf3=np.amax(F3) #the third object varies a lot in force so it is not used

            for i in range(0,int(n/2),2):
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

                #Fuerza1=Arrow(pos1,pos1+Fm1, buff=0,color=GOLD)
                Fuerza2=Arrow(pos2,pos2+Fm2, buff=0,color=GOLD)
                Fuerza3=Arrow(pos3,pos3+Fm3, buff=0,color=GOLD)
                self.add(arrowplanet2,arrowplanet3,Fuerza2,Fuerza3)
                self.add(planet1,planet2,planet3)
                self.wait(1/60)
                self.remove(planet1,planet2,planet3,arrowplanet2,arrowplanet3,Fuerza2,Fuerza3)
            
            #self.add(Text("hi"))
            print(str(time.time()-start) + " seconds")
        
        def animacion_vectores():

            axesss = NumberPlane().set_color(GREY_C).scale(1.5).rotate(PI/2)
            planet1=Dot(radius=0.8,fill_opacity=1,stroke_width=0).set_color(YELLOW)
            planetas2=VGroup()
            posiciones2=VGroup()
            velocidades2=VGroup()
            fuerzas2=VGroup()
            scene_completa = VGroup()

            # range (200, 320, 30) para lo normal
            for i in range(200,550,30):
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
                # MOVE PLANETS
                planet2=Dot(radius=0.3,fill_opacity=1,stroke_width=0).set_color(GREEN)
                planet3=Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)
                planet1.move_to(pos1)
                planet2.move_to(pos2)
                planet3.move_to(pos3)
                
                # CREATE ARROWS VGROUP
                # planetas
                planetas2.add(planet2)
                # velocidades
                arrowplanet2=Arrow(pos2, pos2+v2, buff=0,color=GOLD)
                velocidades2.add(arrowplanet2)
                # fuerzas
                Fuerza2=Arrow(pos2,pos2+Fm2, buff=0,color=RED)
                fuerzas2.add(Fuerza2)
                # posiciones
                planetpos2=Arrow(pos1,pos2,color=BLACK, buff=0)   
                posiciones2.add(planetpos2) 

                scene_completa.add(velocidades2,fuerzas2,posiciones2,planet1,planet2,planet3)

                
                if i==200:
                    # LABEL ARROWS
                    velocity = Tex(r"$\vec{v}$").set_color(BLACK).scale(0.8).next_to(arrowplanet2,LEFT)
                    force = Tex(r"$\vec{F}$").set_color(BLACK).scale(0.8).next_to(Fuerza2,UP)
                    distance = Tex(r"$\vec{p}$").set_color(BLACK).scale(0.8).next_to(planetpos2,DOWN)
                    distance.shift(UP*0.5)
                    # Se crean los planetas
                    self.play(Write(planet1),Create(planet2)) # Create(axesss)
                    # Se crea el vector y el label de fuerza
                    self.play(Create(Fuerza2),Write(force),Create(planetpos2),Write(distance),
                              Create(arrowplanet2),Write(velocity))


                    # Contador para la creacion de los siguiente vectores
                    c = 0
                    ogplanet = planet2.copy()
                    ogFuerza = Fuerza2.copy()
                    ogarrowplanet = arrowplanet2.copy()
                    ogplanetpos = planetpos2.copy()
                    self.add(ogplanet,ogFuerza,ogarrowplanet,ogplanetpos)
                else:
                    # Se crean el resto de los vectores
                    # self.play(FadeIn(planet2),FadeIn(Fuerza2),FadeIn(arrowplanet2),FadeIn(planetpos2), run_time=0.2)


                    # Se va a transformar el vector planet2[c] a planet2[c+1], (tambien Fuerza2, arrowplanet2, planetpos2)
                    self.play(
                    Transform(planetas2[c], planetas2[c+1]),
                    Transform(velocidades2[c], velocidades2[c+1]),
                    Transform(fuerzas2[c], fuerzas2[c+1]),
                    Transform(posiciones2[c], posiciones2[c+1]),
                    run_time=0.4
                    )
                    c+=1



            # Se mueve la camara hacia arriba para tener espacio
            self.play(self.camera.frame.animate.move_to(5*UP))

            # Separacion entre circulo de arriba y de abajo
            sep = 9


            
            """ DEMOSTRAR LOS CAMBIOS USANDO DOS VECTORES """

            # Velocidad es cambio en posicion
            vec1_pos = posiciones2[0].copy()
            vec2_pos = posiciones2[1].copy()
            vec1_vel = velocidades2[0].copy()

            self.play(vec1_pos.animate.shift(UP*sep+RIGHT*2) , vec2_pos.animate.shift(UP*sep+RIGHT*2))
            self.play(vec1_vel.animate.shift(UP*sep+RIGHT*2))

            self.play(Wiggle(vec1_vel))
            self.play(ReplacementTransform(vec1_pos,vec2_pos))
            self.play(FadeOut(vec2_pos),FadeOut(vec1_vel))

            # Aceleracion es cambio en velocidad
            vec1_vel2 = velocidades2[0].copy()
            vec2_vel2 = velocidades2[1].copy()
            vec1_fuerza2 = fuerzas2[0].copy()

            self.play(vec1_vel2.animate.shift(UP*sep+RIGHT*2) , vec2_vel2.animate.shift(UP*sep+RIGHT*2))
            self.play(vec1_fuerza2.animate.shift(UP*sep+RIGHT*2))
            
            # Mover el vector vec1_vel2 y vec2_vel2 para que las bases se alineen
            pos = vec1_vel2.get_start()
            self.play(vec2_vel2.animate.shift(pos - vec2_vel2.get_start()))

            self.play(Wiggle(vec1_fuerza2))
            self.play(ReplacementTransform(vec1_vel2,vec2_vel2))
            self.play(FadeOut(vec2_vel2),FadeOut(vec1_fuerza2))

            MathTex.set_default(color= BLACK)
            # eqv = MathTex(r"\vec{v} = \frac{d\vec{r}}{dt}")
            # eqa = MathTex(r"\vec{a} = \frac{d\vec{v}}{dt}")
            # eqvdt = MathTex(r"v = \frac{d}{t}")
            # eqadt = MathTex(r"a = \frac{v}{t}")

            # EXPLICACION DE LAS ECUACIONES

            uni_v = MathTex(r"\vec{v}=\frac{m}{s}")
            uni_a = MathTex(r"\vec{a}=", r"\frac{m}{s^2}")
            uni_a_s_s = MathTex(r"\vec{a}=", r"\frac{\frac{m}{s}}{s}")

            uni_v.shift(UP*9 + RIGHT*3)
            uni_a.shift(UP*7 + RIGHT*3)
            uni_a_s_s.shift(UP*7 + RIGHT*3)

            uni_pos_vel = MathTex(r"\vec{v} = \frac{\vec{p}}{s}").move_to(uni_v.get_center())
            uni_vel_ac = MathTex(r"\vec{a} = \frac{\vec{v}}{s}").move_to(uni_a.get_center())

            uni_der_vel = MathTex(r"\vec{v} = \frac{d\vec{p}}{dt}").move_to(uni_v.get_center())
            uni_der_acc = MathTex(r"\vec{a} = \frac{d\vec{v}}{dt}").move_to(uni_a.get_center())


            oggroup = VGroup(ogplanet,ogFuerza,ogarrowplanet,ogplanetpos)
            self.play(oggroup.animate.shift(UP*sep + RIGHT*2),
            self.camera.frame.animate.scale(0.8).move_to(UP*sep + RIGHT))

            """ Seccion de ecuaciones, probablemente se tiene que incluir con las de arriba """
            self.wait()
            self.play(Write(uni_v), Wiggle(ogarrowplanet))
            self.wait()
            self.play(Write(uni_a), Wiggle(ogFuerza))
            self.wait()
            self.play(ReplacementTransform(uni_a[0], uni_a_s_s[0]),
            ReplacementTransform(uni_a[1],uni_a_s_s[1]))
            self.wait()
            self.play(ReplacementTransform(uni_a_s_s,uni_vel_ac),
            ReplacementTransform(uni_v,uni_pos_vel))
            self.wait()
            self.play(ReplacementTransform(uni_vel_ac,uni_der_acc),
            ReplacementTransform(uni_pos_vel, uni_der_vel))




            self.play(FadeOut(uni_a_s_s),FadeOut(uni_v),FadeOut(oggroup))



            """ PARTE DONDE SE PROPAGA EL DT """

            # Vamos a hacer copias para mover hacia arriba sin que desaparezca lo de abajo
            posiciones2_arriba = posiciones2.copy()
            distance_arriba = distance.copy()
            velocidades2_arriba = velocidades2.copy()
            velocity_arriba = velocity.copy()

            # Se cambian las posiciones y las velocidades hacia arriba
            self.play(posiciones2_arriba.animate.shift(UP*sep), distance_arriba.animate.shift(UP*sep))
            self.play(velocidades2_arriba.animate.shift(UP*sep), velocity_arriba.animate.shift(UP*sep))
            
            # Se mueven las posiciones en direccion de las velocidades
            for i in range(0,len(posiciones2_arriba)-1):
                if i == 0:
                    self.play(FadeOut(distance_arriba),FadeOut(velocity_arriba),

                    ReplacementTransform(posiciones2_arriba[i],posiciones2_arriba[i+1]),
                    ReplacementTransform(velocidades2_arriba[i],velocidades2_arriba[i+1]),run_time = 0.4)
                else:
                    self.remove(posiciones2_arriba[i],velocidades2_arriba[i])
                    self.play(ReplacementTransform(posiciones2_arriba[i],posiciones2_arriba[i+1]),
                    ReplacementTransform(velocidades2_arriba[i],velocidades2_arriba[i+1]),run_time = 0.4)
            
            # Fade y wait
            self.play(FadeOut(posiciones2_arriba[len(posiciones2)-1]),FadeOut(velocidades2_arriba[len(velocidades2)-1]),)

            
            # Vamos a hacer copias para mover hacia arriba sin que desaparezca lo de abajo
            velocidades_seg_arriba=velocidades2.copy()
            fuerzas2_arriba = fuerzas2.copy()
            force_arriba = force.copy()
            velocity_label_2_arriba = velocity.copy()
            
            # Se cambian las velocidades y aceleraciones hacia arriba
            self.play(fuerzas2_arriba.animate.shift(UP*sep),velocidades_seg_arriba.animate.shift(UP*sep),
            force_arriba.animate.shift(UP*sep), velocity_label_2_arriba.animate.shift(UP*sep))

            # Se mueven las velocidades en direccion de la aceleracion
            for i in range(0,len(fuerzas2_arriba)-1):
                if i == 0:
                    # en el primer ciclo se desaparecen las labels
                    self.play(FadeOut(force_arriba),FadeOut(velocity_label_2_arriba),
                        
                    ReplacementTransform(fuerzas2_arriba[i],fuerzas2_arriba[i+1]),
                    ReplacementTransform(velocidades_seg_arriba[i],velocidades_seg_arriba[i+1]), run_time = 0.4)
                else:
                    # en el resto de los ciclos se mueven los vectores
                    self.remove(fuerzas2_arriba[i], velocidades_seg_arriba[i])
                    self.play(ReplacementTransform(fuerzas2_arriba[i],fuerzas2_arriba[i+1]),
                    ReplacementTransform(velocidades_seg_arriba[i],velocidades_seg_arriba[i+1]), run_time = 0.4)
            
            # Fade y Wait
            self.play(FadeOut(fuerzas2_arriba[len(fuerzas2_arriba)-1]),FadeOut(velocidades_seg_arriba[len(velocidades_seg_arriba)-1]),)
        
        #animacion_frames()
        animacion_vectores()
        
        
