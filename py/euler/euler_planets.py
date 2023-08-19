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

        def compute(
            # """ EARTH SUN ASTEROID"""
            # masa [kg]
            m1 = 1.989e30,
            m2 = 1.89819e28,
            m3 = 0.04784e24,
            # posicion inicial [m]
            r10 = [0, 0],
            r20 = [7.40522e11, 0],
            r30 = [-7.40522e11, 150000],
            # velocidad inicial [m/s]
            dr10 = [0, 0],
            dr20 = [0, 13720],
            dr30 = [-7252.9479, 10370],

            n= 1300*2,
            d=2,
            tf=1.3e+09*2,
            G=6.67e-11
            ):

            # """  Earth Sun Moon  """
            # # masa [kg]
            # m1 = 1.989e30 
            # m2 = 1.89819e28
            # m3 = 0.04784e24
            # # posicion inicial [m]
            # r10 = [0, 0, 0]
            # r20 = [7.40522e11, 0, 0]
            # r30 = [-5*384.4e7 + 7.405e11, 0, 0]
            # # velocidad inicial [m/s]
            # dr10 = [0, 0, 0]
            # dr20 = [0, 13720, 0]
            # dr30 = [0, np.sqrt(G*m2/np.linalg.norm(np.array(r20)-np.array(r30))) + 13720 , 0]
            
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

            # Pal rato pero de una
            planetas3 = VGroup()
            posiciones3 = VGroup()
            velocidades3 = VGroup()
            fuerzas3 = VGroup()

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

                scene_completa.add(velocidades2,fuerzas2,posiciones2,planet1,planet2)

                # Pal rato 
                planetas3.add(planet3)
                arrowplanet3=Arrow(pos3, pos3+v3, buff=0,color=GOLD)
                velocidades3.add(arrowplanet3)
                Fuerza3=Arrow(pos3,pos3+Fm3, buff=0,color=RED)
                fuerzas3.add(Fuerza3)
                planetpos3=Arrow(pos1,pos3,color=BLACK, buff=0)
                posiciones3.add(planetpos3)

                
                if i==200:
                    # LABEL ARROWS
                    
                    velocity = Tex(r"$\vec{v}$").set_color(BLACK).scale(0.8).next_to(arrowplanet2,LEFT)
                    force = Tex(r"$\vec{F}$").set_color(BLACK).scale(0.8).next_to(Fuerza2,UP)
                    distance = Tex(r"$\vec{p}$").set_color(BLACK).scale(0.8).next_to(planetpos2,DOWN)
                    distance.shift(UP*0.5)
                    # Se crean los planetas
                    self.play(Write(planet1),Create(planet2)) # Create(axesss)
                    # Se crea el vector y el label de fuerzas
                    self.play(Create(planetpos2),Write(distance),)
                    self.play(Create(Fuerza2),Write(force),)

                    self.play(Create(arrowplanet2),Write(velocity))
                    

                    grav_formula=MathTex(r"F=G\frac{m_{1}m_{2}}{r^{2}}").set_color(
                        BLACK).shift(UP*3+RIGHT)
                    


                    # Contador para la creacion de los siguiente vectores
                    c = 0
                    ogplanet = planet2.copy()
                    ogFuerza = Fuerza2.copy()
                    ogarrowplanet = arrowplanet2.copy()
                    ogplanetpos = planetpos2.copy()
                    self.add(ogplanet,ogFuerza,ogarrowplanet,ogplanetpos)

                    # Aqui se va a hacer la transformacion del planeta para demostrar que se puede calcular la fuerza desde cualquier posicion
                    mover_planeta = planet2.copy()
                    mover_fuerza = Fuerza2.copy()

                    mover_fuerza.add_updater(
                        lambda m: m.become(
                        # WTF ESTOY HACIENDO YA QUIERO ACABAR ESTO
                            # normalized mover_planeta.get_center() is
                            # mover_planeta.get_center() / np.linalg.norm(mover_planeta.get_center())
                            Arrow(
                        mover_planeta.get_center(),
                        
                        -1.5*mover_planeta.get_center() / np.linalg.norm(mover_planeta.get_center())
                          + mover_planeta.get_center()
                          
                          , buff=0,color=RED)
                        )
                    )
                    self.add(mover_fuerza,mover_planeta)
                    self.play(Write(grav_formula),mover_planeta.animate.shift(DOWN*4 + RIGHT*3), run_time=0.8)
                    self.play(mover_planeta.animate.shift(RIGHT*4+ UP*3), run_time=0.8)
                    self.play(mover_planeta.animate.shift(UP*2 + LEFT*6), run_time=0.8)
                    self.play(mover_planeta.animate.shift(DOWN + LEFT),Unwrite(grav_formula), run_time=0.8)
                    self.remove(mover_planeta,mover_fuerza)


                else:
                    # Se crean el resto de los vectores
                    # self.play(FadeIn(planet2),FadeIn(Fuerza2),FadeIn(arrowplanet2),FadeIn(planetpos2), run_time=0.2)


                    # Se va a transformar el vector planet2[c] a planet2[c+1], (tambien Fuerza2, arrowplanet2, planetpos2)
                    self.play(
                    Transform(planetas2[c], planetas2[c+1]),
                    Transform(velocidades2[c], velocidades2[c+1]),
                    Transform(fuerzas2[c], fuerzas2[c+1]),
                    Transform(posiciones2[c], posiciones2[c+1]),
                    run_time=0.2
                    )
                    #redundante por coso raro de manim
                    self.add(posiciones2[c])
                    c+=1            


            # Se mueve la camara hacia arriba para tener espacio
            self.play(self.camera.frame.animate.move_to(4*UP))

            # Separacion entre circulo de arriba y de abajo
            sep = 9.1


            
            """ DEMOSTRAR LOS CAMBIOS USANDO DOS VECTORES """

            MathTex.set_default(color= BLACK)
            # eqv = MathTex(r"\vec{v} = \frac{d\vec{r}}{dt}")
            # eqa = MathTex(r"\vec{a} = \frac{d\vec{v}}{dt}")
            # eqvdt = MathTex(r"v = \frac{d}{t}")
            # eqadt = MathTex(r"a = \frac{v}{t}")
 
            # EXPLICACION DE LAS ECUACIONES

            uni_v = MathTex(r"v=", r"\frac{m}{s}").scale(1.3)
            uni_a = MathTex(r"a=", r"\frac{m}{s^2}").scale(1.3)
            uni_a_s_s = MathTex(r"a=", r"\frac{\frac{m}{s}}{s}").scale(1.3)

            uni_v.shift(UP*8 + RIGHT*2)
            uni_a.shift(UP*6 + RIGHT*2)
            uni_a_s_s.shift(UP*6 + RIGHT*2)

            uni_pos_vel = MathTex(r"\vec{v}=", r"\frac{\vec{p}}{s}").move_to(uni_v.get_center())
            uni_vel_ac = MathTex(r"\vec{a}=", r"\frac{\vec{v}}{s}").move_to(uni_a.get_center())

            

            shift_direc = UP*(sep+3) + RIGHT*2

            self.play(
                distance.animate.shift(shift_direc),
                ogplanetpos.animate.shift(shift_direc),
                ogplanet.animate.shift(shift_direc),
            )

            self.play(
                velocity.animate.shift(shift_direc),
                ogarrowplanet.animate.shift(shift_direc),
                      )
            
            self.play(
                force.animate.shift(shift_direc),
                ogFuerza.animate.shift(shift_direc),
            )
            

            # Velocidad es cambio en posicion
            vec1_pos = posiciones2[0].copy()
            vec2_pos = posiciones2[1].copy()
            vec1_vel = velocidades2[0].copy()

            self.play(vec1_pos.animate.shift(UP*sep+RIGHT) , vec2_pos.animate.shift(UP*sep+RIGHT))
            self.play(vec1_vel.animate.shift(UP*sep+RIGHT))

            self.play(Wiggle(vec1_vel), Write(uni_v))
            self.play(ReplacementTransform(vec1_pos,vec2_pos))
            self.play(FadeOut(vec2_pos),FadeOut(vec1_vel))


            # Aceleracion es cambio en velocidad
            vec1_vel2 = velocidades2[0].copy()
            vec2_vel2 = velocidades2[1].copy()
            vec1_fuerza2 = fuerzas2[0].copy()


            self.play(vec1_fuerza2.animate.shift(UP*sep+RIGHT), Write(uni_a))
            self.play(vec1_vel2.animate.shift(UP*sep+RIGHT) , vec2_vel2.animate.shift(UP*sep+RIGHT))
            
            
            # Mover el vector vec1_vel2 y vec2_vel2 para que las bases se alineen
            pos = vec1_vel2.get_start()
            self.play(vec2_vel2.animate.shift(pos - vec2_vel2.get_start()), run_time=0.4)


            self.play(Wiggle(vec1_fuerza2))

            self.play(ReplacementTransform(vec1_vel2,vec2_vel2),ReplacementTransform(uni_a[0], uni_a_s_s[0]),
            ReplacementTransform(uni_a[1],uni_a_s_s[1]))

            self.play(FadeOut(vec2_vel2),FadeOut(vec1_fuerza2),
                      FadeOut(ogplanetpos), FadeOut(ogplanet),FadeOut(ogarrowplanet),FadeOut(ogFuerza),FadeOut(velocity),FadeOut(force),FadeOut(distance))
            

            uni_der_vel = MathTex(r"v=", r"\frac{p}{t}").move_to(uni_v.get_center()).scale(1.3)
            uni_der_acc = MathTex(r"a=", r"\frac{v}{t}").move_to(uni_a.get_center()).scale(1.3)
            
            self.wait()
            # Por lo que sabemos que la velocidad es la posicion entre el tiempo
            self.play(ReplacementTransform(uni_v[0],uni_der_vel[0]),
                      ReplacementTransform(uni_v[1],uni_der_vel[1]))
            self.play(ReplacementTransform(uni_a_s_s[0],uni_der_acc[0]),
                        ReplacementTransform(uni_a_s_s[1],uni_der_acc[1]))


            # Y la aceleracion es la velocidad entre el tiempo
            
            
            
            
            
            self.play(
                uni_der_acc.animate.shift(DOWN*2 + RIGHT*2),
                uni_der_vel.animate.shift(DOWN*2.5 + RIGHT*2),
                )



            """ PARTE DONDE SE PROPAGA EL DT """

            # Vamos a hacer copias para mover hacia arriba sin que desaparezca lo de abajo
            posiciones2_arriba = posiciones2.copy()
            distance_arriba = distance.copy()
            velocidades2_arriba = velocidades2.copy()
            velocity_arriba = velocity.copy()

            sep=8.3
            distance_arriba.shift(DOWN*9)
            velocity_arriba.shift(DOWN*12 + RIGHT*2)

            # Se cambian las posiciones y las velocidades hacia arriba
            self.play(posiciones2_arriba.animate.shift(UP*sep),) #distance_arriba.animate.shift(UP*sep))
            self.play(velocidades2_arriba.animate.shift(UP*sep),) #velocity_arriba.animate.shift(UP*sep))
            
            # Se mueven las posiciones en direccion de las velocidades
            for i in range(0,len(posiciones2_arriba)-1):
                if i == 0:
                    self.play(#FadeOut(distance_arriba),FadeOut(velocity_arriba),

                    ReplacementTransform(posiciones2_arriba[i],posiciones2_arriba[i+1]),
                    ReplacementTransform(velocidades2_arriba[i],velocidades2_arriba[i+1]),run_time = 0.25)
                else:
                    self.remove(posiciones2_arriba[i],velocidades2_arriba[i])
                    self.play(ReplacementTransform(posiciones2_arriba[i],posiciones2_arriba[i+1]),
                    ReplacementTransform(velocidades2_arriba[i],velocidades2_arriba[i+1]),run_time = 0.25)
            
            # Fade y wait
            self.play(FadeOut(posiciones2_arriba[len(posiciones2)-1]),FadeOut(velocidades2_arriba[len(velocidades2)-1]),run_time = 0.25)

            
            # Vamos a hacer copias para mover hacia arriba sin que desaparezca lo de abajo
            velocidades_seg_arriba=velocidades2.copy()
            fuerzas2_arriba = fuerzas2.copy()
            force_arriba = force.copy()
            velocity_label_2_arriba = velocity.copy()

            velocity_label_2_arriba.shift(DOWN*9)
            force_arriba.shift(DOWN*9)

            
            
            # Se cambian las velocidades y aceleraciones hacia arriba
            self.play(fuerzas2_arriba.animate.shift(UP*sep),velocidades_seg_arriba.animate.shift(UP*sep),)
            #force_arriba.animate.shift(UP*sep), velocity_label_2_arriba.animate.shift(UP*sep))

            # Se mueven las velocidades en direccion de la aceleracion
            for i in range(0,len(fuerzas2_arriba)-1):
                if i == 0:
                    # en el primer ciclo se desaparecen las labels
                    self.play(#FadeOut(force_arriba),FadeOut(velocity_label_2_arriba),
                        
                    ReplacementTransform(fuerzas2_arriba[i],fuerzas2_arriba[i+1]),
                    ReplacementTransform(velocidades_seg_arriba[i],velocidades_seg_arriba[i+1]), run_time = 0.25)
                else:
                    # en el resto de los ciclos se mueven los vectores
                    self.remove(fuerzas2_arriba[i], velocidades_seg_arriba[i])
                    self.play(ReplacementTransform(fuerzas2_arriba[i],fuerzas2_arriba[i+1]),
                    ReplacementTransform(velocidades_seg_arriba[i],velocidades_seg_arriba[i+1]), run_time = 0.25)
            
            # Fade y Wait
            self.play(FadeOut(fuerzas2_arriba[len(fuerzas2_arriba)-1]),FadeOut(velocidades_seg_arriba[len(velocidades_seg_arriba)-1]),run_time=0.25)

            self.play(
                uni_der_acc.animate.shift(DOWN*11 + LEFT*4),
                uni_der_vel.animate.shift(DOWN*11 + LEFT*4),
                self.camera.frame.animate.move_to(4*DOWN).scale(0.5))

            #Labels en tiempo P_i y P_f
            ecuaciones = VGroup()
            p_i = MathTex(r"\vec{p}_i").set_color(BLACK).scale(0.8).next_to(posiciones2[1],DOWN).shift(LEFT*0.7)
            p_f = MathTex(r"\vec{p}_f").set_color(BLACK).scale(0.8).next_to(posiciones2[2],DOWN).shift(RIGHT*0.2)

            self.play(Write(p_i),Write(p_f))
            self.play(Wiggle(velocidades2[1]), run_time = 1.5)
            self.play(Wiggle(posiciones2[1]),Wiggle(posiciones2[2]), run_time = 1.5)

            # Ecuacion con deltas
            ec_v = MathTex(r"\vec{v}=", r"\frac{\Delta \vec{p}}{\Delta t}").move_to(uni_der_vel.get_center()).scale(1.3)
            ev_v_d = MathTex(r"\vec{v}=", r"\frac{\vec{p}_{f}-\vec{p}_{i}}{\Delta t}").move_to(uni_der_vel.get_center()).scale(1.3)

            ec_v_despejada1 = MathTex(r"\vec{v}\cdot \Delta t =", r" \vec{p}_{f}-\vec{p}_{i}").move_to(uni_der_vel.get_center()).scale(1.3)
            ec_v_despejada2 = MathTex(r"\vec{v}\cdot \Delta t + \vec{p}_{i} =", r" \vec{p}_{f}").move_to(uni_der_vel.get_center()).scale(1.3)
            self.play(ReplacementTransform(uni_der_vel[0],ec_v[0]),
                        ReplacementTransform(uni_der_vel[1],ec_v[1]))
            self.wait()
            self.play(ReplacementTransform(ec_v[0],ev_v_d[0]),
                        ReplacementTransform(ec_v[1],ev_v_d[1]))

            # Labels en tiempo v_i y v_f
            v_i = MathTex(r"\vec{v}_i").set_color(BLACK).scale(0.8).move_to(p_i.get_center()).shift(RIGHT*0.8+DOWN*0.2)
            v_f = MathTex(r"\vec{v}_f").set_color(BLACK).scale(0.8).move_to(p_f.get_center()).shift(RIGHT*0.8+ UP*0.2)


            ec_a = MathTex(r"\vec{a}=", r"\frac{\Delta \vec{v}}{\Delta t}").move_to(uni_der_acc.get_center()).scale(1.3)
            ea_a_d = MathTex(r"\vec{a}=", r"\frac{\vec{v}_{f}-\vec{v}_{i}}{\Delta t}").move_to(uni_der_acc.get_center()).scale(1.3)

            ec_a_despejada1 = MathTex(r"\vec{a}\cdot \Delta t =", r" \vec{v}_{f}-\vec{v}_{i}").move_to(uni_der_acc.get_center()).scale(1.3)
            ec_a_despejada2 = MathTex(r"\vec{a}\cdot \Delta t + \vec{v}_{i} =", r" \vec{v}_{f}").move_to(uni_der_acc.get_center()).scale(1.3)
            

            self.wait(3)

            self.play(Write(v_i),Write(v_f))
            
            self.wait(1)
            
            self.play(ReplacementTransform(uni_der_acc[0],ec_a[0]),
                        ReplacementTransform(uni_der_acc[1],ec_a[1]))
            self.play(ReplacementTransform(ec_a[0],ea_a_d[0]),
                        ReplacementTransform(ec_a[1],ea_a_d[1]))
            
            # Como queremos saber los vectores finales
            pf_box = SurroundingRectangle(p_f, buff = 0.1)
            vf_box = SurroundingRectangle(v_f, buff = 0.1)
            pf_ec_box = SurroundingRectangle(ea_a_d[1], buff = 0)
            vf_ec_box = SurroundingRectangle(ev_v_d[1], buff = 0)

            self.play(Create(pf_box),Create(vf_box))
            self.play(Create(pf_ec_box),Create(vf_ec_box))


            self.wait(1)
            
            self.play(FadeOut(pf_box),FadeOut(vf_box),FadeOut(pf_ec_box),FadeOut(vf_ec_box))

            # Despejando la ecuacion 
            self.play(ReplacementTransform(ev_v_d[0],ec_v_despejada1[0]),
                        ReplacementTransform(ev_v_d[1],ec_v_despejada1[1]),
                        
                        ReplacementTransform(ea_a_d[0],ec_a_despejada1[0]),
                        ReplacementTransform(ea_a_d[1],ec_a_despejada1[1]), run_time = 0.6)
            
            self.play( ReplacementTransform(ec_v_despejada1[0],ec_v_despejada2[0]),
                        ReplacementTransform(ec_v_despejada1[1],ec_v_despejada2[1]),

                        ReplacementTransform(ec_a_despejada1[0],ec_a_despejada2[0]),
                        ReplacementTransform(ec_a_despejada1[1],ec_a_despejada2[1]), run_time = 0.6)

            # maroma xd
            ec_v_despejada_copia = MathTex(r"\vec{v}\cdot \Delta t + \vec{p}_{i}", r"=", r" \vec{p}_{f}").move_to(uni_der_vel.get_center()).scale(1.3)
            ec_a_despejada_copia = MathTex(r"\vec{a}\cdot \Delta t + \vec{v}_{i}", r"=", r" \vec{v}_{f}").move_to(uni_der_acc.get_center()).scale(1.3)

            ec_v_despejada_final = MathTex(r" \vec{p}_{f}" , r"=", r"\vec{v}\cdot \Delta t + \vec{p}_{i}").move_to(uni_der_vel.get_center()).scale(1.3)
            ec_a_despejada_final = MathTex(r" \vec{v}_{f}" , r"=", r"\vec{a}\cdot \Delta t + \vec{v}_{i}").move_to(uni_der_acc.get_center()).scale(1.3)
            

            self.play(FadeOut(ec_v_despejada2),FadeOut(ec_a_despejada2), run_time=0.01)
            

            # Maromeada
            self.play(ec_v_despejada_copia[0].animate.move_to(ec_v_despejada_final[2].get_center()),
                        ec_v_despejada_copia[1].animate.move_to(ec_v_despejada_final[1].get_center()),
                        ec_v_despejada_copia[2].animate.move_to(ec_v_despejada_final[0].get_center()),
                        
                        ec_a_despejada_copia[0].animate.move_to(ec_a_despejada_final[2].get_center()),
                        ec_a_despejada_copia[1].animate.move_to(ec_a_despejada_final[1].get_center()),
                        ec_a_despejada_copia[2].animate.move_to(ec_a_despejada_final[0].get_center()),
                        run_time = 0.8)
            
            # no funciona self.remove()
            ecuaciones.add(ec_v_despejada_copia, ec_a_despejada_copia,)
            self.play(FadeOut(ecuaciones), run_time = 0.001)
            self.add(ec_a_despejada_final,ec_v_despejada_final)
            

            grav_formula2=MathTex(r"F",r"=G\frac{m_{1}m_{2}}{r^{2}}"
                                  ).set_color(BLACK).move_to(ec_v_despejada1,UP*1.5)
            grav_formula2_ma=MathTex(r"m_1\vec{a}",r"=G\frac{m_{1}m_{2}}{r^{2}}"
                                  ).set_color(BLACK).move_to(ec_v_despejada1,UP*1.5)
            grav_formula2_ma[0].shift(LEFT*0.2)

            box_around_v=SurroundingRectangle(ec_v_despejada_final[2],buff=0.1).scale([0.3,1,1])
            v_i_box = SurroundingRectangle(v_i, buff = 0.1)
            p_i_box = SurroundingRectangle(p_i, buff = 0.1)
            box_around_v.shift(LEFT*1.1)


            self.wait()
            self.play(Write(box_around_v),Write(v_i_box))
            
            self.wait()

            self.play(Unwrite(v_i_box),box_around_v.animate.shift(RIGHT*0.9))
            self.wait()
            self.play(box_around_v.animate.shift(RIGHT*1.3), Write(p_i_box))
            self.wait()

            self.play(Unwrite(box_around_v),Unwrite(p_i_box))
            self.wait()

            self.play(ec_v_despejada_final.animate.shift(DOWN),
                      ec_a_despejada_final.animate.shift(DOWN*0.8)
                      , run_time=0.5)
            
            box_around_a=SurroundingRectangle(ec_a_despejada_final[2],buff=0.1).scale([0.3,1,1])
            box_around_a.shift(LEFT*1.1)

            
            self.play(Write(box_around_a),Write(grav_formula2))
            self.wait()
            self.play(ReplacementTransform(grav_formula2[0],grav_formula2_ma[0]),)
            self.wait(2)
            self.play(Unwrite(grav_formula2),box_around_a.animate.shift(RIGHT*0.9))

            self.play(box_around_a.animate.shift(RIGHT*1.3), Write(v_i_box))

            self.play(Unwrite(box_around_a),Unwrite(v_i_box))


            self.wait()


            example_listing = Code(
                "/home/jay/manimations/py/euler/example.py",
                tab_width=4,
                background="window",
                language="python",
                font="Monospace",
                background_stroke_color= WHITE,
            ).move_to(ec_v_despejada_final.get_center()+ UP*2).scale(0.5)

            self.play(Write(example_listing))

            



            self.wait()

            



            newscale = 2.5
            self.play(self.camera.frame.animate.scale(newscale),
                        example_listing.animate.shift(DOWN*3).scale(newscale),
                        ec_v_despejada_final.animate.shift(DOWN*4).scale(newscale),ec_a_despejada_final.animate.shift(4.5*DOWN).scale(newscale),)

            self.wait()

            pos_boxes = VGroup()
            vel_boxes = VGroup()


            # Code Block lines
            pos_boxes.add(SurroundingRectangle(example_listing[2][2],buff=0).shift(DOWN*0.1+LEFT*0.1))
            vel_boxes.add(SurroundingRectangle(example_listing[2][4],buff=0).shift(DOWN*0.1+LEFT*0.1))

            pos_boxes.add(SurroundingRectangle(ec_v_despejada_final,buff=0.2))
            vel_boxes.add(SurroundingRectangle(ec_a_despejada_final,buff=0.2))

            self.play(Create(pos_boxes))
            #self.play(Create(vel_boxes))

            #pos to vel
            self.play(ReplacementTransform(pos_boxes[0],vel_boxes[0]),
                        ReplacementTransform(pos_boxes[1],vel_boxes[1]))
            
            #vel to pos
            self.play(ReplacementTransform(vel_boxes[0],pos_boxes[0]),
                        ReplacementTransform(vel_boxes[1],pos_boxes[1]))
            
            

            self.play(FadeOut(fuerzas2),FadeOut(planetas2),FadeOut(posiciones2),FadeOut(velocidades2),
                      FadeOut(p_i),FadeOut(p_f),FadeOut(v_i),FadeOut(v_f),FadeOut(vel_boxes),FadeOut(pos_boxes),)


            # # Linea nuevacambiando todas las variables por algo similar P1,P2,P3, etc
            P1,P2,P3,dP1,dP2,dP3,f1,f2,f3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30 = compute(
            m1 = 1.989e30,
            m2 = 1.89819e28,
            m3 = 0.04784e24,
            r10 = [0, 0],
            r20 = [7.40522e11, 0],
            r30 = [-7.40522e11, 150000],
            dr10 = [0, 0],
            dr20 = [0, 13720],
            dr30 = [0, 10370],
            n=35,
            d=2,
            tf=1.3e+09,
            G=6.67e-11
            )

            scalingfactor=(8e+11)/4 #distance scaling factor for scene
            scalingfactorv=13720/2.4 #velocity vector scaling factor for scene
            scalingforce=4.66e+18 * 2 #force vector scaling factor for scene
            
            arrowplanets3 = VGroup()

            planet3 = Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)
            
            i=0
            pos3 = np.array([P3[i][0]/scalingfactor,P3[i][1]/scalingfactor,0])
            v3 = np.array([dP3[i][0]/scalingfactorv,dP3[i][1]/scalingfactorv,0])
            #Fm3 = np.array([f3[i][0]/scalingforce,f3[i][1]/scalingforce,0])
            Fm3 = np.array([f3[i][0],f3[i][1],0])*1.5/np.linalg.norm(np.array([f3[i][0],f3[i][1],0]))

            


            # Code Block lines again lol
            pos_boxes2 = VGroup()
            vel_boxes2 = VGroup()
            pos_boxes2.add(SurroundingRectangle(example_listing[2][2],buff=0).shift(DOWN*0.1+LEFT*0.1))
            vel_boxes2.add(SurroundingRectangle(example_listing[2][4],buff=0).shift(DOWN*0.1+LEFT*0.1))

            pos_boxes2.add(SurroundingRectangle(ec_v_despejada_final,buff=0.2))
            vel_boxes2.add(SurroundingRectangle(ec_a_despejada_final,buff=0.2))



            planet3.move_to(pos3)
            traced = TracedPath(planet3.get_center, stroke_color=GREY_C, stroke_width=1.5)
            self.add(traced)
            vel3 = Arrow(pos3, pos3+v3, buff=0,color=GOLD)
            arrowplanets3.add(vel3)
            self.play(Write(planet3),Create(vel3),Write(vel_boxes2))
            
            fuerzas3 = VGroup()

            dt = MathTex(r"\Delta t = 1.17 a\tilde{n}os").move_to(example_listing,UP*2+RIGHT)
            ciclos = MathTex("ciclos = 10").move_to(dt,DOWN)

            self.play(Write(dt),Write(ciclos))

            

            for i in range(1,10):
                pos3 = np.array([P3[i][0]/scalingfactor,P3[i][1]/scalingfactor,0])
                v3i_1 = v3
                v3 = np.array([dP3[i][0]/scalingfactorv,dP3[i][1]/scalingfactorv,0])
                Fm3 = np.array([f3[i][0]/scalingforce,f3[i][1]/scalingforce,0])
                vel3 = Arrow(pos3, pos3+v3, buff=0.1,color=GOLD)
                Fuerza3 = Arrow(pos3,pos3+Fm3, buff=0,color=RED)
                arrowplanets3.add(vel3)
                fuerzas3.add(Fuerza3)
            
                tempvel = vel_boxes2.copy()
                temppos = pos_boxes2.copy()
                
                if i == 1:
                    self.play(arrowplanets3[i-1].animate.move_to(pos3 + (v3i_1)/2),
                        planet3.animate.move_to(pos3),
                            ReplacementTransform(vel_boxes2[0],pos_boxes2[0]),
                            ReplacementTransform(vel_boxes2[1],pos_boxes2[1]),
                            run_time=0.5)
                else:
                    self.play(arrowplanets3[i-1].animate.move_to(pos3 + (v3i_1)/2),
                        FadeOut(fuerzas3[i-2]),
                        planet3.animate.move_to(pos3),
                            ReplacementTransform(vel_boxes2[0],pos_boxes2[0]),
                            ReplacementTransform(vel_boxes2[1],pos_boxes2[1]),
                            run_time=0.5)
                
                vel_boxes2 = tempvel.copy()
                
                
                self.play(Write(Fuerza3),
                            ReplacementTransform(arrowplanets3[i-1],arrowplanets3[i]),
                            ReplacementTransform(pos_boxes2[0],vel_boxes2[0]),
                            ReplacementTransform(pos_boxes2[1],vel_boxes2[1]),
                            run_time=0.5)
                
                
                
                pos_boxes2 = temppos.copy()

            self.play(FadeOut(vel3),FadeOut(Fuerza3),Unwrite(dt),Unwrite(ciclos))
                

            # dt intermedio 

            

            P1,P2,P3,dP1,dP2,dP3,f1,f2,f3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30 = compute(
            m1 = 1.989e30,
            m2 = 1.89819e28,
            m3 = 0.04784e24,
            r10 = [0, 0],
            r20 = [7.40522e11, 0],
            r30 = [-7.40522e11, 150000],
            dr10 = [0, 0],
            dr20 = [0, 13720],
            dr30 = [0, 10370],
            n=35,
            d=2,
            tf=1.3e+09,
            G=6.67e-11
            )


            dt = MathTex(r"\Delta t = 0.117 a\tilde{n}os").move_to(example_listing,UP*2+RIGHT)
            ciclos = MathTex(r"ciclos = 100").move_to(dt,DOWN)


            scalingfactor=(8e+11)/4 #distance scaling factor for scene
            scalingfactorv=13720/2.4 #velocity vector scaling factor for scene

            planet3 = Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)
            pos3 = np.array([P3[0][0]/scalingfactor,P3[0][1]/scalingfactor,0])
            planet3.move_to(pos3)
            self.play(Write(planet3))
            traced = TracedPath(planet3.get_center, stroke_color=GREY_C, stroke_width=1.5)
            self.add(traced)

            planet3.locations = P3/scalingfactor
            planet3.t_offset = 0

            def planet_updater(mob, dt):
                mob.t_offset += 1  #dt*30
                pos2d = mob.locations[mob.t_offset%len(mob.locations)]
                #make it 3d with z = 0
                pos = np.array([pos2d[0],pos2d[1],0])
                mob.move_to(pos)
                
            planet3.add_updater(planet_updater)
            self.add(planet3)



            self.wait(3)

            # for i in range(1,10):
            #     pos3 = np.array([P3[i][0]/scalingfactor,P3[i][1]/scalingfactor,0])
            #     v3i_1 = v3
            #     v3 = np.array([dP3[i][0]/scalingfactorv,dP3[i][1]/scalingfactorv,0])
            #     Fm3 = np.array([f3[i][0]/scalingforce,f3[i][1]/scalingforce,0])
            #     vel3 = Arrow(pos3, pos3+v3, buff=0.1,color=GOLD)
            #     Fuerza3 = Arrow(pos3,pos3+Fm3, buff=0,color=RED)
            #     arrowplanets3.add(vel3)
            #     fuerzas3.add(Fuerza3)
            
            #     tempvel = vel_boxes2.copy()
            #     temppos = pos_boxes2.copy()
                
            #     if i == 1:
            #         self.play(arrowplanets3[i-1].animate.move_to(pos3 + (v3i_1)/2),
            #             planet3.animate.move_to(pos3),
            #                 ReplacementTransform(vel_boxes2[0],pos_boxes2[0]),
            #                 ReplacementTransform(vel_boxes2[1],pos_boxes2[1]),
            #                 run_time=0.5)
            #     else:
            #         self.play(arrowplanets3[i-1].animate.move_to(pos3 + (v3i_1)/2),
            #             FadeOut(fuerzas3[i-2]),
            #             planet3.animate.move_to(pos3),
            #                 ReplacementTransform(vel_boxes2[0],pos_boxes2[0]),
            #                 ReplacementTransform(vel_boxes2[1],pos_boxes2[1]),
            #                 run_time=0.5)
                
            #     vel_boxes2 = tempvel.copy()
                
                
            #     self.play(Write(Fuerza3),
            #                 ReplacementTransform(arrowplanets3[i-1],arrowplanets3[i]),
            #                 ReplacementTransform(pos_boxes2[0],vel_boxes2[0]),
            #                 ReplacementTransform(pos_boxes2[1],vel_boxes2[1]),
            #                 run_time=0.5)
                
                
                
            #     pos_boxes2 = temppos.copy()











            # Segundo con un dt mas pequeño

            # # Linea nuevacambiando todas las variables por algo similar P1,P2,P3, etc
            P1,P2,P3,dP1,dP2,dP3,f1,f2,f3,n,dt,t,G,m1,m2,m3,r10,r20,r30,dr10,dr20,dr30 = compute(
            m1 = 1.989e30,
            m2 = 1.89819e28,
            m3 = 0.04784e24,
            r10 = [0, 0],
            r20 = [7.40522e11, 0],
            r30 = [-7.40522e11, 150000],
            dr10 = [0, 0],
            dr20 = [0, 13720],
            dr30 = [0, 10370],
            n=350,
            d=2,
            tf=1.3e+09,
            G=6.67e-11
            )

            scalingfactor=(8e+11)/4 #distance scaling factor for scene
            scalingfactorv=13720/2.4 #velocity vector scaling factor for scene
            
            planet3 = Dot(radius=0.15,fill_opacity=1,stroke_width=0).set_color(GREY_C)
            pos3 = np.array([P3[0][0]/scalingfactor,P3[0][1]/scalingfactor,0])
            planet3.move_to(pos3)
            self.play(Write(planet3))
            traced = TracedPath(planet3.get_center, stroke_color=GREY_C, stroke_width=1.5)
            self.add(traced)


            planet3.locations = P3/scalingfactor
            planet3.t_offset = 0

            def planet_updater(mob, dt):
                mob.t_offset += 1  #dt*30
                pos2d = mob.locations[mob.t_offset]
                #make it 3d with z = 0
                pos = np.array([pos2d[0],pos2d[1],0])
                mob.move_to(pos)
                
            planet3.add_updater(planet_updater)
            self.add(planet3)



            self.wait(3)









        #animacion_frames()
        animacion_vectores()
        
        
