from manim import *




class Interferometer_Pythagoras(Scene):
    def construct(self):
        """ Scene that describes how the distance between points is calculated using pythagoras
        of the coordinates of the points. """
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
                flash = Circle(radius=0.01).move_to(mobject.get_center())
                flash.radius = 0.01
                flash.add_updater(wave_updater)
                self.add(flash)
                mobject.time = 0        

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

        self.add(fuente1,fuente2,)#distance1,distance2,analysispoint)
        
        self.play(Write(distance1),Write(distance2),Create(analysispoint))
