from manim import *
import numpy as np

width=1080
height=1920
config.frame_size = [width, height]

class Euler(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.camera.frame.scale(0.5)      
                
        def func(x):
            return 0.7*np.exp(x)
        
        def func_integral(x):
            return 0.7*np.exp(x)
        
        def func(x):
            return -2*x

        def func_integral(x):
            return -x**2 +2

        #animación del método de euler
        def punto_euler(func,func_integral,y_0,dx,a,b,animacion):
            
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

            if animacion=='lento1':
                self.play(Write(result[0]))
                GarbageCollection=VGroup()
                for i in range(len(x)-1):
                    
                    posarrow=ax.coords_to_point(x[i], y[i])
                    scale_vect_vel=1/2
                    arrowvect=np.array(  [1*scale_vect_vel,scale_vect_vel*func(x[i])/scalingfactor,0  ] )
                    velocidad=Arrow(posarrow, posarrow+arrowvect, buff=0 ).set_color(GREY_C)
                    gravarrow=Arrow(posarrow,posarrow+DOWN,buff=0).set_color(GOLD)
                    self.play(Write(velocidad))
                    self.play(Write(gravarrow ))

                    real_lines[i].move_to(lines[i].get_center())
                    dot_on_integral[i].move_to(lines[i].get_center())
                    self.play(Create(real_lines[i]))#,Create(dot_on_integral[i]))
                    self.play(Write(result[i+1]),run_time=0.2)
                    self.wait(0.3)
                    self.play(Unwrite(velocidad),Unwrite(gravarrow),run_time=0.2)
                    self.remove(dot_on_integral[i],real_lines[i])
                    GarbageCollection.add(result[i+1])

                self.play(FadeOut(GarbageCollection))


            elif animacion=='lento':
                self.play(Write(result[0]))
                GarbageCollection=VGroup()
                for i in range(len(x)-1):
                    
                    posarrow=ax.coords_to_point(x[i], y[i])
                    scale_vect_vel=1/2
                    arrowvect=np.array(  [1*scale_vect_vel,scale_vect_vel*func(x[i])/scalingfactor,0  ] )
                    velocidad=Arrow(posarrow, posarrow+arrowvect, buff=0 ).set_color(BLACK)
                    gravarrow=Arrow(posarrow,posarrow+DOWN,buff=0).set_color(BLACK)
                    #self.play(Write(velocidad))
                    #self.play(Write(gravarrow ))

                    self.play(Create(real_lines[i]),Create(dot_on_integral[i]),run_time=0.2)
                    self.play(real_lines[i].animate.move_to(lines[i].get_center()), dot_on_integral[i].animate.move_to(lines[i].get_center()), run_time=0.5)
                    self.remove(dot_on_integral[i])
                    self.play(Write(result[i+1]),run_time=0.5)
                    

                    if (i==5):
                        dx_brace=BraceBetweenPoints([result[i+1].get_center()[0],result[i].get_center()[1],0],result[i].get_center(),buff=0.1).set_color(BLACK)
                        dx_brace_text=dx_brace.get_text("dx").set_color(BLACK)
                        self.play(Write(dx_brace),Write(dx_brace_text))
                        slope_brace=BraceBetweenPoints(result[i+1].get_center(),[result[i+1].get_center()[0],result[i].get_center()[1],0],buff=0.05).set_color(BLACK).scale([0.7,1,1])
                        slope_brace_text=slope_brace.get_text("f'\left(x)").set_color(BLACK)
                        self.play(Write(slope_brace),Write(slope_brace_text))
                        self.wait()
                        ecuacion=MathTex(r"y\left(i+1)",r"=",r"y(i)+",r"f'\left(x\right)",r"\cdot",r"dx").shift(DOWN*3.5).set_color(BLACK).scale(0.8)
                        self.play(Write(ecuacion[0:3]))
                        self.play(TransformFromCopy(slope_brace_text,ecuacion[3]),TransformFromCopy(dx_brace_text,ecuacion[5]),FadeIn(ecuacion[4]))

                        self.play(FadeOut(dx_brace),FadeOut(dx_brace_text),FadeOut(slope_brace),FadeOut(slope_brace_text))

                    self.play(Uncreate(lines[i]),Uncreate(real_lines[i]),run_time=0.2)
                    GarbageCollection.add(result[i+1])
                self.play(FadeOut(GarbageCollection))


            elif animacion=='rapido':
                self.play(Write(result[0]))
                GarbageCollection=VGroup()
                for i in range(len(x)-1):
                    self.play(Create(lines[i]),run_time=0.1)
                    self.add(result[i])
                    self.remove(lines[i])
                    GarbageCollection.add(result[i+1])
                self.play(FadeOut(GarbageCollection))

            
            elif animacion=='rapidisimo':
                GarbageCollection=VGroup()
                self.add(result[0])
                for i in range(len(x)-1):
                    self.add(lines[i])
                    self.add(result[i])
                    self.wait(1/10)
                    if (i!=30):
                        
                        self.remove(lines[i])
                    else:
                        ecuacion=MathTex(r"y\left(i+1)",r"=",r"y(i)+",r"\frac{d}{dx}f(x)",r"\cdot",r"dx").shift(UP*0.4+LEFT*1.9).set_color(BLACK).scale(0.5)
                        ecueacion_e_x=MathTex(r"f(x) = e^{x}").shift(UP*0.4+RIGHT*2).set_color(BLACK).scale(0.5)
                        self.add(ecuacion,ecueacion_e_x )
                    GarbageCollection.add(result[i+1])
                self.play(FadeOut(GarbageCollection))

        def ecuaciones():
            grav=MathTex("F\left(r\right)=G\frac{m_{1}m_{2}}{r^{2}}")
        
        
        ax = Axes(
        x_range=[-3.7,4.3,1], y_range=[-1, 4.5, 1], axis_config={"include_tip": True}
        ).set_color(BLACK)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)
        graph_integral = ax.plot(func_integral, color=GOLD)      
        self.play(Write(labels),Write(ax),Write(graph_integral))
        x_range=[-1.5, 1.5]
        punto_euler(func,func_integral,x_range,0.5,x_range[0],x_range[1],'lento1')
        #self.clear()
        punto_euler(func,func_integral,x_range,0.5,x_range[0],x_range[1],'lento')
        #self.clear()
        punto_euler(func,func_integral,x_range,0.2,x_range[0],x_range[1],'rapido')
        #self.clear()
        #punto_euler(lambda x: np.cos(x),lambda x: np.sin(x)+1,x_range,0.1,x_range[0],x_range[1],'rapido')
        punto_euler(func,func_integral,x_range,0.1,x_range[0],x_range[1],'rapidisimo')

        punto_euler(func,func_integral,x_range,0.05,x_range[0],x_range[1],'rapidisimo')
        self.wait()


        

