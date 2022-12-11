from manim import *
import numpy as np
# despues de lo de Blas ya no se xd
class Potential(Scene):

    def construct(self):
        self.camera.background_color = "#E2E2E2"

        def pot(x):
            return np.arctan(x)*(np.exp(-x**2)) + 0.4

        def force(x):
            gradiente= (  np.exp(-x**2) * (1- 2 * (x**3 + x)* np.arctan(x) ) )/(x**2 + 1)
            val = gradiente*(-9.81)
            return val

        def derivative(x):
            gradiente= (  np.exp(-x**2) * (1- 2 * (x**3 + x)* np.arctan(x) ) )/(x**2 + 1)
            vector= np.array([1,gradiente*1.7,0])
            vector_norm= vector/np.linalg.norm(vector)
            return vector_norm

        def norm(x):
            gradiente= (  np.exp(-x**2) * (1- 2 * (x**3 + x)* np.arctan(x) ) )/(x**2 + 1)
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

            
        axes=Axes(x_range=[-3, 2], y_range=[-0.25, 1]).set_color(BLACK)
        axes.shift(DOWN*1.5)

        oneDaxes=NumberLine(x_range=[-6, 6]).set_color(BLACK)
        oneDaxes.move_to(axes.c2p(-0.5,1.25))
        
        E_max=0.3537



        graph=axes.plot(lambda x:pot(x), x_range=[-3.5,2.5]).set_color(BLACK)
        label=axes.get_axis_labels(x_label="x", y_label="U(x)").set_color(BLACK)
        self.play(Create(axes),Create(label),Create(oneDaxes),run_time=1.5)
        self.play(Create(graph))#,Create(derivative))

        # Energy Label and Line
        E_lim=Line(axes.c2p(E_max,pot(E_max)) + 8*LEFT,axes.c2p(E_max,pot(E_max))+ 3*RIGHT).set_color(GREEN)
        E_text=MathTex(r"E_{total}").next_to(E_lim,RIGHT).set_color(GREEN)
        self.play(Write(E_lim),Write(E_text))
        
        animate_ball(-2,2.3, 1, t_max=2, U_x=pot, F=force, rnd_x=False, rnd_v=False, dx=0.01, color=BLUE)
        self.wait()
        animate_ball(-2,2.3, 80, U_x=pot, F=force, dx=0.005)
        self.wait()
        self.play(Uncreate(graph),Uncreate(axes),Uncreate(label),Uncreate(oneDaxes))


