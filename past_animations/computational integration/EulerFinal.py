from manim import *


class EulerFinal(MovingCameraScene):
    def construct(self):

        self.camera.background_color = "#E2E2E2"
        self.camera.frame.scale(0.5)    

        # Set default color of MathTex to black
        MathTex.set_default(color=BLACK)

        """ FORMULA """

        # https://www.desmos.com/calculator/rlat5mbkrr

        # Derivative
        f = MathTex(r"\frac{dx}{dt}", r"=", r"f\left(x\right)")
        
        # Turn into Deltas
        f_delta = MathTex(r"\frac{\Delta x}{\Delta t}", r"=", r"f\left(x\right)")
        # Create division separate in order to smooth out animation
        loner_delta_x = MathTex(r"\Delta x").move_to(f_delta[0].get_center()).shift(UP*0.33)
        loner_delta_t = MathTex(r"\Delta t").move_to(f_delta[0].get_center()).shift(DOWN*0.33)
        prevline = Line(f_delta[0].get_left(), f_delta[0].get_right()).set_color(BLACK).set_stroke(width=2).shift(DOWN*0.01)

        # Next step, turn into x_i+1 - x_i
        f_i = MathTex(r"\frac{x_{i+1}-x_{i}}{\Delta t}", r"=", r"f\left(x\right)")
        # Create division separate in order to smooth out animation
        loner_xi = MathTex(r"x_{i+1}",r"-",r"x_{i}").move_to(f_i[0].get_center()).shift(UP*0.285)
        loner_dt= MathTex(r"\Delta t").move_to(f_i[0].get_center()).shift(DOWN*0.285)
        newline = Line(f_i[0].get_left(), f_i[0].get_right()).set_color(BLACK).set_stroke(width=2)
       
        # Multiply by \Delta t
        f_i2 = MathTex(r"x_{i+1}", r"-", r"x_{i}", r"=", r"f\left(x\right)", r"\Delta t")

        # Add x_i to both sides
        f_i3 = MathTex(r"x_{i+1}", r"=", r"x_{i}", r"+", r"f\left(x\right)", r"\Delta t")

        ecuaciones = VGroup(f,f_delta,f_i,loner_delta_x,loner_delta_t,prevline,loner_xi,loner_dt,newline,f_i2,f_i3)
        ecuaciones.scale(0.5).shift(UP+RIGHT)

        def func_integral(x):
            return -x**2 +2

        def func(x):
            return -2*x


        """ Main animation """
        ax = Axes(
        x_range=[-3.7,4.3,1], y_range=[-1, 4.5, 1], axis_config={"include_tip": True}
        ).set_color(BLACK)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)
        graph_integral = ax.plot(func_integral, color=GOLD)      
        self.play(Write(labels),Write(ax),Write(graph_integral))

        """ REGRESA EL GRUPO DE PUNTOS Y LINEAS DE LA FUNCION DADA """
        # Nota: Usa ax, tiene que haber una grafica hecha que coincida con func y funcintegral
        def punto_euler(func,func_integral,y_0,dx,a,b):
            
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
            scalingfactor=(ax.c2p(0,0)-ax.c2p(1,1) )[0] / (ax.c2p(0,0)-ax.c2p(1,1) )[1] # aaaaaaaaaaaaaaaaaaaaaaa
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
            return result, lines, dot_on_integral, real_lines


        """ Explain the formula """
        # Se escribe el dx/dt
        self.play(Write(f))
        self.wait(2)

        # Se cambian a deltas
        self.play(ReplacementTransform(f, f_delta))
        self.wait(2)

        # Delta x se vuelve x_i y x_i+1
        self.remove(f_delta[0])
        self.play(

        #equal sign
        ReplacementTransform(f_delta[1], f_i[1]),

        #f(x) moves a bit
        ReplacementTransform(f_delta[2], f_i[2]),

        #delta x turns into x_i
        ReplacementTransform(loner_delta_x, loner_xi),

        #delta t turns into new delta t
        ReplacementTransform(loner_delta_t, loner_dt),

        #division line expands
        ReplacementTransform(prevline, newline)
        )
        self.wait(2)
        
        # Se mueve dt al otro lado
        self.remove(f_i[0])
        self.play(
            #division line fades away
            FadeOut(newline),

            #x_i goes down the division
            ReplacementTransform(loner_xi[0], f_i2[0]),
            ReplacementTransform(loner_xi[1], f_i2[1]),
            ReplacementTransform(loner_xi[2], f_i2[2]),

            #dt goes to the other side
            ReplacementTransform(loner_dt, f_i2[5]),

            #equal sign
            ReplacementTransform(f_i[1], f_i2[3]),

            #f(x) moves a bit
            ReplacementTransform(f_i[2], f_i2[4])
            
            )
        self.wait(2)

        # Se mueve xi al otro lado
        self.play(
            #x_i+1 stays where it is
            ReplacementTransform(f_i2[0], f_i3[0]),
            
            #minus sign turns into plus sign
            ReplacementTransform(f_i2[1], f_i3[3]),

            #x_i goes to the other side
            ReplacementTransform(f_i2[2], f_i3[2]),

            #equal sign
            ReplacementTransform(f_i2[3], f_i3[1]),

            #f(x) moves a bit
            ReplacementTransform(f_i2[4], f_i3[4]),

            # delta t moves a bit
            ReplacementTransform(f_i2[5], f_i3[5])
        )
        self.wait(2)

        # Compute Mobjects
        dots, lines, dot_on_integral, lines_on_integral = punto_euler(func,func_integral,[1],0.1,-1,1)
        
        self.play(Write(dots[0]),Write(lines[0]))

        # Updating each Mobject
        for i in range(20):
            self.play(
                ReplacementTransform(dots[i], dots[i+1]),
                ReplacementTransform(lines[i], lines[i+1]),
                run_time=0.2
            )
            

            self.wait(0.1)
 
        
            
            
        


