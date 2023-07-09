from manim import *
import numpy as np
import random as rd
import matplotlib.pyplot as plt




class recodico(ThreeDScene):
    def construct(self):


        # se va a hacer una optimizacion con el metodo de recocido simulado
        # background color
        self.camera.background_color = "#E2E2E2"
        # se define la funcion a optimizar
        def f(x,y):
            return x**2 + y**2 + 25*(np.sin(x)**2 + np.sin(y)**2)

        def param_surface(u, v):
            x = u
            y = v
            z = x**2 + y**2 + 25*(np.sin(x)**2 + np.sin(y)**2)
            return z

        # se define el dominio de la funcion
        x = np.linspace(-5,5,10)
        y = np.linspace(-5,5,10)
        X,Y = np.meshgrid(x,y)

        # funcion analitica
        Z = f(X,Y)
        axes = ThreeDAxes(x_range=(-5, 5, 1), y_range=(-5, 5, 1), z_range=(0, 100, 0.5)).set_color(BLACK)
        # se grafica la funcion analitica
        resolution_fa = 8

        surface = Surface(lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[-5, 5],
            u_range=[-5, 5],
            checkerboard_colors=[BLUE_D, BLUE_E],
            )



        """ COMPUTING THE OPTIMIZATION PATH """
        x_0=rd.uniform(-5,5)
        y_0=rd.uniform(-5,5)

        p_0=np.array([x_0,y_0])
        T_0=300
        T_0_i=T_0
        L=500
        delta_uniforme=0.2
        p_1=p_0
        print(T_0)

        x=np.linspace(-5,5,100)
        y=np.linspace(-5,5,100)
        X,Y=np.meshgrid(x,y)
        Z=f(X,Y)

        plt.contour(X,Y,Z,100)
        ciclos=0
        contador_boltzmann=0
        contador_zi_cuajo=0


        while (T_0>0.01):
            T_0=T_0*0.99
            #print(p_1)
            # make color change according to temperature BLUE->RED
            color=(1-T_0/T_0_i,0,T_0/T_0_i)
            plt.plot(p_0[0],p_0[1],'ro',color=color)
            for i in range(L):
                ciclos+=1
                p_1=[rd.uniform(-0.1,0.1)+p_0[0],rd.uniform(-0.1,0.1)+p_0[1]]
                if (f(p_1[0],p_1[1])<f(p_0[0],p_0[1])):
                    contador_zi_cuajo+=1
                    p_0=p_1
                # if not Boltzmann Gibbz
                else:
                    if (rd.uniform(0,1)<np.exp(-f(p_1[0],p_1[1])/T_0)):
                        contador_boltzmann+=1
                        p_0=p_1
        





        """ ANIMATION SPACE """
        # se hacen los ejes
        self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)

        self.play(Write(surface))
        # rotate camera
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.wait(5)
        # self.stop_ambient_camera_rotation()

        self.wait(1)