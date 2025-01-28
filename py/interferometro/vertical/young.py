from manim import *
import numpy as np

# Set vertical aspect ratio
width = 1080
height = 1920
config.frame_size = [width, height]

class young(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.camera.frame.scale(0.6)  # Scale camera to fit vertical layout
        
        def Create_semi(fuente):
            #Create semi wave
            radius = ValueTracker(0.01)
            radiusfinal=7
            wave=Arc(radius=radius.get_value(),start_angle=-180*DEGREES,angle=-PI,color=BLUE).move_to(fuente.get_center())
            wave.add_updater(lambda m: m.become(
                Arc(radius=radius.get_value(),start_angle=-180*DEGREES,angle=-PI,color=BLUE).align_to(fuente,direction=DOWN).set_opacity((1-(1/radiusfinal)*radius.get_value())).set_x(fuente.get_x())
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
        
        # Adjust positions for vertical layout
        fuente1=Dot(color=BLUE).shift(4*DOWN)  # Move source to bottom
        fuente2=Dot(color=BLUE).shift(LEFT)    # Adjust slit positions
        fuente3=Dot(color=BLUE).shift(RIGHT)
        
        # Adjust slits for vertical layout
        rejilla1=Rectangle(height=0.2, width=np.abs(fuente2.get_x()-fuente3.get_x()-0.2),color=BLACK).move_to(fuente2.get_y()*UP)
        rejilla2=Rectangle(width=4, height=0.2,color=BLACK).align_to(fuente2,direction=RIGHT).shift(LEFT*0.2)
        rejilla3=Rectangle(width=4, height=0.2,color=BLACK).align_to(fuente3,direction=LEFT).shift(RIGHT*0.2)
        
        # Move screen to top
        pantalla=Rectangle(width=8,height=0.2,color=BLACK).move_to(UP*4)

        # Define the sinc function
        def sinc_func(x):
            if x == 0:
                return 1
            else:
                return -(0.8*np.sin(1.5*x) / x)

        # Create the axes
        axes = Axes(
            x_range=[-16, 16, 1],
            y_range=[-2, 2, 1],
            x_axis_config={"include_tip": False},
            y_axis_config={"include_tip": False},
        )

        axes.shift(UP * 3.5)  # Move axes near top screen

        # Create the graph
        graph = axes.plot(sinc_func, x_range=[-16, 16], color=BLUE)
        # No need to rotate the graph since we want horizontal interference pattern

        # Animations
        self.play(FadeIn(fuente1),FadeIn(rejilla1),FadeIn(rejilla2),FadeIn(rejilla3),FadeIn(pantalla))
        self.play(Create_wave(fuente1),run_time=0.5, rate_func=linear)
        self.play(Create_semi(fuente2),Create_semi(fuente3),Create_wave(fuente1),run_time=0.5)
        self.play(Create_semi(fuente2),Create_semi(fuente3),Create_wave(fuente1),Create(graph),run_time=0.5)
        
        # Repeat wave animations
        for _ in range(6):
            self.play(Create_semi(fuente2),Create_semi(fuente3),Create_wave(fuente1),run_time=0.5)

        self.wait()
