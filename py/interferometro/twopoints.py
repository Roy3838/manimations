from manim import *



class Points(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"

        def Create_wave(fuente):
            #Create wave
            radius = ValueTracker(0.01)
            radiusfinal=5
            wave=Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center())
            wave.add_updater(lambda m: m.become(Circle(radius=radius.get_value(),color=BLUE).move_to(fuente.get_center()).set_opacity((1-(1/radiusfinal)*radius.get_value()))))
            self.add(wave)
            return radius.animate.set_value(radiusfinal)

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




        ''' ANIMACIONES 1'''
        self.add(fuente1,fuente2,distance1,distance2,analysispoint)
        self.play(Create_wave(fuente1),Create_wave(fuente2))
        self.play(Create_wave(fuente1),Create_wave(fuente2))
        self.play(Create_wave(fuente1),Create_wave(fuente2))
        self.play(Create_wave(fuente1),Create_wave(fuente2))
        self.wait(0.5)
        self.play(analysispoint.animate.move_to(0.5*RIGHT))
        self.play(Write(bracedis1),Write(dis1label),Write(bracedis2),Write(dis2label))
        self.play(analysispoint.animate.shift(LEFT))
        self.play(analysispoint.animate.shift(1.5*RIGHT),run_time=1.5)
        self.play(FadeOut(distance1),FadeOut(distance2))
        self.play(FadeOut(fuente1),FadeOut(fuente2),FadeOut(analysispoint),
                FadeOut(bracedis1),FadeOut(dis1label),FadeOut(bracedis2),FadeOut(dis2label))
        self.wait(0.5)


        # ''' PART 2 PLANO GENERAL'''
        # self.add(fuente1,fuente2,distance1,distance2,analysispoint)
        # self.play(analysispoint.animate.move_to(0.5*RIGHT+UP))
        # self.play(Write(bracedis1),Write(dis1label),Write(bracedis2),Write(dis2label))
        # self.play(analysispoint.animate.shift(LEFT+2*DOWN))
        # self.play(analysispoint.animate.shift(1.5*RIGHT+2*UP))
        # self.play(FadeOut(distance1),FadeOut(distance2))
        # self.play(FadeOut(fuente1),FadeOut(fuente2),FadeOut(analysispoint),
        #         FadeOut(bracedis1),FadeOut(dis1label),FadeOut(bracedis2),FadeOut(dis2label))
        # self.wait(0.5)
            