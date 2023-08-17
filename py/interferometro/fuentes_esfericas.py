from manim import *



class Points(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

            

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
                flash = Circle(radius=0.01).move_to(mobject.get_center()).set_color(BLUE)
                flash.radius = 0.01
                flash.add_updater(wave_updater)
                self.add(flash)
                mobject.time = 0        

        #Create two points
        fuente1=Dot(color=BLUE).shift(3*LEFT)
        fuente2=Dot(color=BLUE).shift(3*RIGHT)
            

        analysispoint=Dot(color=BLACK).shift(DOWN+LEFT)
        # Make an arrow pointing to the analysis point
        tip = analysispoint.get_center()
        arrow = Arrow(tip + RIGHT + UP, tip, buff=0.1, color=BLACK)
        # Update arrow to stick to the analysis point
        arrow.add_updater(lambda x: x.become(
            Arrow(analysispoint.get_center() + RIGHT + UP, analysispoint.get_center(), buff=0, color=BLACK)
        ))
        # Add label to arrow that says YOU
        label = MathTex(r"\text{you}", color=BLACK).move_to(arrow.get_center() + 0.2*DOWN+ 0.3*RIGHT).scale(0.8)

        # Superposicion de las dos ondas
        equation = MathTex(r"\psi_{total} = ", r"\psi_1 ",r"+", r"\psi_2").scale(1.5).set_color(BLACK).move_to(UP*2)

        
        fuente1.time = 0
        fuente1.flashing = False
        fuente1.add_updater(begin_flashing)
        fuente2.time = 0
        fuente2.flashing = False
        fuente2.add_updater(begin_flashing)

        ''' ANIMACIONES 1'''
        self.play(Create(fuente1),Create(fuente2,))#distance1,distance2,analysispoint)

        fuente1.flashing = True
        fuente2.flashing = True
        self.wait()
        
        self.play(Create(analysispoint), Create(arrow), Write(label))

        self.wait(2)
        
        self.play(analysispoint.animate.move_to(0.5*RIGHT),
                  Unwrite(arrow),
                  FadeOut(label),
                   run_time = 1.2)
        self.play(analysispoint.animate.move_to(1.5*LEFT+0.5*UP),run_time =1.2)
        self.play(analysispoint.animate.move_to(1.5*RIGHT+1.5*DOWN),run_time =1.2)

        copy1= fuente1.copy()
        copy2= fuente2.copy()

        copy1.flashing = False
        copy2.flashing = False

        self.wait()

        self.play(analysispoint.animate.shift(UP + RIGHT), 
                  Write(equation[2]),
                  Transform(copy1,equation[1]),
                  Transform(copy2,equation[3]),
                  Transform(analysispoint,equation[0]),
                  
                  run_time = 1)


        fuente1.flashing = False
        fuente2.flashing = False
        self.wait(4)
        self.play(FadeOut(fuente1),FadeOut(fuente2),FadeOut(analysispoint),FadeOut(copy1),FadeOut(copy2),FadeOut(equation))

            