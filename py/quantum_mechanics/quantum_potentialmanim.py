import numpy as np
from scipy import integrate
from scipy import sparse
from manim import *
import time

class quantum(MovingCameraScene):
        def construct(self):
            time1=time.time()
            self.camera.background_color = "#E2E2E2"
            magnitud=1650
            squish=5
            def force(x):
                gradiente= 0.001*(np.exp(-2.5 * (x - 5)**2) * 
                ((206250 * x**3 - 3093750 * x**2 + 1.5477*10**7 * x - 25822500) * 
                np.arctan(25 - 5 * x) + 8250))/(25 * x**2 - 250 * x + 626)
                val = gradiente*(-9.81)
                return val
            def pot(x):
                return magnitud*np.arctan(squish*x-squish*5)*(np.exp(-0.1*(squish*x-squish*5)**2)) + 300
            def derivative(x):
                gradiente= 0.001*(np.exp(-2.5 * (x - 5)**2) * 
                ((206250 * x**3 - 3093750 * x**2 + 1.5477*10**7 * x - 25822500) * 
                np.arctan(25 - 5 * x) + 8250))/(25 * x**2 - 250 * x + 626)
                vector= np.array([1,gradiente*1.7,0])
                vector_norm= vector/np.linalg.norm(vector)
                return vector_norm
            def norm(x):
                gradiente= 0.001*(np.exp(-2.5 * (x - 5)**2) * 
                ((206250 * x**3 - 3093750 * x**2 + 1.5477*10**7 * x - 25822500) * 
                np.arctan(25 - 5 * x) + 8250))/(25 * x**2 - 250 * x + 626)
                gradiente = -gradiente
                #vect= np.array([gradiente, 1,0])
                #norma = np.linalg.norm(vect)
                vector= np.array([gradiente*1.7, 1, 0])
                vector_norm = vector/np.linalg.norm(vector)
                return vector_norm
            def animate_ball(x_0,v_0,
                            particulas, 
                            U_x, F,
                            dx=0.005, 
                            t_max=3, 
                            size=0.1,
                            color=RED,
                            colorarrow=RED,
                            rnd_v=True,
                            rnd_x=True):
                E=0.7

                #v = lambda x :np.sqrt((E-U(x))*2*m) + v_0

                # Reference Ball
                ball = Dot().move_to([x_0,U_x(x_0),0])
                ball.set_color(color)
                

                # Make velocity and position vectors
                v = [np.arange(0, t_max, dx) for i in range(particulas)]
                x = [np.arange(0, t_max, dx) for i in range(particulas)]

                # Randomize v_0 or not
                if rnd_v:
                    for vs in range (particulas):
                        v[vs][0] = v_0 + np.random.normal(0,0.5)
                else:
                    for vs in range (particulas):
                        v[vs][0] = v_0

                # Randomize x_0 or not
                if rnd_x:
                    for xs in range(particulas):
                        x[xs][0] = x_0 + np.random.normal(0,0.05)
                else:
                    for xs in range(particulas):
                        x[xs][0] = x_0
                
                # Compute the position and velocity of the particles every t as j
                for j in range(len(x[0])-1):
                    balls=VGroup()
                    balls1d=VGroup()
                    NormalVectors=VGroup()
                    SpeedVectors=VGroup()
                    for i in range(len(x)):
                        # Euler integration
                        v[i][j+1] = v[i][j] + F(x[i][j])*dx
                        x[i][j+1] = x[i][j] + v[i][j]*dx
                        # Position and Velocity Vectors
                        nor_v=norm(x[i][j+1])
                        contact_vector=norm(x[i][j+1])*0.12
                        speedabs= v[i][j+1]/2
                        speedvector=speedabs*( derivative(x[i][j+1]))
                        ball_pos=axes.c2p(x[i][j+1],U_x(x[i][j+1])) + contact_vector

                        if U_x(x[i][j+1]) > 0.7:
                            # If Balls are in the prohibited region, they have less fill opacity
                            balls.add(Dot(fill_opacity=0.2).move_to(ball_pos)).set_color(color)
                            balls1d.add(Dot(fill_opacity=0.2).move_to(axes.c2p(x[i][j+1],1.25)).set_color(color))
                        else:
                            # Make Mobjects
                            balls.add(ball.copy().move_to(ball_pos))
                            balls1d.add(Dot().move_to(axes.c2p(x[i][j+1],1.25)).set_color(color))
                            NormalVectors.add(Arrow(ball_pos ,nor_v + ball_pos , buff=0.1)).set_color(colorarrow)
                            SpeedVectors.add(Arrow( ball_pos , speedvector + ball_pos , buff=0.1).set_color(colorarrow))
                    
                    self.add(balls,balls1d,NormalVectors,SpeedVectors)
                    self.wait(1/60)
                    self.remove(balls,balls1d,NormalVectors,SpeedVectors)


            def compute_schrodingers():
                dx = 0.005                  # spatial separation
                x = np.arange(0, 10, dx)    # spatial grid points
                kx = 50                     # wave number
                m = 1                       # mass
                sigma = 0.5                 # width of initial gaussian wave-packet
                x0 = 3.0                    # center of initial gaussian wave-packet
                hbar = 1
                # Initial Wavefunction
                A = 1.0 / (sigma * np.sqrt(np.pi))  # normalization constant
                psi0 = np.sqrt(A) * np.exp(-(x-x0)**2 / (2.0 * sigma**2)) * np.exp(1j * kx * x)


                V = magnitud*np.arctan(squish*x-squish*5)*(np.exp(-0.1*(squish*x-squish*5)**2)) + 300
                D2 = sparse.diags([1, -2, 1], [-1, 0, 1], shape=(x.size, x.size)) / dx**2
                def psi_t(t, psi):
                    return -1j * (- 0.5 * hbar / m * D2.dot(psi) + V / hbar * psi)
                # Solve the Initial Value Problem
                dt = 0.001  # time interval for snapshots
                t0 = 0.0    # initial time
                tf = 0.4    # final time
                t_eval = np.arange(t0, tf, dt)  # recorded time shots
                print("integrating...")
                sol = integrate.solve_ivp(psi_t,
                                        t_span=[t0, tf],
                                        y0=psi0,
                                        t_eval=t_eval,
                                        method="RK23")

                for i in range(0,len(t_eval),10):
                    print(i/len(t_eval)*100)
                    phi_2=np.abs(sol.y[:, i])**2
                    phi=axes.plot_line_graph(
                        y_values=phi_2,
                        x_values=x,
                        add_vertex_dots=False,
                        stroke_width = 4,
                    ).set_color(BLACK)
                    phi.align_to(oneDaxes,DOWN)
                    phi.shift(UP*0.1)
                    self.add(phi)
                    self.wait(1/30)
                    self.remove(phi)
            

            axes=Axes(x_range=[0, 10], y_range=[-1, 3]).set_color(BLACK)
            axes.shift(DOWN*1)

            #time2=time.time()
            #used to time creation of mobject to see if adding it frame by frame is feasible
            #it took 0.09 seconds to create the mobject
            #print(str(time.time()-time2) + " seconds MAKING MOBJECT")

            oneDaxes=NumberLine(x_range=[0, 10]).set_color(BLACK)
            oneDaxes.move_to(UP)
            graph=axes.plot(lambda x:pot(x)*0.001, x_range=[0,10]).set_color(GREY)
            label=axes.get_axis_labels(x_label="x", y_label="U(x)").set_color(BLACK)
            self.play(Create(axes),Create(label),run_time=1.5)
            #self.play(Create(phi))
            self.play(Create(graph))#,Create(derivative))
            self.play(Create(oneDaxes))
            self.wait()

            #compute_schrodingers()
            animate_ball(0,5, 1, t_max=2, U_x=pot, F=force, rnd_x=False, rnd_v=False, dx=0.01, color=BLUE)
            print(str(time.time()-time1) + " seconds")
            