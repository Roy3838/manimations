from manim import *
import numpy as np



class Potential(Scene):
    def construct(self):

        def U(x):
            return np.arctan(x)*(np.exp(-x**2)) + 0.4

        def F(x):
            gradiente= (  np.exp(-x**2) * (1- 2 * (x**3 + x)* np.arctan(x) ) )/(x**2 + 1)
            val = gradiente*(-9.81)
            return val
        
        def animate_ball(particulas,x_0=-2,v_0=2.35, size=0.1, color=RED):
            E=0.7

            #v = lambda x :np.sqrt((E-U(x))*2*m) + v_0



            ball = Dot(size=size).move_to([x_0,U(x_0),0])
            ball.set_color(color)

            E_lim=Line(axes.c2p(0.3537,0.7) + 8*LEFT,axes.c2p(0.3537,0.7)+ 3*RIGHT).set_color(GREEN)
            E_text=MathTex(r"E_{total}").next_to(E_lim,RIGHT).set_color(GREEN)
            self.play(Write(E_lim),Write(E_text))

            dx=0.005
            #dx=0.05
            #t = np.arange(0, 3, dx)
            particulas=40
            v = [np.arange(0, 3, dx) for i in range(particulas)]
            x = [np.arange(0, 3, dx) for i in range(particulas)]

            
            print(len(x))
            print(len(x[0]))
            #euler integration
            #make v_0
            for vs in range (particulas):
                v[vs][0] = v_0 + np.random.normal(0,0.4)

            #make x_0
            for xs in range(particulas):
                x[xs][0] = x_0 #+ np.random.normal(0,0.6)
            
            for j in range(len(x[0])-1):
                balls=VGroup()
                for i in range(len(x)):
                    v[i][j+1] = v[i][j] + F(x[i][j])*dx
                    x[i][j+1] = x[i][j] + v[i][j]*dx
                    if U(x[i][j+1]) > 0.7:
                        balls.add(Dot(fill_opacity=0.4).move_to(axes.c2p(x[i][j+1],U(x[i][j+1])) + UP*0.12).set_color(RED))
                    else:
                        balls.add(ball.copy().move_to(axes.c2p(x[i][j+1],U(x[i][j+1])) + UP*0.12))
                self.add(balls)
                print(i)
                self.wait(1/60)
                self.remove(balls)

            
        axes=Axes(x_range=[-3, 2], y_range=[-0.25, 1]).set_color(BLACK)



        self.camera.background_color = "#E2E2E2"
        #initial_point = [axes.coords_to_point(-2, U(-2))]
        #dot = Dot(point=initial_point).set_color(BLACK)
        #dot.add_updater(lambda x: x.move_to(axes.c2p( )))
        graph=axes.plot(lambda x:U(x), x_range=[-3.5,2.5]).set_color(BLACK)
        label=axes.get_axis_labels(x_label="x", y_label="U(x)").set_color(BLACK)
        #derivative=axes.plot(v).set_color(BLUE)
        self.play(Create(graph),Create(axes),Create(label))#,Create(derivative))
        #self.play(t.animate.set_value(1.25))
        animate_ball(-2,0)
        self.wait()


