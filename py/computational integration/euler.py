from manim import *
import numpy as np

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
            x_range=x_range, y_range=[0, 3, 1], axis_config={"include_tip": False}
            ).set_color(BLACK)
            labels = ax.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)
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

            result.add(*[Dot(radius=0.05, color=RED).move_to(ax.coords_to_point(x[i], y[i])) for i in range(len(x))])
            dot_on_integral.add(*[Dot(radius=0.05, color=RED).move_to(ax.coords_to_point(x[i], func_integral(x[i]))) for i in range(len(x))])
            lines.add(*[
                FunctionGraph(
                    lambda t: func(x[i])*t/scalingfactor
                    ).set_color(MAROON).move_to(ax.coords_to_point(x[i], y[i])) for i in range(len(x))
            ])
            real_lines.add(*[
                FunctionGraph(
                    lambda t: func(x[i])*t/scalingfactor
                    ).set_color(MAROON).move_to(ax.coords_to_point(x[i], func_integral(x[i]))) for i in range(len(x))
            ])



            #self.add(result,lines)
            self.play(Write(labels),Write(ax),Write(graph_integral))
            if animacion=='lento':
                self.play(Write(result[0]))
                for i in range(len(x)-1):
                    self.play(Create(real_lines[i]),Create(dot_on_integral[i]),run_time=0.2)
                    self.play(real_lines[i].animate.move_to(lines[i].get_center()), dot_on_integral[i].animate.move_to(lines[i].get_center()), run_time=0.5)
                    self.remove(dot_on_integral[i])
                    self.play(Write(result[i+1]),run_time=0.2)

                    if (i==3):
                        dx_brace=BraceBetweenPoints(result[i].get_center(),[result[i+1].get_center()[0],result[i].get_center()[1],0],buff=0.1).set_color(BLACK)
                        dx_brace_text=dx_brace.get_text("dx").set_color(BLACK)
                        self.play(Write(dx_brace),Write(dx_brace_text))
                        slope_brace=BraceBetweenPoints([result[i+1].get_center()[0],result[i].get_center()[1],0],result[i+1].get_center(),buff=0.05).set_color(BLACK).scale([0.7,1,1])
                        slope_brace_text=slope_brace.get_text("slope").set_color(BLACK)
                        self.play(Write(slope_brace),Write(slope_brace_text))
                        self.wait()
                        ecuacion=MathTex(r"y\left(i+1)",r"=",r"y(i)+",r"\frac{d}{dx}f(x)",r"\cdot",r"dx").shift(UP+LEFT*3).set_color(BLACK).scale(0.8)
                        self.play(Write(ecuacion[0:3]))
                        self.play(TransformFromCopy(slope_brace_text,ecuacion[3]),TransformFromCopy(dx_brace_text,ecuacion[5]),FadeIn(ecuacion[4]))

                        self.play(FadeOut(dx_brace),FadeOut(dx_brace_text),FadeOut(slope_brace),FadeOut(slope_brace_text))

                    self.play(Uncreate(lines[i]),Uncreate(real_lines[i]),run_time=0.2)

            elif animacion=='rapido':
                self.play(Write(result[0]))
                for i in range(len(x)-1):
                    self.play(Create(lines[i]),run_time=0.1)
                    self.add(result[i])
                    self.remove(lines[i])
            elif animacion=='rapidisimo':
                self.add(result[0])
                for i in range(len(x)-1):
                    self.add(lines[i])
                    self.add(result[i])
                    self.wait(0.1)
                    self.remove(lines[i])

            
            self.clear()
            
            
            '''
            for i in range(len(y)-1):
                y[i + 1] = y[i] + dx*func(x[i])
                self.play(Create(Dot().move_to(ax.coords_to_point(x[i], y[i])) ), run_time=0.2)
            '''
        x_range=[-2, 2]
        punto_euler(func,func_integral,x_range,0.5,x_range[0],x_range[1],'lento')
        punto_euler(lambda x: np.cos(x),lambda x: np.sin(x)+1,x_range,0.1,x_range[0],x_range[1],'rapido')
        punto_euler(func,func_integral,x_range,0.05,x_range[0],x_range[1],'rapidisimo')
        

