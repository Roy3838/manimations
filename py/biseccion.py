from manim import *





class Biseccion(Scene):
    def construct(self):
        def func(x):
            return (x-3)**3 + 2*(x-3)**2 - (x-3) - 1



        #definir ejes y funcion
        ax=Axes(x_range=[0,5],y_range=[-2,2]).set_color(BLACK)
        graph=ax.plot(func,color=MAROON)

        #metodo de biseccion recursivo
        def biseccion(a,b,tol):
            c=(a+b)/2
            brace_a_c=BraceBetweenPoints(ax.c2p(a,0),ax.c2p(c,0),buff=0).set_color(BLACK)
            brace_b_c=BraceBetweenPoints(ax.c2p(c,0),ax.c2p(b,0),buff=0).set_color(BLACK)
            label_a=Text("a="+str(a)).set_color(BLACK).move_to(ax.c2p(a,-0.5)).scale(0.5)
            label_b=Text("b="+str(b)).set_color(BLACK).move_to(ax.c2p(b,-0.5)).scale(0.5)
            label_c=Text("c="+str(c)).set_color(BLACK).move_to(ax.c2p(c,-0.5)).scale(0.5)
            line_a=Line(ax.c2p(a,0),ax.c2p(a,func(a)),color=GOLD_A).scale([0.1,1,1])
            line_b=Line(ax.c2p(b,0),ax.c2p(b,func(b)),color=GOLD_A).scale([0.1,1,1])
            line_c=Line(ax.c2p(c,0),ax.c2p(c,func(c)),color=GOLD_A).scale([0.1,1,1])
            dot_a=Dot(ax.c2p(a,0),color=BLUE).scale(0.5)
            dot_b=Dot(ax.c2p(b,0),color=BLUE).scale(0.5)
            dot_c=Dot(ax.c2p(c,0),color=BLUE).scale(0.5)
            temporal=VGroup(brace_a_c,brace_b_c,label_a,label_b,label_c,line_a,line_b,line_c)
            #operation
            a_c=MathTex(r"f(a)",r"\cdot ",r"f(c)",r" = " , str(np.round(func(a)*func(c),2))).scale(0.5).move_to(2*DOWN+LEFT*2).set_color(BLACK)
            b_c=MathTex(r"f(b)",r"\cdot ",r"f(c)",r" = " , str(np.round(func(b)*func(c),2))).scale(0.5).move_to(2*DOWN+RIGHT*2).set_color(BLACK)
            

            self.play(Create(brace_a_c),Create(brace_b_c))
            self.play(Write(label_a),Write(label_b),Write(label_c))
            self.play(Write(line_a),Write(line_b),Write(line_c))
            self.play(Create(dot_a),Create(dot_b),Create(dot_c))
            self.play(dot_a.animate.move_to(ax.c2p(a,func(a))),dot_b.animate.move_to(ax.c2p(b,func(b))),dot_c.animate.move_to(ax.c2p(c,func(c))))
            self.play(FadeOut(temporal))
            self.play(Write(a_c),Write(b_c))
            self.play(FadeOut(a_c),FadeOut(b_c))
            
            if func(a)*func(c)<0 and np.abs(func(a)-func(c))>tol:
                
                biseccion(a,c,tol)
            elif func(b)*func(c)<0 and np.abs(func(b)-func(c))>tol:
                
                biseccion(c,b,tol)
            else:
                return c



        self.camera.background_color = "#E2E2E2"
        #animaciones
        self.play(Create(ax),Create(graph))

        biseccion(1,4,0.5)

