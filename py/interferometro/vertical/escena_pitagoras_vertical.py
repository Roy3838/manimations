
from manim import *
import numpy as np


width=int(1080)
height=int(1920)
config.frame_size = [width, height]



class Interferometer_Pythagoras(MovingCameraScene):
    def construct(self):
        """ Scene that describes how the distance between points is calculated using pythagoras
        of the coordinates of the points. """
        self.camera.background_color = "#E2E2E2"

        self.camera.frame.scale(0.5)

            

        def wave_updater(mobject, dt):
            #Create wave
            mobject.radius += 0.01 + 3*dt
            radius = mobject.radius
            radiusfinal=5 
            mobject.become(Circle(radius=radius,color=BLUE)
                                                .move_to(mobject.get_center())
                                                .set_opacity(0.5*(1-(1/radiusfinal)*radius)))

        def begin_flashing(mobject, dt):
            mobject.time += dt
            if mobject.time > 0.5 and mobject.flashing == True:
                flash = Circle(radius=0.01).move_to(mobject.get_center())
                flash.radius = 0.01
                flash.add_updater(wave_updater)
                self.add(flash)
                mobject.time = 0        

        # Set default color to black of bracebetweenpoints
        
        BraceBetweenPoints.set_default(color=BLACK)

        #Create two points
        fuente1=Dot(color=BLUE).shift(3*LEFT)
        fuente2=Dot(color=BLUE).shift(3*RIGHT)
            
        analysispoint=Dot(color=BLACK)
        
        distance1=Line(fuente1,analysispoint).set_color(GOLD)
        distance2=Line(fuente2,analysispoint).set_color(GOLD)

        distance1.add_updater(lambda x: x.become(
            Line(fuente1,analysispoint).set_color(GOLD)
        ))
        distance2.add_updater(lambda x: x.become(
            Line(fuente2,analysispoint).set_color(GOLD)
        ))
        
        bracedis1=BraceBetweenPoints(fuente1.get_center(),analysispoint.get_center(),buff=0,color=BLACK)
        bracedis1.add_updater(lambda z: z.become(
            BraceBetweenPoints(fuente1.get_center(),analysispoint.get_center(),buff=0,color=BLACK)
        ))
        dis1label=MathTex(r"d_{1}", color=BLACK).move_to(bracedis1.get_center()+0.5*DOWN)
        dis1label.add_updater(lambda z: z.move_to(bracedis1.get_center()+0.5*DOWN))
        
        bracedis2=BraceBetweenPoints(analysispoint.get_center(),fuente2.get_center(),buff=0,color=BLACK)
        bracedis2.add_updater(lambda z: z.become(
            BraceBetweenPoints(analysispoint.get_center(),fuente2.get_center(),buff=0,color=BLACK)
        ))
        dis2label=MathTex(r"d_{2}", color=BLACK).move_to(bracedis2.get_center()+0.5*DOWN)
        dis2label.add_updater(lambda z: z.move_to(bracedis2.get_center()+0.5*DOWN))

        """
        Revision: add distances at the bottom to show the diference
        """

        r_point1 = Dot(color=BLACK).move_to(DOWN*4 + LEFT*3)
        r_point2 = Dot(color=BLACK).move_to(DOWN*5 + LEFT*3)

        d_point1 = Dot(color=BLACK)
        d_point2 = Dot(color=BLACK)

        rdLine1 = Line(r_point1,d_point1)
        rdLine2 = Line(r_point2,d_point2)

        def distances1_updater(mobject):
            mobject.move_to(r_point1.get_center() + [np.linalg.norm(distance1.get_vector()),0,0])

        def distances2_updater(mobject):
            mobject.move_to(r_point2.get_center() + [np.linalg.norm(distance2.get_vector()),0,0])

        def line1_updater(mobject):
            mobject.become(Line(r_point1,d_point1))

        def line2_updater(mobject):
            mobject.become(Line(r_point2,d_point2))

        d_point1.add_updater(distances1_updater)
        d_point2.add_updater(distances2_updater)


        rdLine1.add_updater(line1_updater)
        rdLine2.add_updater(line2_updater)



        self.add(r_point1, r_point2, d_point1, d_point2, rdLine1, rdLine2)

        equation = MathTex(r"\Delta d", r"=" ,r"d_{2}" ,r"-" ,r"d_{1}", color=BLACK).move_to(5.5*UP)

        ax = NumberPlane(x_range=(-5, 5, 1),
            y_range=(-1, 3, 1),
            background_line_style={"stroke_color" : GREY, "stroke_opacity": 0.3}
            ).shift(UP)
        ax.axes.set_color(BLACK).set_opacity(0.5)



        coords_labels = Text('(x, y)').next_to(analysispoint, UP+RIGHT).set_color(BLACK).scale(0.7).add_updater(lambda z: z.next_to(analysispoint, UP+RIGHT))




        self.play(Create(fuente1),Create(fuente2,))#distance1,distance2,analysispoint)

        self.play(Write(distance1),Write(distance2),Create(analysispoint))



        self.play(Write(bracedis1),Write(dis1label),Write(bracedis2),Write(dis2label))

        self.play(Write(equation))

        self.play(self.camera.frame.animate.shift(UP),
                  equation.animate.shift(UP))



        self.play(analysispoint.animate.shift(UP*2+LEFT))

        self.play(analysispoint.animate.shift(2*RIGHT))

        self.play(analysispoint.animate(path_arc=PI/4).shift(2*LEFT+ DOWN))

        self.play(analysispoint.animate(path_arc=PI/2).shift(2*RIGHT + UP))

        highlightbox = SurroundingRectangle(equation[0], buff = .1)

        self.play(Create(highlightbox))

        self.play(Wiggle(highlightbox))

        self.play(FadeOut(highlightbox))

        self.wait()


        self.play(Write(coords_labels), Create(ax))

        self.wait()


        #Polygon that represents triangle
        triangle=Polygon(fuente1.get_center(),[analysispoint.get_x(),0,0],analysispoint.get_center(),color=BLUE)

        d1_label = MathTex(r"d_{1}", color=BLACK).move_to(0.5*(fuente1.get_center()+analysispoint.get_center())+0.5*UP)

        d2_label = MathTex(r"d_{2}", color=BLACK).move_to(0.5*(fuente2.get_center()+analysispoint.get_center())+0.5*UP)

        self.play(Write(triangle))

        self.play(FadeOut(bracedis1),FadeOut(bracedis2), 
                  ReplacementTransform(dis1label,d1_label),ReplacementTransform(dis2label,d2_label))


        y1_brace = BraceBetweenPoints([analysispoint.get_x(),0,0],analysispoint.get_center())
        y1_brace_text = y1_brace.get_text(r"y").set_color(BLACK)

        x_0_brace = BraceBetweenPoints(fuente1.get_center(),ORIGIN,)
        x_0_brace_text = x_0_brace.get_text(r"x0").set_color(BLACK)

        x_brace = BraceBetweenPoints(ORIGIN,[analysispoint.get_x(),0,0])
        x_brace_text = x_brace.get_text(r"x").set_color(BLACK)

        self.play(Write(y1_brace),Write(y1_brace_text))

        self.wait(2)

        self.play(Write(x_0_brace),Write(x_0_brace_text))

        self.play(Write(x_brace),Write(x_brace_text))

        formulaso1 = MathTex(r"d_1^2",r"=",r"y^2", r"+", r"(x_0+x)^2").shift(UP*4+LEFT).set_color(BLACK)

        self.wait(2)


        self.play(ReplacementTransform(d1_label,formulaso1[0]))

        self.play(Write(formulaso1[1]),run_time=0.5)

        self.play(ReplacementTransform(y1_brace_text,formulaso1[2]))

        self.play(Write(formulaso1[3]),run_time=0.5)

        self.play(ReplacementTransform(x_0_brace_text,formulaso1[4]),
                  ReplacementTransform(x_brace_text,formulaso1[4]))

        self.play(FadeOut(y1_brace),FadeOut(x_0_brace),FadeOut(x_brace),FadeOut(triangle))

        # Next Polygon
        triangle2=Polygon(fuente2.get_center(),[analysispoint.get_x(),0,0],analysispoint.get_center(),color=BLUE)

        self.play(Write(triangle2))

        y2_brace = BraceBetweenPoints(analysispoint.get_center(),[analysispoint.get_x(),0,0])
        y2_brace_text = y2_brace.get_text(r"y").set_color(BLACK)

        x_0_brace = BraceBetweenPoints(ORIGIN,fuente2.get_center())
        x_0_brace_text = x_0_brace.get_text(r"x0").set_color(BLACK)

        x_brace = BraceBetweenPoints(ORIGIN,[analysispoint.get_x(),0,0]).shift(DOWN).set_color(RED)
        x_brace_text = x_brace.get_text(r"x").set_color(BLACK)

        self.play(Write(y2_brace),Write(y2_brace_text))

        self.play(Write(x_0_brace),Write(x_0_brace_text))

        self.play(Write(x_brace),Write(x_brace_text))

        formulaso2 = MathTex(r"d_2^2",r"=",r"y^2", r"+", r"(x_0-x)^2").shift(UP*3+LEFT).set_color(BLACK)

        self.play(ReplacementTransform(d2_label,formulaso2[0]))

        self.play(Write(formulaso2[1]),run_time=0.5)

        self.play(ReplacementTransform(y2_brace_text,formulaso2[2]))

        self.play(Write(formulaso2[3]),run_time=0.5)

        self.play(ReplacementTransform(x_0_brace_text,formulaso2[4]),
                    ReplacementTransform(x_brace_text,formulaso2[4]))

        self.play(FadeOut(y2_brace),FadeOut(x_0_brace),FadeOut(x_brace),FadeOut(triangle2))

        formulaso1_despejado = MathTex(r"d_1",r"=",r"\sqrt{y^{2}+\left(x_{0}+x\right)^{2}}").shift(UP*4+LEFT).set_color(BLACK)
        formulaso2_despejado = MathTex(r"d_2",r"=",r"\sqrt{y^{2}+\left(x_{0}-x\right)^{2}}").shift(UP*3+LEFT).set_color(BLACK)

        #self.remove(x_0_brace_text,x_brace_text)
        self.play(ReplacementTransform(formulaso1,formulaso1_despejado),
                    ReplacementTransform(formulaso2,formulaso2_despejado))

        # Bonito
        self.play(ReplacementTransform(formulaso1_despejado[0],equation[4]),
                    ReplacementTransform(formulaso2_despejado[0],equation[2]),)

        formula_final= MathTex(r"\Delta d", r"=" ,r"\sqrt{y^{2}+\left(x_{0}-x\right)^{2}}" ,r"-" ,r"\sqrt{y^{2}+\left(x_{0}+x\right)^{2}}", color=BLACK).move_to(5.5*UP).scale(0.75)

        self.play(FadeOut(formulaso1_despejado[1:]),FadeOut(formulaso2_despejado[1:]),
            *[ReplacementTransform(eq_elem, final_elem) for eq_elem, final_elem in zip(equation, formula_final)])


        self.play(analysispoint.animate.shift(DOWN*3+ LEFT*1.5))

        self.play(analysispoint.animate(path_arc=PI/4).shift(UP*2))

        self.play(analysispoint.animate(path_arc=PI/2).shift(DOWN*2+RIGHT*2))


        self.wait(3)

