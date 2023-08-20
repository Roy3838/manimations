from manim import *
import numpy as np

width=2048*3
height=1152*3
config.pixel_width = width
config.pixel_height = height

class Euler(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        
        
        
        def func(x):
            return 0.7*np.exp(x)
        
        def func_integral(x):
            return 0.7*np.exp(x)
        
        
        #animación del método de euler
        def punto_euler(func,func_integral,y_0,dx,a,b,animacion):
            
            ax = Axes(
            x_range=x_range, y_range=[-5, 10, 1], axis_config={"include_tip": True}
            ).set_color(BLACK)
            labels = ax.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)
            labels[0].scale(0.7)
            labels[1].scale(0.7)
            graph_integral = ax.plot(func_integral, color=GOLD)


            x = np.arange(a, b + dx, dx)
            y = np.zeros(len(x))
            y[0] = func_integral(y_0[0])
            
            result = VGroup()
            lines = VGroup()
            real_lines = VGroup()
            dot_on_integral = VGroup()
            #Función de Euler
            for i in range(len(y)-1):
                y[i + 1] = y[i] + dx*func(x[i])
            #me di cuenta que el eje x y el y no eran de exactamente el mismo tamanyo por lo que hice una función para que se adaptara a los ejes, ya que la pendiente esta en un espacio cuadrado pero la grafica no
            scalingfactor=(ax.c2p(0,0)-ax.c2p(1,1) )[0] / (ax.c2p(0,0)-ax.c2p(1,1) )[1]
            #forma complicada de sacar la relacion de x a y.

            result.add(*[Dot(radius=0.05, color=GRAY_D).move_to(ax.coords_to_point(x[i], y[i])) for i in range(len(x))])
            dot_on_integral.add(*[Dot(radius=0.05, color=RED).move_to(ax.coords_to_point(x[i], func_integral(x[i]))) for i in range(len(x))])
            lines.add(*[
                FunctionGraph(
                    lambda t: func(x[i])*t/scalingfactor
                    ).set_color(GREY_D).move_to(ax.coords_to_point(x[i], y[i])) for i in range(len(x))
            ])
            real_lines.add(*[
                FunctionGraph(
                    lambda t: func(x[i])*t/scalingfactor
                    ).set_color(GREY_D).move_to(ax.coords_to_point(x[i], func_integral(x[i]))) for i in range(len(x))
            ])



            #self.add(result,lines)
            #self.play(Write(labels),Write(ax),Write(graph_integral))
            self.add(ax,labels)

            self.add(result[0])
            for i in range(len(x)-1):
                self.add(lines[i])
                self.add(result[i])
                #self.wait(0.1)
                if (i!=30):
                    
                    self.remove(lines[i])
                else:
                    ecuacion=MathTex(r"f\left(i+1)",r"=",r"f(i)+",r"\frac{d}{dx}f'(x)",r"\cdot",r"dx").shift(UP*0.85+RIGHT*2.6).set_color(BLACK).scale(0.37)
                    ecueacion_e_x=MathTex(r"f(x) = e^{x}").shift(RIGHT*1.8+UP*0.5).set_color(BLACK).scale(0.37)
                    self.add(ecuacion,ecueacion_e_x )


            # not using MathTex
            Slogan = Tex(r"$\mathbb{R}\{\vec{S}\} = $ $\vec{\mathbf{S}}$implify $\mathbb{C}$omplexit$\hat{y}$", color=GRAY_D).scale(2)
            Slogan2 = Tex(r"$\mathbf{U}$sing your $\mathbb{I}$maginatio$\bar{n}$", color=GRAY_D).scale(2)
            Slogan3 = Tex(r"$\mathbf{M}$ake the $\mathbb{R}$eal World Bette$\vec{r}$", color=GRAY_D).scale(2)

            # COMBINING SUM AND CIR \sum of Curiosity Inspiration and Reflection
            summ = MathTex(r"\sum ",r"\mathbb{C}uriosity", r" \mathbb{I}nspiration",r" \mathbb{R}eflection", color=GRAY_D)
            summ.arrange(DOWN, buff=0.1)
            # Align left part
            summ[1].align_to(summ[0], LEFT)
            summ[2].align_to(summ[0], LEFT)
            summ[3].align_to(summ[0], LEFT)
            summ[0].move_to(summ[2]).shift(LEFT*2)
            summ[0].scale([1.5,2,1])
            summ.shift(RIGHT*2.5+DOWN*3.4)
            summ.scale(1.4)



            slogan = VGroup(Slogan, Slogan2, Slogan3).arrange(DOWN, buff=0.5)
            slogan.add(summ)
            Slogan.shift(LEFT*1.3)
            Slogan3.shift(LEFT*1.1)


            #self.play(Write(Reuler), run_time=2)\
            #self.add(espacioReuler)

            slogan.scale(0.26)
            slogan.shift(LEFT*1.3+UP*1.7)

            self.add(slogan)
            
                    

            
            #self.clear()
            
            
            '''
            for i in range(len(y)-1):
                y[i + 1] = y[i] + dx*func(x[i])
                self.play(Create(Dot().move_to(ax.coords_to_point(x[i], y[i])) ), run_time=0.2)
            '''
        x_range=[-2.5, 2]
        #punto_euler(func,func_integral,x_range,0.5,x_range[0],x_range[1],'lento')
        #punto_euler(lambda x: np.cos(x),lambda x: np.sin(x)+1,x_range,0.1,x_range[0],x_range[1],'rapido')
        punto_euler(func,func_integral,x_range,0.1,x_range[0],x_range[1],'rapidisimo')
        

