

from manim import *
import numpy as np

class young(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        
        """
        DECLARATIONS
        """

        def Create_semi(fuente):
            #Create semi wave
            radius = ValueTracker(0.01)
            radiusfinal=7
            wave=Arc(radius=radius.get_value(),start_angle=-90*DEGREES,angle=PI,color=BLUE).move_to(fuente.get_center())
            wave.add_updater(lambda m: m.become(
                Arc(radius=radius.get_value(),start_angle=-90*DEGREES,angle=PI,color=BLUE).align_to(fuente,direction=LEFT).set_opacity((1-(1/radiusfinal)*radius.get_value())).set_y(fuente.get_y())
                ))
            
            self.add(wave)
            return radius.animate.set_value(radiusfinal)
        
        def Create_wave(fuente):
            #Create wave with circle
            radius = ValueTracker(0.01)
            radiusfinal=6.5
            wave=Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center())
            wave.add_updater(lambda m: m.become(Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center()).set_opacity((1-(1/radiusfinal)*radius.get_value()))))
            self.add(wave)
            return radius.animate.set_value(radiusfinal)
        
        #fuente de la izquierda
        fuente1=Dot(color=BLUE).shift(6*LEFT)
        #fuentes que representan las rendijas
        fuente2=Dot(color=BLUE).shift(UP)
        fuente3=Dot(color=BLUE).shift(DOWN)
        #rejilla entre las dos fuentes
        rejilla1=Rectangle(height=np.abs(fuente2.get_y()-fuente3.get_y()-0.2), width=0.2,color=BLACK).move_to(fuente2.get_x())
        #rejillas arriba y abajo
        rejilla2=Rectangle(height=4, width=0.2,color=BLACK).align_to(fuente2,direction=DOWN).shift(UP*0.2)
        rejilla3=Rectangle(height=4, width=0.2,color=BLACK).align_to(fuente3,direction=UP).shift(DOWN*0.2)
        #pantalla
        pantalla=Rectangle(height=8,width=0.2,color=BLACK).move_to(RIGHT*6)
        
        #distancias
        analysispoint=Dot(color=RED).move_to(pantalla.get_center())
        distance1=Line(fuente2,analysispoint).set_color(GOLD)
        distance2=Line(fuente3,analysispoint).set_color(GOLD)

        distance1.add_updater(lambda x: x.become(
            Line(fuente2,analysispoint).set_color(GOLD)
        ))
        distance2.add_updater(lambda x: x.become(
            Line(fuente3,analysispoint3 ).set_color(GOLD)
        ))
        
        #animaciones
        self.play(FadeIn(fuente1),FadeIn(rejilla1),FadeIn(rejilla2),FadeIn(rejilla3),FadeIn(pantalla))
        self.play(Create_wave(fuente1),run_time=1.5, rate_func=linear)
        self.play(Create_semi(fuente2),Create_semi(fuente3),Create_wave(fuente1),run_time=1.5)
        self.play(Create_semi(fuente2),Create_semi(fuente3),Create_wave(fuente1),run_time=1.5)
        self.play(Create_semi(fuente2),Create_semi(fuente3),Create_wave(fuente1),run_time=1.5)
        
        # Create a sinc function vertical on the wall at pantalla

        # Add sinc function

        # Define the sinc function
        def sinc_func(x):
            if x == 0:
                return 1
            else:
                return (0.5*np.sin(x) / x)**2

        # Create the axes
        axes = Axes(
            x_range=[-16, 16, 1],
            y_range=[-2, 2, 1],
            x_axis_config={"include_tip": False},
            y_axis_config={"include_tip": False},
        )

        axes.shift(RIGHT * 5.5)

        # Create the graph
        graph = axes.plot(sinc_func, x_range=[-16, 16], color=BLUE)
        graph.rotate(PI/2, about_point=axes.c2p(0, 0))

        # Add the axes and graph to the scene
        self.play(Create(graph))

        self.wait(7)





        # self.play(FadeIn(fuente2),FadeIn(fuente3))
        # self.play(Create_wave(fuente2),Create_wave(fuente3),run_time=1.5)
        # self.play(Create_wave(fuente2),Create_wave(fuente3),run_time=1.5)
        # self.wait()
        # self.play(Create(distance1),Create(distance2),Create(analysispoint),run_time=1.5)
        # self.wait()
        # self.play(analysispoint.animate.shift(UP))
        # self.wait()
        # self.play(Create_wave(fuente2),Create_wave(fuente3),run_time=1.5)
        # self.play(analysispoint.animate.shift(DOWN*3),run_time=2)
        # self.play(Create_wave(fuente2),Create_wave(fuente3),run_time=1.5)
        # self.wait()

        #self.play(FadeOut(distance1),FadeOut(distance2),FadeOut(analysispoint))
        #self.play(FadeOut(fuente1),FadeOut(fuente2),FadeOut(fuente3),FadeOut(rejilla1),FadeOut(rejilla2),FadeOut(rejilla3),FadeOut(pantalla))
        